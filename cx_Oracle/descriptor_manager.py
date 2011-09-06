import oci
from ctypes import byref

class DescriptorManager(object):
    def finalize(self, variable_type, var, oracle_descriptor_type):
        typed_data = variable_type.get_typed_data()
        for i in xrange(var.allocelems):
            if typed_data[i]:
                oci.OCIDescriptorFree(typed_data[i], oracle_descriptor_type)
                
    def initialize(self, variable_type, var, cursor, oracle_descriptor_type, message):
        typed_data = variable_type.get_typed_data(var)
        # initialize the LOB locators
        for i in xrange(var.allocelems):
            status = oci.OCIDescriptorAlloc(var.environment.handle, byref(typed_data[i]), oracle_descriptor_type, 0, 0)
            var.environment.check_for_error(status, message)