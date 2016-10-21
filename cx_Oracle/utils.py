import sys
import operator

# Python3 compatibility names - maybe I could use six here
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
    cxString = str 
else:
    cxBinary = buffer
    cxString = bytes

def is_sequence(obj):
    try:
        from collections import Sequence
    except ImportError:
        from operator import isSequenceType
        return operator.isSequenceType(obj)
    else:
        return isinstance(obj, Sequence)

if python3_or_better():
    xrange = range
    dict_iteritems = dict.items
else:
    xrange = xrange
    dict_iteritems = dict.iteritems

# C constants
INT_MAX = 2147483647 # both GCC and VS seem to define at this value for 32 and 64 bits

DRIVER_NAME = 'cx_Oracle-0.1'

MAX_STRING_CHARS = 4000
MAX_BINARY_BYTES = 4000
