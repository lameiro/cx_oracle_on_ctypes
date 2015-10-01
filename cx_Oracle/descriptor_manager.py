import oci
from ctypes import byref
from utils import AnythingGoes

class DescriptorManager(object):
    def finalize(self, variable_type, var, oracle_descriptor_type):
        typed_data = variable_type.get_typed_data(var)
        for i in xrange(var.allocelems):
            if typed_data[i]:
                oci.OCIDescriptorFree(typed_data[i], oracle_descriptor_type)
                
    def initialize(self, variable_type, var, cursor, oracle_descriptor_type, message):
        typed_data = variable_type.get_typed_data(var)
        WrappedOCIDescriptorAlloc = oci.OCIDescriptorAlloc
        original_argtypes = oci.OCIDescriptorAlloc.argtypes
        WrappedOCIDescriptorAlloc.argtypes = [original_argtypes[0], AnythingGoes()] + original_argtypes[2:]
        arg4 = original_argtypes[4]()
        for i in xrange(var.allocelems):
            element = typed_data[i]
            status = WrappedOCIDescriptorAlloc(var.environment.handle, byref(element),
                                               oracle_descriptor_type, 0, arg4)
            var.environment.check_for_error(status, message)
