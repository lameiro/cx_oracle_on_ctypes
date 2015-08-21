import sys
import ctypes
import oci
import operator


def python3_or_better():
    return sys.version_info.major >= 3


def python2():
    return sys.version_info.major == 2

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

is_sequence = operator.isSequenceType

DRIVER_NAME = 'cx_Oracle-0.1'

MAX_STRING_CHARS = 4000
MAX_BINARY_BYTES = 4000

class AnythingGoes(object):
    def from_param(self, val):
        return val

class ReplaceArgtypeByVoidPointerContextManager(object):
    def __init__(self, oci_function, pos):
        self.oci_function = oci_function
        self.pos = pos
    
    def __enter__(self):
        self.old_argtypes = self.oci_function.argtypes
        self.oci_function.argtypes = self.old_argtypes[:self.pos] + [AnythingGoes()] + self.old_argtypes[self.pos+1:]
        
    def __exit__(self):
        self.oci_function.argtypes = self.old_argtypes