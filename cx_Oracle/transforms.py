import ctypes
from ctypes import byref
from datetime import date, datetime, timedelta

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

def oracle_timestamp_to_python_date(environment, value):
    """Return a Python date object given an Oracle timestamp."""
    year = oci.sb2()
    month = oci.ub1()
    day = oci.ub1()
    hour = oci.ub1()
    minute = oci.ub1()
    second = oci.ub1()
    fsecond = oci.ub4()
    
    status = oci.OCIDateTimeGetDate(environment.handle, environment.error_handle,
                                    value, byref(year), byref(month), byref(day))
    environment.check_for_error(status, "OracleTimestampToPythonDate(): date portion")
    
    status = oci.OCIDateTimeGetTime(environment.handle, environment.error_handle,
                                    value, byref(hour), byref(minute), byref(second), byref(fsecond))
    environment.check_for_error(status, "OracleTimestampToPythonDate(): time portion")
    
    return datetime(year.value, month.value, day.value, hour.value, minute.value, second.value, fsecond.value / 1000)

def oracle_interval_to_python_delta(environment, value):
    days = oci.sb4()
    hours = oci.sb4()
    minutes = oci.sb4()
    seconds = oci.sb4()
    fseconds = oci.sb4()
    
    status = oci.OCIIntervalGetDaySecond(environment.handle, environment.error_handle, byref(days), 
                                         byref(hours), byref(minutes), byref(seconds), byref(fseconds),
                                         value)
    environment.check_for_error(status, "OracleIntervalToPythonDelta()")
    seconds = hours.value * 3600 + minutes.value * 60 + seconds.value
    return timedelta(days=days.value, seconds=seconds, microseconds=fseconds.value/1000)