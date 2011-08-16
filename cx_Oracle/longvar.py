import oci
from variable_type import VariableType

class LONG_STRING(object):
    pass

class LONG_BINARY(object):
    pass

class LongVarBaseType(VariableType):
    def __init__(self):
        VariableType.__init__(self)
        self.initialize_proc = None
        self.finalize_proc = None
        self.pre_define_proc = None
        self.post_define_proc = None
        self.pre_fetch_proc = None
        self.is_null_proc = None
        self.set_value_proc = self.set_value
        self.get_value_proc = self.get_value
        self.get_buffer_size_proc = self.get_buffer_size
        self.charset_form = oci.SQLCS_IMPLICIT
        self.size = 128 * 1024
        self.is_variable_length = True
        self.can_be_copied = True
        self.can_be_in_array = False

    def set_value(self):
        raise NotImplementedError()

    def get_value(self):
        raise NotImplementedError()

    def get_buffer_size(self):
        raise NotImplementedError()

class LongStringVariableType(LongVarBaseType):
    def __init__(self):
        LongVarBaseType.__init__(self)
        self.python_type = LONG_STRING
        self.oracle_type = oci.SQLT_LVC
        self.is_character_data = True

class LongBinaryVariableType(LongVarBaseType):
    def __init__(self):
        LongVarBaseType.__init__(self)
        self.python_type = LONG_BINARY
        self.oracle_type = oci.SQLT_LVB
        self.is_character_data = False

vt_LongString = LongStringVariableType()
vt_LongBinary = LongBinaryVariableType()
