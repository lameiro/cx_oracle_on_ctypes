import ctypes
from ctypes import byref, cast, c_void_p, POINTER

from cx_Oracle import oci


def OCIAttrGet(handle, oci_function, oci_type, oci_subfunction, environment, context):
    c_result = oci_type()
    argtypes = oci.OCIAttrGet.argtypes
    status = oci.OCIAttrGet(handle, oci_function, byref(c_result), argtypes[3](), oci_subfunction, environment.error_handle)
    environment.check_for_error(status, context)
    return c_result.value

def OCIAttrGet_nounwrap(handle, oci_function, oci_type, oci_subfunction, environment, context):
    c_result = oci_type()
    argtypes = oci.OCIAttrGet.argtypes
    status = oci.OCIAttrGet(handle, oci_function, byref(c_result), argtypes[3](), oci_subfunction, environment.error_handle)
    environment.check_for_error(status, context)
    return c_result

def OCIAttrSet(handle, handle_type, attribute_pointer, size, attribute_type, environment, context):
    status = oci.OCIAttrSet(handle, handle_type, attribute_pointer, size, attribute_type, environment.error_handle)
    environment.check_for_error(status, context)

def OCIParamGet(handle, htype, environment, pos, context):
    # cant pass cast_param to OCI and return non-cast param. ctypes doesn't know the cast param and the non-cast param are the same.
    param_type = oci.POINTER(oci.OCIParam)
    param = ctypes.c_void_p()
    # acquire parameter descriptor
    status = oci.OCIParamGet(handle, htype, environment.error_handle,
                             byref(param), pos)
    environment.check_for_error(status, context)
    
    result = ctypes.cast(param, param_type)
    return result

def OCIHandleAlloc(environment, handle, handle_type, error_message):
    # TODO: We should allocate the python-level pointer and return it, like the helpers above do
    argtypes = oci.OCIHandleAlloc.argtypes
    status = oci.OCIHandleAlloc(environment.handle, cast(byref(handle), POINTER(c_void_p)), handle_type, 0, argtypes[4]())

    environment.check_for_error(status, error_message)
