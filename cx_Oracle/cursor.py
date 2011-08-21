from ctypes import byref
import ctypes

import oci
from custom_exceptions import InterfaceError, ProgrammingError, DatabaseError
from buffer import cxBuffer
from utils import is_sequence, cxString_from_encoded_string, python3_or_better
from variable import Variable
from objectvar import OBJECTVAR
from numbervar import NUMBER
from stringvar import STRING, BINARY, FIXED_CHAR
if not python3_or_better():
    from stringvar import UNICODE, FIXED_UNICODE
#from something import DATETIME

class Cursor(object):
    def __init__(self, connection):
        """Create a new cursor object."""
        self.connection = connection # public interface
        self.environment = connection.environment
        self.arraysize = 50 # public
        self.fetch_array_size = 50
        self.bindarraysize = 1 # public
        self.statement_type = -1
        self.output_size = -1
        self.output_size_column = -1
        self.is_open = True

        self.handle = oci.POINTER(oci.OCIStmt)()
        self.statement = None # public interface
        self.input_sizes = 0
        self.numbersAsStrings = None # public interface
        self.inputtypehandler = None # public interface
        self.outputtypehandler = None # public interface
        self.rowfactory = None # public interface

    def raise_if_not_open(self):
        if not self.is_open:
            raise InterfaceError("not open")
        
        return self.connection.raise_if_not_connected()

    def free_handle(self, raise_exception):
        """Free the handle which may be reallocated if necessary."""
        if self.handle:
            if self.is_owned:
                status = oci.OCIHandleFree(self.handle, oci.OCI_HTYPE_STMT)
                if raise_exception:
                    self.environment.check_for_error(status, "Cursor_FreeHandle()")
            elif self.connection.handle:
                try:
                    buffer = cxBuffer.new_from_object(self.statement_tag, self.environment.encoding)
                except:
                    if raise_exception:
                        raise

                status = oci.OCIStmtRelease(self.handle, self.environment.error_handle, buffer.c_struct.ptr, buffer.c_struct.size, oci.OCI_DEFAULT)

                if raise_exception:
                    self.environment.check_for_error(status, "Cursor_FreeHandle()")

            self.handle = oci.POINTER(oci.OCIStmt)()

    def internal_prepare(self, statement, statement_tag):
        """Internal method for preparing a statement for execution."""

        # make sure we don't get a situation where nothing is to be executed
        if statement is None and not self.statement:
            raise ProgrammingError("no statement specified and no prior statement prepared")

        # nothing to do if the statement is identical to the one already stored
        # but go ahead and prepare anyway for create, alter and drop statments
        if statement is None or statement == self.statement:
            if self.statement_type not in (oci.OCI_STMT_CREATE, oci.OCI_STMT_DROP, oci.OCI_STMT_ALTER):
                return
            statement = self.statement

        # keep track of the statement
        self.statement = statement

        # release existing statement, if necessary
        self.statement_tag = statement_tag
        self.free_handle(True)

        # prepare statement
        self.is_owned = False
        statement_buffer = cxBuffer.new_from_object(statement, self.environment.encoding)

        tag_buffer = cxBuffer.new_from_object(statement_tag, self.environment.encoding)

        status = oci.OCIStmtPrepare2(self.connection.handle, byref(self.handle), self.environment.error_handle, statement_buffer.c_struct.ptr, statement_buffer.c_struct.size, tag_buffer.c_struct.ptr, tag_buffer.c_struct.size, oci.OCI_NTV_SYNTAX, oci.OCI_DEFAULT)

        try:
            self.environment.check_for_error(status, "Cursor_InternalPrepare(): prepare")
        except:
            # this is needed to avoid "invalid handle" errors since Oracle doesn't
            # seem to leave the pointer alone when an error is raised but the
            # resulting handle is still invalid
            self.handle = oci.POINTER(oci.OCIStmt)()
            raise

        # clear bind variables, if applicable
        if not self.input_sizes:
            self.bindvars = None

        # clear row factory, if applicable
        self.row_factory = None

        # determine if statement is a query
        self.get_statement_type()

    def get_statement_type(self):
        c_statement_type = oci.ub2()

        status = oci.OCIAttrGet(self.handle, oci.OCI_HTYPE_STMT, byref(c_statement_type), 0, oci.OCI_ATTR_STMT_TYPE, self.environment.error_handle)
        self.environment.check_for_error(status, "Cursor_GetStatementType()")
        self.statement_type = c_statement_type.value
        self.fetch_variables = None

    def perform_define(self):
        c_num_params = ctypes.c_int()

        # determine number of items in select-list
        status = oci.OCIAttrGet(self.handle, oci.OCI_HTYPE_STMT, byref(c_num_params), 0, oci.OCI_ATTR_PARAM_COUNT, self.environment.error_handle)
        self.environment.check_for_error(status, "Cursor_PerformDefine()")

        num_params = c_num_params.value

        # create a list corresponding to the number of items
        self.fetch_variables = [None] * num_params # or should I use appends?

        # define a variable for each select-item
        self.fetch_array_size = self.arraysize
        for pos in xrange(1, num_params+1):
            var = Variable.define(self, self.fetch_array_size, pos)
            self.fetch_variables[pos - 1] = var

    def internal_execute(self, num_iters):
        """Perform the work of executing a cursor and set the rowcount appropriately
           regardless of whether an error takes place."""

        if self.connection.autocommit:
            mode = oci.OCI_COMMIT_ON_SUCCESS
        else:   
            mode = oci.OCI_DEFAULT

        status = oci.OCIStmtExecute(self.connection.handle, self.handle, self.environment.error_handle, num_iters, 0, 0, 0, mode)
        # here the OCI will change variable.c_actual_elements, given at bind time
        
        try:
            self.environment.check_for_error(status, "Cursor_InternalExecute()")
        except Exception, e:
            new_exception = self.set_error_offset(e)
            try:
                self.set_row_count()
            except:
                pass
            raise new_exception

        return self.set_row_count()

    def set_bind_variables(self, parameters, num_elements, array_pos, defer_type_assignment):
        """Create or set bind variables."""
        # make sure positional and named binds are not being intermixed
        num_params = 0
        bound_by_pos = is_sequence(parameters)
        if bound_by_pos:
            num_params = len(parameters)

        if self.bindvars:
            orig_bound_by_pos = isinstance(self.bindvars, list)
            if bound_by_pos != orig_bound_by_pos:
                raise ProgrammingError("positional and named binds cannot be intermixed")

            orig_num_params = len(self.bindvars)

        # otherwise, create the list or dictionary if needed
        else:
            if bound_by_pos:
                self.bindvars = [None] * num_params
            else:
                self.bindvars = {}

            orig_num_params = 0
        
        # handle positional binds
        if bound_by_pos:
            for i, value in enumerate(parameters):
                if i < orig_num_params:
                    orig_var = self.bindvars[i]
                else:
                    orig_var = None
                
                new_var = self.set_bind_variable_helper(num_elements, array_pos, value, orig_var, defer_type_assignment)

                if new_var:
                    if i < len(self.bindvars):
                        self.bindvars[i] = new_var
                    else:
                        self.bindvars.append(new_var)

        # handle named binds
        else:
            for key, value in parameters.iteritems():
                orig_var = self.bindvars.get(key, None)
                new_var = self.set_bind_variable_helper(num_elements, array_pos, value, orig_var, defer_type_assignment)

                if new_var:
                    self.bindvars[key] = new_var

    def set_bind_variable_helper(self, num_elements, array_pos, value, orig_var, defer_type_assignment):
        """Helper for setting a bind variable."""

        # initialization
        new_var = None 
        is_value_var = isinstance(value, Variable)

        # handle case where variable is already bound
        if orig_var:
            # if the value is a variable object, rebind it if necessary
            if is_value_var:
                if orig_var != value:
                    new_var = value

            # if the number of elements has changed, create a new variable
            # this is only necessary for executemany() since execute() always
            # passes a value of 1 for the number of elements
            elif num_elements > orig_var.numElements:
                new_var = Variable(self, num_elements, orig_var.type, orig_var.size)
                new_var.set_value(array_pos, value)

            # otherwise, attempt to set the value
            else:
                try:
                    orig_var.set_value(array_pos, value)
                except Exception, e:
                    # executemany() should simply fail after the first element
                    if array_pos > 0:
                        raise
                    
                    # anything other than index error or type error should fail
                    if not isinstance(e, (IndexError, TypeError)):
                        raise

                    orig_var = None

        # if no original variable used, create a new one
        if not orig_var:

            # if the value is a variable object, bind it directly
            if is_value_var:
                new_var = value
                new_var.bound_pos = 0
                new_var.bound_name = None

            # otherwise, create a new variable, unless the value is None and
            # we wish to defer type assignment
            elif value is not None or not defer_type_assignment:
                new_var = Variable.new_by_value(self, value, num_elements)
                new_var.set_value(array_pos, value)

        return new_var


    def execute(self, statement, *args, **kwargs):
        """Execute the statement."""
        execute_args = undefined = object() # avoid mixing up user-provided None with our None.

        if args:
            execute_args = args[0]

        if execute_args is not undefined and kwargs:
            raise InterfaceError("expecting argument or keyword arguments, not both")
        
        if kwargs:
            execute_args = kwargs

        if execute_args is not undefined:
            if not isinstance(execute_args, dict) and not is_sequence(execute_args):
                raise TypeError("expecting a dictionary, sequence or keyword args")

        # make sure the cursor is open
        self.raise_if_not_open()

        # prepare the statement, if applicable
        self.internal_prepare(statement, None)
        
        # perform binds
        if execute_args is not undefined:
            self.set_bind_variables(execute_args, 1, 0, 0)

        self.perform_bind()
        
        # execute the statement
        is_query = self.statement_type == oci.OCI_STMT_SELECT
        if is_query:
            num_iters = 0
        else:
            num_iters = 1

        self.internal_execute(num_iters)
        
        # perform defines, if necessary
        if is_query and self.fetch_variables is None:
            self.perform_define()

        # reset the values of setoutputsize()
        self.output_size = -1
        self.output_size_column = -1

        # for queries, return the cursor for convenience
        if is_query:
            return self

        # for all other statements, simply return None
        return None

    def prepare(self, statement, statement_tag=None):
        """Prepare the statement for execution."""

        # make sure the cursor is open
        self.raise_if_not_open()

        # prepare the statement
        self.internal_prepare(statement, statement_tag)

    def executemany(self, statement, list_of_arguments):
        """Execute the statement many times. The number of times is equivalent to the number of elements in the array 
of dictionaries."""
        # make sure the cursor is open - ctypes: prepare already checks that
        # self.raise_if_not_open()

        # prepare the statement
        self.prepare(statement, None)

        # queries are not supported as the result is undefined
        if self.statement_type == oci.OCI_STMT_SELECT:
            raise NotSupportedError("queries not supported: results undefined")

        # perform binds
        num_rows = len(list_of_arguments)
        for i, arguments in enumerate(list_of_arguments):
            if not isinstance(arguments, dict) and not is_sequence(arguments):
                raise InterfaceError("expecting a list of dictionaries or sequences")
            self.set_bind_variables(arguments, num_rows, i, (i < num_rows - 1))

        self.perform_bind()

        # execute the statement, but only if the number of rows is greater than zero since Oracle raises an error 
        # otherwise
        if num_rows > 0:
            self.internal_execute(num_rows)

    def set_row_count(self):
        """Set the rowcount variable."""
        # rowcount is not row_count because it is public interface

        if self.statement_type == oci.OCI_STMT_SELECT:
            self.rowcount = 0
            self.actual_rows = -1 # not public interface
            self.row_num = 0
        else:
            if self.statement_type in (oci.OCI_STMT_INSERT, oci.OCI_STMT_UPDATE, oci.OCI_STMT_DELETE):
                c_row_count = oci.ub4()
                status = oci.OCIAttrGet(self.handle, oci.OCI_HTYPE_STMT, byref(c_row_count), 0, oci.OCI_ATTR_ROW_COUNT, self.environment.error_handle)
                self.environment.check_for_error(status, "Cursor_SetRowCount()")
                self.rowcount = c_row_count.value
            else:
                self.rowcount = -1

    def perform_bind(self):
        """Perform the binds on the cursor."""

        # ensure that input sizes are reset
        # this is done before binding is attempted so that if binding fails and
        # a new statement is prepared, the bind variables will be reset and
        # spurious errors will not occur
        self.input_sizes = 0

        # set values and perform binds for all bind variables
        if self.bindvars:
            if isinstance(self.bindvars, dict):
                for key, var in self.bindvars.iteritems():
                    var.bind(self, key, 0)
            else:
                for i, var in enumerate(self.bindvars):
                    if var is not None:
                        var.bind(self, None, i + 1)

    def fixup_bound_cursor(self):
        """Fixup a cursor so that fetching and returning cursor descriptions are successful after binding a cursor to another cursor."""
        if self.handle and self.statement_type < 0:
            self.get_statement_type()
            try:
                self.perform_define()
            except:
                if self.statement_type == oci.OCI_STMT_SELECT:
                    raise

            self.set_row_count()
    
    def verify_fetch(self):
        self.raise_if_not_open()
        self.fixup_bound_cursor()

        if self.statement_type != oci.OCI_STMT_SELECT:
            raise InterfaceError("not a query")

    def internal_fetch(self, num_rows):
        """Performs the actual fetch from Oracle."""
        
        if not self.fetch_variables:
            raise InterfaceError("query not executed")

        for var in self.fetch_variables:
            var.internal_fetch_num += 1
            if var.type.pre_fetch_proc:
                var.type.pre_fetch_proc(var)
            
        status = oci.OCIStmtFetch(self.handle, self.environment.error_handle, num_rows, oci.OCI_FETCH_NEXT, oci.OCI_DEFAULT)

        if status != oci.OCI_NO_DATA:
            self.environment.check_for_error(status, "Cursor_InternalFetch(): fetch")

        row_count = oci.ub4()
        status = oci.OCIAttrGet(self.handle, oci.OCI_HTYPE_STMT, byref(row_count), 0, oci.OCI_ATTR_ROW_COUNT, self.environment.error_handle)
        self.environment.check_for_error(status, "Cursor_InternalFetch(): row count")

        self.actual_rows = row_count.value - self.rowcount
        self.row_num = 0

    def create_row(self):
        """Create an object for the row. The object created is a tuple unless a row
           factory function has been defined in which case it is the result of the
           row factory function called with the argument tuple that would otherwise be
           returned."""

        # create a new tuple
        result_as_list = [None] * len(self.fetch_variables)

        # acquire the value for each item
        for pos, var in enumerate(self.fetch_variables):
            item = var.getvalue(self.row_num)
            result_as_list[pos] = item

        # increment row counters
        self.row_num += 1
        self.rowcount += 1

        # if a row factory is defined, call it
        if self.rowfactory is not None:
            return self.rowfactory(tuple)

        return tuple(result_as_list)

    def more_rows(self):
        """Returns a boolean indicating if more rows can be retrieved from the cursor."""
        if self.row_num >= self.actual_rows:
            if self.actual_rows < 0 or self.actual_rows == self.fetch_array_size:
                self.internal_fetch(self.fetch_array_size)

            if self.row_num >= self.actual_rows:
                return False

        return True
    
    def fetchmany(self, rowLimit=None):
        if rowLimit is None:
            rowLimit = self.arraysize
        
        # verify fetch can be performed
        self.verify_fetch()
        
        return self.multi_fetch(rowLimit)
        
    def fetchone(self): # public
        """Fetch a single row from the cursor."""

        # verify fetch can be performed
        self.verify_fetch()

        # setup return value
        more_rows_to_fetch = self.more_rows()
        if not more_rows_to_fetch:
            return None
        return self.create_row()

    def fetchall(self):
        """Fetch all remaining rows from the cursor."""
        self.verify_fetch()
        return self.multi_fetch(0)

    def multi_fetch(self, row_limit):
        """Return a list consisting of the remaining rows up to the given row limit (if specified)."""

        results = []

        # fetch as many rows as possible
        row_num = 0
        while row_limit == 0 or row_num < row_limit:
            more_rows_available = self.more_rows()
            if more_rows_available:
                row = self.create_row()
                results.append(row)
            else:
                break
            row_num += 1

        return results
    
    def set_error_offset(self, exception):
        """Set the error offset on the error object, if applicable."""
        if isinstance(exception, DatabaseError):
            error = exception.args[0]
            c_offset = oci.ub4()
            oci.OCIAttrGet(self.handle, oci.OCI_HTYPE_STMT, byref(c_offset), 0, oci.OCI_ATTR_PARSE_ERROR_OFFSET, self.environment.error_handle)
            error.offset = c_offset.value

        return exception



    def call_build_statement(self, name, return_value, list_of_arguments, keyword_arguments):
        """Determine the statement and the bind variables to bind to the statement that is created for calling a stored procedure or function."""

        # initialize the bind variables to the list of positional arguments
        if list_of_arguments:
            bind_variables = list(list_of_arguments) # copy to avoid messing up with the sequence from the user?
        else:
            bind_variables = []

        # insert the return variable, if applicable
        if return_value:
            bind_variables.insert(0, return_value)

        # initialize format arguments
        format_args = [name]

        # begin building the statement_template
        arg_num = 1
        statement_template = 'begin '

        if return_value:
            statement_template += ":1 := "
            arg_num += 1

        statement_template += "%s ("

        # include any positional arguments first
        if list_of_arguments:
            for i, argument in enumerate(list_of_arguments):
                if i > 0:
                    statement_template += ','
                statement_template += ":%d" % arg_num
                arg_num += 1
                if isinstance(argument, bool):
                    statement_template += " = 1"

        # next append any keyword arguments
        if keyword_arguments:
            pos = 0
            for key, value in keyword_arguments.iteritems():
                bind_variables.append(value)
                format_args.append(key)
                if (arg_num > 1 and not return_value) or (arg_num > 2 and return_value):
                    statement_template += ','
                statement_template += "%%s => :%d" % arg_num
                arg_num += 1
                if isinstance(value, bool):
                    statement_template +=  " = 1"

        statement_template += "); end;"

        
        statement = statement_template % tuple(format_args)

        return statement, bind_variables

    def call(self, return_value, name, list_of_arguments, keyword_arguments): # kwargs are the stored procedure kwargs, not Python!
        """Call a stored procedure or function."""

        # verify that the arguments are passed correctly
        if list_of_arguments:
            if not is_sequence(list_of_arguments):
                raise TypeError("arguments must be a sequence")

        # make sure the cursor is open
        self.raise_if_not_open()

        # determine the statement to execute and the argument to pass
        statement, bind_variables = self.call_build_statement(name, return_value, list_of_arguments, keyword_arguments)

        # execute the statement on the cursor
        self.execute(statement, bind_variables)

    def callproc(self, name, parameters=None, keywordParameters=None):
        """Call a stored procedure and return the (possibly modified) arguments."""
        # call the stored procedure
        self.call(None, name, parameters, keywordParameters)

        # create the return value
        results = [var.getvalue(0) for var in self.bindvars]
        return results

    def callfunc(self, name, return_type, parameters=None, keywordParameters=None):
        """Call a stored function and return the return value of the function."""

        # create the return variable
        var = Variable.new_by_type(self, return_type, 1)

        # call the function
        self.call(var, name, parameters, keywordParameters)

        # determine the results
        results = var.getvalue(0)
        return results

    def close(self):
        # make sure we are actually open
        self.raise_if_not_open()

        # close the cursor
        self.free_handle(True)

        self.is_open = False
        
    def get_bind_names(self, num_elements):
        """Return a list of bind variable names. At this point the cursor must have already been prepared."""

        # ensure that a statement has already been prepared
        if not self.statement:
            raise ProgrammingError("statement must be prepared first")
        
        # avoid bus errors on 64-bit platforms
        num_elements = num_elements + (ctypes.sizeof(ctypes.c_void_p) - num_elements % ctypes.sizeof(ctypes.c_void_p))
    
        # initialize the buffers
        # code simplified, but now uses multiple mallocs
        bind_names = (ctypes.c_char_p * num_elements)() # one pointer per string. who allocates the str?
        bind_name_lengths = (oci.ub1 * num_elements)() # one ub1 per str
        indicator_names = (ctypes.c_char_p * num_elements)() # same of bind names
        indicator_name_lengths = (oci.ub1 * num_elements)()
        duplicate = (oci.ub1 * num_elements)()
        bind_handles = (oci.POINTER(oci.OCIBind) * num_elements)()
    
        c_found_elements = oci.sb4()
        # get the bind information
        status = oci.OCIStmtGetBindInfo(self.handle, self.environment.error_handle, num_elements, 
                                    1, byref(c_found_elements), bind_names, bind_name_lengths, indicator_names,
                                    indicator_name_lengths, duplicate, bind_handles)
        found_elements = c_found_elements.value
        
        try:
            self.environment.check_for_error(status, "Cursor_GetBindNames()")
        except:
            if status != oci.OCI_NO_DATA:
                raise
        
        if found_elements < 0:
            names = None
            return abs(found_elements), names
        
        names = []
        
        # process the bind information returned
        for i in xrange(found_elements):
            if not duplicate[i]:
                temp = cxString_from_encoded_string(bind_names[i],
                        self.connection.environment.encoding) # removed num bytes arg
                names.append(temp)
                
        return num_elements, names

    def bindnames(self):
        """Return a list of bind variable names."""

        # make sure the cursor is open
        self.raise_if_not_open()

        # results renamed to found_elements
        found_elements, names = self.get_bind_names(8)
        if found_elements < 0:
            return None
        found_elements, names = self.get_bind_names(found_elements)
        if not names and found_elements < 0:
            return None
        return names

    def __iter__(self):
        """Return a reference to the cursor which supports the iterator protocol."""
        self.verify_fetch()
        return self
    
    def next(self):
        """Return a reference to the cursor which supports the iterator protocol."""
        self.verify_fetch()
        more_rows_available = self.more_rows()
        if more_rows_available:
            return self.create_row()
        
        raise StopIteration() # TODO: is this right?

    def __del__(self):
        self.free_handle(False)
        
    def var(self, type, size=0, arraysize=None, inconverter=None, outconverter=None, typename=None):
        """Create a bind variable and return it."""

        # parse arguments
        if arraysize is None:
            arraysize = self.bindarraysize
            
        array_size = arraysize # ctypes: normalize name
        
        # determine the type of variable
        var_type = Variable.type_by_python_type(self, type)
        if var_type.is_variable_length and size == 0:
            size = var_type.size
        
        if type is OBJECTVAR and not typename:
            raise TypeError("expecting type name for object variables")
    
        # create the variable
        var = Variable(self, array_size, var_type, size)
        var.inconverter = inconverter
        var.outconverter = outconverter
    
        # define the object type if needed
        if type is OBJECTVAR:
            var.object_type = ObjectType.new_by_name(self.connection, typeName)
        
        return var
    
    def setinputsizes(self, *args, **kwargs):
        """Set the sizes of the bind variables."""
        # only expect keyword arguments or positional arguments, not both
        if args and kwargs:
            raise InterfaceError("expecting arguments or keyword arguments, not both")
        
        self.raise_if_not_open()
    
        # eliminate existing bind variables
        if kwargs:
            self.bindvars = {}
        else:
            self.bindvars = [None] * len(args)
        
        self.input_sizes = 1
    
        # process each input
        if kwargs:
            for key, value in kwargs.iteritems():
                var = Variable.new_by_type(self, value, self.bindarraysize)
                self.bindvars[key] = var
        else:
            for i, value in enumerate(args):
                if value is None:
                    var = None
                else:
                    var = Variable.new_by_type(self, value, self.bindarraysize)
                
                self.bindvars[i] = var
        
        return self.bindvars
    
    def arrayvar(self, type, value, size=0):
        """Create an array bind variable and return it."""
        
        # determine the type of variable
        var_type = Variable.type_by_python_type(self, type)
        if var_type.is_variable_length and size == 0:
            size = var_type.size
    
        # determine the number of elements to create
        if isinstance(value, list):
            num_elements = len(value)
        elif isinstance(value, int):
            num_elements = value
        else:
            raise TypeError("expecting integer or list of values")
        
        # create the variable
        var = Variable(self, num_elements, var_type, size)
        var.make_array()
    
        # set the value, if applicable
        if isinstance(value, list):
            var.set_array_value(value)
        
        return var
    
    def get_item_description_helper(self, pos, param):
        """Helper for Cursor_ItemDescription() used so that it is not necessary to
constantly free the descriptor when an error takes place."""
        # acquire usable type of item
        var_type = Variable.type_by_oracle_descriptor(param, self.environment)
        
        c_internal_size = oci.ub2()
        # acquire internal size of item
        status = oci.OCIAttrGet(param, oci.OCI_HTYPE_DESCRIBE, byref(c_internal_size), 0,
                oci.OCI_ATTR_DATA_SIZE, self.environment.error_handle)
        self.environment.check_for_error(status, "Cursor_ItemDescription(): internal size")
        internal_size = c_internal_size.value
        
        # null OK must be converted to bool!
    
        # acquire character size of item
        c_char_size = oci.ub2()
        status = oci.OCIAttrGet(param, oci.OCI_HTYPE_DESCRIBE, byref(c_char_size), 0,
                oci.OCI_ATTR_CHAR_SIZE, self.environment.error_handle)
        self.environment.check_for_error(status, "Cursor_ItemDescription(): character size")
        char_size = c_char_size.value
        
        # aquire name of item
        c_name = ctypes.c_char_p()
        c_name_length = oci.ub4()
        
        status = oci.OCIAttrGet(param, oci.OCI_HTYPE_DESCRIBE, byref(c_name),
                byref(c_name_length), oci.OCI_ATTR_NAME, self.environment.error_handle)
        self.environment.check_for_error(status, "Cursor_ItemDescription(): name")
        name = c_name.value[:c_name_length.value] # doesn't it give back a NULL terminated string?!
        
        python_type = var_type.python_type
        
        if python_type == NUMBER:
            # lookup precision and scale
            c_scale = oci.sb1()
            c_precision = oci.sb2()
            status = oci.OCIAttrGet(param, oci.OCI_HTYPE_DESCRIBE, byref(c_scale), 0,
                    oci.OCI_ATTR_SCALE, self.environment.error_handle)
            self.environment.check_for_error(status, "Cursor_ItemDescription(): scale")
            scale = c_scale.value
            
            status = oci.OCIAttrGet(param, oci.OCI_HTYPE_DESCRIBE, byref(c_precision), 0,
                    oci.OCI_ATTR_PRECISION, self.environment.error_handle)
            self.environment.check_for_error(status, "Cursor_ItemDescription(): precision")
            precision = c_precision.value
        
        # lookup whether null is permitted for the attribute
        c_null_ok = oci.ub1()
        status = oci.OCIAttrGet(param, oci.OCI_HTYPE_DESCRIBE, byref(c_null_ok), 0,
                oci.OCI_ATTR_IS_NULL, self.environment.error_handle)
        self.environment.check_for_error(status, "Cursor_ItemDescription(): nullable")
        null_ok = c_null_ok.value # should make null_ok a bool
        
        # set display size based on data type
        
        if python_type == NUMBER:
            if precision:
                display_size = precision + 1
                if scale > 0:
                    display_size += scale + 1
            else:
                display_size = 127
        else:
            mapping = {
                STRING: char_size,
                BINARY: internal_size,
                FIXED_CHAR: char_size,
                DATETIME: 23,
            }
            
            if not python3_or_better():
                mapping.update({
                    UNICODE: char_size,
                    FIXED_UNICODE: char_size,
                })
            
            display_size = mapping.get(python_type, -1)
        
        result = cxString_from_encoded_string(name, self.connection.environment.encoding), python_type, display_size, internal_size, precision, scale, null_ok
    
        return result
    
    def get_item_description(self, pos):
        """Return a tuple describing the item at the given position."""
        param = oci.POINTER(oci.OCIParam)()
        
        # acquire parameter descriptor
        status = oci.OCIParamGet(self.handle, oci.OCI_HTYPE_STMT, self.environment.error_handle,
                                 byref(param), pos)
        self.environment.check_for_error(status, "Cursor_ItemDescription(): parameter")
        
        # use helper routine to get tuple
        description_element = self.get_item_description_helper(pos, param)
        oci.OCIDescriptorFree(param, oci.OCI_DTYPE_PARAM)
        
        return description_element
    
    @property
    def description(self):
        """Return a list of 7-tuples consisting of the description of the define variables."""
        
        # make sure the cursor is open
        self.raise_if_not_open()
        
        # fixup bound cursor, if necessary
        self.fixup_bound_cursor()
    
        # if not a query, return None
        if self.statement_type != oci.OCI_STMT_SELECT:
            return None
    
        # determine number of items in select-list
        c_num_items = ctypes.c_int()
        status = oci.OCIAttrGet(self.handle, oci.OCI_HTYPE_STMT, byref(c_num_items), 0,
                                oci.OCI_ATTR_PARAM_COUNT, self.environment.error_handle)
        self.environment.check_for_error(status, "Cursor_GetDescription()")
        
        num_items = c_num_items.value
        
        # create a list of the required length
        results = [None] * num_items
    
        # create tuples corresponding to the select-items
        for index in xrange(num_items):
            description_element = self.get_item_description(index + 1)
            results[index] = description_element
    
        return results