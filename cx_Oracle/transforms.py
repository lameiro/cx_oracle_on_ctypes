import ctypes
from ctypes import byref
from datetime import date, datetime

import oci

def oracle_number_to_python_float(environment, value):
    c_double_value = ctypes.c_double()
    status = oci.OCINumberToReal(environment.error_handle, value, ctypes.sizeof(c_double_value), byref(c_double_value))
    environment.check_for_error(status, "OracleNumberToPythonFloat()")

    return c_double_value.value


def oracle_date_to_python_date(value, python_datetime):
    year, month, day = oci.OCIDateGetDate(value)
    hour, minute, second = oci.OCIDateGetTime(value)

    if python_datetime:
        return datetime(year, month, day, hour, minute, second);
    
    return date(year, month, day)