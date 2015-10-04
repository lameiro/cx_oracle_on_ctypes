import oci
from ctypes import byref, cast, POINTER, c_void_p

class DescriptorManager(object):
    def finalize(self, variable_type, var, oracle_descriptor_type):
        typed_data = variable_type.get_typed_data(var)
        for i in xrange(var.allocelems):
            if typed_data[i]:
                oci.OCIDescriptorFree(typed_data[i], oracle_descriptor_type)
                
    def initialize(self, variable_type, var, cursor, oracle_descriptor_type, message):
        typed_data = variable_type.get_typed_data(var)

        arg4 = oci.OCIDescriptorAlloc.argtypes[4]()
        for i in xrange(var.allocelems):
            element = typed_data[i]
            element_cast = cast(byref(element), POINTER(c_void_p)) # type must be void **
            status = oci.OCIDescriptorAlloc(var.environment.handle, element_cast,
                                            oracle_descriptor_type, 0, arg4)
            var.environment.check_for_error(status, message)