import oci
import ctypes
from ctypes import byref

def oracle_number_to_python_float(environment, value):
    c_double_value = ctypes.c_double()
    status = oci.OCINumberToReal(environment.error_handle, value, ctypes.sizeof(c_double_value), byref(c_double_value))
    environment.check_for_error(status, "OracleNumberToPythonFloat()")

    return c_double_value.value
