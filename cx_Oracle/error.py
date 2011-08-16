from ctypes import byref
import ctypes
from custom_exceptions import InternalError
import oci

class Error(object):
    def __init__(self, environment, context, retrieve_error):
        self.context = context
        if retrieve_error:
            if environment.error_handle:
                handle = environment.error_handle
                handle_type = oci.OCI_HTYPE_ERROR
            else:
                handle = environment.handle
                handle_type = oci.OCI_HTYPE_ENV

            error_text = ctypes.create_string_buffer(4096)
            c_code = oci.sb4()
            status = oci.OCIErrorGet(handle, 1, 0, byref(c_code), error_text, len(error_text), handle_type)
            self.code = c_code.value
            if status != oci.OCI_SUCCESS:
                raise InternalError("No Oracle error?")

    ##if PY_MAJOR_VERSION < 3 # TODO
            self.message = error_text.value
    ##else
    #       self.message = errorText.decode(environment.encoding)
    #endif

    def __str__(self):
        return self.message
