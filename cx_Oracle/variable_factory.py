import ctypes
from ctypes import byref
from datetime import datetime, date, timedelta
from decimal import Decimal

import oci
from pythonic_oci import OCIAttrGet, OCIParamGet

from utils import python3_or_better, cxBinary, cxString, MAX_STRING_CHARS, MAX_BINARY_BYTES

from numbervar import vt_Float, vt_NumberAsString, vt_Boolean, vt_LongInteger
from stringvar import vt_String, vt_FixedNationalChar, vt_NationalCharString, vt_FixedChar, vt_Rowid, vt_Binary
from longvar import vt_LongString, vt_LongBinary
from datetimevar import vt_DateTime, vt_Date
from lobvar import vt_NCLOB, vt_CLOB, vt_BLOB, vt_BFILE
from timestampvar import vt_Timestamp
from intervalvar import vt_Interval
from cursorvar import vt_Cursor

from variable import Variable

if not python3_or_better():
    from numbervar import vt_Integer
    
all_variable_types = [vt_Float, vt_NumberAsString, vt_Boolean, vt_LongInteger, vt_String, vt_FixedNationalChar, vt_NationalCharString, vt_FixedChar, vt_Rowid, vt_Binary, vt_LongString, vt_LongBinary, vt_DateTime, vt_Date, vt_NCLOB, vt_CLOB, vt_BLOB, vt_BFILE, vt_Timestamp, vt_Interval, vt_Cursor]

if not python3_or_better():
    all_variable_types.append(vt_Integer)

from numbervar import NUMBER, NATIVE_FLOAT
from stringvar import STRING, FIXED_CHAR, ROWID, BINARY
from longvar import LONG_STRING, LONG_BINARY
from datetimevar import DATETIME
from lobvar import NCLOB, CLOB, BLOB, BFILE
from timestampvar import TIMESTAMP
from intervalvar import INTERVAL
from cursorvar import CURSOR

if not python3_or_better():
    from stringvar import UNICODE, FIXED_UNICODE

from variable_type import VariableType
from custom_exceptions import NotSupportedError

# TODO: Not implemented yet
vt_Object = VariableType()
vt_NativeFloat = VariableType()

# this dict is only for debugging purposes.
vt_to_name = {
    vt_DateTime: 'vt_DateTime', 
    vt_Timestamp: 'vt_Timestamp', 
    vt_Interval: 'vt_Interval',
    vt_BLOB :'vt_BLOB',
    vt_BFILE :'vt_BFILE',
    vt_Cursor :'vt_Cursor',
    vt_Object :'vt_Object',
    vt_NativeFloat :'vt_NativeFloat',
    vt_NCLOB :'vt_NCLOB',
    vt_CLOB:  'vt_CLOB',
    
    vt_Float: 'vt_Float',
    vt_NumberAsString: 'vt_NumberAsString',
    vt_Boolean: 'vt_Boolean',
    vt_LongInteger: 'vt_LongInteger',
    
    vt_String: 'vt_String',
    vt_FixedNationalChar: 'vt_FixedNationalChar',
    vt_NationalCharString: 'vt_FixedNationalChar',
    vt_FixedChar: 'vt_FixedChar',
    vt_Rowid: 'vt_Rowid',
    vt_Binary: 'vt_Binary',
    
    vt_LongString: 'vt_LongString',
    vt_LongBinary: 'vt_LongBinary',
}

mapping_python_type_to_variable_type = {
    STRING: vt_String,
    str: vt_String,
    FIXED_CHAR: vt_FixedChar,
    NCLOB: vt_NCLOB,
    ROWID: vt_Rowid,
    BINARY: vt_Binary,
    cxBinary: vt_Binary,
    LONG_STRING: vt_LongString,
    LONG_BINARY: vt_LongBinary,
    BFILE: vt_BFILE,
    BLOB: vt_BLOB,
    CLOB: vt_CLOB,
    float: vt_Float,
    long: vt_LongInteger,
    bool: vt_Boolean,
    DATETIME: vt_DateTime,
    date: vt_Date,
    datetime: vt_DateTime,
    INTERVAL: vt_Interval,
    #timedelta: vt_Interval,
    TIMESTAMP: vt_Timestamp,
    CURSOR: vt_Cursor,
    #OBJECT: vt_Object,
}

#ifdef SQLT_BFLOAT
    #NATIVE_FLOAT: vt_NativeFloat
#endif

        
if not python3_or_better():
    mapping_python_type_to_variable_type[UNICODE] = vt_NationalCharString
    mapping_python_type_to_variable_type[unicode] = vt_NationalCharString
    mapping_python_type_to_variable_type[FIXED_UNICODE] = vt_FixedNationalChar
    mapping_python_type_to_variable_type[int] = vt_Integer

mapping_variable_type_to_python_type = {}

for variable_type in all_variable_types:
    mapping_variable_type_to_python_type[variable_type] = variable_type.python_type

#for python_type, variable_type in mapping_python_type_to_variable_type.iteritems():
    #if isinstance(python_type, Variable):
        #mapping_variable_type_to_python_type[variable_type] = python_type



class VariableFactory(object):
    """Instantiates subclasses of variables. Removes most of the staticmethods and references to subclasses 
    from Variable"""

    def define(self, cursor, num_elements, position):
        """Allocate a variable and define it for the given statement."""
        
        # retrieve parameter descriptor
        param = OCIParamGet(cursor.handle, oci.OCI_HTYPE_STMT, cursor.environment, position, "Variable_Define(): parameter")

        # call the helper to do the actual work
        var = self.define_helper(cursor, param, position, num_elements)
        oci.OCIDescriptorFree(param, oci.OCI_DTYPE_PARAM)
        
        return var

    def define_helper(self, cursor, param, position, num_elements):
        # determine data type
        var_type = self.type_by_oracle_descriptor(param, cursor.environment)
        if not var_type:
            return

        if cursor.numbersAsStrings and var_type is vt_Float:
            var_type = vt_NumberAsString

        # retrieve size of the parameter
        size = var_type.size
        if var_type.is_variable_length:
            # determine the maximum length from Oracle
            size_from_oracle = OCIAttrGet(param, oci.OCI_HTYPE_DESCRIBE, oci.ub2, oci.OCI_ATTR_DATA_SIZE, cursor.environment, "Variable_Define(): data size")
            
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
            var = self.new_by_output_type_handler(cursor, param, cursor.outputtypehandler, var_type, size, num_elements)
        elif cursor.connection.outputtypehandler:
            var = self.new_by_output_type_handler(cursor, param, cursor.connection.outputtypehandler, var_type, size, num_elements)
        else:
            var = self.new(cursor, num_elements, var_type, size)

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
    
    
    def type_by_oracle_descriptor(self, param, environment):
        """Return a variable type given an Oracle descriptor."""
    
        # retrieve datatype of the parameter
        data_type = OCIAttrGet(param, oci.OCI_HTYPE_DESCRIBE, oci.ub2, oci.OCI_ATTR_DATA_TYPE, environment, "Variable_TypeByOracleDescriptor(): data type")

        # retrieve character set form of the parameter
        if data_type not in (oci.SQLT_CHR, oci.SQLT_AFC, oci.SQLT_CLOB):
            charset_form = oci.SQLCS_IMPLICIT
        else:
            charset_form = OCIAttrGet(param, oci.OCI_HTYPE_DESCRIBE, oci.ub1, oci.OCI_ATTR_CHARSET_FORM, environment, "Variable_TypeByOracleDescriptor(): charset form")

        return self.type_by_oracle_data_type(data_type, charset_form)

    def type_by_oracle_data_type(self, oracle_data_type, charset_form):
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
                    #oci.SQLT_BFLOAT: vt_NativeFloat, # TODO: removed #ifdef SQLT_BFLOAT
                    #oci.SQLT_IBFLOAT: vt_NativeFloat,
                    #oci.SQLT_BDOUBLE: vt_NativeFloat,
                    #oci.SQLT_IBDOUBLE: vt_NativeFloat,
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
        
    def new_by_type(self, cursor, value, num_elements):
        """Allocate a new variable by looking at the Python data type."""

        # passing an integer is assumed to be a string
        if isinstance(value, int):
            if value > MAX_STRING_CHARS:
                var_type = vt_LongString
            else:
                var_type = vt_String
            
            return self.new(cursor, num_elements, var_type, value)

        # passing an array of two elements to define an array
        if isinstance(value, list):
            return self.new_array_by_type(cursor, value)

        # handle directly bound variables
        from variable import Variable # here it is fine to use Variable
        if isinstance(value, Variable):
            return value
        del Variable

        # everything else ought to be a Python type
        var_type = self.type_by_python_type(cursor, value)
        return self.new(cursor, num_elements, var_type, var_type.size)
    
    def new_array_by_type(self, cursor, value):
        """Allocate a new PL/SQL array by looking at the Python data type."""
        if len(value) != 2:
            raise ProgrammingError("expecting an array of two elements [type, numelems]")
        
        var_type, num_elements = value
        
        if not isinstance(num_elements, int):
            raise ProgrammingErrorException("number of elements must be an integer")
        
        var_type = self.type_by_python_type(cursor, var_type)
    
        var = self.new(cursor, num_elements, var_type, var_type.size)
        var.make_array()
        
        return var

    def type_by_python_type(self, cursor, type):
        """Return a variable type given a Python type object or NULL if the Python type does not have a corresponding
variable type."""
        
        if type == NUMBER:
            if cursor.numbersAsStrings:
                return vt_NumberAsString
            else:
                return vt_Float
        
        try:
            return mapping_python_type_to_variable_type[type]
        except KeyError:
            raise NotSupportedError("Variable_TypeByPythonType(): unhandled data type")


    def new_by_value(self, cursor, value, num_elements):
        """Allocate a new variable by looking at the type of the data."""
        if cursor.inputtypehandler is not None:
            return self.new_by_input_type_handler(cursor, cursor.inputtypehandler, value, num_elements)
        if cursor.connection.inputtypehandler is not None:
            return self.new_by_input_type_handler(cursor, cursor.connection.inputtypehandler, value, num_elements)
        
        return self.default_new_by_value(cursor, value, num_elements)
    
    def new_by_input_type_handler(self, cursor, input_type_handler, value, num_elements):
        """Allocate a new variable by looking at the type of the data."""
        var = input_type_handler(cursor, value, num_elements)

        if var is not None:
            if not isinstance(var, Variable):
                raise TypeError("expecting variable from input type handler")

            return var

        return self.default_new_by_value(cursor, value, num_elements)

    def default_new_by_value(self, cursor, value, num_elements):
        """Default method for determining the type of variable to use for the data."""

        var_type, size, new_num_elements = self.type_by_value(value)
        
        if new_num_elements:
            num_elements = new_num_elements
        
        var = self.new(cursor, num_elements, var_type, size)
        if isinstance(value, list):
            var.make_array()

        return var

    def type_by_value(self, value):
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
                size = len(value)
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

            var_type, _, _ = self.type_by_value(element_value)
            num_elements = len(value)
            size = var_type.size
            return var_type, size, num_elements

        raise NotSupportedError("Variable_TypeByValue(): unhandled data type %.*s" % type(value))
    
    def new(self, cursor, num_elements, type, size):
        variable_class = mapping_variable_type_to_python_type.get(type)
        
        if variable_class is None:
            raise NotSupportedError('Type %s (%s) not found in mapping to python type' % (type, vt_to_name[type]))
        
        var = variable_class(cursor, num_elements, type, size)
        
        return var