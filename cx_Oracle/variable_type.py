import ctypes

import oci

class VariableType(object):
    def __init__(self):
        #self.initialize_proc = None
        #self.finalize_proc = None
        #self.pre_define_proc = None
        #self.post_define_proc = None
        #self.pre_fetch_proc = None
        #self.is_null_proc = None
        #self.set_value_proc = None
        #self.get_value_proc = None
        #self.get_buffer_size_proc = None
        self.python_type = None
        self.oracle_type = None
        self.charset_form = None
        self.size = None
        self.is_character_data = None
        self.is_variable_length = None
        self.can_be_copied = None
        self.can_be_in_array = None
        
        #self.oci_type = oci.SOME_OCI_TYPE
    
    def initialize_proc(self, var, cursor):
        raise NotImplementedError()

    def get_buffer_size_proc(self, var):
        raise NotImplementedError()
    
    def finalize_proc(self, var):
        raise NotImplementedError()
    
    def pre_define_proc(self, *args, **kwargs):
        raise NotImplementedError()

    def post_define_proc(self, *args, **kwargs):
        raise NotImplementedError()

    def pre_fetch_proc(self, var):
        raise NotImplementedError()

    def is_null_proc(self, *args, **kwargs):
        raise NotImplementedError()

    def set_value_proc(self, var, pos, value):
        raise NotImplementedError()

    def get_value_proc(self, var, pos):
        raise NotImplementedError()
    
    # Not cx_Oracle
    
    def get_typed_data(self, var):
        return ctypes.cast(var.data, oci.POINTER(self.oci_type))