from ctypes import byref
import ctypes
import sys
from datetime import datetime, date, timedelta
from decimal import Decimal

from utils import python3_or_better, cxBinary, cxString, MAX_STRING_CHARS, MAX_BINARY_BYTES
from custom_exceptions import NotSupportedError, DatabaseError
from error import Error
from variable_type import VariableType
from buffer import cxBuffer

from numbervar import vt_Float, vt_NumberAsString, vt_Boolean, vt_LongInteger
from stringvar import vt_String, vt_FixedNationalChar, vt_NationalCharString, vt_FixedChar, vt_Rowid, vt_Binary
from longvar import vt_LongString, vt_LongBinary

if not python3_or_better():
    from numbervar import vt_Integer

from numbervar import NUMBER, NATIVE_FLOAT
from stringvar import STRING, FIXED_CHAR, ROWID, BINARY
from longvar import LONG_STRING, LONG_BINARY

if not python3_or_better():
    from stringvar import UNICODE, FIXED_UNICODE


import oci

vt_DateTime = VariableType()
#print vt_DateTime
vt_Timestamp = VariableType()
#print vt_Timestamp
vt_Interval = VariableType()
#print vt_Interval
vt_BLOB = VariableType()
#print vt_BLOB
vt_BFILE = VariableType()
#print vt_BFILE
vt_Cursor = VariableType()
#print vt_Cursor
vt_Object = VariableType()
#print vt_Object
vt_NativeFloat = VariableType()
#print vt_NativeFloat
vt_NCLOB = VariableType()
#print vt_NCLOB
vt_CLOB = VariableType()
#print vt_CLOB

#print '---'
#print vt_Float, vt_NumberAsString
#print vt_String, vt_FixedNationalChar, vt_NationalCharString, vt_FixedChar, vt_Rowid, vt_Binary



class Variable(object):
    def __init__(self, cursor, num_elements, type, size):
        self.environment = cursor.connection.environment

        self.bind_handle = oci.POINTER(oci.OCIBind)()
        self.define_handle = oci.POINTER(oci.OCIDefine)()
        self.bound_cursor_handle = oci.POINTER(oci.OCIStmt)()
        self.bound_name = None
        self.inconverter = None # public
        self.outconverter = None  # public
        self.bound_pos = 0

        if num_elements < 1:
            self.numElements = self.allocelems = 1
        else:
            self.numElements = self.allocelems = num_elements

        self.actual_elements = 0
        self.internal_fetch_num = 0
        self.is_array = False
        self.is_allocated_internally = True
        self.type = type
        self.indicator = oci.POINTER(oci.sb2)()
        self.data = oci.POINTER(None)
        self.actual_length = oci.POINTER(oci.ub2)()
        self.return_code = oci.POINTER(oci.ub2)()

        # set the maximum length of the variable, ensure that a minimum of
        # 2 bytes is allocated to ensure that the array size check works
        self.size = type.size
        if type.is_variable_length:
            if size < ctypes.sizeof(oci.ub2):
                size = ctypes.sizeof(oci.ub2)
            self.size = size

        # allocate the data for the variable
        self.allocate_data()

        # allocate the indicator for the variable
        self.indicator = (self.numElements * oci.sb2)()

        # ensure that all variable values start out NULL
        for i in xrange(self.numElements):
            self.indicator[i] = oci.OCI_IND_NULL

        # for variable length data, also allocate the return code
        if type.is_variable_length:
            self.return_code = (self.numElements * oci.ub2)()

        # perform extended initialization
        if self.type.initialize_proc:
            self.type.initialize_proc(self, cursor)

    def allocate_data(self):
        """Allocate the data for the variable."""

        # set the buffer size for the variable
        # bufferSize is public
        if self.type.get_buffer_size_proc:
            # TODO: Refactor self.bufferSize = self.maxlength with a property to help maintain the 2 variables always equal
            self.bufferSize = self.maxlength = self.type.get_buffer_size_proc(self)
        else:
            self.bufferSize = self.maxlength = self.size

        # allocate the data as long as it is small enough
        data_length = self.numElements * self.bufferSize
        if data_length > sys.maxint:
            raise ValueError("array size too large")

        self.data = ctypes.create_string_buffer(data_length) # TODO: would be nicer to use a typed array here.

    @staticmethod
    def define(cursor, num_elements, position):
        """Allocate a variable and define it for the given statement."""
        
        param = oci.POINTER(oci.OCIParam)()

        # retrieve parameter descriptor
        status = oci.OCIParamGet(cursor.handle, oci.OCI_HTYPE_STMT, cursor.environment.error_handle, byref(param), position)
        cursor.environment.check_for_error(status, "Variable_Define(): parameter")

        # call the helper to do the actual work
        var = Variable.define_helper(cursor, param, position, num_elements)
        oci.OCIDescriptorFree(param, oci.OCI_DTYPE_PARAM)
        
        return var

    @staticmethod
    def define_helper(cursor, param, position, num_elements):
        #udt_VariableType *varType
        #udt_Variable *var
        #ub4 size

        # determine data type
        var_type = Variable.type_by_oracle_descriptor(param, cursor.environment)
        if not var_type:
            return

        if cursor.numbersAsStrings and var_type is vt_Float:
            var_type = vt_NumberAsString

        # retrieve size of the parameter
        size = var_type.size
        if var_type.is_variable_length:
            # determine the maximum length from Oracle
            c_size_from_oracle = oci.ub2()
            status = oci.OCIAttrGet(param, oci.OCI_HTYPE_DESCRIBE, byref(c_size_from_oracle), 0, oci.OCI_ATTR_DATA_SIZE, cursor.environment.error_handle)
            cursor.environment.check_for_error(status, "Variable_Define(): data size")
            size_from_oracle = c_size_from_oracle.value
            
            # use the length from Oracle directly if available
            if size_from_oracle:
                size = size_from_oracle

            # otherwise, use the value set with the setoutputsize() parameter
            else:
                if cursor.output_size >= 0:
                    if cursor.output_size_column < 0 or position == cursor.output_size_column:
                        size = cursor.output_size

        # create a variable of the correct type
        if cursor.outputtypehandler:
            var = Variable.new_by_output_type_handler(cursor, param, cursor.outputtypehandler, var_type, size, num_elements)
        elif cursor.connection.outputtypehandler:
            var = Variable.new_by_output_type_handler(cursor, param, cursor.connection.outputtypehandler, var_type, size, num_elements)
        else:
            var = Variable(cursor, num_elements, var_type, size)

        if not var:
            return

        # call the procedure to set values prior to define
        if var.type.pre_define_proc:
            var.type.pre_define_proc(var, param)

        # perform the define
        status = oci.OCIDefineByPos(cursor.handle, byref(var.define_handle), var.environment.error_handle, position, var.data, var.bufferSize, var.type.oracle_type, var.indicator, var.actual_length, var.return_code, oci.OCI_DEFAULT)
        var.environment.check_for_error(status, "Variable_Define(): define")

        # call the procedure to set values after define
        if var.type.post_define_proc:
            var.type.post_define_proc(var)

        return var

    @staticmethod
    def type_by_oracle_descriptor(param, environment):
        """Return a variable type given an Oracle descriptor."""
    
        # retrieve datatype of the parameter
        c_data_type = oci.ub2()
        status = oci.OCIAttrGet(param, oci.OCI_HTYPE_DESCRIBE, byref(c_data_type), 0, oci.OCI_ATTR_DATA_TYPE, environment.error_handle)
        environment.check_for_error(status, "Variable_TypeByOracleDescriptor(): data type")
        data_type = c_data_type.value

        # retrieve character set form of the parameter
        if data_type not in (oci.SQLT_CHR, oci.SQLT_AFC, oci.SQLT_CLOB):
            charset_form = oci.SQLCS_IMPLICIT
        else:
            c_charset_form = oci.ub1()
            status = oci.OCIAttrGet(param, oci.OCI_HTYPE_DESCRIBE, byref(c_charset_form), 0, oci.OCI_ATTR_CHARSET_FORM, environment.error_handle)
            environment.check_for_error(status, "Variable_TypeByOracleDescriptor(): charset form")
            charset_form = c_charset_form.value

        return Variable.type_by_oracle_data_type(data_type, charset_form)

    @staticmethod
    def type_by_oracle_data_type(oracle_data_type, charset_form):
        mapping = {
                    oci.SQLT_LNG: vt_LongString,
                    oci.SQLT_RDD: vt_Rowid,
                    oci.SQLT_BIN: vt_Binary,
                    oci.SQLT_LBI: vt_LongBinary,
                    oci.SQLT_NUM: vt_Float,
                    oci.SQLT_VNU: vt_Float,
                    oci.SQLT_DAT: vt_DateTime,
                    oci.SQLT_ODT: vt_DateTime,
                    oci.SQLT_DATE: vt_Timestamp,
                    oci.SQLT_TIMESTAMP: vt_Timestamp,
                    oci.SQLT_TIMESTAMP_TZ: vt_Timestamp,
                    oci.SQLT_TIMESTAMP_LTZ: vt_Timestamp,
                    oci.SQLT_INTERVAL_DS: vt_Interval,
                    oci.SQLT_BLOB: vt_BLOB,
                    oci.SQLT_BFILE: vt_BFILE,
                    oci.SQLT_RSET: vt_Cursor,
                    oci.SQLT_NTY: vt_Object,
                    oci.SQLT_BFLOAT: vt_NativeFloat, # removed #ifdef SQLT_BFLOAT
                    oci.SQLT_IBFLOAT: vt_NativeFloat,
                    oci.SQLT_BDOUBLE: vt_NativeFloat,
                    oci.SQLT_IBDOUBLE: vt_NativeFloat,
                  }

        if oracle_data_type == oci.SQLT_AFC:
            if not python3_or_better() and charset_form == oci.SQLCS_NCHAR:
                return vt_FixedNationalChar
            else:
                return vt_FixedChar

        if oracle_data_type == oci.SQLT_CHR:
            if not python3_or_better() and charset_form == oci.SQLCS_NCHAR:
                return vt_NationalCharString
            else:
                return vt_String
        
        if oracle_data_type == oci.SQLT_CLOB:
            if charset_form == oci.SQLCS_NCHAR:
                return vt_NCLOB
            else:
                return vt_CLOB
        
        try:
            return mapping[oracle_data_type]
        except KeyError:
            raise NotSupportedError("Variable_TypeByOracleDataType: unhandled data type %d" % oracle_data_type)

    def get_single_value(self, array_pos):
        """Return the value of the variable at the given position."""

        # ensure we do not exceed the number of allocated elements
        if array_pos >= self.numElements:
            raise(IndexError, "Variable_GetSingleValue: array size exceeded")

        # check for a NULL value
        if self.type.is_null_proc:
            is_null = self.type.is_null_proc(self, array_pos)
        else:
            is_null = self.indicator[array_pos] == oci.OCI_IND_NULL

        if is_null:
            return None

        # check for truncation or other problems on retrieve
        self.verify_fetch(array_pos)

        # calculate value to return
        value = self.type.get_value_proc(self, array_pos)
        if self.outconverter is not None:
            result = self.outconverter(value)
            return result

        return value
    
    def _get_value(self, array_pos):
        """Return the value of the variable."""
        if self.is_array:
            return self.get_array_value(self.actual_elements)
        return self.get_single_value(array_pos)
    
    def getvalue(self, pos=0):
        """Return the value of the variable at the given position."""
        # TODO: Type check like cx_oracle
        return self._get_value(pos)

    def verify_fetch(self, array_pos):
        """Verifies that truncation or other problems did not take place on retrieve."""
        if self.type.is_variable_length:
            if self.return_code[array_pos] != 0:
                error = Error(self.environment, "Variable_VerifyFetch()", 0)
                error.code = self.return_code[array_pos]
                error.message = "column at array pos %d fetched with error: %d" % (array_pos, self.return_code[array_pos])

                raise DatabaseError(error)

    def get_array_value(self, num_elements):
        """Return the value of the variable as an array."""
        return [self.get_single_value(i) for i in xrange(num_elements)]

    def bind(self, cursor, name, pos):
        """Allocate a variable and bind it to the given statement."""

        # nothing to do if already bound
        if self.bind_handle and name == self.bound_name and pos == self.bound_pos:
            return

        # set the instance variables specific for binding
        self.bound_pos = pos
        self.bound_cursor_handle = cursor.handle
        self.bound_name = name

        # perform the bind
        return self.internal_bind()


    def internal_bind(self):
        """Allocate a variable and bind it to the given statement."""

        if self.is_array:
            alloc_elems = self.allocelems
            actual_elements_ref = byref(self.actual_elements)
        else:
            alloc_elems = 0
            actual_elements_ref = 0

        # perform the bind
        if self.bound_name:
            buffer = cxBuffer.new_from_object(self.bound_name, self.environment.encoding)
            status = oci.OCIBindByName(self.bound_cursor_handle, byref(self.bind_handle),
                        self.environment.error_handle, buffer.c_struct.ptr,
                        buffer.c_struct.size, self.data, self.bufferSize,
                        self.type.oracle_type, self.indicator, self.actual_length,
                        self.return_code, alloc_elems,
                        actual_elements_ref, oci.OCI_DEFAULT)
        else:
            status = oci.OCIBindByPos(self.bound_cursor_handle, byref(self.bind_handle),
                        self.environment.error_handle, self.bound_pos, self.data,
                        self.bufferSize, self.type.oracle_type, self.indicator,
                        self.actual_length, self.return_code, alloc_elems,
                        actual_elements_ref, oci.OCI_DEFAULT)

        self.environment.check_for_error(status, "Variable_InternalBind()")

        if not python3_or_better():
            # set the charset form and id if applicable
            if self.type.charset_form != oci.SQLCS_IMPLICIT:
                c_charset_form = oci.ub1()
                status = oci.OCIAttrSet(self.bind_handle, oci.OCI_HTYPE_BIND,
                        byref(c_charset_form), 0, oci.OCI_ATTR_CHARSET_FORM,
                        self.environment.error_handle)
                self.type.charset_form = c_charset_form.value
                self.environment.check_for_error(status, "Variable_InternalBind(): set charset form")

                c_buffer_size = oci.ub4()
                status = oci.OCIAttrSet(self.bind_handle, oci.OCI_HTYPE_BIND,
                        byref(c_buffer_size), 0, oci.OCI_ATTR_MAXDATA_SIZE,
                        self.environment.error_handle)
                self.bufferSize = self.maxlength = c_buffer_size.value
                self.environment.check_for_error(status, "Variable_InternalBind(): set max data size")

        # set the max data size for strings
        if (self.type == vt_String or self.type == vt_FixedChar) and self.size > self.type.size:
            c_size = oci.ub4()
            status = oci.OCIAttrSet(self.bind_handle, oci.OCI_HTYPE_BIND,
                    byref(c_size), 0, oci.OCI_ATTR_MAXDATA_SIZE,
                    self.environment.error_handle)
            self.type.size = c_size.value
            self.environment.check_for_error(status, "Variable_InternalBind(): set max data size")

    @staticmethod
    def new_by_type(cursor, value, num_elements):
        """Allocate a new variable by looking at the Python data type."""

        # passing an integer is assumed to be a string
        if isinstance(value, int):
            if value > MAX_STRING_CHARS:
                var_type = vt_LongString
            else:
                var_type = vt_String

            return Variable(cursor, num_elements, var_type, value)

        # passing an array of two elements to define an array
        if isinstance(value, list):
            return Variable.new_array_by_type(cursor, value) # TODO: Implement

        # handle directly bound variables
        if isinstance(value, Variable):
            return value

        # everything else ought to be a Python type
        var_type = Variable.type_by_python_type(cursor, value)
        return Variable(cursor, num_elements, var_type, var_type.size)

    @staticmethod
    def type_by_python_type(cursor, type):
        """Return a variable type given a Python type object or NULL if the Python type does not have a corresponding
variable type."""
        mapping = {
            STRING: vt_String,
            str: vt_String,
            FIXED_CHAR: vt_FixedChar,
#        if (type == (PyObject*) &g_NCLOBVarType)
#            return &vt_NCLOB
            ROWID: vt_Rowid,
            BINARY: vt_Binary,
            cxBinary: vt_Binary,
            LONG_STRING: vt_LongString,
            LONG_BINARY: vt_LongBinary,
#        if (type == (PyObject*) &g_BFILEVarType)
#            return &vt_BFILE
#        if (type == (PyObject*) &g_BLOBVarType)
#            return &vt_BLOB
#        if (type == (PyObject*) &g_CLOBVarType)
#            return &vt_CLOB
            float: vt_Float,
            long: vt_LongInteger,
            bool: vt_Boolean,
            
#        if (type == (PyObject*) &g_DateTimeVarType)
#            return &vt_DateTime
#            date: vt_Date,
#            datetime: vt_DateTime,
#        if (type == (PyObject*) &g_IntervalVarType)
#            return &vt_Interval
#        timedelta: vt_Interval,
#        if (type == (PyObject*) &g_TimestampVarType)
#            return &vt_Timestamp
#        if (type == (PyObject*) &g_CursorVarType)
#            return &vt_Cursor
#    #ifdef SQLT_BFLOAT
#        if (type == (PyObject*) &g_NativeFloatVarType)
#            return &vt_NativeFloat
#    #endif
#        if (type == (PyObject*) &g_ObjectVarType)
#            return &vt_Object
#
#
        }
        if not python3_or_better():
            mapping[UNICODE] = vt_NationalCharString
            mapping[unicode] = vt_NationalCharString
            mapping[FIXED_UNICODE] = vt_FixedNationalChar
            mapping[int] = vt_Integer

        if cursor.numbersAsStrings:
            mapping[NUMBER] = vt_NumberAsString
        else:
            mapping[NUMBER] = vt_Float

        try:
            return mapping[type]
        except KeyError:
            raise NotSupportedError("Variable_TypeByPythonType(): unhandled data type")


    @staticmethod
    def new_by_value(cursor, value, num_elements):
        """Allocate a new variable by looking at the type of the data."""
        if cursor.inputtypehandler is not None:
            return Variable.new_by_input_type_handler(cursor, cursor.inputtypehandler, value, num_elements)
        if cursor.connection.inputtypehandler is not None:
            return Variable.new_by_input_type_handler(cursor, cursor.connection.inputtypehandler, value, num_elements)
        
        return Variable.default_new_by_value(cursor, value, num_elements)

    @staticmethod
    def new_by_input_type_handler(cursor, input_type_handler, value, num_elements):
        """Allocate a new variable by looking at the type of the data."""
        var = input_type_handler(cursor, value, num_elements)

        if var is not None:
            if not isinstance(var, Variable):
                raise TypeError("expecting variable from input type handler")

            return var

        return Variable.default_new_by_value(cursor, value, num_elements)

    @staticmethod
    def default_new_by_value(cursor, value, num_elements):
        """Default method for determining the type of variable to use for the data."""

        var_type, size, new_num_elements = Variable.type_by_value(value)
        
        if new_num_elements:
            num_elements = new_num_elements
        
        var = Variable(cursor, num_elements, var_type, size)
        if isinstance(value, list):
            var.make_array()

        return var

    def make_array(self):
        """Make the variable an array, ensuring that the type supports arrays."""
        if not self.type.can_be_in_array:
            raise NotSupportedError("Variable_MakeArray(): type does not support arrays")

        self.is_array = True

    @staticmethod
    def type_by_value(value):
        """Return a variable type given a Python object or NULL if the Python object does not have a corresponding 
variable type."""

        # handle scalars
        if value is None:
            return vt_String, 1, None

        if isinstance(value, cxString):
            size = len(value) # assuming cxString_GetSize = len
            if size > MAX_STRING_CHARS:
                type = vt_LongString
            else:
                type = vt_String
            return type, size, None

        if not python3_or_better():
            if isinstance(value, unicode):
                size = PyUnicode_GET_SIZE(value)
                if size > MAX_STRING_CHARS:
                    type = vt_LongString
                else:
                    type = vt_NationalCharString
                return type, size, None

            if isinstance(value, int):
                return vt_Integer, None, None
        else:
            if isinstance(value, bytes):
                size = len(value)
                if size > MAX_BINARY_BYTES:
                    type = vt_LongBinary
                else:
                    type = vt_Binary

                return type, None, None

        if isinstance(value, long):
            return vt_LongInteger, None, None
        if isinstance(value, float):
            return vt_Float, None, None
        if isinstance(value, cxBinary):
            size = len(value)
            if size > MAX_BINARY_BYTES:
                type = vt_LongBinary
            else:
                type = vt_Binary
            
            return type, size, None

        if isinstance(value, bool):
            return vt_Boolean, None, None
        if isinstance(value, datetime):
            return vt_DateTime, None, None
        if isinstance(value, date):
            return vt_DateTime, None, None
        if isinstance(value, timedelta):
            return vt_Interval, None, None

        from cursor import Cursor

        is_cursor = isinstance(value, Cursor)
        if is_cursor:
            return vt_Cursor, None, None

        if isinstance(value, Decimal):
            return vt_NumberAsString, None, None

        # handle arrays
        if isinstance(value, list):
            for element_value in value:
                if element_value is not None:
                    break

            var_type, _, _ = Variable.type_by_value(element_value)
            num_elements = len(value)
            size = var_type.size
            return var_type, size, num_elements

        raise NotSupportedError("Variable_TypeByValue(): unhandled data type %.*s", type(value))

    def set_value(self, array_pos, value):
        """Set the value of the variable."""
        if self.is_array:
            if array_pos > 0:
                raise NotSupportedError("arrays of arrays are not supported by the OCI")

            return self.set_array_value(value)

        return self.set_single_value(array_pos, value)
    
    setvalue = set_value # TODO: Type check like cx_oracle

    def set_single_value(self, array_pos, value):
        """Set a single value in the variable."""

        # ensure we do not exceed the number of allocated elements
        if array_pos >= self.numElements:
            raise IndexError("Variable_SetSingleValue: array size exceeded")

        # convert value, if necessary
        if self.inconverter is not None:
            value = self.inconverter(value)

        # check for a NULL value
        if value is None:
            self.indicator[array_pos] = oci.OCI_IND_NULL
            return None

        self.indicator[array_pos] = oci.OCI_IND_NOTNULL
        if self.type.is_variable_length:
            self.return_code[array_pos] = 0
        self.type.set_value_proc(self, array_pos, value) # ctypes: in C, the return value was to signal exception

    def set_array_value(self, value):
        """Set all of the array values for the variable."""

        # ensure we have an array to set
        if isinstance(value, list):
            raise TypeError("expecting array data")

        # ensure we haven't exceeded the number of allocated elements
        num_elements = len(value)
        if num_elements > self.numElements:
            raise IndexError("Variable_SetArrayValue: array size exceeded")

        # set all of the values
        self.actual_elements = num_elements

        for i, element_value in enumerate(value):
            var.set_single_value(i, element_value)
            
    #def __repr__(self):
        #if self.is_array:
            #value = self.get_array_value(self.actual_elements)
        #elif self.allocelems == 1:
            #value = self.get_single_value(0)
        #else:
            #value = self.get_array_value(self.allocelems)
        
        #return '<%s.%s with value %s>' % (type(self).__module__, type(self).__name__, 'TODO')
