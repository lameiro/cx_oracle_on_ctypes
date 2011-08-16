import ctypes
from ctypes import byref

from variable_type import VariableType
import oci
from utils import python3_or_better, cxString_from_encoded_string
from utils import MAX_STRING_CHARS, MAX_BINARY_BYTES
from buffer import cxBuffer

class STRING(object):
    pass

if not python3_or_better():
    class UNICODE(object):
        pass

    class FIXED_UNICODE(object):
        pass

class FIXED_CHAR(object):
    pass

class ROWID(object):
    pass

class BINARY(object):
    pass

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

        if var.type.is_character_data and buffer.c_struct.num_characters > MAX_STRING_CHARS:
            raise ValueError("string data too large")
        elif not var.type.is_character_data and buffer.c_struct.size > MAX_BINARY_BYTES:
            raise ValueError("binary data too large")

        # ensure that the buffer is large enough
        if buffer.c_struct.size > var.bufferSize:
            var.resize(buffer.c_struct.num_characters)

        # keep a copy of the string
        var.actual_length[pos] = buffer.c_struct.size
        if buffer.c_struct.size:
            ctypes.memmove(byref(var.data, var.bufferSize * pos), buffer.c_struct.ptr, buffer.c_struct.size)

class StringType(BaseStringType):
    def __init__(self):
        BaseStringType.__init__(self)        
        self.get_buffer_size_proc = self.get_buffer_size
        self.python_type = STRING
        self.oracle_type = oci.SQLT_CHR
        self.charset_form = oci.SQLCS_IMPLICIT
        self.size = MAX_STRING_CHARS
        
        self.is_character_data = True
        self.is_variable_length = True
    
    def get_buffer_size(self, var):
        if var.type.is_character_data:
            return var.size * var.environment.maxBytesPerCharacter
        return var.size

class BinaryType(BaseStringType):
    def __init__(self):
        BaseStringType.__init__(self)
        self.python_type = BINARY
        self.oracle_type = oci.SQLT_BIN
        self.charset_form = oci.SQLCS_IMPLICIT
        self.size = MAX_BINARY_BYTES
        
        self.is_character_data = False
        self.is_variable_length = True


vt_String = StringType()
vt_Binary = BinaryType()

# TODO
vt_FixedNationalChar = VariableType()
vt_NationalCharString = VariableType()
vt_FixedChar = VariableType()
vt_Rowid = VariableType()
