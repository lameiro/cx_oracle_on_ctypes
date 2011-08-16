#-----------------------------------------------------------------------------
# Buffer.c
#   Defines buffer structure and routines for populating it. These are used
# to translate Python objects into the buffers needed for Oracle, including
# Unicode or buffer objects.
#-----------------------------------------------------------------------------

import ctypes
from custom_exceptions import CXORA_TYPE_ERROR

# define structure for abstracting string buffers
class cxBufferStruct(ctypes.Structure):
    _fields_  = [
        ('ptr', ctypes.c_void_p),
        ('num_characters', ctypes.c_ssize_t),
        ('size', ctypes.c_ssize_t),
        ('obj', ctypes.py_object)
    ]

class cxBuffer(object):
    def __init__(self):
        self._as_parameter_ = self.c_struct = cxBufferStruct()

    @staticmethod
    def new_as_copy(copy_from_buf):
        """Copy the contents of the buffer."""

        # could use struct constructor here.
        result = cxBuffer()
        buf = result.c_struct

        buf.ptr = copy_from_buf.ptr
        buf.size = copy_from_buf.size
        buf.numCharacters = copy_from_buf.numCharacters
        buf.obj = copy_from_buf.obj

        return result

    @staticmethod
    def new_from_object(obj, encoding):
        """Populate the string buffer from a unicode object."""

        result = cxBuffer()

        if obj is None:
            return result
        
        if isinstance(obj, unicode):
            as_bytes = obj.encode(encoding)
        elif isinstance(obj, str):
            as_bytes = obj
        else:
            raise TypeError(CXORA_TYPE_ERROR) # missing import
        
        buf = result.c_struct
        buf.ptr = ctypes.cast(ctypes.create_string_buffer(as_bytes), ctypes.c_void_p)
        buf.size = len(as_bytes)
        buf.numCharacters = len(obj)

        return result

    @property
    def size(self):
        return self.c_struct.size
