import ctypes
from ctypes import byref

from variable_type import VariableType
import oci
from utils import python3_or_better, cxString_from_encoded_string
from utils import MAX_STRING_CHARS, MAX_BINARY_BYTES
from buffer import cxBuffer
from variable import Variable

# TODO: Deduplicate method set_max_data_size in STRING and FIXED_CHAR

class STRING(Variable):
    def set_max_data_size(self):
        if (self.type == vt_String or self.type == vt_FixedChar) and self.size > self.type.size:
            c_size = oci.ub4()
            status = oci.OCIAttrSet(self.bind_handle, oci.OCI_HTYPE_BIND,
                    byref(c_size), 0, oci.OCI_ATTR_MAXDATA_SIZE,
                    self.environment.error_handle)
            self.type.size = c_size.value
            self.environment.check_for_error(status, "Variable_InternalBind(): set max data size")
            
    @staticmethod
    def get_display_size(precision, scale, char_size, internal_size):
        return char_size

if not python3_or_better():
    class UNICODE(Variable):
        @staticmethod
        def get_display_size(precision, scale, char_size, internal_size):
            return char_size

    class FIXED_UNICODE(Variable):
        @staticmethod
        def get_display_size(precision, scale, char_size, internal_size):
            return char_size

class FIXED_CHAR(Variable):
    def set_max_data_size(self):
        if (self.type == vt_String or self.type == vt_FixedChar) and self.size > self.type.size:
            c_size = oci.ub4()
            status = oci.OCIAttrSet(self.bind_handle, oci.OCI_HTYPE_BIND,
                    byref(c_size), 0, oci.OCI_ATTR_MAXDATA_SIZE,
                    self.environment.error_handle)
            self.type.size = c_size.value
            self.environment.check_for_error(status, "Variable_InternalBind(): set max data size")
            
    @staticmethod
    def get_display_size(precision, scale, char_size, internal_size):
        return char_size


class ROWID(Variable):
    pass

class BINARY(Variable):
    @staticmethod
    def get_display_size(precision, scale, char_size, internal_size):
        return internal_size


class BaseStringType(VariableType):
    def __init__(self):
        VariableType.__init__(self)
        self.initialize_proc = self.initialize
        self.finalize_proc = None
        self.pre_define_proc = None
        #self.post_define_proc = None
        self.pre_fetch_proc = None
        self.is_null_proc = None
        self.set_value_proc =  self.set_value
        self.get_value_proc =  self.get_value
        #self.get_buffer_size_proc = None

        #self.is_character_data = None
        #self.is_variable_length = None
        self.can_be_copied = True
        self.can_be_in_array = True

    def initialize(self, var, cursor):
        var.actual_length = (oci.ub2 * var.numElements)()

    def get_value(self, var, pos):
        """Returns the value stored at the given array position."""
        data_start_index = pos * var.bufferSize # was pointer arithmetic

        the_data = var.data[data_start_index:data_start_index+var.actual_length[pos]]
        if var.type is vt_Binary:
            return the_data
            
        if not python3_or_better():
            if var.type in (vt_FixedNationalChar, vt_NationalCharString):
                return the_data.decode(var.environment.nencoding)
    
        return cxString_from_encoded_string(the_data, var.environment.encoding)

    def set_value(self, var, pos, value):
        # populate the buffer and confirm the maximum size is not exceeded
        buffer = cxBuffer.new_from_object(value, var.environment.encoding)

        if var.type.is_character_data and buffer.num_characters > MAX_STRING_CHARS:
            raise ValueError("string data too large")
        elif not var.type.is_character_data and buffer.size > MAX_BINARY_BYTES:
            raise ValueError("binary data too large")

        # ensure that the buffer is large enough
        if buffer.size > var.bufferSize:
            var.resize(buffer.num_characters)

        # keep a copy of the string
        var.actual_length[pos] = buffer.size
        if buffer.size:
            ctypes.memmove(byref(var.data, var.bufferSize * pos), buffer.ptr, buffer.size)

class BaseNonBinaryStringType(BaseStringType):
    def __init__(self):
        BaseStringType.__init__(self)
        #self.post_define_proc = None
        self.get_buffer_size_proc = self.get_buffer_size
        self.is_character_data = True
        #self.is_variable_length = None
    
    def get_buffer_size(self, var):
        if var.type.is_character_data:
            return var.size * var.environment.maxBytesPerCharacter
        return var.size

class StringType(BaseNonBinaryStringType):
    def __init__(self):
        BaseNonBinaryStringType.__init__(self)
        self.post_define_proc = None
        self.python_type = STRING
        self.oracle_type = oci.SQLT_CHR
        self.charset_form = oci.SQLCS_IMPLICIT
        self.size = MAX_STRING_CHARS
        
        self.is_variable_length = True
        
class FixedCharType(BaseNonBinaryStringType):
    def __init__(self):
        BaseNonBinaryStringType.__init__(self)
        self.post_define_proc = None
        self.python_type = FIXED_CHAR
        self.oracle_type = oci.SQLT_AFC
        self.charset_form = oci.SQLCS_IMPLICIT
        self.size = 2000
        
        self.is_variable_length = True
        
class RowIdType(BaseNonBinaryStringType):
    def __init__(self):
        BaseNonBinaryStringType.__init__(self)
        self.post_define_proc = None
        self.python_type = ROWID
        self.oracle_type = oci.SQLT_CHR
        self.charset_form = oci.SQLCS_IMPLICIT
        self.size = 18
        
        self.is_variable_length = False
    

class BinaryType(BaseStringType):
    def __init__(self):
        BaseStringType.__init__(self)
        self.post_define_proc = None
        self.get_buffer_size_proc = None
        
        self.python_type = BINARY
        self.oracle_type = oci.SQLT_BIN
        self.charset_form = oci.SQLCS_IMPLICIT
        self.size = MAX_BINARY_BYTES
        
        self.is_character_data = False
        self.is_variable_length = True


vt_String = StringType()
vt_Binary = BinaryType()
vt_FixedChar = FixedCharType()
vt_Rowid = RowIdType()

# TODO
vt_FixedNationalChar = VariableType()
vt_NationalCharString = VariableType()

