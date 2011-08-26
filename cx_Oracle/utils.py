import sys
import ctypes

def python3_or_better():
    return sys.version_info.major >= 3

if python3_or_better():
    def cxString_from_ascii(a_str):
        return a_str.decode('ascii')
    def cxString_from_encoded_string(a_str, encoding): # removed num bytes
        return a_str.decode(encoding)
else:
    # not very sure in this part
    def cxString_from_ascii(a_str):
        return a_str
    def cxString_from_encoded_string(a_str, encoding): # removed num bytes
        return a_str

try:
    bytes = bytes # puts bytes in the local namespace
except NameError:
    bytes = str

if python3_or_better():
    cxBinary = bytes
    cxString = unicode
else:
    cxBinary = buffer
    cxString = bytes

PySequence_Check = ctypes.pythonapi.PySequence_Check
PySequence_Check.argtypes = [ctypes.py_object]
PySequence_Check.restype = bool

is_sequence = PySequence_Check

DRIVER_NAME = 'cx_Oracle-0.1'

MAX_STRING_CHARS = 4000
MAX_BINARY_BYTES = 4000

