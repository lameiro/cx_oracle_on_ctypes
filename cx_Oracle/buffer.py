# -----------------------------------------------------------------------------
# Buffer.c
#   Defines buffer structure and routines for populating it. These are used
# to translate Python objects into the buffers needed for Oracle, including
# Unicode or buffer objects.
# -----------------------------------------------------------------------------

import ctypes
from custom_exceptions import CXORA_TYPE_ERROR
from utils import bytes, python2
import oci

class cxBuffer(object):
    # not using a ctypes.structure here because we don't really use it as a struct.
    def __init__(self, ptr, size, num_characters, obj):
        self.ptr = ptr
        self.size = size
        self.num_characters = num_characters
        self.obj = obj
        
        self.cast_ptr = ctypes.cast(ptr, ctypes.POINTER(oci.ub1))
    
    @staticmethod
    def new_as_copy(copy_from_buf):
        """Copy the contents of the buffer."""

        result = cxBuffer(
            copy_from_buf.ptr,  # shares the ptr!
            copy_from_buf.size,
            copy_from_buf.num_characters,
            copy_from_buf.obj
        )
        
        return result

    @staticmethod
    def new_from_object(obj, encoding):
        """Populate the string buffer from a unicode object."""
        
        if obj is None:
            return cxBuffer.new_null()

        if isinstance(obj, unicode):
            as_bytes = obj.encode(encoding)
        elif isinstance(obj, bytes):
            as_bytes = obj
        elif python2() and isinstance(obj, buffer):  # this is not cxBuffer, but the Python2 buffer
            as_bytes = str(obj) # PyObject_AsReadBuffer in cx_Oracle. TODO: maybe this will reallocate memory?
        else:
            raise TypeError(CXORA_TYPE_ERROR)
        
        typed_ptr = ctypes.create_string_buffer(as_bytes)
        result = cxBuffer(
            typed_ptr,
            len(as_bytes),
            len(obj),
            obj,
        )
        result.keepalive = typed_ptr
        
        return result
    
    @staticmethod
    def new_null():
        result = cxBuffer(
            ctypes.c_void_p(),
            0,
            0,
            None
        )
        
        return result
