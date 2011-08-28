import oci
import ctypes
from ctypes import byref

from variable import Variable
from variable_type import VariableType
from transforms import oracle_date_to_python_date

from datetime import date, datetime

class DATETIME(Variable):
    @staticmethod
    def get_display_size(precision, scale, char_size, internal_size):
        return 23
    
class DateTimeVariableType(VariableType):
    def __init__(self):
        self.oci_type = oci.OCIDate
        
        self.initialize_proc = None
        self.finalize_proc = None
        self.pre_define_proc = None
        self.post_define_proc = None
        self.pre_fetch_proc = None
        self.is_null_proc = None
        self.set_value_proc = self.set_value
        self.get_value_proc = self.get_value
        self.get_buffer_size_proc = None
        self.python_type = DATETIME
        self.oracle_type = oci.SQLT_ODT
        self.charset_form = oci.SQLCS_IMPLICIT
        self.size = ctypes.sizeof(self.oci_type)
        self.is_character_data = False
        self.is_variable_length = False
        self.can_be_copied = True
        self.can_be_in_array = True
        
    def set_value(self, var, pos, value):
        if isinstance(value, datetime):
            year = value.year
            month = value.month
            day = value.day
            hour = value.hour
            minute = value.minute
            second = value.second
        elif isinstance(value, date):
            year = value.year
            month = value.month
            day = value.day
            hour = minute = second = 0;
        else:
            raise TypeError("expecting date data")
        
        typed_data = self.get_typed_data(var)
        
        # store a copy of the value
        oci.OCIDateSetDate(typed_data[pos], year, month, day)
        oci.OCIDateSetTime(typed_data[pos], hour, minute, second)

    def get_value(self, var, pos):
        typed_data = self.get_typed_data(var)
        return_datetime = var.type == vt_DateTime
        return oracle_date_to_python_date(typed_data[pos], return_datetime)
    
vt_DateTime = DateTimeVariableType()
vt_Date = DateTimeVariableType()