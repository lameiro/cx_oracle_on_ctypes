import ctypes
from ctypes import byref
from datetime import datetime

from variable_type import VariableType
import oci
from utils import python3_or_better, cxString_from_encoded_string
from buffer import cxBuffer
from variable import Variable

from descriptor_manager import DescriptorManager
from transforms import oracle_timestamp_to_python_date
from custom_exceptions import DataError

class TIMESTAMP(Variable):
    pass

class TimestampType(VariableType):
    def __init__(self):
        VariableType.__init__(self)
        self.oci_type = oci.POINTER(oci.OCIDateTime)
        
        self.initialize_proc = self.initialize
        self.finalize_proc = self.finalize
        self.pre_define_proc = None
        self.post_define_proc = None
        self.pre_fetch_proc = None
        self.is_null_proc = None
        self.set_value_proc = self.set_value
        self.get_value_proc = self.get_value
        self.get_buffer_size_proc = None
        
        self.python_type = TIMESTAMP
        self.oracle_type = oci.SQLT_TIMESTAMP
        self.charset_form = oci.SQLCS_IMPLICIT
        self.size = ctypes.sizeof(self.oci_type)
        self.is_character_data = False
        self.is_variable_length = False
        self.can_be_copied = True
        self.can_be_in_array = True
        
        self.descriptor_manager = DescriptorManager()
        
    def initialize(self, var, cursor):
        self.descriptor_manager.initialize(self, var, cursor, oci.OCI_DTYPE_TIMESTAMP, "TimestampVar_Initialize()")

    def finalize(self, var):
        self.descriptor_manager.finalize(self, var, oci.OCI_DTYPE_TIMESTAMP)
    
    def set_value(self, var, pos, value):
        # make sure a timestamp is being bound
        if not isinstance(value, datetime):
            raise TypeError("expecting timestamp data")
    
        typed_data = self.get_typed_data(var)
        # store a copy of the value
        status = oci.OCIDateTimeConstruct(var.environment.handle,
                var.environment.error_handle, typed_data[pos],
                value.year,
                value.month,
                value.day,
                value.hour,
                value.minute,
                value.second,
                value.microsecond * 1000, None, 0);
        var.environment.check_for_error(status, "TimestampVar_SetValue(): create structure")
        c_invalid = oci.uword()
        status = oci.OCIDateTimeCheck(var.environment.handle,
                var.environment.error_handle, typed_data[pos], byref(c_invalid))
        invalid = c_invalid.value
        var.environment.check_for_error(status, "TimestampVar_SetValue()")
        
        if invalid:
            raise DataError("invalid date")

    def get_value(self, var, pos):
        typed_data = self.get_typed_data(var)
        return oracle_timestamp_to_python_date(var.environment, typed_data[pos])

vt_Timestamp = TimestampType()