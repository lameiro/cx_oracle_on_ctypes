'''Wrapper for oci.h

Generated with:
/home/lameiro/projects/ctypesgen/ctypesgen.py /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h -I /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include -o oci_generated_10.py -l libclntsh.so.10.1

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

#def POINTER(obj):
    #p = ctypes.POINTER(obj)

    ## Convert None to a real NULL pointer to work around bugs
    ## in how ctypes handles None on 64-bit platforms
    #if not isinstance(p.from_param, classmethod):
        #def from_param(cls, x):
            #if x is None:
                #return cls()
            #else:
                #return x
        #p.from_param = classmethod(from_param)

    #return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

# MANUALLY changed: fix for windows, which has a different library name
if sys.platform == 'win32':
    _libs["libclntsh.so.10.1"] = load_library("oci.dll")
else:
    _libs["libclntsh.so.10.1"] = load_library("libclntsh.so.10.1")


# 1 libraries
# End libraries

# No modules

ub1 = c_ubyte # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 29

sb1 = c_char # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 30

ub2 = c_ushort # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 71

sb2 = c_short # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 72

ub4 = c_uint # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 110

sb4 = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 111

oraub8 = c_ulonglong # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 144

oratext = c_ubyte # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 188

text = oratext # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 196

OraText = oratext # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 197

boolean = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 216

eword = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 225

uword = c_uint # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 226

sword = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 227

ubig_ora = c_ulong # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 253

sbig_ora = c_long # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 254

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 94
class struct_anon_17(Structure):
    pass

struct_anon_17.__slots__ = [
    'rcs4',
    'rcs5',
    'rcs6',
]
struct_anon_17._fields_ = [
    ('rcs4', ub4),
    ('rcs5', ub2),
    ('rcs6', ub1),
]

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 93
class struct_anon_18(Structure):
    pass

struct_anon_18.__slots__ = [
    'rd',
    'rcs7',
    'rcs8',
]
struct_anon_18._fields_ = [
    ('rd', struct_anon_17),
    ('rcs7', ub4),
    ('rcs8', ub2),
]

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 82
class struct_cda_head(Structure):
    pass

struct_cda_head.__slots__ = [
    'v2_rc',
    'ft',
    'rpc',
    'peo',
    'fc',
    'rcs1',
    'rc',
    'wrn',
    'rcs2',
    'rcs3',
    'rid',
    'ose',
    'chk',
    'rcsp',
]
struct_cda_head._fields_ = [
    ('v2_rc', sb2),
    ('ft', ub2),
    ('rpc', ub4),
    ('peo', ub2),
    ('fc', ub1),
    ('rcs1', ub1),
    ('rc', ub2),
    ('wrn', ub1),
    ('rcs2', ub1),
    ('rcs3', sword),
    ('rid', struct_anon_18),
    ('ose', sword),
    ('chk', ub1),
    ('rcsp', POINTER(None)),
]

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 138
class struct_anon_19(Structure):
    pass

struct_anon_19.__slots__ = [
    'rcs4',
    'rcs5',
    'rcs6',
]
struct_anon_19._fields_ = [
    ('rcs4', ub4),
    ('rcs5', ub2),
    ('rcs6', ub1),
]

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 137
class struct_anon_20(Structure):
    pass

struct_anon_20.__slots__ = [
    'rd',
    'rcs7',
    'rcs8',
]
struct_anon_20._fields_ = [
    ('rd', struct_anon_19),
    ('rcs7', ub4),
    ('rcs8', ub2),
]

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 126
class struct_cda_def(Structure):
    pass

struct_cda_def.__slots__ = [
    'v2_rc',
    'ft',
    'rpc',
    'peo',
    'fc',
    'rcs1',
    'rc',
    'wrn',
    'rcs2',
    'rcs3',
    'rid',
    'ose',
    'chk',
    'rcsp',
    'rcs9',
]
struct_cda_def._fields_ = [
    ('v2_rc', sb2),
    ('ft', ub2),
    ('rpc', ub4),
    ('peo', ub2),
    ('fc', ub1),
    ('rcs1', ub1),
    ('rc', ub2),
    ('wrn', ub1),
    ('rcs2', ub1),
    ('rcs3', sword),
    ('rid', struct_anon_20),
    ('ose', sword),
    ('chk', ub1),
    ('rcsp', POINTER(None)),
    ('rcs9', ub1 * (64 - sizeof(struct_cda_head))),
]

Cda_Def = struct_cda_def # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 152

Lda_Def = struct_cda_def # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 156

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2324
class struct_OCIEnv(Structure):
    pass

OCIEnv = struct_OCIEnv # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2324

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2325
class struct_OCIError(Structure):
    pass

OCIError = struct_OCIError # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2325

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2326
class struct_OCISvcCtx(Structure):
    pass

OCISvcCtx = struct_OCISvcCtx # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2326

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2327
class struct_OCIStmt(Structure):
    pass

OCIStmt = struct_OCIStmt # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2327

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2328
class struct_OCIBind(Structure):
    pass

OCIBind = struct_OCIBind # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2328

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2329
class struct_OCIDefine(Structure):
    pass

OCIDefine = struct_OCIDefine # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2329

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2330
class struct_OCIDescribe(Structure):
    pass

OCIDescribe = struct_OCIDescribe # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2330

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2331
class struct_OCIServer(Structure):
    pass

OCIServer = struct_OCIServer # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2331

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2332
class struct_OCISession(Structure):
    pass

OCISession = struct_OCISession # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2332

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2333
class struct_OCIComplexObject(Structure):
    pass

OCIComplexObject = struct_OCIComplexObject # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2333

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2334
class struct_OCITrans(Structure):
    pass

OCITrans = struct_OCITrans # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2334

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2335
class struct_OCISecurity(Structure):
    pass

OCISecurity = struct_OCISecurity # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2335

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2336
class struct_OCISubscription(Structure):
    pass

OCISubscription = struct_OCISubscription # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2336

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2338
class struct_OCICPool(Structure):
    pass

OCICPool = struct_OCICPool # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2338

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2339
class struct_OCISPool(Structure):
    pass

OCISPool = struct_OCISPool # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2339

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2340
class struct_OCIAuthInfo(Structure):
    pass

OCIAuthInfo = struct_OCIAuthInfo # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2340

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2341
class struct_OCIAdmin(Structure):
    pass

OCIAdmin = struct_OCIAdmin # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2341

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2342
class struct_OCIEvent(Structure):
    pass

OCIEvent = struct_OCIEvent # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2342

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2345
class struct_OCISnapshot(Structure):
    pass

OCISnapshot = struct_OCISnapshot # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2345

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2346
class struct_OCIResult(Structure):
    pass

OCIResult = struct_OCIResult # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2346

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2347
class struct_OCILobLocator(Structure):
    pass

OCILobLocator = struct_OCILobLocator # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2347

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2348
class struct_OCIParam(Structure):
    pass

OCIParam = struct_OCIParam # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2348

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2349
class struct_OCIComplexObjectComp(Structure):
    pass

OCIComplexObjectComp = struct_OCIComplexObjectComp # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2349

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2351
class struct_OCIRowid(Structure):
    pass

OCIRowid = struct_OCIRowid # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2351

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2353
class struct_OCIDateTime(Structure):
    pass

OCIDateTime = struct_OCIDateTime # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2353

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2354
class struct_OCIInterval(Structure):
    pass

OCIInterval = struct_OCIInterval # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2354

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2356
class struct_OCIUcb(Structure):
    pass

OCIUcb = struct_OCIUcb # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2356

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2357
class struct_OCIServerDNs(Structure):
    pass

OCIServerDNs = struct_OCIServerDNs # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2357

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2360
class struct_OCIAQEnqOptions(Structure):
    pass

OCIAQEnqOptions = struct_OCIAQEnqOptions # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2360

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2361
class struct_OCIAQDeqOptions(Structure):
    pass

OCIAQDeqOptions = struct_OCIAQDeqOptions # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2361

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2362
class struct_OCIAQMsgProperties(Structure):
    pass

OCIAQMsgProperties = struct_OCIAQMsgProperties # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2362

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2363
class struct_OCIAQAgent(Structure):
    pass

OCIAQAgent = struct_OCIAQAgent # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2363

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2364
class struct_OCIAQNfyDescriptor(Structure):
    pass

OCIAQNfyDescriptor = struct_OCIAQNfyDescriptor # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2364

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2365
class struct_OCIAQSignature(Structure):
    pass

OCIAQSignature = struct_OCIAQSignature # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2365

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2366
class struct_OCIAQListenOpts(Structure):
    pass

OCIAQListenOpts = struct_OCIAQListenOpts # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2366

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2367
class struct_OCIAQLisMsgProps(Structure):
    pass

OCIAQLisMsgProps = struct_OCIAQLisMsgProps # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2367

OCIClobLocator = struct_OCILobLocator # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2372

OCIBlobLocator = struct_OCILobLocator # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2373

OCIBFileLocator = struct_OCILobLocator # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2374

OCILobOffset = ub4 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2395

OCILobLength = ub4 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2405

enum_OCILobMode = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2417

OCI_LOBMODE_READONLY = 1 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2417

OCI_LOBMODE_READWRITE = 2 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2417

OCILobMode = enum_OCILobMode # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2422

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2522
class struct_OCIPicklerTdsCtx(Structure):
    pass

OCIPicklerTdsCtx = struct_OCIPicklerTdsCtx # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2522

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2523
class struct_OCIPicklerTds(Structure):
    pass

OCIPicklerTds = struct_OCIPicklerTds # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2523

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2524
class struct_OCIPicklerImage(Structure):
    pass

OCIPicklerImage = struct_OCIPicklerImage # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2524

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2525
class struct_OCIPicklerFdo(Structure):
    pass

OCIPicklerFdo = struct_OCIPicklerFdo # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2525

OCIPicklerTdsElement = ub4 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2526

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2528
class struct_OCIAnyData(Structure):
    pass

OCIAnyData = struct_OCIAnyData # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2528

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2530
class struct_OCIAnyDataSet(Structure):
    pass

OCIAnyDataSet = struct_OCIAnyDataSet # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2530

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2531
class struct_OCIAnyDataCtx(Structure):
    pass

OCIAnyDataCtx = struct_OCIAnyDataCtx # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2531

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2638
class struct_OCIMsg(Structure):
    pass

OCIMsg = struct_OCIMsg # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2638

OCIWchar = ub4 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2639

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci1.h: 124
class struct_OCIFileObject(Structure):
    pass

OCIFileObject = struct_OCIFileObject # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci1.h: 124

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci1.h: 133
class struct_OCIThreadMutex(Structure):
    pass

OCIThreadMutex = struct_OCIThreadMutex # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci1.h: 133

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci1.h: 136
class struct_OCIThreadKey(Structure):
    pass

OCIThreadKey = struct_OCIThreadKey # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci1.h: 136

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci1.h: 139
class struct_OCIThreadId(Structure):
    pass

OCIThreadId = struct_OCIThreadId # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci1.h: 139

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci1.h: 142
class struct_OCIThreadHandle(Structure):
    pass

OCIThreadHandle = struct_OCIThreadHandle # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci1.h: 142

OCIThreadKeyDestFunc = CFUNCTYPE(UNCHECKED(None), ) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci1.h: 148

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 278
class struct_OCIRef(Structure):
    pass

OCIRef = struct_OCIRef # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 278

OCIInd = sb2 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 291

enum_OCIPinOpt = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 322

OCI_PIN_DEFAULT = 1 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 322

OCI_PIN_ANY = 3 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 322

OCI_PIN_RECENT = 4 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 322

OCI_PIN_LATEST = 5 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 322

OCIPinOpt = enum_OCIPinOpt # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 330

enum_OCILockOpt = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 368

OCI_LOCK_NONE = 1 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 368

OCI_LOCK_X = 2 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 368

OCI_LOCK_X_NOWAIT = 3 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 368

OCILockOpt = enum_OCILockOpt # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 375

enum_OCIMarkOpt = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 386

OCI_MARK_DEFAULT = 1 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 386

OCI_MARK_NONE = OCI_MARK_DEFAULT # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 386

OCI_MARK_UPDATE = (OCI_MARK_NONE + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 386

OCIMarkOpt = enum_OCIMarkOpt # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 393

OCIDuration = ub2 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 403

enum_OCIObjectProperty = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 469

OCI_OBJECTPROP_DIRTIED = 1 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 469

OCI_OBJECTPROP_LOADED = (OCI_OBJECTPROP_DIRTIED + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 469

OCI_OBJECTPROP_LOCKED = (OCI_OBJECTPROP_LOADED + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 469

OCIObjectProperty = enum_OCIObjectProperty # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 476

enum_OCIRefreshOpt = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 484

OCI_REFRESH_LOADED = 1 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 484

OCIRefreshOpt = enum_OCIRefreshOpt # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 489

enum_OCIObjectEvent = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 504

OCI_OBJECTEVENT_BEFORE_FLUSH = 1 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 504

OCI_OBJECTEVENT_AFTER_FLUSH = (OCI_OBJECTEVENT_BEFORE_FLUSH + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 504

OCI_OBJECTEVENT_BEFORE_REFRESH = (OCI_OBJECTEVENT_AFTER_FLUSH + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 504

OCI_OBJECTEVENT_AFTER_REFRESH = (OCI_OBJECTEVENT_BEFORE_REFRESH + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 504

OCI_OBJECTEVENT_WHEN_MARK_UPDATED = (OCI_OBJECTEVENT_AFTER_REFRESH + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 504

OCI_OBJECTEVENT_WHEN_MARK_DELETED = (OCI_OBJECTEVENT_WHEN_MARK_UPDATED + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 504

OCI_OBJECTEVENT_WHEN_UNMARK = (OCI_OBJECTEVENT_WHEN_MARK_DELETED + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 504

OCI_OBJECTEVENT_WHEN_LOCK = (OCI_OBJECTEVENT_WHEN_UNMARK + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 504

OCIObjectEvent = enum_OCIObjectEvent # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 516

OCIObjectPropId = ub1 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 548

enum_OCIObjectLifetime = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 565

OCI_OBJECT_PERSISTENT = 1 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 565

OCI_OBJECT_TRANSIENT = (OCI_OBJECT_PERSISTENT + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 565

OCI_OBJECT_VALUE = (OCI_OBJECT_TRANSIENT + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 565

OCIObjectLifetime = enum_OCIObjectLifetime # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 572

OCIObjectMarkStatus = uword # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 581

OCITypeCode = ub2 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 695

enum_OCITypeGetOpt = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 700

OCI_TYPEGET_HEADER = 0 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 700

OCI_TYPEGET_ALL = (OCI_TYPEGET_HEADER + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 700

OCITypeGetOpt = enum_OCITypeGetOpt # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 706

enum_OCITypeEncap = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 728

OCI_TYPEENCAP_PRIVATE = 0 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 728

OCI_TYPEENCAP_PUBLIC = (OCI_TYPEENCAP_PRIVATE + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 728

OCITypeEncap = enum_OCITypeEncap # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 734

enum_OCITypeMethodFlag = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_INLINE = 1 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_CONSTANT = 2 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_VIRTUAL = 4 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_CONSTRUCTOR = 8 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_DESTRUCTOR = 16 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_OPERATOR = 32 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_SELFISH = 64 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_MAP = 128 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_ORDER = 256 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_RNDS = 512 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_WNDS = 1024 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_RNPS = 2048 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_WNPS = 4096 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_ABSTRACT = 8192 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_OVERRIDING = 16384 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCI_TYPEMETHOD_PIPELINED = 32768 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 742

OCITypeMethodFlag = enum_OCITypeMethodFlag # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 764

enum_OCITypeParamMode = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 842

OCI_TYPEPARAM_IN = 0 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 842

OCI_TYPEPARAM_OUT = (OCI_TYPEPARAM_IN + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 842

OCI_TYPEPARAM_INOUT = (OCI_TYPEPARAM_OUT + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 842

OCI_TYPEPARAM_BYREF = (OCI_TYPEPARAM_INOUT + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 842

OCI_TYPEPARAM_OUTNCPY = (OCI_TYPEPARAM_BYREF + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 842

OCI_TYPEPARAM_INOUTNCPY = (OCI_TYPEPARAM_OUTNCPY + 1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 842

OCITypeParamMode = enum_OCITypeParamMode # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 852

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 694
class struct_OCIType(Structure):
    pass

OCIType = struct_OCIType # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 694

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 714
class struct_OCITypeElem(Structure):
    pass

OCITypeElem = struct_OCITypeElem # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 714

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 731
class struct_OCITypeMethod(Structure):
    pass

OCITypeMethod = struct_OCITypeMethod # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 731

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 746
class struct_OCITypeIter(Structure):
    pass

OCITypeIter = struct_OCITypeIter # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 746

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 760
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeIterNew'):
    OCITypeIterNew = _libs['libclntsh.so.10.1'].OCITypeIterNew
    OCITypeIterNew.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType), POINTER(POINTER(OCITypeIter))]
    OCITypeIterNew.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 788
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeIterSet'):
    OCITypeIterSet = _libs['libclntsh.so.10.1'].OCITypeIterSet
    OCITypeIterSet.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType), POINTER(OCITypeIter)]
    OCITypeIterSet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 815
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeIterFree'):
    OCITypeIterFree = _libs['libclntsh.so.10.1'].OCITypeIterFree
    OCITypeIterFree.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeIter)]
    OCITypeIterFree.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 843
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeByName'):
    OCITypeByName = _libs['libclntsh.so.10.1'].OCITypeByName
    OCITypeByName.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx), POINTER(oratext), ub4, POINTER(oratext), ub4, POINTER(oratext), ub4, OCIDuration, OCITypeGetOpt, POINTER(POINTER(OCIType))]
    OCITypeByName.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 891
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeArrayByName'):
    OCITypeArrayByName = _libs['libclntsh.so.10.1'].OCITypeArrayByName
    OCITypeArrayByName.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx), ub4, POINTER(POINTER(oratext)), POINTER(ub4), POINTER(POINTER(oratext)), POINTER(ub4), POINTER(POINTER(oratext)), POINTER(ub4), OCIDuration, OCITypeGetOpt, POINTER(POINTER(OCIType))]
    OCITypeArrayByName.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 961
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeByRef'):
    OCITypeByRef = _libs['libclntsh.so.10.1'].OCITypeByRef
    OCITypeByRef.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIRef), OCIDuration, OCITypeGetOpt, POINTER(POINTER(OCIType))]
    OCITypeByRef.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 998
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeArrayByRef'):
    OCITypeArrayByRef = _libs['libclntsh.so.10.1'].OCITypeArrayByRef
    OCITypeArrayByRef.argtypes = [POINTER(OCIEnv), POINTER(OCIError), ub4, POINTER(POINTER(OCIRef)), OCIDuration, OCITypeGetOpt, POINTER(POINTER(OCIType))]
    OCITypeArrayByRef.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1049
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeName'):
    OCITypeName = _libs['libclntsh.so.10.1'].OCITypeName
    OCITypeName.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType), POINTER(ub4)]
    OCITypeName.restype = POINTER(oratext)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1080
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeSchema'):
    OCITypeSchema = _libs['libclntsh.so.10.1'].OCITypeSchema
    OCITypeSchema.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType), POINTER(ub4)]
    OCITypeSchema.restype = POINTER(oratext)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1111
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeTypeCode'):
    OCITypeTypeCode = _libs['libclntsh.so.10.1'].OCITypeTypeCode
    OCITypeTypeCode.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType)]
    OCITypeTypeCode.restype = OCITypeCode

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1138
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeCollTypeCode'):
    OCITypeCollTypeCode = _libs['libclntsh.so.10.1'].OCITypeCollTypeCode
    OCITypeCollTypeCode.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType)]
    OCITypeCollTypeCode.restype = OCITypeCode

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1168
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeVersion'):
    OCITypeVersion = _libs['libclntsh.so.10.1'].OCITypeVersion
    OCITypeVersion.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType), POINTER(ub4)]
    OCITypeVersion.restype = POINTER(oratext)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1199
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeAttrs'):
    OCITypeAttrs = _libs['libclntsh.so.10.1'].OCITypeAttrs
    OCITypeAttrs.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType)]
    OCITypeAttrs.restype = ub4

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1225
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeMethods'):
    OCITypeMethods = _libs['libclntsh.so.10.1'].OCITypeMethods
    OCITypeMethods.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType)]
    OCITypeMethods.restype = ub4

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1256
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeElemName'):
    OCITypeElemName = _libs['libclntsh.so.10.1'].OCITypeElemName
    OCITypeElemName.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeElem), POINTER(ub4)]
    OCITypeElemName.restype = POINTER(oratext)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1287
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeElemTypeCode'):
    OCITypeElemTypeCode = _libs['libclntsh.so.10.1'].OCITypeElemTypeCode
    OCITypeElemTypeCode.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeElem)]
    OCITypeElemTypeCode.restype = OCITypeCode

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1322
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeElemType'):
    OCITypeElemType = _libs['libclntsh.so.10.1'].OCITypeElemType
    OCITypeElemType.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeElem), POINTER(POINTER(OCIType))]
    OCITypeElemType.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1358
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeElemFlags'):
    OCITypeElemFlags = _libs['libclntsh.so.10.1'].OCITypeElemFlags
    OCITypeElemFlags.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeElem)]
    OCITypeElemFlags.restype = ub4

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1389
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeElemNumPrec'):
    OCITypeElemNumPrec = _libs['libclntsh.so.10.1'].OCITypeElemNumPrec
    OCITypeElemNumPrec.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeElem)]
    OCITypeElemNumPrec.restype = ub1

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1414
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeElemNumScale'):
    OCITypeElemNumScale = _libs['libclntsh.so.10.1'].OCITypeElemNumScale
    OCITypeElemNumScale.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeElem)]
    OCITypeElemNumScale.restype = sb1

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1436
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeElemLength'):
    OCITypeElemLength = _libs['libclntsh.so.10.1'].OCITypeElemLength
    OCITypeElemLength.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeElem)]
    OCITypeElemLength.restype = ub4

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1459
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeElemCharSetID'):
    OCITypeElemCharSetID = _libs['libclntsh.so.10.1'].OCITypeElemCharSetID
    OCITypeElemCharSetID.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeElem)]
    OCITypeElemCharSetID.restype = ub2

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1482
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeElemCharSetForm'):
    OCITypeElemCharSetForm = _libs['libclntsh.so.10.1'].OCITypeElemCharSetForm
    OCITypeElemCharSetForm.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeElem)]
    OCITypeElemCharSetForm.restype = ub2

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1511
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeElemParameterizedType'):
    OCITypeElemParameterizedType = _libs['libclntsh.so.10.1'].OCITypeElemParameterizedType
    OCITypeElemParameterizedType.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeElem), POINTER(POINTER(OCIType))]
    OCITypeElemParameterizedType.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1556
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeElemExtTypeCode'):
    OCITypeElemExtTypeCode = _libs['libclntsh.so.10.1'].OCITypeElemExtTypeCode
    OCITypeElemExtTypeCode.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeElem)]
    OCITypeElemExtTypeCode.restype = OCITypeCode

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1589
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeAttrByName'):
    OCITypeAttrByName = _libs['libclntsh.so.10.1'].OCITypeAttrByName
    OCITypeAttrByName.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType), POINTER(oratext), ub4, POINTER(POINTER(OCITypeElem))]
    OCITypeAttrByName.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1630
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeAttrNext'):
    OCITypeAttrNext = _libs['libclntsh.so.10.1'].OCITypeAttrNext
    OCITypeAttrNext.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeIter), POINTER(POINTER(OCITypeElem))]
    OCITypeAttrNext.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1672
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeCollElem'):
    OCITypeCollElem = _libs['libclntsh.so.10.1'].OCITypeCollElem
    OCITypeCollElem.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType), POINTER(POINTER(OCITypeElem))]
    OCITypeCollElem.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1717
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeCollSize'):
    OCITypeCollSize = _libs['libclntsh.so.10.1'].OCITypeCollSize
    OCITypeCollSize.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType), POINTER(ub4)]
    OCITypeCollSize.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1752
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeCollExtTypeCode'):
    OCITypeCollExtTypeCode = _libs['libclntsh.so.10.1'].OCITypeCollExtTypeCode
    OCITypeCollExtTypeCode.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType), POINTER(OCITypeCode)]
    OCITypeCollExtTypeCode.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1791
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeMethodOverload'):
    OCITypeMethodOverload = _libs['libclntsh.so.10.1'].OCITypeMethodOverload
    OCITypeMethodOverload.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType), POINTER(oratext), ub4]
    OCITypeMethodOverload.restype = ub4

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1824
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeMethodByName'):
    OCITypeMethodByName = _libs['libclntsh.so.10.1'].OCITypeMethodByName
    OCITypeMethodByName.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType), POINTER(oratext), ub4, POINTER(POINTER(OCITypeMethod))]
    OCITypeMethodByName.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1868
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeMethodNext'):
    OCITypeMethodNext = _libs['libclntsh.so.10.1'].OCITypeMethodNext
    OCITypeMethodNext.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeIter), POINTER(POINTER(OCITypeMethod))]
    OCITypeMethodNext.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1910
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeMethodName'):
    OCITypeMethodName = _libs['libclntsh.so.10.1'].OCITypeMethodName
    OCITypeMethodName.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeMethod), POINTER(ub4)]
    OCITypeMethodName.restype = POINTER(oratext)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1939
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeMethodEncap'):
    OCITypeMethodEncap = _libs['libclntsh.so.10.1'].OCITypeMethodEncap
    OCITypeMethodEncap.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeMethod)]
    OCITypeMethodEncap.restype = OCITypeEncap

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1966
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeMethodFlags'):
    OCITypeMethodFlags = _libs['libclntsh.so.10.1'].OCITypeMethodFlags
    OCITypeMethodFlags.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeMethod)]
    OCITypeMethodFlags.restype = OCITypeMethodFlag

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 1997
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeMethodMap'):
    OCITypeMethodMap = _libs['libclntsh.so.10.1'].OCITypeMethodMap
    OCITypeMethodMap.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType), POINTER(POINTER(OCITypeMethod))]
    OCITypeMethodMap.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2034
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeMethodOrder'):
    OCITypeMethodOrder = _libs['libclntsh.so.10.1'].OCITypeMethodOrder
    OCITypeMethodOrder.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType), POINTER(POINTER(OCITypeMethod))]
    OCITypeMethodOrder.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2071
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeMethodParams'):
    OCITypeMethodParams = _libs['libclntsh.so.10.1'].OCITypeMethodParams
    OCITypeMethodParams.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeMethod)]
    OCITypeMethodParams.restype = ub4

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2103
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeResult'):
    OCITypeResult = _libs['libclntsh.so.10.1'].OCITypeResult
    OCITypeResult.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeMethod), POINTER(POINTER(OCITypeElem))]
    OCITypeResult.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2141
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeParamByPos'):
    OCITypeParamByPos = _libs['libclntsh.so.10.1'].OCITypeParamByPos
    OCITypeParamByPos.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeMethod), ub4, POINTER(POINTER(OCITypeElem))]
    OCITypeParamByPos.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2177
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeParamByName'):
    OCITypeParamByName = _libs['libclntsh.so.10.1'].OCITypeParamByName
    OCITypeParamByName.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeMethod), POINTER(oratext), ub4, POINTER(POINTER(OCITypeElem))]
    OCITypeParamByName.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2215
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeParamPos'):
    OCITypeParamPos = _libs['libclntsh.so.10.1'].OCITypeParamPos
    OCITypeParamPos.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeMethod), POINTER(oratext), ub4, POINTER(ub4), POINTER(POINTER(OCITypeElem))]
    OCITypeParamPos.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2257
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeElemParamMode'):
    OCITypeElemParamMode = _libs['libclntsh.so.10.1'].OCITypeElemParamMode
    OCITypeElemParamMode.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeElem)]
    OCITypeElemParamMode.restype = OCITypeParamMode

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2285
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeElemDefaultValue'):
    OCITypeElemDefaultValue = _libs['libclntsh.so.10.1'].OCITypeElemDefaultValue
    OCITypeElemDefaultValue.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITypeElem), POINTER(ub4)]
    OCITypeElemDefaultValue.restype = POINTER(oratext)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2328
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeVTInit'):
    OCITypeVTInit = _libs['libclntsh.so.10.1'].OCITypeVTInit
    OCITypeVTInit.argtypes = [POINTER(OCIEnv), POINTER(OCIError)]
    OCITypeVTInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2351
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeVTInsert'):
    OCITypeVTInsert = _libs['libclntsh.so.10.1'].OCITypeVTInsert
    OCITypeVTInsert.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(oratext), ub4, POINTER(oratext), ub4, POINTER(oratext), ub4]
    OCITypeVTInsert.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2390
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeVTSelect'):
    OCITypeVTSelect = _libs['libclntsh.so.10.1'].OCITypeVTSelect
    OCITypeVTSelect.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(oratext), ub4, POINTER(oratext), ub4, POINTER(POINTER(oratext)), POINTER(ub4), POINTER(ub2)]
    OCITypeVTSelect.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2427
if hasattr(_libs['libclntsh.so.10.1'], 'ortgcty'):
    ortgcty = _libs['libclntsh.so.10.1'].ortgcty
    ortgcty.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIType), POINTER(POINTER(OCIType))]
    ortgcty.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2434
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeBeginCreate'):
    OCITypeBeginCreate = _libs['libclntsh.so.10.1'].OCITypeBeginCreate
    OCITypeBeginCreate.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), OCITypeCode, OCIDuration, POINTER(POINTER(OCIType))]
    OCITypeBeginCreate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2478
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeSetCollection'):
    OCITypeSetCollection = _libs['libclntsh.so.10.1'].OCITypeSetCollection
    OCITypeSetCollection.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIType), POINTER(OCIParam), ub4]
    OCITypeSetCollection.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2504
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeSetBuiltin'):
    OCITypeSetBuiltin = _libs['libclntsh.so.10.1'].OCITypeSetBuiltin
    OCITypeSetBuiltin.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIType), POINTER(OCIParam)]
    OCITypeSetBuiltin.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2530
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeAddAttr'):
    OCITypeAddAttr = _libs['libclntsh.so.10.1'].OCITypeAddAttr
    OCITypeAddAttr.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIType), POINTER(oratext), ub4, POINTER(OCIParam)]
    OCITypeAddAttr.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2556
if hasattr(_libs['libclntsh.so.10.1'], 'OCITypeEndCreate'):
    OCITypeEndCreate = _libs['libclntsh.so.10.1'].OCITypeEndCreate
    OCITypeEndCreate.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIType)]
    OCITypeEndCreate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 579
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectNew'):
    OCIObjectNew = _libs['libclntsh.so.10.1'].OCIObjectNew
    OCIObjectNew.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx), OCITypeCode, POINTER(OCIType), POINTER(None), OCIDuration, boolean, POINTER(POINTER(None))]
    OCIObjectNew.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 667
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectPin'):
    OCIObjectPin = _libs['libclntsh.so.10.1'].OCIObjectPin
    OCIObjectPin.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIRef), POINTER(OCIComplexObject), OCIPinOpt, OCIDuration, OCILockOpt, POINTER(POINTER(None))]
    OCIObjectPin.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 760
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectUnpin'):
    OCIObjectUnpin = _libs['libclntsh.so.10.1'].OCIObjectUnpin
    OCIObjectUnpin.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None)]
    OCIObjectUnpin.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 807
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectPinCountReset'):
    OCIObjectPinCountReset = _libs['libclntsh.so.10.1'].OCIObjectPinCountReset
    OCIObjectPinCountReset.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None)]
    OCIObjectPinCountReset.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 847
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectLock'):
    OCIObjectLock = _libs['libclntsh.so.10.1'].OCIObjectLock
    OCIObjectLock.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None)]
    OCIObjectLock.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 878
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectLockNoWait'):
    OCIObjectLockNoWait = _libs['libclntsh.so.10.1'].OCIObjectLockNoWait
    OCIObjectLockNoWait.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None)]
    OCIObjectLockNoWait.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 911
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectMarkUpdate'):
    OCIObjectMarkUpdate = _libs['libclntsh.so.10.1'].OCIObjectMarkUpdate
    OCIObjectMarkUpdate.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None)]
    OCIObjectMarkUpdate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 951
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectUnmark'):
    OCIObjectUnmark = _libs['libclntsh.so.10.1'].OCIObjectUnmark
    OCIObjectUnmark.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None)]
    OCIObjectUnmark.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 982
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectUnmarkByRef'):
    OCIObjectUnmarkByRef = _libs['libclntsh.so.10.1'].OCIObjectUnmarkByRef
    OCIObjectUnmarkByRef.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIRef)]
    OCIObjectUnmarkByRef.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1013
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectFree'):
    OCIObjectFree = _libs['libclntsh.so.10.1'].OCIObjectFree
    OCIObjectFree.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None), ub2]
    OCIObjectFree.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1069
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectMarkDeleteByRef'):
    OCIObjectMarkDeleteByRef = _libs['libclntsh.so.10.1'].OCIObjectMarkDeleteByRef
    OCIObjectMarkDeleteByRef.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIRef)]
    OCIObjectMarkDeleteByRef.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1105
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectMarkDelete'):
    OCIObjectMarkDelete = _libs['libclntsh.so.10.1'].OCIObjectMarkDelete
    OCIObjectMarkDelete.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None)]
    OCIObjectMarkDelete.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1139
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectFlush'):
    OCIObjectFlush = _libs['libclntsh.so.10.1'].OCIObjectFlush
    OCIObjectFlush.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None)]
    OCIObjectFlush.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1171
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectRefresh'):
    OCIObjectRefresh = _libs['libclntsh.so.10.1'].OCIObjectRefresh
    OCIObjectRefresh.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None)]
    OCIObjectRefresh.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1222
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectCopy'):
    OCIObjectCopy = _libs['libclntsh.so.10.1'].OCIObjectCopy
    OCIObjectCopy.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx), POINTER(None), POINTER(None), POINTER(None), POINTER(None), POINTER(OCIType), OCIDuration, ub1]
    OCIObjectCopy.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1278
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectGetTypeRef'):
    OCIObjectGetTypeRef = _libs['libclntsh.so.10.1'].OCIObjectGetTypeRef
    OCIObjectGetTypeRef.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None), POINTER(OCIRef)]
    OCIObjectGetTypeRef.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1306
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectGetObjectRef'):
    OCIObjectGetObjectRef = _libs['libclntsh.so.10.1'].OCIObjectGetObjectRef
    OCIObjectGetObjectRef.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None), POINTER(OCIRef)]
    OCIObjectGetObjectRef.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1335
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectMakeObjectRef'):
    OCIObjectMakeObjectRef = _libs['libclntsh.so.10.1'].OCIObjectMakeObjectRef
    OCIObjectMakeObjectRef.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx), POINTER(None), POINTER(POINTER(None)), ub4, POINTER(OCIRef)]
    OCIObjectMakeObjectRef.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1376
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectGetPrimaryKeyTypeRef'):
    OCIObjectGetPrimaryKeyTypeRef = _libs['libclntsh.so.10.1'].OCIObjectGetPrimaryKeyTypeRef
    OCIObjectGetPrimaryKeyTypeRef.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx), POINTER(None), POINTER(OCIRef)]
    OCIObjectGetPrimaryKeyTypeRef.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1407
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectGetInd'):
    OCIObjectGetInd = _libs['libclntsh.so.10.1'].OCIObjectGetInd
    OCIObjectGetInd.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None), POINTER(POINTER(None))]
    OCIObjectGetInd.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1437
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectExists'):
    OCIObjectExists = _libs['libclntsh.so.10.1'].OCIObjectExists
    OCIObjectExists.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None), POINTER(boolean)]
    OCIObjectExists.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1463
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectGetProperty'):
    OCIObjectGetProperty = _libs['libclntsh.so.10.1'].OCIObjectGetProperty
    OCIObjectGetProperty.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None), OCIObjectPropId, POINTER(None), POINTER(ub4)]
    OCIObjectGetProperty.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1592
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectIsLocked'):
    OCIObjectIsLocked = _libs['libclntsh.so.10.1'].OCIObjectIsLocked
    OCIObjectIsLocked.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None), POINTER(boolean)]
    OCIObjectIsLocked.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1619
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectIsDirty'):
    OCIObjectIsDirty = _libs['libclntsh.so.10.1'].OCIObjectIsDirty
    OCIObjectIsDirty.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None), POINTER(boolean)]
    OCIObjectIsDirty.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1646
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectPinTable'):
    OCIObjectPinTable = _libs['libclntsh.so.10.1'].OCIObjectPinTable
    OCIObjectPinTable.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx), POINTER(oratext), ub4, POINTER(oratext), ub4, POINTER(OCIRef), OCIDuration, POINTER(POINTER(None))]
    OCIObjectPinTable.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1682
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectArrayPin'):
    OCIObjectArrayPin = _libs['libclntsh.so.10.1'].OCIObjectArrayPin
    OCIObjectArrayPin.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(POINTER(OCIRef)), ub4, POINTER(POINTER(OCIComplexObject)), ub4, OCIPinOpt, OCIDuration, OCILockOpt, POINTER(POINTER(None)), POINTER(ub4)]
    OCIObjectArrayPin.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1731
if hasattr(_libs['libclntsh.so.10.1'], 'OCICacheFlush'):
    OCICacheFlush = _libs['libclntsh.so.10.1'].OCICacheFlush
    OCICacheFlush.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx), POINTER(None), CFUNCTYPE(UNCHECKED(POINTER(OCIRef)), POINTER(None), POINTER(ub1)), POINTER(POINTER(OCIRef))]
    OCICacheFlush.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1791
if hasattr(_libs['libclntsh.so.10.1'], 'OCICacheRefresh'):
    OCICacheRefresh = _libs['libclntsh.so.10.1'].OCICacheRefresh
    OCICacheRefresh.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx), OCIRefreshOpt, POINTER(None), CFUNCTYPE(UNCHECKED(POINTER(OCIRef)), POINTER(None)), POINTER(POINTER(OCIRef))]
    OCICacheRefresh.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1847
if hasattr(_libs['libclntsh.so.10.1'], 'OCICacheUnpin'):
    OCICacheUnpin = _libs['libclntsh.so.10.1'].OCICacheUnpin
    OCICacheUnpin.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx)]
    OCICacheUnpin.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1875
if hasattr(_libs['libclntsh.so.10.1'], 'OCICacheFree'):
    OCICacheFree = _libs['libclntsh.so.10.1'].OCICacheFree
    OCICacheFree.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx)]
    OCICacheFree.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1903
if hasattr(_libs['libclntsh.so.10.1'], 'OCICacheUnmark'):
    OCICacheUnmark = _libs['libclntsh.so.10.1'].OCICacheUnmark
    OCICacheUnmark.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx)]
    OCICacheUnmark.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1930
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDurationBegin'):
    OCIDurationBegin = _libs['libclntsh.so.10.1'].OCIDurationBegin
    OCIDurationBegin.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx), OCIDuration, POINTER(OCIDuration)]
    OCIDurationBegin.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 1997
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDurationEnd'):
    OCIDurationEnd = _libs['libclntsh.so.10.1'].OCIDurationEnd
    OCIDurationEnd.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx), OCIDuration]
    OCIDurationEnd.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 2050
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDurationGetParent'):
    OCIDurationGetParent = _libs['libclntsh.so.10.1'].OCIDurationGetParent
    OCIDurationGetParent.argtypes = [POINTER(OCIEnv), POINTER(OCIError), OCIDuration, POINTER(OCIDuration)]
    OCIDurationGetParent.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 2053
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectAlwaysLatest'):
    OCIObjectAlwaysLatest = _libs['libclntsh.so.10.1'].OCIObjectAlwaysLatest
    OCIObjectAlwaysLatest.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None)]
    OCIObjectAlwaysLatest.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 2055
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectNotAlwaysLatest'):
    OCIObjectNotAlwaysLatest = _libs['libclntsh.so.10.1'].OCIObjectNotAlwaysLatest
    OCIObjectNotAlwaysLatest.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None)]
    OCIObjectNotAlwaysLatest.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 2058
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectFlushRefresh'):
    OCIObjectFlushRefresh = _libs['libclntsh.so.10.1'].OCIObjectFlushRefresh
    OCIObjectFlushRefresh.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None)]
    OCIObjectFlushRefresh.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 2060
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectIsLoaded'):
    OCIObjectIsLoaded = _libs['libclntsh.so.10.1'].OCIObjectIsLoaded
    OCIObjectIsLoaded.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None), POINTER(boolean)]
    OCIObjectIsLoaded.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 2063
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectIsDirtied'):
    OCIObjectIsDirtied = _libs['libclntsh.so.10.1'].OCIObjectIsDirtied
    OCIObjectIsDirtied.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None), POINTER(boolean)]
    OCIObjectIsDirtied.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 2066
if hasattr(_libs['libclntsh.so.10.1'], 'OCICacheGetObjects'):
    OCICacheGetObjects = _libs['libclntsh.so.10.1'].OCICacheGetObjects
    OCICacheGetObjects.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx), OCIObjectProperty, POINTER(None), CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None))]
    OCICacheGetObjects.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 2074
if hasattr(_libs['libclntsh.so.10.1'], 'OCICacheRegister'):
    OCICacheRegister = _libs['libclntsh.so.10.1'].OCICacheRegister
    OCICacheRegister.argtypes = [POINTER(OCIEnv), POINTER(OCIError), OCIObjectEvent, POINTER(None), CFUNCTYPE(UNCHECKED(None), POINTER(None), OCIObjectEvent, POINTER(None))]
    OCICacheRegister.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 2082
if hasattr(_libs['libclntsh.so.10.1'], 'OCICacheFlushRefresh'):
    OCICacheFlushRefresh = _libs['libclntsh.so.10.1'].OCICacheFlushRefresh
    OCICacheFlushRefresh.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx), POINTER(None), CFUNCTYPE(UNCHECKED(POINTER(OCIRef)), POINTER(None), POINTER(ub1)), POINTER(POINTER(OCIRef))]
    OCICacheFlushRefresh.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 2087
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectSetData'):
    OCIObjectSetData = _libs['libclntsh.so.10.1'].OCIObjectSetData
    OCIObjectSetData.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None), POINTER(None)]
    OCIObjectSetData.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ori.h: 2090
if hasattr(_libs['libclntsh.so.10.1'], 'OCIObjectGetNewOID'):
    OCIObjectGetNewOID = _libs['libclntsh.so.10.1'].OCIObjectGetNewOID
    OCIObjectGetNewOID.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx), POINTER(ub1)]
    OCIObjectGetNewOID.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 479
class struct_OCINumber(Structure):
    pass

struct_OCINumber.__slots__ = [
    'OCINumberPart',
]
struct_OCINumber._fields_ = [
    ('OCINumberPart', ub1 * 22),
]

OCINumber = struct_OCINumber # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 483

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 601
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberInc'):
    OCINumberInc = _libs['libclntsh.so.10.1'].OCINumberInc
    OCINumberInc.argtypes = [POINTER(OCIError), POINTER(OCINumber)]
    OCINumberInc.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 624
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberDec'):
    OCINumberDec = _libs['libclntsh.so.10.1'].OCINumberDec
    OCINumberDec.argtypes = [POINTER(OCIError), POINTER(OCINumber)]
    OCINumberDec.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 647
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberSetZero'):
    OCINumberSetZero = _libs['libclntsh.so.10.1'].OCINumberSetZero
    OCINumberSetZero.argtypes = [POINTER(OCIError), POINTER(OCINumber)]
    OCINumberSetZero.restype = None

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 659
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberSetPi'):
    OCINumberSetPi = _libs['libclntsh.so.10.1'].OCINumberSetPi
    OCINumberSetPi.argtypes = [POINTER(OCIError), POINTER(OCINumber)]
    OCINumberSetPi.restype = None

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 670
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberAdd'):
    OCINumberAdd = _libs['libclntsh.so.10.1'].OCINumberAdd
    OCINumberAdd.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberAdd.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 692
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberSub'):
    OCINumberSub = _libs['libclntsh.so.10.1'].OCINumberSub
    OCINumberSub.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberSub.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 714
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberMul'):
    OCINumberMul = _libs['libclntsh.so.10.1'].OCINumberMul
    OCINumberMul.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberMul.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 736
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberDiv'):
    OCINumberDiv = _libs['libclntsh.so.10.1'].OCINumberDiv
    OCINumberDiv.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberDiv.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 762
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberMod'):
    OCINumberMod = _libs['libclntsh.so.10.1'].OCINumberMod
    OCINumberMod.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberMod.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 786
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberIntPower'):
    OCINumberIntPower = _libs['libclntsh.so.10.1'].OCINumberIntPower
    OCINumberIntPower.argtypes = [POINTER(OCIError), POINTER(OCINumber), sword, POINTER(OCINumber)]
    OCINumberIntPower.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 810
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberShift'):
    OCINumberShift = _libs['libclntsh.so.10.1'].OCINumberShift
    OCINumberShift.argtypes = [POINTER(OCIError), POINTER(OCINumber), sword, POINTER(OCINumber)]
    OCINumberShift.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 834
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberNeg'):
    OCINumberNeg = _libs['libclntsh.so.10.1'].OCINumberNeg
    OCINumberNeg.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberNeg.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 856
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberToText'):
    OCINumberToText = _libs['libclntsh.so.10.1'].OCINumberToText
    OCINumberToText.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(oratext), ub4, POINTER(oratext), ub4, POINTER(ub4), POINTER(oratext)]
    OCINumberToText.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 901
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberFromText'):
    OCINumberFromText = _libs['libclntsh.so.10.1'].OCINumberFromText
    OCINumberFromText.argtypes = [POINTER(OCIError), POINTER(oratext), ub4, POINTER(oratext), ub4, POINTER(oratext), ub4, POINTER(OCINumber)]
    OCINumberFromText.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 942
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberToInt'):
    OCINumberToInt = _libs['libclntsh.so.10.1'].OCINumberToInt
    OCINumberToInt.argtypes = [POINTER(OCIError), POINTER(OCINumber), uword, uword, POINTER(None)]
    OCINumberToInt.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 971
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberFromInt'):
    OCINumberFromInt = _libs['libclntsh.so.10.1'].OCINumberFromInt
    OCINumberFromInt.argtypes = [POINTER(OCIError), POINTER(None), uword, uword, POINTER(OCINumber)]
    OCINumberFromInt.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1000
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberToReal'):
    OCINumberToReal = _libs['libclntsh.so.10.1'].OCINumberToReal
    OCINumberToReal.argtypes = [POINTER(OCIError), POINTER(OCINumber), uword, POINTER(None)]
    OCINumberToReal.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1028
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberToRealArray'):
    OCINumberToRealArray = _libs['libclntsh.so.10.1'].OCINumberToRealArray
    OCINumberToRealArray.argtypes = [POINTER(OCIError), POINTER(POINTER(OCINumber)), uword, uword, POINTER(None)]
    OCINumberToRealArray.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1057
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberFromReal'):
    OCINumberFromReal = _libs['libclntsh.so.10.1'].OCINumberFromReal
    OCINumberFromReal.argtypes = [POINTER(OCIError), POINTER(None), uword, POINTER(OCINumber)]
    OCINumberFromReal.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1083
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberCmp'):
    OCINumberCmp = _libs['libclntsh.so.10.1'].OCINumberCmp
    OCINumberCmp.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber), POINTER(sword)]
    OCINumberCmp.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1106
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberSign'):
    OCINumberSign = _libs['libclntsh.so.10.1'].OCINumberSign
    OCINumberSign.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(sword)]
    OCINumberSign.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1129
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberIsZero'):
    OCINumberIsZero = _libs['libclntsh.so.10.1'].OCINumberIsZero
    OCINumberIsZero.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(boolean)]
    OCINumberIsZero.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1151
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberIsInt'):
    OCINumberIsInt = _libs['libclntsh.so.10.1'].OCINumberIsInt
    OCINumberIsInt.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(boolean)]
    OCINumberIsInt.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1173
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberAssign'):
    OCINumberAssign = _libs['libclntsh.so.10.1'].OCINumberAssign
    OCINumberAssign.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberAssign.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1195
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberAbs'):
    OCINumberAbs = _libs['libclntsh.so.10.1'].OCINumberAbs
    OCINumberAbs.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberAbs.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1218
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberCeil'):
    OCINumberCeil = _libs['libclntsh.so.10.1'].OCINumberCeil
    OCINumberCeil.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberCeil.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1241
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberFloor'):
    OCINumberFloor = _libs['libclntsh.so.10.1'].OCINumberFloor
    OCINumberFloor.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberFloor.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1264
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberSqrt'):
    OCINumberSqrt = _libs['libclntsh.so.10.1'].OCINumberSqrt
    OCINumberSqrt.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberSqrt.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1288
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberTrunc'):
    OCINumberTrunc = _libs['libclntsh.so.10.1'].OCINumberTrunc
    OCINumberTrunc.argtypes = [POINTER(OCIError), POINTER(OCINumber), sword, POINTER(OCINumber)]
    OCINumberTrunc.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1313
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberPower'):
    OCINumberPower = _libs['libclntsh.so.10.1'].OCINumberPower
    OCINumberPower.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberPower.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1337
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberRound'):
    OCINumberRound = _libs['libclntsh.so.10.1'].OCINumberRound
    OCINumberRound.argtypes = [POINTER(OCIError), POINTER(OCINumber), sword, POINTER(OCINumber)]
    OCINumberRound.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1362
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberPrec'):
    OCINumberPrec = _libs['libclntsh.so.10.1'].OCINumberPrec
    OCINumberPrec.argtypes = [POINTER(OCIError), POINTER(OCINumber), eword, POINTER(OCINumber)]
    OCINumberPrec.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1387
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberSin'):
    OCINumberSin = _libs['libclntsh.so.10.1'].OCINumberSin
    OCINumberSin.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberSin.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1409
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberArcSin'):
    OCINumberArcSin = _libs['libclntsh.so.10.1'].OCINumberArcSin
    OCINumberArcSin.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberArcSin.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1432
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberHypSin'):
    OCINumberHypSin = _libs['libclntsh.so.10.1'].OCINumberHypSin
    OCINumberHypSin.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberHypSin.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1457
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberCos'):
    OCINumberCos = _libs['libclntsh.so.10.1'].OCINumberCos
    OCINumberCos.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberCos.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1479
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberArcCos'):
    OCINumberArcCos = _libs['libclntsh.so.10.1'].OCINumberArcCos
    OCINumberArcCos.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberArcCos.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1502
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberHypCos'):
    OCINumberHypCos = _libs['libclntsh.so.10.1'].OCINumberHypCos
    OCINumberHypCos.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberHypCos.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1527
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberTan'):
    OCINumberTan = _libs['libclntsh.so.10.1'].OCINumberTan
    OCINumberTan.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberTan.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1549
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberArcTan'):
    OCINumberArcTan = _libs['libclntsh.so.10.1'].OCINumberArcTan
    OCINumberArcTan.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberArcTan.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1571
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberArcTan2'):
    OCINumberArcTan2 = _libs['libclntsh.so.10.1'].OCINumberArcTan2
    OCINumberArcTan2.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberArcTan2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1597
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberHypTan'):
    OCINumberHypTan = _libs['libclntsh.so.10.1'].OCINumberHypTan
    OCINumberHypTan.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberHypTan.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1622
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberExp'):
    OCINumberExp = _libs['libclntsh.so.10.1'].OCINumberExp
    OCINumberExp.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberExp.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1644
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberLn'):
    OCINumberLn = _libs['libclntsh.so.10.1'].OCINumberLn
    OCINumberLn.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberLn.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1668
if hasattr(_libs['libclntsh.so.10.1'], 'OCINumberLog'):
    OCINumberLog = _libs['libclntsh.so.10.1'].OCINumberLog
    OCINumberLog.argtypes = [POINTER(OCIError), POINTER(OCINumber), POINTER(OCINumber), POINTER(OCINumber)]
    OCINumberLog.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1695
class struct_OCITime(Structure):
    pass

struct_OCITime.__slots__ = [
    'OCITimeHH',
    'OCITimeMI',
    'OCITimeSS',
]
struct_OCITime._fields_ = [
    ('OCITimeHH', ub1),
    ('OCITimeMI', ub1),
    ('OCITimeSS', ub1),
]

OCITime = struct_OCITime # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1701

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1711
class struct_OCIDate(Structure):
    pass

struct_OCIDate.__slots__ = [
    'OCIDateYYYY',
    'OCIDateMM',
    'OCIDateDD',
]
struct_OCIDate._fields_ = [
    ('OCIDateYYYY', sb2),
    ('OCIDateMM', ub1),
    ('OCIDateDD', ub1),
]

OCIDate = struct_OCIDate # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1718

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1872
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateAssign'):
    OCIDateAssign = _libs['libclntsh.so.10.1'].OCIDateAssign
    OCIDateAssign.argtypes = [POINTER(OCIError), POINTER(OCIDate), POINTER(OCIDate)]
    OCIDateAssign.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1891
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateToText'):
    OCIDateToText = _libs['libclntsh.so.10.1'].OCIDateToText
    OCIDateToText.argtypes = [POINTER(OCIError), POINTER(OCIDate), POINTER(oratext), ub1, POINTER(oratext), ub4, POINTER(ub4), POINTER(oratext)]
    OCIDateToText.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1936
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateFromText'):
    OCIDateFromText = _libs['libclntsh.so.10.1'].OCIDateFromText
    OCIDateFromText.argtypes = [POINTER(OCIError), POINTER(oratext), ub4, POINTER(oratext), ub1, POINTER(oratext), ub4, POINTER(OCIDate)]
    OCIDateFromText.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1975
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateCompare'):
    OCIDateCompare = _libs['libclntsh.so.10.1'].OCIDateCompare
    OCIDateCompare.argtypes = [POINTER(OCIError), POINTER(OCIDate), POINTER(OCIDate), POINTER(sword)]
    OCIDateCompare.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2001
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateAddMonths'):
    OCIDateAddMonths = _libs['libclntsh.so.10.1'].OCIDateAddMonths
    OCIDateAddMonths.argtypes = [POINTER(OCIError), POINTER(OCIDate), sb4, POINTER(OCIDate)]
    OCIDateAddMonths.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2032
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateAddDays'):
    OCIDateAddDays = _libs['libclntsh.so.10.1'].OCIDateAddDays
    OCIDateAddDays.argtypes = [POINTER(OCIError), POINTER(OCIDate), sb4, POINTER(OCIDate)]
    OCIDateAddDays.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2058
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateLastDay'):
    OCIDateLastDay = _libs['libclntsh.so.10.1'].OCIDateLastDay
    OCIDateLastDay.argtypes = [POINTER(OCIError), POINTER(OCIDate), POINTER(OCIDate)]
    OCIDateLastDay.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2082
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateDaysBetween'):
    OCIDateDaysBetween = _libs['libclntsh.so.10.1'].OCIDateDaysBetween
    OCIDateDaysBetween.argtypes = [POINTER(OCIError), POINTER(OCIDate), POINTER(OCIDate), POINTER(sb4)]
    OCIDateDaysBetween.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2106
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateZoneToZone'):
    OCIDateZoneToZone = _libs['libclntsh.so.10.1'].OCIDateZoneToZone
    OCIDateZoneToZone.argtypes = [POINTER(OCIError), POINTER(OCIDate), POINTER(oratext), ub4, POINTER(oratext), ub4, POINTER(OCIDate)]
    OCIDateZoneToZone.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2138
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateNextDay'):
    OCIDateNextDay = _libs['libclntsh.so.10.1'].OCIDateNextDay
    OCIDateNextDay.argtypes = [POINTER(OCIError), POINTER(OCIDate), POINTER(oratext), ub4, POINTER(OCIDate)]
    OCIDateNextDay.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2186
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateCheck'):
    OCIDateCheck = _libs['libclntsh.so.10.1'].OCIDateCheck
    OCIDateCheck.argtypes = [POINTER(OCIError), POINTER(OCIDate), POINTER(uword)]
    OCIDateCheck.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2233
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateSysDate'):
    OCIDateSysDate = _libs['libclntsh.so.10.1'].OCIDateSysDate
    OCIDateSysDate.argtypes = [POINTER(OCIError), POINTER(OCIDate)]
    OCIDateSysDate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2276
class struct_OCIString(Structure):
    pass

OCIString = struct_OCIString # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2276

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2280
if hasattr(_libs['libclntsh.so.10.1'], 'OCIStringAssign'):
    OCIStringAssign = _libs['libclntsh.so.10.1'].OCIStringAssign
    OCIStringAssign.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIString), POINTER(POINTER(OCIString))]
    OCIStringAssign.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2306
if hasattr(_libs['libclntsh.so.10.1'], 'OCIStringAssignText'):
    OCIStringAssignText = _libs['libclntsh.so.10.1'].OCIStringAssignText
    OCIStringAssignText.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(oratext), ub4, POINTER(POINTER(OCIString))]
    OCIStringAssignText.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2333
if hasattr(_libs['libclntsh.so.10.1'], 'OCIStringResize'):
    OCIStringResize = _libs['libclntsh.so.10.1'].OCIStringResize
    OCIStringResize.argtypes = [POINTER(OCIEnv), POINTER(OCIError), ub4, POINTER(POINTER(OCIString))]
    OCIStringResize.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2368
if hasattr(_libs['libclntsh.so.10.1'], 'OCIStringSize'):
    OCIStringSize = _libs['libclntsh.so.10.1'].OCIStringSize
    OCIStringSize.argtypes = [POINTER(OCIEnv), POINTER(OCIString)]
    OCIStringSize.restype = ub4

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2382
if hasattr(_libs['libclntsh.so.10.1'], 'OCIStringPtr'):
    OCIStringPtr = _libs['libclntsh.so.10.1'].OCIStringPtr
    OCIStringPtr.argtypes = [POINTER(OCIEnv), POINTER(OCIString)]
    OCIStringPtr.restype = POINTER(oratext)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2396
if hasattr(_libs['libclntsh.so.10.1'], 'OCIStringAllocSize'):
    OCIStringAllocSize = _libs['libclntsh.so.10.1'].OCIStringAllocSize
    OCIStringAllocSize.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIString), POINTER(ub4)]
    OCIStringAllocSize.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2436
class struct_OCIRaw(Structure):
    pass

OCIRaw = struct_OCIRaw # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2436

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2440
if hasattr(_libs['libclntsh.so.10.1'], 'OCIRawAssignRaw'):
    OCIRawAssignRaw = _libs['libclntsh.so.10.1'].OCIRawAssignRaw
    OCIRawAssignRaw.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIRaw), POINTER(POINTER(OCIRaw))]
    OCIRawAssignRaw.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2465
if hasattr(_libs['libclntsh.so.10.1'], 'OCIRawAssignBytes'):
    OCIRawAssignBytes = _libs['libclntsh.so.10.1'].OCIRawAssignBytes
    OCIRawAssignBytes.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(ub1), ub4, POINTER(POINTER(OCIRaw))]
    OCIRawAssignBytes.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2491
if hasattr(_libs['libclntsh.so.10.1'], 'OCIRawResize'):
    OCIRawResize = _libs['libclntsh.so.10.1'].OCIRawResize
    OCIRawResize.argtypes = [POINTER(OCIEnv), POINTER(OCIError), ub4, POINTER(POINTER(OCIRaw))]
    OCIRawResize.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2524
if hasattr(_libs['libclntsh.so.10.1'], 'OCIRawSize'):
    OCIRawSize = _libs['libclntsh.so.10.1'].OCIRawSize
    OCIRawSize.argtypes = [POINTER(OCIEnv), POINTER(OCIRaw)]
    OCIRawSize.restype = ub4

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2537
if hasattr(_libs['libclntsh.so.10.1'], 'OCIRawPtr'):
    OCIRawPtr = _libs['libclntsh.so.10.1'].OCIRawPtr
    OCIRawPtr.argtypes = [POINTER(OCIEnv), POINTER(OCIRaw)]
    OCIRawPtr.restype = POINTER(ub1)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2551
if hasattr(_libs['libclntsh.so.10.1'], 'OCIRawAllocSize'):
    OCIRawAllocSize = _libs['libclntsh.so.10.1'].OCIRawAllocSize
    OCIRawAllocSize.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIRaw), POINTER(ub4)]
    OCIRawAllocSize.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2587
if hasattr(_libs['libclntsh.so.10.1'], 'OCIRefClear'):
    OCIRefClear = _libs['libclntsh.so.10.1'].OCIRefClear
    OCIRefClear.argtypes = [POINTER(OCIEnv), POINTER(OCIRef)]
    OCIRefClear.restype = None

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2607
if hasattr(_libs['libclntsh.so.10.1'], 'OCIRefAssign'):
    OCIRefAssign = _libs['libclntsh.so.10.1'].OCIRefAssign
    OCIRefAssign.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIRef), POINTER(POINTER(OCIRef))]
    OCIRefAssign.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2632
if hasattr(_libs['libclntsh.so.10.1'], 'OCIRefIsEqual'):
    OCIRefIsEqual = _libs['libclntsh.so.10.1'].OCIRefIsEqual
    OCIRefIsEqual.argtypes = [POINTER(OCIEnv), POINTER(OCIRef), POINTER(OCIRef)]
    OCIRefIsEqual.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2652
if hasattr(_libs['libclntsh.so.10.1'], 'OCIRefIsNull'):
    OCIRefIsNull = _libs['libclntsh.so.10.1'].OCIRefIsNull
    OCIRefIsNull.argtypes = [POINTER(OCIEnv), POINTER(OCIRef)]
    OCIRefIsNull.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2673
if hasattr(_libs['libclntsh.so.10.1'], 'OCIRefHexSize'):
    OCIRefHexSize = _libs['libclntsh.so.10.1'].OCIRefHexSize
    OCIRefHexSize.argtypes = [POINTER(OCIEnv), POINTER(OCIRef)]
    OCIRefHexSize.restype = ub4

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2689
if hasattr(_libs['libclntsh.so.10.1'], 'OCIRefFromHex'):
    OCIRefFromHex = _libs['libclntsh.so.10.1'].OCIRefFromHex
    OCIRefFromHex.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISvcCtx), POINTER(oratext), ub4, POINTER(POINTER(OCIRef))]
    OCIRefFromHex.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2720
if hasattr(_libs['libclntsh.so.10.1'], 'OCIRefToHex'):
    OCIRefToHex = _libs['libclntsh.so.10.1'].OCIRefToHex
    OCIRefToHex.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIRef), POINTER(oratext), POINTER(ub4)]
    OCIRefToHex.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2807
class struct_OCIColl(Structure):
    pass

OCIColl = struct_OCIColl # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2807

OCIArray = OCIColl # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2810

OCITable = OCIColl # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2813

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2816
class struct_OCIIter(Structure):
    pass

OCIIter = struct_OCIIter # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2816

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2820
if hasattr(_libs['libclntsh.so.10.1'], 'OCICollSize'):
    OCICollSize = _libs['libclntsh.so.10.1'].OCICollSize
    OCICollSize.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIColl), POINTER(sb4)]
    OCICollSize.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2867
if hasattr(_libs['libclntsh.so.10.1'], 'OCICollMax'):
    OCICollMax = _libs['libclntsh.so.10.1'].OCICollMax
    OCICollMax.argtypes = [POINTER(OCIEnv), POINTER(OCIColl)]
    OCICollMax.restype = sb4

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2886
if hasattr(_libs['libclntsh.so.10.1'], 'OCICollGetElem'):
    OCICollGetElem = _libs['libclntsh.so.10.1'].OCICollGetElem
    OCICollGetElem.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIColl), sb4, POINTER(boolean), POINTER(POINTER(None)), POINTER(POINTER(None))]
    OCICollGetElem.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2964
if hasattr(_libs['libclntsh.so.10.1'], 'OCICollGetElemArray'):
    OCICollGetElemArray = _libs['libclntsh.so.10.1'].OCICollGetElemArray
    OCICollGetElemArray.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIColl), sb4, POINTER(boolean), POINTER(POINTER(None)), POINTER(POINTER(None)), POINTER(uword)]
    OCICollGetElemArray.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3043
if hasattr(_libs['libclntsh.so.10.1'], 'OCICollAssignElem'):
    OCICollAssignElem = _libs['libclntsh.so.10.1'].OCICollAssignElem
    OCICollAssignElem.argtypes = [POINTER(OCIEnv), POINTER(OCIError), sb4, POINTER(None), POINTER(None), POINTER(OCIColl)]
    OCICollAssignElem.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3081
if hasattr(_libs['libclntsh.so.10.1'], 'OCICollAssign'):
    OCICollAssign = _libs['libclntsh.so.10.1'].OCICollAssign
    OCICollAssign.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIColl), POINTER(OCIColl)]
    OCICollAssign.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3117
if hasattr(_libs['libclntsh.so.10.1'], 'OCICollAppend'):
    OCICollAppend = _libs['libclntsh.so.10.1'].OCICollAppend
    OCICollAppend.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(None), POINTER(None), POINTER(OCIColl)]
    OCICollAppend.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3156
if hasattr(_libs['libclntsh.so.10.1'], 'OCICollTrim'):
    OCICollTrim = _libs['libclntsh.so.10.1'].OCICollTrim
    OCICollTrim.argtypes = [POINTER(OCIEnv), POINTER(OCIError), sb4, POINTER(OCIColl)]
    OCICollTrim.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3185
if hasattr(_libs['libclntsh.so.10.1'], 'OCICollIsLocator'):
    OCICollIsLocator = _libs['libclntsh.so.10.1'].OCICollIsLocator
    OCICollIsLocator.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIColl), POINTER(boolean)]
    OCICollIsLocator.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3209
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIterCreate'):
    OCIIterCreate = _libs['libclntsh.so.10.1'].OCIIterCreate
    OCIIterCreate.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIColl), POINTER(POINTER(OCIIter))]
    OCIIterCreate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3245
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIterDelete'):
    OCIIterDelete = _libs['libclntsh.so.10.1'].OCIIterDelete
    OCIIterDelete.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(POINTER(OCIIter))]
    OCIIterDelete.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3269
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIterInit'):
    OCIIterInit = _libs['libclntsh.so.10.1'].OCIIterInit
    OCIIterInit.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIColl), POINTER(OCIIter)]
    OCIIterInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3298
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIterGetCurrent'):
    OCIIterGetCurrent = _libs['libclntsh.so.10.1'].OCIIterGetCurrent
    OCIIterGetCurrent.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIIter), POINTER(POINTER(None)), POINTER(POINTER(None))]
    OCIIterGetCurrent.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3326
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIterNext'):
    OCIIterNext = _libs['libclntsh.so.10.1'].OCIIterNext
    OCIIterNext.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIIter), POINTER(POINTER(None)), POINTER(POINTER(None)), POINTER(boolean)]
    OCIIterNext.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3361
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIterPrev'):
    OCIIterPrev = _libs['libclntsh.so.10.1'].OCIIterPrev
    OCIIterPrev.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIIter), POINTER(POINTER(None)), POINTER(POINTER(None)), POINTER(boolean)]
    OCIIterPrev.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3401
if hasattr(_libs['libclntsh.so.10.1'], 'OCITableSize'):
    OCITableSize = _libs['libclntsh.so.10.1'].OCITableSize
    OCITableSize.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITable), POINTER(sb4)]
    OCITableSize.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3444
if hasattr(_libs['libclntsh.so.10.1'], 'OCITableExists'):
    OCITableExists = _libs['libclntsh.so.10.1'].OCITableExists
    OCITableExists.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITable), sb4, POINTER(boolean)]
    OCITableExists.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3470
if hasattr(_libs['libclntsh.so.10.1'], 'OCITableDelete'):
    OCITableDelete = _libs['libclntsh.so.10.1'].OCITableDelete
    OCITableDelete.argtypes = [POINTER(OCIEnv), POINTER(OCIError), sb4, POINTER(OCITable)]
    OCITableDelete.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3499
if hasattr(_libs['libclntsh.so.10.1'], 'OCITableFirst'):
    OCITableFirst = _libs['libclntsh.so.10.1'].OCITableFirst
    OCITableFirst.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITable), POINTER(sb4)]
    OCITableFirst.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3524
if hasattr(_libs['libclntsh.so.10.1'], 'OCITableLast'):
    OCITableLast = _libs['libclntsh.so.10.1'].OCITableLast
    OCITableLast.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCITable), POINTER(sb4)]
    OCITableLast.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3549
if hasattr(_libs['libclntsh.so.10.1'], 'OCITableNext'):
    OCITableNext = _libs['libclntsh.so.10.1'].OCITableNext
    OCITableNext.argtypes = [POINTER(OCIEnv), POINTER(OCIError), sb4, POINTER(OCITable), POINTER(sb4), POINTER(boolean)]
    OCITableNext.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3578
if hasattr(_libs['libclntsh.so.10.1'], 'OCITablePrev'):
    OCITablePrev = _libs['libclntsh.so.10.1'].OCITablePrev
    OCITablePrev.argtypes = [POINTER(OCIEnv), POINTER(OCIError), sb4, POINTER(OCITable), POINTER(sb4), POINTER(boolean)]
    OCITablePrev.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3623
class struct_OCIXMLType(Structure):
    pass

OCIXMLType = struct_OCIXMLType # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3623

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3626
class struct_OCIDOMDocument(Structure):
    pass

OCIDOMDocument = struct_OCIDOMDocument # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3626

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 504
class struct_nzttIdentity(Structure):
    pass

nzttIdentity = struct_nzttIdentity # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 216

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 217
class struct_nzttIdentityPrivate(Structure):
    pass

nzttIdentityPrivate = struct_nzttIdentityPrivate # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 217

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 472
class struct_nzttPersona(Structure):
    pass

nzttPersona = struct_nzttPersona # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 218

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 219
class struct_nzttPersonaPrivate(Structure):
    pass

nzttPersonaPrivate = struct_nzttPersonaPrivate # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 219

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 446
class struct_nzttWallet(Structure):
    pass

nzttWallet = struct_nzttWallet # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 220

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 221
class struct_nzttWalletPrivate(Structure):
    pass

nzttWalletPrivate = struct_nzttWalletPrivate # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 221

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 223
class struct_nzssEntry(Structure):
    pass

nzssEntry = struct_nzssEntry # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 223

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 224
class struct_nzpkcs11_Info(Structure):
    pass

nzpkcs11_Info = struct_nzpkcs11_Info # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 224

enum_nzttces = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 236

nzttces = enum_nzttces # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 242

enum_nzttcef = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 250

nzttcef = enum_nzttcef # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 263

enum_nzttCipherType = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 300

nzttCipherType = enum_nzttCipherType # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 310

enum_nztttdufmt = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 318

nztttdufmt = enum_nztttdufmt # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 325

enum_nzttPolicy = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 345

nzttPolicy = enum_nzttPolicy # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 352

enum_nzttIdentType = c_int # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 380

nzttIdentType = enum_nzttIdentType # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 390

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 432
class struct_nzttBufferBlock(Structure):
    pass

struct_nzttBufferBlock.__slots__ = [
    'flags_nzttBufferBlock',
    'buflen_nzttBufferBlock',
    'usedlen_nzttBufferBlock',
    'buffer_nzttBufferBlock',
]
struct_nzttBufferBlock._fields_ = [
    ('flags_nzttBufferBlock', uword),
    ('buflen_nzttBufferBlock', ub4),
    ('usedlen_nzttBufferBlock', ub4),
    ('buffer_nzttBufferBlock', POINTER(ub1)),
]

nzttBufferBlock = struct_nzttBufferBlock # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 441

struct_nzttWallet.__slots__ = [
    'ldapName_nzttWallet',
    'ldapNamelen_nzttWallet',
    'securePolicy_nzttWallet',
    'openPolicy_nzttWallet',
    'persona_nzttWallet',
    'private_nzttWallet',
]
struct_nzttWallet._fields_ = [
    ('ldapName_nzttWallet', POINTER(ub1)),
    ('ldapNamelen_nzttWallet', ub4),
    ('securePolicy_nzttWallet', nzttPolicy),
    ('openPolicy_nzttWallet', nzttPolicy),
    ('persona_nzttWallet', POINTER(nzttPersona)),
    ('private_nzttWallet', POINTER(nzttWalletPrivate)),
]

struct_nzttPersona.__slots__ = [
    'genericName_nzttPersona',
    'genericNamelen_nzttPersona',
    'private_nzttPersona',
    'mycertreqs_nzttPersona',
    'mycerts_nzttPersona',
    'mytps_nzttPersona',
    'mystore_nzttPersona',
    'mypkcs11Info_nzttPersona',
    'next_nzttPersona',
]
struct_nzttPersona._fields_ = [
    ('genericName_nzttPersona', POINTER(ub1)),
    ('genericNamelen_nzttPersona', ub4),
    ('private_nzttPersona', POINTER(nzttPersonaPrivate)),
    ('mycertreqs_nzttPersona', POINTER(nzttIdentity)),
    ('mycerts_nzttPersona', POINTER(nzttIdentity)),
    ('mytps_nzttPersona', POINTER(nzttIdentity)),
    ('mystore_nzttPersona', POINTER(nzssEntry)),
    ('mypkcs11Info_nzttPersona', POINTER(nzpkcs11_Info)),
    ('next_nzttPersona', POINTER(struct_nzttPersona)),
]

struct_nzttIdentity.__slots__ = [
    'dn_nzttIdentity',
    'dnlen_nzttIdentity',
    'comment_nzttIdentity',
    'commentlen_nzttIdentity',
    'private_nzttIdentity',
    'next_nzttIdentity',
]
struct_nzttIdentity._fields_ = [
    ('dn_nzttIdentity', POINTER(text)),
    ('dnlen_nzttIdentity', ub4),
    ('comment_nzttIdentity', POINTER(text)),
    ('commentlen_nzttIdentity', ub4),
    ('private_nzttIdentity', POINTER(nzttIdentityPrivate)),
    ('next_nzttIdentity', POINTER(nzttIdentity)),
]

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 523
class struct_nzttPKCS7ProtInfo(Structure):
    pass

struct_nzttPKCS7ProtInfo.__slots__ = [
    'mictype_nzttPKCS7ProtInfo',
    'symmtype_nzttPKCS7ProtInfo',
    'keylen_nzttPKCS7ProtInfo',
]
struct_nzttPKCS7ProtInfo._fields_ = [
    ('mictype_nzttPKCS7ProtInfo', nzttCipherType),
    ('symmtype_nzttPKCS7ProtInfo', nzttCipherType),
    ('keylen_nzttPKCS7ProtInfo', ub4),
]

nzttPKCS7ProtInfo = struct_nzttPKCS7ProtInfo # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 529

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 536
class union_nzttProtInfo(Union):
    pass

union_nzttProtInfo.__slots__ = [
    'pkcs7_nzttProtInfo',
]
union_nzttProtInfo._fields_ = [
    ('pkcs7_nzttProtInfo', nzttPKCS7ProtInfo),
]

nzttProtInfo = union_nzttProtInfo # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 540

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 556
class struct_nzttPersonaDesc(Structure):
    pass

struct_nzttPersonaDesc.__slots__ = [
    'privlen_nzttPersonaDesc',
    'priv_nzttPersonaDesc',
    'prllen_nzttPersonaDesc',
    'prl_nzttPersonaDesc',
    'aliaslen_nzttPersonaDesc',
    'alias_nzttPersonaDesc',
    'longlen_nzttPersonaDesc',
    'long_nzttPersonaDesc',
]
struct_nzttPersonaDesc._fields_ = [
    ('privlen_nzttPersonaDesc', ub4),
    ('priv_nzttPersonaDesc', POINTER(ub1)),
    ('prllen_nzttPersonaDesc', ub4),
    ('prl_nzttPersonaDesc', POINTER(text)),
    ('aliaslen_nzttPersonaDesc', ub4),
    ('alias_nzttPersonaDesc', POINTER(text)),
    ('longlen_nzttPersonaDesc', ub4),
    ('long_nzttPersonaDesc', POINTER(text)),
]

nzttPersonaDesc = struct_nzttPersonaDesc # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 567

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 577
class struct_nzttIdentityDesc(Structure):
    pass

struct_nzttIdentityDesc.__slots__ = [
    'publen_nzttIdentityDesc',
    'pub_nzttIdentityDesc',
    'dnlen_nzttIdentityDesc',
    'dn_nzttIdentityDesc',
    'longlen_nzttIdentityDesc',
    'long_nzttIdentityDesc',
    'quallen_nzttIdentityDesc',
    'trustqual_nzttIdentityDesc',
]
struct_nzttIdentityDesc._fields_ = [
    ('publen_nzttIdentityDesc', ub4),
    ('pub_nzttIdentityDesc', POINTER(ub1)),
    ('dnlen_nzttIdentityDesc', ub4),
    ('dn_nzttIdentityDesc', POINTER(text)),
    ('longlen_nzttIdentityDesc', ub4),
    ('long_nzttIdentityDesc', POINTER(text)),
    ('quallen_nzttIdentityDesc', ub4),
    ('trustqual_nzttIdentityDesc', POINTER(text)),
]

nzttIdentityDesc = struct_nzttIdentityDesc # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/nzt.h: 588

OCICallbackInBind = CFUNCTYPE(UNCHECKED(sb4), POINTER(None), POINTER(OCIBind), ub4, ub4, POINTER(POINTER(None)), POINTER(ub4), POINTER(ub1), POINTER(POINTER(None))) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6338

OCICallbackOutBind = CFUNCTYPE(UNCHECKED(sb4), POINTER(None), POINTER(OCIBind), ub4, ub4, POINTER(POINTER(None)), POINTER(POINTER(ub4)), POINTER(ub1), POINTER(POINTER(None)), POINTER(POINTER(ub2))) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6342

OCICallbackDefine = CFUNCTYPE(UNCHECKED(sb4), POINTER(None), POINTER(OCIDefine), ub4, POINTER(POINTER(None)), POINTER(POINTER(ub4)), POINTER(ub1), POINTER(POINTER(None)), POINTER(POINTER(ub2))) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6347

OCIUserCallback = CFUNCTYPE(UNCHECKED(sword), POINTER(None), POINTER(None), ub4, ub4, ub4, sword, POINTER(sb4), c_void_p) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6351

OCIEnvCallbackType = CFUNCTYPE(UNCHECKED(sword), POINTER(OCIEnv), ub4, c_size_t, POINTER(None), POINTER(OCIUcb)) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6355

OCICallbackLobRead = CFUNCTYPE(UNCHECKED(sb4), POINTER(None), POINTER(None), ub4, ub1) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6359

OCICallbackLobWrite = CFUNCTYPE(UNCHECKED(sb4), POINTER(None), POINTER(None), POINTER(ub4), POINTER(ub1)) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6362

OCICallbackLobRead2 = CFUNCTYPE(UNCHECKED(sb4), POINTER(None), POINTER(None), oraub8, ub1, POINTER(POINTER(None)), POINTER(oraub8)) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6367

OCICallbackLobWrite2 = CFUNCTYPE(UNCHECKED(sb4), POINTER(None), POINTER(None), POINTER(oraub8), POINTER(ub1), POINTER(POINTER(None)), POINTER(oraub8)) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6371

OCICallbackLobArrayRead = CFUNCTYPE(UNCHECKED(sb4), POINTER(None), ub4, POINTER(None), oraub8, ub1, POINTER(POINTER(None)), POINTER(oraub8)) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6375

OCICallbackLobArrayWrite = CFUNCTYPE(UNCHECKED(sb4), POINTER(None), ub4, POINTER(None), POINTER(oraub8), POINTER(ub1), POINTER(POINTER(None)), POINTER(oraub8)) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6380

OCICallbackAQEnq = CFUNCTYPE(UNCHECKED(sb4), POINTER(None), POINTER(POINTER(None)), POINTER(POINTER(None))) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6387

OCICallbackAQDeq = CFUNCTYPE(UNCHECKED(sb4), POINTER(None), POINTER(POINTER(None)), POINTER(POINTER(None))) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6390

OCICallbackFailover = CFUNCTYPE(UNCHECKED(sb4), POINTER(None), POINTER(None), POINTER(None), ub4, ub4) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6394

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6403
class struct_anon_21(Structure):
    pass

struct_anon_21.__slots__ = [
    'callback_function',
    'fo_ctx',
]
struct_anon_21._fields_ = [
    ('callback_function', OCICallbackFailover),
    ('fo_ctx', POINTER(None)),
]

OCIFocbkStruct = struct_anon_21 # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6403

OCICallbackStmtCache = CFUNCTYPE(UNCHECKED(sword), POINTER(None), POINTER(OCIStmt), ub4) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6407

OCIEventCallback = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(OCIEvent)) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6410

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6417
if hasattr(_libs['libclntsh.so.10.1'], 'OCIInitialize'):
    OCIInitialize = _libs['libclntsh.so.10.1'].OCIInitialize
    OCIInitialize.argtypes = [ub4, POINTER(None), CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(None), c_size_t), CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(None), POINTER(None), c_size_t), CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None))]
    OCIInitialize.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6422
if hasattr(_libs['libclntsh.so.10.1'], 'OCITerminate'):
    OCITerminate = _libs['libclntsh.so.10.1'].OCITerminate
    OCITerminate.argtypes = [ub4]
    OCITerminate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6424
if hasattr(_libs['libclntsh.so.10.1'], 'OCIEnvCreate'):
    OCIEnvCreate = _libs['libclntsh.so.10.1'].OCIEnvCreate
    OCIEnvCreate.argtypes = [POINTER(POINTER(OCIEnv)), ub4, POINTER(None), CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(None), c_size_t), CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(None), POINTER(None), c_size_t), CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None)), c_size_t, POINTER(POINTER(None))]
    OCIEnvCreate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6430
if hasattr(_libs['libclntsh.so.10.1'], 'OCIEnvNlsCreate'):
    OCIEnvNlsCreate = _libs['libclntsh.so.10.1'].OCIEnvNlsCreate
    OCIEnvNlsCreate.argtypes = [POINTER(POINTER(OCIEnv)), ub4, POINTER(None), CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(None), c_size_t), CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(None), POINTER(None), c_size_t), CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None)), c_size_t, POINTER(POINTER(None)), ub2, ub2]
    OCIEnvNlsCreate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6437
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFEnvCreate'):
    OCIFEnvCreate = _libs['libclntsh.so.10.1'].OCIFEnvCreate
    OCIFEnvCreate.argtypes = [POINTER(POINTER(OCIEnv)), ub4, POINTER(None), CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(None), c_size_t), CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(None), POINTER(None), c_size_t), CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None)), c_size_t, POINTER(POINTER(None)), POINTER(None)]
    OCIFEnvCreate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6443
if hasattr(_libs['libclntsh.so.10.1'], 'OCIHandleAlloc'):
    OCIHandleAlloc = _libs['libclntsh.so.10.1'].OCIHandleAlloc
    OCIHandleAlloc.argtypes = [POINTER(None), POINTER(POINTER(None)), ub4, c_size_t, POINTER(POINTER(None))]
    OCIHandleAlloc.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6446
if hasattr(_libs['libclntsh.so.10.1'], 'OCIHandleFree'):
    OCIHandleFree = _libs['libclntsh.so.10.1'].OCIHandleFree
    OCIHandleFree.argtypes = [POINTER(None), ub4]
    OCIHandleFree.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6449
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDescriptorAlloc'):
    OCIDescriptorAlloc = _libs['libclntsh.so.10.1'].OCIDescriptorAlloc
    OCIDescriptorAlloc.argtypes = [POINTER(None), POINTER(POINTER(None)), ub4, c_size_t, POINTER(POINTER(None))]
    OCIDescriptorAlloc.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6453
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDescriptorFree'):
    OCIDescriptorFree = _libs['libclntsh.so.10.1'].OCIDescriptorFree
    OCIDescriptorFree.argtypes = [POINTER(None), ub4]
    OCIDescriptorFree.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6455
if hasattr(_libs['libclntsh.so.10.1'], 'OCIEnvInit'):
    OCIEnvInit = _libs['libclntsh.so.10.1'].OCIEnvInit
    OCIEnvInit.argtypes = [POINTER(POINTER(OCIEnv)), ub4, c_size_t, POINTER(POINTER(None))]
    OCIEnvInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6458
if hasattr(_libs['libclntsh.so.10.1'], 'OCIServerAttach'):
    OCIServerAttach = _libs['libclntsh.so.10.1'].OCIServerAttach
    OCIServerAttach.argtypes = [POINTER(OCIServer), POINTER(OCIError), POINTER(OraText), sb4, ub4]
    OCIServerAttach.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6461
if hasattr(_libs['libclntsh.so.10.1'], 'OCIServerDetach'):
    OCIServerDetach = _libs['libclntsh.so.10.1'].OCIServerDetach
    OCIServerDetach.argtypes = [POINTER(OCIServer), POINTER(OCIError), ub4]
    OCIServerDetach.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6463
if hasattr(_libs['libclntsh.so.10.1'], 'OCISessionBegin'):
    OCISessionBegin = _libs['libclntsh.so.10.1'].OCISessionBegin
    OCISessionBegin.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCISession), ub4, ub4]
    OCISessionBegin.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6466
if hasattr(_libs['libclntsh.so.10.1'], 'OCISessionEnd'):
    OCISessionEnd = _libs['libclntsh.so.10.1'].OCISessionEnd
    OCISessionEnd.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCISession), ub4]
    OCISessionEnd.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6469
if hasattr(_libs['libclntsh.so.10.1'], 'OCILogon'):
    OCILogon = _libs['libclntsh.so.10.1'].OCILogon
    OCILogon.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(POINTER(OCISvcCtx)), POINTER(OraText), ub4, POINTER(OraText), ub4, POINTER(OraText), ub4]
    OCILogon.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6474
if hasattr(_libs['libclntsh.so.10.1'], 'OCILogon2'):
    OCILogon2 = _libs['libclntsh.so.10.1'].OCILogon2
    OCILogon2.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(POINTER(OCISvcCtx)), POINTER(OraText), ub4, POINTER(OraText), ub4, POINTER(OraText), ub4, ub4]
    OCILogon2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6480
if hasattr(_libs['libclntsh.so.10.1'], 'OCILogoff'):
    OCILogoff = _libs['libclntsh.so.10.1'].OCILogoff
    OCILogoff.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError)]
    OCILogoff.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6483
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPasswordChange'):
    OCIPasswordChange = _libs['libclntsh.so.10.1'].OCIPasswordChange
    OCIPasswordChange.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OraText), ub4, POINTER(OraText), ub4, POINTER(OraText), ub4, ub4]
    OCIPasswordChange.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6489
if hasattr(_libs['libclntsh.so.10.1'], 'OCIStmtPrepare'):
    OCIStmtPrepare = _libs['libclntsh.so.10.1'].OCIStmtPrepare
    OCIStmtPrepare.argtypes = [POINTER(OCIStmt), POINTER(OCIError), POINTER(OraText), ub4, ub4, ub4]
    OCIStmtPrepare.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6492
if hasattr(_libs['libclntsh.so.10.1'], 'OCIStmtPrepare2'):
    OCIStmtPrepare2 = _libs['libclntsh.so.10.1'].OCIStmtPrepare2
    OCIStmtPrepare2.argtypes = [POINTER(OCISvcCtx), POINTER(POINTER(OCIStmt)), POINTER(OCIError), POINTER(OraText), ub4, POINTER(OraText), ub4, ub4, ub4]
    OCIStmtPrepare2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6496
if hasattr(_libs['libclntsh.so.10.1'], 'OCIStmtRelease'):
    OCIStmtRelease = _libs['libclntsh.so.10.1'].OCIStmtRelease
    OCIStmtRelease.argtypes = [POINTER(OCIStmt), POINTER(OCIError), POINTER(OraText), ub4, ub4]
    OCIStmtRelease.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6499
if hasattr(_libs['libclntsh.so.10.1'], 'OCIBindByPos'):
    OCIBindByPos = _libs['libclntsh.so.10.1'].OCIBindByPos
    OCIBindByPos.argtypes = [POINTER(OCIStmt), POINTER(POINTER(OCIBind)), POINTER(OCIError), ub4, POINTER(None), sb4, ub2, POINTER(None), POINTER(ub2), POINTER(ub2), ub4, POINTER(ub4), ub4]
    OCIBindByPos.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6504
if hasattr(_libs['libclntsh.so.10.1'], 'OCIBindByName'):
    OCIBindByName = _libs['libclntsh.so.10.1'].OCIBindByName
    OCIBindByName.argtypes = [POINTER(OCIStmt), POINTER(POINTER(OCIBind)), POINTER(OCIError), POINTER(OraText), sb4, POINTER(None), sb4, ub2, POINTER(None), POINTER(ub2), POINTER(ub2), ub4, POINTER(ub4), ub4]
    OCIBindByName.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6510
if hasattr(_libs['libclntsh.so.10.1'], 'OCIBindObject'):
    OCIBindObject = _libs['libclntsh.so.10.1'].OCIBindObject
    OCIBindObject.argtypes = [POINTER(OCIBind), POINTER(OCIError), POINTER(OCIType), POINTER(POINTER(None)), POINTER(ub4), POINTER(POINTER(None)), POINTER(ub4)]
    OCIBindObject.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6514
if hasattr(_libs['libclntsh.so.10.1'], 'OCIBindDynamic'):
    OCIBindDynamic = _libs['libclntsh.so.10.1'].OCIBindDynamic
    OCIBindDynamic.argtypes = [POINTER(OCIBind), POINTER(OCIError), POINTER(None), OCICallbackInBind, POINTER(None), OCICallbackOutBind]
    OCIBindDynamic.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6518
if hasattr(_libs['libclntsh.so.10.1'], 'OCIBindArrayOfStruct'):
    OCIBindArrayOfStruct = _libs['libclntsh.so.10.1'].OCIBindArrayOfStruct
    OCIBindArrayOfStruct.argtypes = [POINTER(OCIBind), POINTER(OCIError), ub4, ub4, ub4, ub4]
    OCIBindArrayOfStruct.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6522
if hasattr(_libs['libclntsh.so.10.1'], 'OCIStmtGetPieceInfo'):
    OCIStmtGetPieceInfo = _libs['libclntsh.so.10.1'].OCIStmtGetPieceInfo
    OCIStmtGetPieceInfo.argtypes = [POINTER(OCIStmt), POINTER(OCIError), POINTER(POINTER(None)), POINTER(ub4), POINTER(ub1), POINTER(ub4), POINTER(ub4), POINTER(ub1)]
    OCIStmtGetPieceInfo.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6527
if hasattr(_libs['libclntsh.so.10.1'], 'OCIStmtSetPieceInfo'):
    OCIStmtSetPieceInfo = _libs['libclntsh.so.10.1'].OCIStmtSetPieceInfo
    OCIStmtSetPieceInfo.argtypes = [POINTER(None), ub4, POINTER(OCIError), POINTER(None), POINTER(ub4), ub1, POINTER(None), POINTER(ub2)]
    OCIStmtSetPieceInfo.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6531
if hasattr(_libs['libclntsh.so.10.1'], 'OCIStmtExecute'):
    OCIStmtExecute = _libs['libclntsh.so.10.1'].OCIStmtExecute
    OCIStmtExecute.argtypes = [POINTER(OCISvcCtx), POINTER(OCIStmt), POINTER(OCIError), ub4, ub4, POINTER(OCISnapshot), POINTER(OCISnapshot), ub4]
    OCIStmtExecute.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6535
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDefineByPos'):
    OCIDefineByPos = _libs['libclntsh.so.10.1'].OCIDefineByPos
    OCIDefineByPos.argtypes = [POINTER(OCIStmt), POINTER(POINTER(OCIDefine)), POINTER(OCIError), ub4, POINTER(None), sb4, ub2, POINTER(None), POINTER(ub2), POINTER(ub2), ub4]
    OCIDefineByPos.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6539
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDefineObject'):
    OCIDefineObject = _libs['libclntsh.so.10.1'].OCIDefineObject
    OCIDefineObject.argtypes = [POINTER(OCIDefine), POINTER(OCIError), POINTER(OCIType), POINTER(POINTER(None)), POINTER(ub4), POINTER(POINTER(None)), POINTER(ub4)]
    OCIDefineObject.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6543
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDefineDynamic'):
    OCIDefineDynamic = _libs['libclntsh.so.10.1'].OCIDefineDynamic
    OCIDefineDynamic.argtypes = [POINTER(OCIDefine), POINTER(OCIError), POINTER(None), OCICallbackDefine]
    OCIDefineDynamic.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6546
if hasattr(_libs['libclntsh.so.10.1'], 'OCIRowidToChar'):
    OCIRowidToChar = _libs['libclntsh.so.10.1'].OCIRowidToChar
    OCIRowidToChar.argtypes = [POINTER(OCIRowid), POINTER(OraText), POINTER(ub2), POINTER(OCIError)]
    OCIRowidToChar.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6549
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDefineArrayOfStruct'):
    OCIDefineArrayOfStruct = _libs['libclntsh.so.10.1'].OCIDefineArrayOfStruct
    OCIDefineArrayOfStruct.argtypes = [POINTER(OCIDefine), POINTER(OCIError), ub4, ub4, ub4, ub4]
    OCIDefineArrayOfStruct.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6552
if hasattr(_libs['libclntsh.so.10.1'], 'OCIStmtFetch'):
    OCIStmtFetch = _libs['libclntsh.so.10.1'].OCIStmtFetch
    OCIStmtFetch.argtypes = [POINTER(OCIStmt), POINTER(OCIError), ub4, ub2, ub4]
    OCIStmtFetch.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6555
if hasattr(_libs['libclntsh.so.10.1'], 'OCIStmtFetch2'):
    OCIStmtFetch2 = _libs['libclntsh.so.10.1'].OCIStmtFetch2
    OCIStmtFetch2.argtypes = [POINTER(OCIStmt), POINTER(OCIError), ub4, ub2, sb4, ub4]
    OCIStmtFetch2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6558
if hasattr(_libs['libclntsh.so.10.1'], 'OCIStmtGetBindInfo'):
    OCIStmtGetBindInfo = _libs['libclntsh.so.10.1'].OCIStmtGetBindInfo
    OCIStmtGetBindInfo.argtypes = [POINTER(OCIStmt), POINTER(OCIError), ub4, ub4, POINTER(sb4), POINTER(POINTER(OraText)), POINTER(ub1), POINTER(POINTER(OraText)), POINTER(ub1), POINTER(ub1), POINTER(POINTER(OCIBind))]
    OCIStmtGetBindInfo.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6564
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDescribeAny'):
    OCIDescribeAny = _libs['libclntsh.so.10.1'].OCIDescribeAny
    OCIDescribeAny.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(None), ub4, ub1, ub1, ub1, POINTER(OCIDescribe)]
    OCIDescribeAny.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6569
if hasattr(_libs['libclntsh.so.10.1'], 'OCIParamGet'):
    OCIParamGet = _libs['libclntsh.so.10.1'].OCIParamGet
    OCIParamGet.argtypes = [POINTER(None), ub4, POINTER(OCIError), POINTER(POINTER(None)), ub4]
    OCIParamGet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6572
if hasattr(_libs['libclntsh.so.10.1'], 'OCIParamSet'):
    OCIParamSet = _libs['libclntsh.so.10.1'].OCIParamSet
    OCIParamSet.argtypes = [POINTER(None), ub4, POINTER(OCIError), POINTER(None), ub4, ub4]
    OCIParamSet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6575
if hasattr(_libs['libclntsh.so.10.1'], 'OCITransStart'):
    OCITransStart = _libs['libclntsh.so.10.1'].OCITransStart
    OCITransStart.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), uword, ub4]
    OCITransStart.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6578
if hasattr(_libs['libclntsh.so.10.1'], 'OCITransDetach'):
    OCITransDetach = _libs['libclntsh.so.10.1'].OCITransDetach
    OCITransDetach.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), ub4]
    OCITransDetach.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6580
if hasattr(_libs['libclntsh.so.10.1'], 'OCITransCommit'):
    OCITransCommit = _libs['libclntsh.so.10.1'].OCITransCommit
    OCITransCommit.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), ub4]
    OCITransCommit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6582
if hasattr(_libs['libclntsh.so.10.1'], 'OCITransRollback'):
    OCITransRollback = _libs['libclntsh.so.10.1'].OCITransRollback
    OCITransRollback.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), ub4]
    OCITransRollback.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6584
if hasattr(_libs['libclntsh.so.10.1'], 'OCITransPrepare'):
    OCITransPrepare = _libs['libclntsh.so.10.1'].OCITransPrepare
    OCITransPrepare.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), ub4]
    OCITransPrepare.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6586
if hasattr(_libs['libclntsh.so.10.1'], 'OCITransMultiPrepare'):
    OCITransMultiPrepare = _libs['libclntsh.so.10.1'].OCITransMultiPrepare
    OCITransMultiPrepare.argtypes = [POINTER(OCISvcCtx), ub4, POINTER(POINTER(OCITrans)), POINTER(POINTER(OCIError))]
    OCITransMultiPrepare.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6589
if hasattr(_libs['libclntsh.so.10.1'], 'OCITransForget'):
    OCITransForget = _libs['libclntsh.so.10.1'].OCITransForget
    OCITransForget.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), ub4]
    OCITransForget.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6591
if hasattr(_libs['libclntsh.so.10.1'], 'OCIErrorGet'):
    OCIErrorGet = _libs['libclntsh.so.10.1'].OCIErrorGet
    OCIErrorGet.argtypes = [POINTER(None), ub4, POINTER(OraText), POINTER(sb4), POINTER(OraText), ub4, ub4]
    OCIErrorGet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6594
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobAppend'):
    OCILobAppend = _libs['libclntsh.so.10.1'].OCILobAppend
    OCILobAppend.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(OCILobLocator)]
    OCILobAppend.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6598
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobAssign'):
    OCILobAssign = _libs['libclntsh.so.10.1'].OCILobAssign
    OCILobAssign.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCILobLocator), POINTER(POINTER(OCILobLocator))]
    OCILobAssign.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6602
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobCharSetForm'):
    OCILobCharSetForm = _libs['libclntsh.so.10.1'].OCILobCharSetForm
    OCILobCharSetForm.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCILobLocator), POINTER(ub1)]
    OCILobCharSetForm.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6605
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobCharSetId'):
    OCILobCharSetId = _libs['libclntsh.so.10.1'].OCILobCharSetId
    OCILobCharSetId.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCILobLocator), POINTER(ub2)]
    OCILobCharSetId.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6608
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobCopy'):
    OCILobCopy = _libs['libclntsh.so.10.1'].OCILobCopy
    OCILobCopy.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(OCILobLocator), ub4, ub4, ub4]
    OCILobCopy.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6612
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobCreateTemporary'):
    OCILobCreateTemporary = _libs['libclntsh.so.10.1'].OCILobCreateTemporary
    OCILobCreateTemporary.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), ub2, ub1, ub1, boolean, OCIDuration]
    OCILobCreateTemporary.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6622
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobClose'):
    OCILobClose = _libs['libclntsh.so.10.1'].OCILobClose
    OCILobClose.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator)]
    OCILobClose.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6627
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobDisableBuffering'):
    OCILobDisableBuffering = _libs['libclntsh.so.10.1'].OCILobDisableBuffering
    OCILobDisableBuffering.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator)]
    OCILobDisableBuffering.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6631
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobEnableBuffering'):
    OCILobEnableBuffering = _libs['libclntsh.so.10.1'].OCILobEnableBuffering
    OCILobEnableBuffering.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator)]
    OCILobEnableBuffering.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6635
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobErase'):
    OCILobErase = _libs['libclntsh.so.10.1'].OCILobErase
    OCILobErase.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(ub4), ub4]
    OCILobErase.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6638
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobFileClose'):
    OCILobFileClose = _libs['libclntsh.so.10.1'].OCILobFileClose
    OCILobFileClose.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator)]
    OCILobFileClose.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6641
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobFileCloseAll'):
    OCILobFileCloseAll = _libs['libclntsh.so.10.1'].OCILobFileCloseAll
    OCILobFileCloseAll.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError)]
    OCILobFileCloseAll.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6643
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobFileExists'):
    OCILobFileExists = _libs['libclntsh.so.10.1'].OCILobFileExists
    OCILobFileExists.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(boolean)]
    OCILobFileExists.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6647
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobFileGetName'):
    OCILobFileGetName = _libs['libclntsh.so.10.1'].OCILobFileGetName
    OCILobFileGetName.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCILobLocator), POINTER(OraText), POINTER(ub2), POINTER(OraText), POINTER(ub2)]
    OCILobFileGetName.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6652
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobFileIsOpen'):
    OCILobFileIsOpen = _libs['libclntsh.so.10.1'].OCILobFileIsOpen
    OCILobFileIsOpen.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(boolean)]
    OCILobFileIsOpen.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6656
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobFileOpen'):
    OCILobFileOpen = _libs['libclntsh.so.10.1'].OCILobFileOpen
    OCILobFileOpen.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), ub1]
    OCILobFileOpen.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6660
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobFileSetName'):
    OCILobFileSetName = _libs['libclntsh.so.10.1'].OCILobFileSetName
    OCILobFileSetName.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(POINTER(OCILobLocator)), POINTER(OraText), ub2, POINTER(OraText), ub2]
    OCILobFileSetName.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6665
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobFlushBuffer'):
    OCILobFlushBuffer = _libs['libclntsh.so.10.1'].OCILobFlushBuffer
    OCILobFlushBuffer.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), ub4]
    OCILobFlushBuffer.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6670
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobFreeTemporary'):
    OCILobFreeTemporary = _libs['libclntsh.so.10.1'].OCILobFreeTemporary
    OCILobFreeTemporary.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator)]
    OCILobFreeTemporary.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6674
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobGetChunkSize'):
    OCILobGetChunkSize = _libs['libclntsh.so.10.1'].OCILobGetChunkSize
    OCILobGetChunkSize.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(ub4)]
    OCILobGetChunkSize.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6679
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobGetLength'):
    OCILobGetLength = _libs['libclntsh.so.10.1'].OCILobGetLength
    OCILobGetLength.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(ub4)]
    OCILobGetLength.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6683
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobIsEqual'):
    OCILobIsEqual = _libs['libclntsh.so.10.1'].OCILobIsEqual
    OCILobIsEqual.argtypes = [POINTER(OCIEnv), POINTER(OCILobLocator), POINTER(OCILobLocator), POINTER(boolean)]
    OCILobIsEqual.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6687
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobIsOpen'):
    OCILobIsOpen = _libs['libclntsh.so.10.1'].OCILobIsOpen
    OCILobIsOpen.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(boolean)]
    OCILobIsOpen.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6692
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobIsTemporary'):
    OCILobIsTemporary = _libs['libclntsh.so.10.1'].OCILobIsTemporary
    OCILobIsTemporary.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCILobLocator), POINTER(boolean)]
    OCILobIsTemporary.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6697
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobLoadFromFile'):
    OCILobLoadFromFile = _libs['libclntsh.so.10.1'].OCILobLoadFromFile
    OCILobLoadFromFile.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(OCILobLocator), ub4, ub4, ub4]
    OCILobLoadFromFile.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6703
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobLocatorAssign'):
    OCILobLocatorAssign = _libs['libclntsh.so.10.1'].OCILobLocatorAssign
    OCILobLocatorAssign.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(POINTER(OCILobLocator))]
    OCILobLocatorAssign.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6708
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobLocatorIsInit'):
    OCILobLocatorIsInit = _libs['libclntsh.so.10.1'].OCILobLocatorIsInit
    OCILobLocatorIsInit.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCILobLocator), POINTER(boolean)]
    OCILobLocatorIsInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6712
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobOpen'):
    OCILobOpen = _libs['libclntsh.so.10.1'].OCILobOpen
    OCILobOpen.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), ub1]
    OCILobOpen.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6717
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobRead'):
    OCILobRead = _libs['libclntsh.so.10.1'].OCILobRead
    OCILobRead.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(ub4), ub4, POINTER(None), ub4, POINTER(None), OCICallbackLobRead, ub2, ub1]
    OCILobRead.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6721
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobTrim'):
    OCILobTrim = _libs['libclntsh.so.10.1'].OCILobTrim
    OCILobTrim.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), ub4]
    OCILobTrim.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6724
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobWrite'):
    OCILobWrite = _libs['libclntsh.so.10.1'].OCILobWrite
    OCILobWrite.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(ub4), ub4, POINTER(None), ub4, ub1, POINTER(None), OCICallbackLobWrite, ub2, ub1]
    OCILobWrite.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6729
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobWriteAppend'):
    OCILobWriteAppend = _libs['libclntsh.so.10.1'].OCILobWriteAppend
    OCILobWriteAppend.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(ub4), POINTER(None), ub4, ub1, POINTER(None), OCICallbackLobWrite, ub2, ub1]
    OCILobWriteAppend.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6733
if hasattr(_libs['libclntsh.so.10.1'], 'OCIBreak'):
    OCIBreak = _libs['libclntsh.so.10.1'].OCIBreak
    OCIBreak.argtypes = [POINTER(None), POINTER(OCIError)]
    OCIBreak.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6735
if hasattr(_libs['libclntsh.so.10.1'], 'OCIReset'):
    OCIReset = _libs['libclntsh.so.10.1'].OCIReset
    OCIReset.argtypes = [POINTER(None), POINTER(OCIError)]
    OCIReset.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6737
if hasattr(_libs['libclntsh.so.10.1'], 'OCIServerVersion'):
    OCIServerVersion = _libs['libclntsh.so.10.1'].OCIServerVersion
    OCIServerVersion.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OraText), ub4, ub1]
    OCIServerVersion.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6741
if hasattr(_libs['libclntsh.so.10.1'], 'OCIServerRelease'):
    OCIServerRelease = _libs['libclntsh.so.10.1'].OCIServerRelease
    OCIServerRelease.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OraText), ub4, ub1, POINTER(ub4)]
    OCIServerRelease.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6745
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAttrGet'):
    OCIAttrGet = _libs['libclntsh.so.10.1'].OCIAttrGet
    OCIAttrGet.argtypes = [POINTER(None), ub4, POINTER(None), POINTER(ub4), ub4, POINTER(OCIError)]
    OCIAttrGet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6749
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAttrSet'):
    OCIAttrSet = _libs['libclntsh.so.10.1'].OCIAttrSet
    OCIAttrSet.argtypes = [POINTER(None), ub4, POINTER(None), ub4, ub4, POINTER(OCIError)]
    OCIAttrSet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6752
if hasattr(_libs['libclntsh.so.10.1'], 'OCISvcCtxToLda'):
    OCISvcCtxToLda = _libs['libclntsh.so.10.1'].OCISvcCtxToLda
    OCISvcCtxToLda.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(Lda_Def)]
    OCISvcCtxToLda.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6754
if hasattr(_libs['libclntsh.so.10.1'], 'OCILdaToSvcCtx'):
    OCILdaToSvcCtx = _libs['libclntsh.so.10.1'].OCILdaToSvcCtx
    OCILdaToSvcCtx.argtypes = [POINTER(POINTER(OCISvcCtx)), POINTER(OCIError), POINTER(Lda_Def)]
    OCILdaToSvcCtx.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6756
if hasattr(_libs['libclntsh.so.10.1'], 'OCIResultSetToStmt'):
    OCIResultSetToStmt = _libs['libclntsh.so.10.1'].OCIResultSetToStmt
    OCIResultSetToStmt.argtypes = [POINTER(OCIResult), POINTER(OCIError)]
    OCIResultSetToStmt.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6758
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFileClose'):
    OCIFileClose = _libs['libclntsh.so.10.1'].OCIFileClose
    OCIFileClose.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIFileObject)]
    OCIFileClose.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6760
if hasattr(_libs['libclntsh.so.10.1'], 'OCIUserCallbackRegister'):
    OCIUserCallbackRegister = _libs['libclntsh.so.10.1'].OCIUserCallbackRegister
    OCIUserCallbackRegister.argtypes = [POINTER(None), ub4, POINTER(None), OCIUserCallback, POINTER(None), ub4, ub4, POINTER(OCIUcb)]
    OCIUserCallbackRegister.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6764
if hasattr(_libs['libclntsh.so.10.1'], 'OCIUserCallbackGet'):
    OCIUserCallbackGet = _libs['libclntsh.so.10.1'].OCIUserCallbackGet
    OCIUserCallbackGet.argtypes = [POINTER(None), ub4, POINTER(None), ub4, ub4, POINTER(OCIUserCallback), POINTER(POINTER(None)), POINTER(OCIUcb)]
    OCIUserCallbackGet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6768
if hasattr(_libs['libclntsh.so.10.1'], 'OCISharedLibInit'):
    OCISharedLibInit = _libs['libclntsh.so.10.1'].OCISharedLibInit
    OCISharedLibInit.argtypes = [POINTER(None), POINTER(None), ub4, sword, POINTER(POINTER(None)), OCIEnvCallbackType]
    OCISharedLibInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6771
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFileExists'):
    OCIFileExists = _libs['libclntsh.so.10.1'].OCIFileExists
    OCIFileExists.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OraText), POINTER(OraText), POINTER(ub1)]
    OCIFileExists.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6774
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFileFlush'):
    OCIFileFlush = _libs['libclntsh.so.10.1'].OCIFileFlush
    OCIFileFlush.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIFileObject)]
    OCIFileFlush.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6777
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFileGetLength'):
    OCIFileGetLength = _libs['libclntsh.so.10.1'].OCIFileGetLength
    OCIFileGetLength.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OraText), POINTER(OraText), POINTER(ubig_ora)]
    OCIFileGetLength.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6780
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFileInit'):
    OCIFileInit = _libs['libclntsh.so.10.1'].OCIFileInit
    OCIFileInit.argtypes = [POINTER(None), POINTER(OCIError)]
    OCIFileInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6782
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFileOpen'):
    OCIFileOpen = _libs['libclntsh.so.10.1'].OCIFileOpen
    OCIFileOpen.argtypes = [POINTER(None), POINTER(OCIError), POINTER(POINTER(OCIFileObject)), POINTER(OraText), POINTER(OraText), ub4, ub4, ub4]
    OCIFileOpen.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6786
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFileRead'):
    OCIFileRead = _libs['libclntsh.so.10.1'].OCIFileRead
    OCIFileRead.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIFileObject), POINTER(None), ub4, POINTER(ub4)]
    OCIFileRead.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6789
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFileSeek'):
    OCIFileSeek = _libs['libclntsh.so.10.1'].OCIFileSeek
    OCIFileSeek.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIFileObject), uword, ubig_ora, sb1]
    OCIFileSeek.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6792
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFileTerm'):
    OCIFileTerm = _libs['libclntsh.so.10.1'].OCIFileTerm
    OCIFileTerm.argtypes = [POINTER(None), POINTER(OCIError)]
    OCIFileTerm.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6795
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFileWrite'):
    OCIFileWrite = _libs['libclntsh.so.10.1'].OCIFileWrite
    OCIFileWrite.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIFileObject), POINTER(None), ub4, POINTER(ub4)]
    OCIFileWrite.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6801
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobCopy2'):
    OCILobCopy2 = _libs['libclntsh.so.10.1'].OCILobCopy2
    OCILobCopy2.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(OCILobLocator), oraub8, oraub8, oraub8]
    OCILobCopy2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6805
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobErase2'):
    OCILobErase2 = _libs['libclntsh.so.10.1'].OCILobErase2
    OCILobErase2.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(oraub8), oraub8]
    OCILobErase2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6808
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobGetLength2'):
    OCILobGetLength2 = _libs['libclntsh.so.10.1'].OCILobGetLength2
    OCILobGetLength2.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(oraub8)]
    OCILobGetLength2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6811
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobLoadFromFile2'):
    OCILobLoadFromFile2 = _libs['libclntsh.so.10.1'].OCILobLoadFromFile2
    OCILobLoadFromFile2.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(OCILobLocator), oraub8, oraub8, oraub8]
    OCILobLoadFromFile2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6817
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobRead2'):
    OCILobRead2 = _libs['libclntsh.so.10.1'].OCILobRead2
    OCILobRead2.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(oraub8), POINTER(oraub8), oraub8, POINTER(None), oraub8, ub1, POINTER(None), OCICallbackLobRead2, ub2, ub1]
    OCILobRead2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6822
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobArrayRead'):
    OCILobArrayRead = _libs['libclntsh.so.10.1'].OCILobArrayRead
    OCILobArrayRead.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(ub4), POINTER(POINTER(OCILobLocator)), POINTER(oraub8), POINTER(oraub8), POINTER(oraub8), POINTER(POINTER(None)), POINTER(oraub8), ub1, POINTER(None), OCICallbackLobArrayRead, ub2, ub1]
    OCILobArrayRead.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6829
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobTrim2'):
    OCILobTrim2 = _libs['libclntsh.so.10.1'].OCILobTrim2
    OCILobTrim2.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), oraub8]
    OCILobTrim2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6832
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobWrite2'):
    OCILobWrite2 = _libs['libclntsh.so.10.1'].OCILobWrite2
    OCILobWrite2.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(oraub8), POINTER(oraub8), oraub8, POINTER(None), oraub8, ub1, POINTER(None), OCICallbackLobWrite2, ub2, ub1]
    OCILobWrite2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6837
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobArrayWrite'):
    OCILobArrayWrite = _libs['libclntsh.so.10.1'].OCILobArrayWrite
    OCILobArrayWrite.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(ub4), POINTER(POINTER(OCILobLocator)), POINTER(oraub8), POINTER(oraub8), POINTER(oraub8), POINTER(POINTER(None)), POINTER(oraub8), ub1, POINTER(None), OCICallbackLobArrayWrite, ub2, ub1]
    OCILobArrayWrite.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6844
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobWriteAppend2'):
    OCILobWriteAppend2 = _libs['libclntsh.so.10.1'].OCILobWriteAppend2
    OCILobWriteAppend2.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(oraub8), POINTER(oraub8), POINTER(None), oraub8, ub1, POINTER(None), OCICallbackLobWrite2, ub2, ub1]
    OCILobWriteAppend2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6849
if hasattr(_libs['libclntsh.so.10.1'], 'OCILobGetStorageLimit'):
    OCILobGetStorageLimit = _libs['libclntsh.so.10.1'].OCILobGetStorageLimit
    OCILobGetStorageLimit.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCILobLocator), POINTER(oraub8)]
    OCILobGetStorageLimit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6857
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityInitialize'):
    OCISecurityInitialize = _libs['libclntsh.so.10.1'].OCISecurityInitialize
    OCISecurityInitialize.argtypes = [POINTER(OCISecurity), POINTER(OCIError)]
    OCISecurityInitialize.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6859
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityTerminate'):
    OCISecurityTerminate = _libs['libclntsh.so.10.1'].OCISecurityTerminate
    OCISecurityTerminate.argtypes = [POINTER(OCISecurity), POINTER(OCIError)]
    OCISecurityTerminate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6861
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityOpenWallet'):
    OCISecurityOpenWallet = _libs['libclntsh.so.10.1'].OCISecurityOpenWallet
    OCISecurityOpenWallet.argtypes = [POINTER(OCISecurity), POINTER(OCIError), c_size_t, POINTER(OraText), c_size_t, POINTER(OraText), POINTER(nzttWallet)]
    OCISecurityOpenWallet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6869
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityCloseWallet'):
    OCISecurityCloseWallet = _libs['libclntsh.so.10.1'].OCISecurityCloseWallet
    OCISecurityCloseWallet.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttWallet)]
    OCISecurityCloseWallet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6873
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityCreateWallet'):
    OCISecurityCreateWallet = _libs['libclntsh.so.10.1'].OCISecurityCreateWallet
    OCISecurityCreateWallet.argtypes = [POINTER(OCISecurity), POINTER(OCIError), c_size_t, POINTER(OraText), c_size_t, POINTER(OraText), POINTER(nzttWallet)]
    OCISecurityCreateWallet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6881
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityDestroyWallet'):
    OCISecurityDestroyWallet = _libs['libclntsh.so.10.1'].OCISecurityDestroyWallet
    OCISecurityDestroyWallet.argtypes = [POINTER(OCISecurity), POINTER(OCIError), c_size_t, POINTER(OraText), c_size_t, POINTER(OraText)]
    OCISecurityDestroyWallet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6888
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityStorePersona'):
    OCISecurityStorePersona = _libs['libclntsh.so.10.1'].OCISecurityStorePersona
    OCISecurityStorePersona.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(POINTER(nzttPersona)), POINTER(nzttWallet)]
    OCISecurityStorePersona.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6893
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityOpenPersona'):
    OCISecurityOpenPersona = _libs['libclntsh.so.10.1'].OCISecurityOpenPersona
    OCISecurityOpenPersona.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona)]
    OCISecurityOpenPersona.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6897
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityClosePersona'):
    OCISecurityClosePersona = _libs['libclntsh.so.10.1'].OCISecurityClosePersona
    OCISecurityClosePersona.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona)]
    OCISecurityClosePersona.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6901
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityRemovePersona'):
    OCISecurityRemovePersona = _libs['libclntsh.so.10.1'].OCISecurityRemovePersona
    OCISecurityRemovePersona.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(POINTER(nzttPersona))]
    OCISecurityRemovePersona.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6905
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityCreatePersona'):
    OCISecurityCreatePersona = _libs['libclntsh.so.10.1'].OCISecurityCreatePersona
    OCISecurityCreatePersona.argtypes = [POINTER(OCISecurity), POINTER(OCIError), nzttIdentType, nzttCipherType, POINTER(nzttPersonaDesc), POINTER(POINTER(nzttPersona))]
    OCISecurityCreatePersona.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6912
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecuritySetProtection'):
    OCISecuritySetProtection = _libs['libclntsh.so.10.1'].OCISecuritySetProtection
    OCISecuritySetProtection.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), nzttcef, nztttdufmt, POINTER(nzttProtInfo)]
    OCISecuritySetProtection.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6919
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityGetProtection'):
    OCISecurityGetProtection = _libs['libclntsh.so.10.1'].OCISecurityGetProtection
    OCISecurityGetProtection.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), nzttcef, POINTER(nztttdufmt), POINTER(nzttProtInfo)]
    OCISecurityGetProtection.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6926
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityRemoveIdentity'):
    OCISecurityRemoveIdentity = _libs['libclntsh.so.10.1'].OCISecurityRemoveIdentity
    OCISecurityRemoveIdentity.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(POINTER(nzttIdentity))]
    OCISecurityRemoveIdentity.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6930
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityCreateIdentity'):
    OCISecurityCreateIdentity = _libs['libclntsh.so.10.1'].OCISecurityCreateIdentity
    OCISecurityCreateIdentity.argtypes = [POINTER(OCISecurity), POINTER(OCIError), nzttIdentType, POINTER(nzttIdentityDesc), POINTER(POINTER(nzttIdentity))]
    OCISecurityCreateIdentity.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6936
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityAbortIdentity'):
    OCISecurityAbortIdentity = _libs['libclntsh.so.10.1'].OCISecurityAbortIdentity
    OCISecurityAbortIdentity.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(POINTER(nzttIdentity))]
    OCISecurityAbortIdentity.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6940
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityFreeIdentity'):
    OCISecurityFreeIdentity = _libs['libclntsh.so.10.1'].OCISecurityFreeIdentity
    OCISecurityFreeIdentity.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(POINTER(nzttIdentity))]
    OCISecurityFreeIdentity.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6945
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityStoreTrustedIdentity'):
    OCISecurityStoreTrustedIdentity = _libs['libclntsh.so.10.1'].OCISecurityStoreTrustedIdentity
    OCISecurityStoreTrustedIdentity.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(POINTER(nzttIdentity)), POINTER(nzttPersona)]
    OCISecurityStoreTrustedIdentity.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6950
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecuritySign'):
    OCISecuritySign = _libs['libclntsh.so.10.1'].OCISecuritySign
    OCISecuritySign.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), nzttces, c_size_t, POINTER(ub1), POINTER(nzttBufferBlock)]
    OCISecuritySign.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6958
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecuritySignExpansion'):
    OCISecuritySignExpansion = _libs['libclntsh.so.10.1'].OCISecuritySignExpansion
    OCISecuritySignExpansion.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), c_size_t, POINTER(c_size_t)]
    OCISecuritySignExpansion.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6964
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityVerify'):
    OCISecurityVerify = _libs['libclntsh.so.10.1'].OCISecurityVerify
    OCISecurityVerify.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), nzttces, c_size_t, POINTER(ub1), POINTER(nzttBufferBlock), POINTER(boolean), POINTER(boolean), POINTER(POINTER(nzttIdentity))]
    OCISecurityVerify.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6975
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityValidate'):
    OCISecurityValidate = _libs['libclntsh.so.10.1'].OCISecurityValidate
    OCISecurityValidate.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), POINTER(nzttIdentity), POINTER(boolean)]
    OCISecurityValidate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6981
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecuritySignDetached'):
    OCISecuritySignDetached = _libs['libclntsh.so.10.1'].OCISecuritySignDetached
    OCISecuritySignDetached.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), nzttces, c_size_t, POINTER(ub1), POINTER(nzttBufferBlock)]
    OCISecuritySignDetached.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6989
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecuritySignDetExpansion'):
    OCISecuritySignDetExpansion = _libs['libclntsh.so.10.1'].OCISecuritySignDetExpansion
    OCISecuritySignDetExpansion.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), c_size_t, POINTER(c_size_t)]
    OCISecuritySignDetExpansion.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 6995
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityVerifyDetached'):
    OCISecurityVerifyDetached = _libs['libclntsh.so.10.1'].OCISecurityVerifyDetached
    OCISecurityVerifyDetached.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), nzttces, c_size_t, POINTER(ub1), c_size_t, POINTER(ub1), POINTER(boolean), POINTER(boolean), POINTER(POINTER(nzttIdentity))]
    OCISecurityVerifyDetached.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7007
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurity_PKEncrypt'):
    OCISecurity_PKEncrypt = _libs['libclntsh.so.10.1'].OCISecurity_PKEncrypt
    OCISecurity_PKEncrypt.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), c_size_t, POINTER(nzttIdentity), nzttces, c_size_t, POINTER(ub1), POINTER(nzttBufferBlock)]
    OCISecurity_PKEncrypt.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7017
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityPKEncryptExpansion'):
    OCISecurityPKEncryptExpansion = _libs['libclntsh.so.10.1'].OCISecurityPKEncryptExpansion
    OCISecurityPKEncryptExpansion.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), c_size_t, c_size_t, POINTER(c_size_t)]
    OCISecurityPKEncryptExpansion.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7024
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityPKDecrypt'):
    OCISecurityPKDecrypt = _libs['libclntsh.so.10.1'].OCISecurityPKDecrypt
    OCISecurityPKDecrypt.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), nzttces, c_size_t, POINTER(ub1), POINTER(nzttBufferBlock)]
    OCISecurityPKDecrypt.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7032
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityEncrypt'):
    OCISecurityEncrypt = _libs['libclntsh.so.10.1'].OCISecurityEncrypt
    OCISecurityEncrypt.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), nzttces, c_size_t, POINTER(ub1), POINTER(nzttBufferBlock)]
    OCISecurityEncrypt.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7040
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityEncryptExpansion'):
    OCISecurityEncryptExpansion = _libs['libclntsh.so.10.1'].OCISecurityEncryptExpansion
    OCISecurityEncryptExpansion.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), c_size_t, POINTER(c_size_t)]
    OCISecurityEncryptExpansion.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7046
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityDecrypt'):
    OCISecurityDecrypt = _libs['libclntsh.so.10.1'].OCISecurityDecrypt
    OCISecurityDecrypt.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), nzttces, c_size_t, POINTER(ub1), POINTER(nzttBufferBlock)]
    OCISecurityDecrypt.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7054
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityEnvelope'):
    OCISecurityEnvelope = _libs['libclntsh.so.10.1'].OCISecurityEnvelope
    OCISecurityEnvelope.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), c_size_t, POINTER(nzttIdentity), nzttces, c_size_t, POINTER(ub1), POINTER(nzttBufferBlock)]
    OCISecurityEnvelope.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7064
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityDeEnvelope'):
    OCISecurityDeEnvelope = _libs['libclntsh.so.10.1'].OCISecurityDeEnvelope
    OCISecurityDeEnvelope.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), nzttces, c_size_t, POINTER(ub1), POINTER(nzttBufferBlock), POINTER(boolean), POINTER(boolean), POINTER(POINTER(nzttIdentity))]
    OCISecurityDeEnvelope.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7075
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityKeyedHash'):
    OCISecurityKeyedHash = _libs['libclntsh.so.10.1'].OCISecurityKeyedHash
    OCISecurityKeyedHash.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), nzttces, c_size_t, POINTER(ub1), POINTER(nzttBufferBlock)]
    OCISecurityKeyedHash.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7083
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityKeyedHashExpansion'):
    OCISecurityKeyedHashExpansion = _libs['libclntsh.so.10.1'].OCISecurityKeyedHashExpansion
    OCISecurityKeyedHashExpansion.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), c_size_t, POINTER(c_size_t)]
    OCISecurityKeyedHashExpansion.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7089
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityHash'):
    OCISecurityHash = _libs['libclntsh.so.10.1'].OCISecurityHash
    OCISecurityHash.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), nzttces, c_size_t, POINTER(ub1), POINTER(nzttBufferBlock)]
    OCISecurityHash.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7097
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityHashExpansion'):
    OCISecurityHashExpansion = _libs['libclntsh.so.10.1'].OCISecurityHashExpansion
    OCISecurityHashExpansion.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), c_size_t, POINTER(c_size_t)]
    OCISecurityHashExpansion.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7103
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecuritySeedRandom'):
    OCISecuritySeedRandom = _libs['libclntsh.so.10.1'].OCISecuritySeedRandom
    OCISecuritySeedRandom.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), c_size_t, POINTER(ub1)]
    OCISecuritySeedRandom.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7109
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityRandomBytes'):
    OCISecurityRandomBytes = _libs['libclntsh.so.10.1'].OCISecurityRandomBytes
    OCISecurityRandomBytes.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), c_size_t, POINTER(nzttBufferBlock)]
    OCISecurityRandomBytes.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7115
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityRandomNumber'):
    OCISecurityRandomNumber = _libs['libclntsh.so.10.1'].OCISecurityRandomNumber
    OCISecurityRandomNumber.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttPersona), POINTER(uword)]
    OCISecurityRandomNumber.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7120
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityInitBlock'):
    OCISecurityInitBlock = _libs['libclntsh.so.10.1'].OCISecurityInitBlock
    OCISecurityInitBlock.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttBufferBlock)]
    OCISecurityInitBlock.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7124
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityReuseBlock'):
    OCISecurityReuseBlock = _libs['libclntsh.so.10.1'].OCISecurityReuseBlock
    OCISecurityReuseBlock.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttBufferBlock)]
    OCISecurityReuseBlock.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7128
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityPurgeBlock'):
    OCISecurityPurgeBlock = _libs['libclntsh.so.10.1'].OCISecurityPurgeBlock
    OCISecurityPurgeBlock.argtypes = [POINTER(OCISecurity), POINTER(OCIError), POINTER(nzttBufferBlock)]
    OCISecurityPurgeBlock.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7132
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecuritySetBlock'):
    OCISecuritySetBlock = _libs['libclntsh.so.10.1'].OCISecuritySetBlock
    OCISecuritySetBlock.argtypes = [POINTER(OCISecurity), POINTER(OCIError), uword, c_size_t, c_size_t, POINTER(ub1), POINTER(nzttBufferBlock)]
    OCISecuritySetBlock.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7140
if hasattr(_libs['libclntsh.so.10.1'], 'OCISecurityGetIdentity'):
    OCISecurityGetIdentity = _libs['libclntsh.so.10.1'].OCISecurityGetIdentity
    OCISecurityGetIdentity.argtypes = [POINTER(OCISecurity), POINTER(OCIError), c_size_t, POINTER(OraText), POINTER(POINTER(nzttIdentity))]
    OCISecurityGetIdentity.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7146
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAQEnq'):
    OCIAQEnq = _libs['libclntsh.so.10.1'].OCIAQEnq
    OCIAQEnq.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OraText), POINTER(OCIAQEnqOptions), POINTER(OCIAQMsgProperties), POINTER(OCIType), POINTER(POINTER(None)), POINTER(POINTER(None)), POINTER(POINTER(OCIRaw)), ub4]
    OCIAQEnq.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7151
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAQDeq'):
    OCIAQDeq = _libs['libclntsh.so.10.1'].OCIAQDeq
    OCIAQDeq.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OraText), POINTER(OCIAQDeqOptions), POINTER(OCIAQMsgProperties), POINTER(OCIType), POINTER(POINTER(None)), POINTER(POINTER(None)), POINTER(POINTER(OCIRaw)), ub4]
    OCIAQDeq.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7156
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAQEnqArray'):
    OCIAQEnqArray = _libs['libclntsh.so.10.1'].OCIAQEnqArray
    OCIAQEnqArray.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OraText), POINTER(OCIAQEnqOptions), POINTER(ub4), POINTER(POINTER(OCIAQMsgProperties)), POINTER(OCIType), POINTER(POINTER(None)), POINTER(POINTER(None)), POINTER(POINTER(OCIRaw)), POINTER(None), OCICallbackAQEnq, ub4]
    OCIAQEnqArray.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7162
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAQDeqArray'):
    OCIAQDeqArray = _libs['libclntsh.so.10.1'].OCIAQDeqArray
    OCIAQDeqArray.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OraText), POINTER(OCIAQDeqOptions), POINTER(ub4), POINTER(POINTER(OCIAQMsgProperties)), POINTER(OCIType), POINTER(POINTER(None)), POINTER(POINTER(None)), POINTER(POINTER(OCIRaw)), POINTER(None), OCICallbackAQDeq, ub4]
    OCIAQDeqArray.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7168
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAQListen'):
    OCIAQListen = _libs['libclntsh.so.10.1'].OCIAQListen
    OCIAQListen.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(POINTER(OCIAQAgent)), ub4, sb4, POINTER(POINTER(OCIAQAgent)), ub4]
    OCIAQListen.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7173
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAQListen2'):
    OCIAQListen2 = _libs['libclntsh.so.10.1'].OCIAQListen2
    OCIAQListen2.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(POINTER(OCIAQAgent)), ub4, POINTER(OCIAQListenOpts), POINTER(POINTER(OCIAQAgent)), POINTER(OCIAQLisMsgProps), ub4]
    OCIAQListen2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7178
if hasattr(_libs['libclntsh.so.10.1'], 'OCIExtractInit'):
    OCIExtractInit = _libs['libclntsh.so.10.1'].OCIExtractInit
    OCIExtractInit.argtypes = [POINTER(None), POINTER(OCIError)]
    OCIExtractInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7180
if hasattr(_libs['libclntsh.so.10.1'], 'OCIExtractTerm'):
    OCIExtractTerm = _libs['libclntsh.so.10.1'].OCIExtractTerm
    OCIExtractTerm.argtypes = [POINTER(None), POINTER(OCIError)]
    OCIExtractTerm.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7182
if hasattr(_libs['libclntsh.so.10.1'], 'OCIExtractReset'):
    OCIExtractReset = _libs['libclntsh.so.10.1'].OCIExtractReset
    OCIExtractReset.argtypes = [POINTER(None), POINTER(OCIError)]
    OCIExtractReset.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7184
if hasattr(_libs['libclntsh.so.10.1'], 'OCIExtractSetNumKeys'):
    OCIExtractSetNumKeys = _libs['libclntsh.so.10.1'].OCIExtractSetNumKeys
    OCIExtractSetNumKeys.argtypes = [POINTER(None), POINTER(OCIError), uword]
    OCIExtractSetNumKeys.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7186
if hasattr(_libs['libclntsh.so.10.1'], 'OCIExtractSetKey'):
    OCIExtractSetKey = _libs['libclntsh.so.10.1'].OCIExtractSetKey
    OCIExtractSetKey.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OraText), ub1, ub4, POINTER(None), POINTER(sb4), POINTER(POINTER(OraText))]
    OCIExtractSetKey.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7190
if hasattr(_libs['libclntsh.so.10.1'], 'OCIExtractFromFile'):
    OCIExtractFromFile = _libs['libclntsh.so.10.1'].OCIExtractFromFile
    OCIExtractFromFile.argtypes = [POINTER(None), POINTER(OCIError), ub4, POINTER(OraText)]
    OCIExtractFromFile.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7193
if hasattr(_libs['libclntsh.so.10.1'], 'OCIExtractFromStr'):
    OCIExtractFromStr = _libs['libclntsh.so.10.1'].OCIExtractFromStr
    OCIExtractFromStr.argtypes = [POINTER(None), POINTER(OCIError), ub4, POINTER(OraText)]
    OCIExtractFromStr.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7195
if hasattr(_libs['libclntsh.so.10.1'], 'OCIExtractToInt'):
    OCIExtractToInt = _libs['libclntsh.so.10.1'].OCIExtractToInt
    OCIExtractToInt.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OraText), uword, POINTER(sb4)]
    OCIExtractToInt.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7198
if hasattr(_libs['libclntsh.so.10.1'], 'OCIExtractToBool'):
    OCIExtractToBool = _libs['libclntsh.so.10.1'].OCIExtractToBool
    OCIExtractToBool.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OraText), uword, POINTER(ub1)]
    OCIExtractToBool.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7201
if hasattr(_libs['libclntsh.so.10.1'], 'OCIExtractToStr'):
    OCIExtractToStr = _libs['libclntsh.so.10.1'].OCIExtractToStr
    OCIExtractToStr.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OraText), uword, POINTER(OraText), uword]
    OCIExtractToStr.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7204
if hasattr(_libs['libclntsh.so.10.1'], 'OCIExtractToOCINum'):
    OCIExtractToOCINum = _libs['libclntsh.so.10.1'].OCIExtractToOCINum
    OCIExtractToOCINum.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OraText), uword, POINTER(OCINumber)]
    OCIExtractToOCINum.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7207
if hasattr(_libs['libclntsh.so.10.1'], 'OCIExtractToList'):
    OCIExtractToList = _libs['libclntsh.so.10.1'].OCIExtractToList
    OCIExtractToList.argtypes = [POINTER(None), POINTER(OCIError), POINTER(uword)]
    OCIExtractToList.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7209
if hasattr(_libs['libclntsh.so.10.1'], 'OCIExtractFromList'):
    OCIExtractFromList = _libs['libclntsh.so.10.1'].OCIExtractFromList
    OCIExtractFromList.argtypes = [POINTER(None), POINTER(OCIError), uword, POINTER(POINTER(OraText)), POINTER(ub1), POINTER(uword), POINTER(POINTER(POINTER(None)))]
    OCIExtractFromList.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7215
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMemoryAlloc'):
    OCIMemoryAlloc = _libs['libclntsh.so.10.1'].OCIMemoryAlloc
    OCIMemoryAlloc.argtypes = [POINTER(None), POINTER(OCIError), POINTER(POINTER(None)), OCIDuration, ub4, ub4]
    OCIMemoryAlloc.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7218
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMemoryResize'):
    OCIMemoryResize = _libs['libclntsh.so.10.1'].OCIMemoryResize
    OCIMemoryResize.argtypes = [POINTER(None), POINTER(OCIError), POINTER(POINTER(None)), ub4, ub4]
    OCIMemoryResize.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7221
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMemoryFree'):
    OCIMemoryFree = _libs['libclntsh.so.10.1'].OCIMemoryFree
    OCIMemoryFree.argtypes = [POINTER(None), POINTER(OCIError), POINTER(None)]
    OCIMemoryFree.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7223
if hasattr(_libs['libclntsh.so.10.1'], 'OCIContextSetValue'):
    OCIContextSetValue = _libs['libclntsh.so.10.1'].OCIContextSetValue
    OCIContextSetValue.argtypes = [POINTER(None), POINTER(OCIError), OCIDuration, POINTER(ub1), ub1, POINTER(None)]
    OCIContextSetValue.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7226
if hasattr(_libs['libclntsh.so.10.1'], 'OCIContextGetValue'):
    OCIContextGetValue = _libs['libclntsh.so.10.1'].OCIContextGetValue
    OCIContextGetValue.argtypes = [POINTER(None), POINTER(OCIError), POINTER(ub1), ub1, POINTER(POINTER(None))]
    OCIContextGetValue.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7229
if hasattr(_libs['libclntsh.so.10.1'], 'OCIContextClearValue'):
    OCIContextClearValue = _libs['libclntsh.so.10.1'].OCIContextClearValue
    OCIContextClearValue.argtypes = [POINTER(None), POINTER(OCIError), POINTER(ub1), ub1]
    OCIContextClearValue.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7232
if hasattr(_libs['libclntsh.so.10.1'], 'OCIContextGenerateKey'):
    OCIContextGenerateKey = _libs['libclntsh.so.10.1'].OCIContextGenerateKey
    OCIContextGenerateKey.argtypes = [POINTER(None), POINTER(OCIError), POINTER(ub4)]
    OCIContextGenerateKey.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7234
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMemorySetCurrentIDs'):
    OCIMemorySetCurrentIDs = _libs['libclntsh.so.10.1'].OCIMemorySetCurrentIDs
    OCIMemorySetCurrentIDs.argtypes = [POINTER(None), POINTER(OCIError), ub4, ub4, ub4]
    OCIMemorySetCurrentIDs.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7238
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerTdsCtxInit'):
    OCIPicklerTdsCtxInit = _libs['libclntsh.so.10.1'].OCIPicklerTdsCtxInit
    OCIPicklerTdsCtxInit.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(POINTER(OCIPicklerTdsCtx))]
    OCIPicklerTdsCtxInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7241
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerTdsCtxFree'):
    OCIPicklerTdsCtxFree = _libs['libclntsh.so.10.1'].OCIPicklerTdsCtxFree
    OCIPicklerTdsCtxFree.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerTdsCtx)]
    OCIPicklerTdsCtxFree.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7243
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerTdsInit'):
    OCIPicklerTdsInit = _libs['libclntsh.so.10.1'].OCIPicklerTdsInit
    OCIPicklerTdsInit.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerTdsCtx), POINTER(POINTER(OCIPicklerTds))]
    OCIPicklerTdsInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7246
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerTdsFree'):
    OCIPicklerTdsFree = _libs['libclntsh.so.10.1'].OCIPicklerTdsFree
    OCIPicklerTdsFree.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerTds)]
    OCIPicklerTdsFree.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7248
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerTdsCreateElementNumber'):
    OCIPicklerTdsCreateElementNumber = _libs['libclntsh.so.10.1'].OCIPicklerTdsCreateElementNumber
    OCIPicklerTdsCreateElementNumber.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerTds), ub1, sb1, POINTER(OCIPicklerTdsElement)]
    OCIPicklerTdsCreateElementNumber.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7252
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerTdsCreateElementChar'):
    OCIPicklerTdsCreateElementChar = _libs['libclntsh.so.10.1'].OCIPicklerTdsCreateElementChar
    OCIPicklerTdsCreateElementChar.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerTds), ub2, POINTER(OCIPicklerTdsElement)]
    OCIPicklerTdsCreateElementChar.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7256
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerTdsCreateElementVarchar'):
    OCIPicklerTdsCreateElementVarchar = _libs['libclntsh.so.10.1'].OCIPicklerTdsCreateElementVarchar
    OCIPicklerTdsCreateElementVarchar.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerTds), ub2, POINTER(OCIPicklerTdsElement)]
    OCIPicklerTdsCreateElementVarchar.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7260
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerTdsCreateElementRaw'):
    OCIPicklerTdsCreateElementRaw = _libs['libclntsh.so.10.1'].OCIPicklerTdsCreateElementRaw
    OCIPicklerTdsCreateElementRaw.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerTds), ub2, POINTER(OCIPicklerTdsElement)]
    OCIPicklerTdsCreateElementRaw.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7264
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerTdsCreateElement'):
    OCIPicklerTdsCreateElement = _libs['libclntsh.so.10.1'].OCIPicklerTdsCreateElement
    OCIPicklerTdsCreateElement.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerTds), OCITypeCode, POINTER(OCIPicklerTdsElement)]
    OCIPicklerTdsCreateElement.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7268
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerTdsAddAttr'):
    OCIPicklerTdsAddAttr = _libs['libclntsh.so.10.1'].OCIPicklerTdsAddAttr
    OCIPicklerTdsAddAttr.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerTds), OCIPicklerTdsElement]
    OCIPicklerTdsAddAttr.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7271
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerTdsGenerate'):
    OCIPicklerTdsGenerate = _libs['libclntsh.so.10.1'].OCIPicklerTdsGenerate
    OCIPicklerTdsGenerate.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerTds)]
    OCIPicklerTdsGenerate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7274
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerTdsGetAttr'):
    OCIPicklerTdsGetAttr = _libs['libclntsh.so.10.1'].OCIPicklerTdsGetAttr
    OCIPicklerTdsGetAttr.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerTds), ub1, POINTER(OCITypeCode), POINTER(ub2)]
    OCIPicklerTdsGetAttr.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7278
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerFdoInit'):
    OCIPicklerFdoInit = _libs['libclntsh.so.10.1'].OCIPicklerFdoInit
    OCIPicklerFdoInit.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(POINTER(OCIPicklerFdo))]
    OCIPicklerFdoInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7281
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerFdoFree'):
    OCIPicklerFdoFree = _libs['libclntsh.so.10.1'].OCIPicklerFdoFree
    OCIPicklerFdoFree.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerFdo)]
    OCIPicklerFdoFree.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7284
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerImageInit'):
    OCIPicklerImageInit = _libs['libclntsh.so.10.1'].OCIPicklerImageInit
    OCIPicklerImageInit.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerFdo), POINTER(OCIPicklerTds), POINTER(POINTER(OCIPicklerImage))]
    OCIPicklerImageInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7289
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerImageFree'):
    OCIPicklerImageFree = _libs['libclntsh.so.10.1'].OCIPicklerImageFree
    OCIPicklerImageFree.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerImage)]
    OCIPicklerImageFree.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7292
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerImageAddScalar'):
    OCIPicklerImageAddScalar = _libs['libclntsh.so.10.1'].OCIPicklerImageAddScalar
    OCIPicklerImageAddScalar.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerImage), POINTER(None), ub4]
    OCIPicklerImageAddScalar.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7296
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerImageAddNullScalar'):
    OCIPicklerImageAddNullScalar = _libs['libclntsh.so.10.1'].OCIPicklerImageAddNullScalar
    OCIPicklerImageAddNullScalar.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerImage)]
    OCIPicklerImageAddNullScalar.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7299
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerImageGenerate'):
    OCIPicklerImageGenerate = _libs['libclntsh.so.10.1'].OCIPicklerImageGenerate
    OCIPicklerImageGenerate.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerImage)]
    OCIPicklerImageGenerate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7302
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerImageGetScalarSize'):
    OCIPicklerImageGetScalarSize = _libs['libclntsh.so.10.1'].OCIPicklerImageGetScalarSize
    OCIPicklerImageGetScalarSize.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerImage), ub4, POINTER(ub4)]
    OCIPicklerImageGetScalarSize.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7306
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerImageGetScalar'):
    OCIPicklerImageGetScalar = _libs['libclntsh.so.10.1'].OCIPicklerImageGetScalar
    OCIPicklerImageGetScalar.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerImage), ub4, POINTER(None), POINTER(ub4), POINTER(OCIInd)]
    OCIPicklerImageGetScalar.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7310
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerImageCollBegin'):
    OCIPicklerImageCollBegin = _libs['libclntsh.so.10.1'].OCIPicklerImageCollBegin
    OCIPicklerImageCollBegin.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerImage), POINTER(OCIPicklerTds)]
    OCIPicklerImageCollBegin.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7313
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerImageCollAddScalar'):
    OCIPicklerImageCollAddScalar = _libs['libclntsh.so.10.1'].OCIPicklerImageCollAddScalar
    OCIPicklerImageCollAddScalar.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerImage), POINTER(None), ub4, OCIInd]
    OCIPicklerImageCollAddScalar.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7317
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerImageCollEnd'):
    OCIPicklerImageCollEnd = _libs['libclntsh.so.10.1'].OCIPicklerImageCollEnd
    OCIPicklerImageCollEnd.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerImage)]
    OCIPicklerImageCollEnd.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7321
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerImageCollBeginScan'):
    OCIPicklerImageCollBeginScan = _libs['libclntsh.so.10.1'].OCIPicklerImageCollBeginScan
    OCIPicklerImageCollBeginScan.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerImage), POINTER(OCIPicklerTds), ub4, ub4, POINTER(OCIInd)]
    OCIPicklerImageCollBeginScan.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7325
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerImageCollGetScalarSize'):
    OCIPicklerImageCollGetScalarSize = _libs['libclntsh.so.10.1'].OCIPicklerImageCollGetScalarSize
    OCIPicklerImageCollGetScalarSize.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerTds), POINTER(ub4)]
    OCIPicklerImageCollGetScalarSize.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7328
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPicklerImageCollGetScalar'):
    OCIPicklerImageCollGetScalar = _libs['libclntsh.so.10.1'].OCIPicklerImageCollGetScalar
    OCIPicklerImageCollGetScalar.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCIPicklerImage), POINTER(None), POINTER(ub4), POINTER(OCIInd)]
    OCIPicklerImageCollGetScalar.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7332
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataGetType'):
    OCIAnyDataGetType = _libs['libclntsh.so.10.1'].OCIAnyDataGetType
    OCIAnyDataGetType.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyData), POINTER(OCITypeCode), POINTER(POINTER(OCIType))]
    OCIAnyDataGetType.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7335
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataIsNull'):
    OCIAnyDataIsNull = _libs['libclntsh.so.10.1'].OCIAnyDataIsNull
    OCIAnyDataIsNull.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyData), POINTER(boolean)]
    OCIAnyDataIsNull.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7338
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataConvert'):
    OCIAnyDataConvert = _libs['libclntsh.so.10.1'].OCIAnyDataConvert
    OCIAnyDataConvert.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), OCITypeCode, POINTER(OCIType), OCIDuration, POINTER(None), POINTER(None), ub4, POINTER(POINTER(OCIAnyData))]
    OCIAnyDataConvert.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7342
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataBeginCreate'):
    OCIAnyDataBeginCreate = _libs['libclntsh.so.10.1'].OCIAnyDataBeginCreate
    OCIAnyDataBeginCreate.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), OCITypeCode, POINTER(OCIType), OCIDuration, POINTER(POINTER(OCIAnyData))]
    OCIAnyDataBeginCreate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7345
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataDestroy'):
    OCIAnyDataDestroy = _libs['libclntsh.so.10.1'].OCIAnyDataDestroy
    OCIAnyDataDestroy.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyData)]
    OCIAnyDataDestroy.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7347
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataAttrSet'):
    OCIAnyDataAttrSet = _libs['libclntsh.so.10.1'].OCIAnyDataAttrSet
    OCIAnyDataAttrSet.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyData), OCITypeCode, POINTER(OCIType), POINTER(None), POINTER(None), ub4, boolean]
    OCIAnyDataAttrSet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7351
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataCollAddElem'):
    OCIAnyDataCollAddElem = _libs['libclntsh.so.10.1'].OCIAnyDataCollAddElem
    OCIAnyDataCollAddElem.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyData), OCITypeCode, POINTER(OCIType), POINTER(None), POINTER(None), ub4, boolean, boolean]
    OCIAnyDataCollAddElem.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7355
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataEndCreate'):
    OCIAnyDataEndCreate = _libs['libclntsh.so.10.1'].OCIAnyDataEndCreate
    OCIAnyDataEndCreate.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyData)]
    OCIAnyDataEndCreate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7358
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataAccess'):
    OCIAnyDataAccess = _libs['libclntsh.so.10.1'].OCIAnyDataAccess
    OCIAnyDataAccess.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyData), OCITypeCode, POINTER(OCIType), POINTER(None), POINTER(None), POINTER(ub4)]
    OCIAnyDataAccess.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7362
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataGetCurrAttrNum'):
    OCIAnyDataGetCurrAttrNum = _libs['libclntsh.so.10.1'].OCIAnyDataGetCurrAttrNum
    OCIAnyDataGetCurrAttrNum.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyData), POINTER(ub4)]
    OCIAnyDataGetCurrAttrNum.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7365
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataAttrGet'):
    OCIAnyDataAttrGet = _libs['libclntsh.so.10.1'].OCIAnyDataAttrGet
    OCIAnyDataAttrGet.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyData), OCITypeCode, POINTER(OCIType), POINTER(None), POINTER(None), POINTER(ub4), boolean]
    OCIAnyDataAttrGet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7369
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataCollGetElem'):
    OCIAnyDataCollGetElem = _libs['libclntsh.so.10.1'].OCIAnyDataCollGetElem
    OCIAnyDataCollGetElem.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyData), OCITypeCode, POINTER(OCIType), POINTER(None), POINTER(None), POINTER(ub4), boolean]
    OCIAnyDataCollGetElem.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7406
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataSetBeginCreate'):
    OCIAnyDataSetBeginCreate = _libs['libclntsh.so.10.1'].OCIAnyDataSetBeginCreate
    OCIAnyDataSetBeginCreate.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), OCITypeCode, POINTER(OCIType), OCIDuration, POINTER(POINTER(OCIAnyDataSet))]
    OCIAnyDataSetBeginCreate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7423
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataSetDestroy'):
    OCIAnyDataSetDestroy = _libs['libclntsh.so.10.1'].OCIAnyDataSetDestroy
    OCIAnyDataSetDestroy.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyDataSet)]
    OCIAnyDataSetDestroy.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7460
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataSetAddInstance'):
    OCIAnyDataSetAddInstance = _libs['libclntsh.so.10.1'].OCIAnyDataSetAddInstance
    OCIAnyDataSetAddInstance.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyDataSet), POINTER(POINTER(OCIAnyData))]
    OCIAnyDataSetAddInstance.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7479
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataSetEndCreate'):
    OCIAnyDataSetEndCreate = _libs['libclntsh.so.10.1'].OCIAnyDataSetEndCreate
    OCIAnyDataSetEndCreate.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyDataSet)]
    OCIAnyDataSetEndCreate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7501
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataSetGetType'):
    OCIAnyDataSetGetType = _libs['libclntsh.so.10.1'].OCIAnyDataSetGetType
    OCIAnyDataSetGetType.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyDataSet), POINTER(OCITypeCode), POINTER(POINTER(OCIType))]
    OCIAnyDataSetGetType.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7517
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataSetGetCount'):
    OCIAnyDataSetGetCount = _libs['libclntsh.so.10.1'].OCIAnyDataSetGetCount
    OCIAnyDataSetGetCount.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyDataSet), POINTER(ub4)]
    OCIAnyDataSetGetCount.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7552
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAnyDataSetGetInstance'):
    OCIAnyDataSetGetInstance = _libs['libclntsh.so.10.1'].OCIAnyDataSetGetInstance
    OCIAnyDataSetGetInstance.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAnyDataSet), POINTER(POINTER(OCIAnyData))]
    OCIAnyDataSetGetInstance.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7557
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatInit'):
    OCIFormatInit = _libs['libclntsh.so.10.1'].OCIFormatInit
    OCIFormatInit.argtypes = [POINTER(None), POINTER(OCIError)]
    OCIFormatInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7559
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatString'):
    _func = _libs['libclntsh.so.10.1'].OCIFormatString
    _restype = sword
    _argtypes = [POINTER(None), POINTER(OCIError), POINTER(OraText), sbig_ora, POINTER(sbig_ora), POINTER(OraText)]
    OCIFormatString = _variadic_function(_func,_restype,_argtypes)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7563
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTerm'):
    OCIFormatTerm = _libs['libclntsh.so.10.1'].OCIFormatTerm
    OCIFormatTerm.argtypes = [POINTER(None), POINTER(OCIError)]
    OCIFormatTerm.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7565
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTUb1'):
    OCIFormatTUb1 = _libs['libclntsh.so.10.1'].OCIFormatTUb1
    OCIFormatTUb1.argtypes = []
    OCIFormatTUb1.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7566
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTUb2'):
    OCIFormatTUb2 = _libs['libclntsh.so.10.1'].OCIFormatTUb2
    OCIFormatTUb2.argtypes = []
    OCIFormatTUb2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7567
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTUb4'):
    OCIFormatTUb4 = _libs['libclntsh.so.10.1'].OCIFormatTUb4
    OCIFormatTUb4.argtypes = []
    OCIFormatTUb4.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7568
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTUword'):
    OCIFormatTUword = _libs['libclntsh.so.10.1'].OCIFormatTUword
    OCIFormatTUword.argtypes = []
    OCIFormatTUword.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7569
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTUbig_ora'):
    OCIFormatTUbig_ora = _libs['libclntsh.so.10.1'].OCIFormatTUbig_ora
    OCIFormatTUbig_ora.argtypes = []
    OCIFormatTUbig_ora.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7570
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTSb1'):
    OCIFormatTSb1 = _libs['libclntsh.so.10.1'].OCIFormatTSb1
    OCIFormatTSb1.argtypes = []
    OCIFormatTSb1.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7571
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTSb2'):
    OCIFormatTSb2 = _libs['libclntsh.so.10.1'].OCIFormatTSb2
    OCIFormatTSb2.argtypes = []
    OCIFormatTSb2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7572
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTSb4'):
    OCIFormatTSb4 = _libs['libclntsh.so.10.1'].OCIFormatTSb4
    OCIFormatTSb4.argtypes = []
    OCIFormatTSb4.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7573
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTSword'):
    OCIFormatTSword = _libs['libclntsh.so.10.1'].OCIFormatTSword
    OCIFormatTSword.argtypes = []
    OCIFormatTSword.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7574
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTSbig_ora'):
    OCIFormatTSbig_ora = _libs['libclntsh.so.10.1'].OCIFormatTSbig_ora
    OCIFormatTSbig_ora.argtypes = []
    OCIFormatTSbig_ora.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7575
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTEb1'):
    OCIFormatTEb1 = _libs['libclntsh.so.10.1'].OCIFormatTEb1
    OCIFormatTEb1.argtypes = []
    OCIFormatTEb1.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7576
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTEb2'):
    OCIFormatTEb2 = _libs['libclntsh.so.10.1'].OCIFormatTEb2
    OCIFormatTEb2.argtypes = []
    OCIFormatTEb2.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7577
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTEb4'):
    OCIFormatTEb4 = _libs['libclntsh.so.10.1'].OCIFormatTEb4
    OCIFormatTEb4.argtypes = []
    OCIFormatTEb4.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7578
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTEword'):
    OCIFormatTEword = _libs['libclntsh.so.10.1'].OCIFormatTEword
    OCIFormatTEword.argtypes = []
    OCIFormatTEword.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7579
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTChar'):
    OCIFormatTChar = _libs['libclntsh.so.10.1'].OCIFormatTChar
    OCIFormatTChar.argtypes = []
    OCIFormatTChar.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7580
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTText'):
    OCIFormatTText = _libs['libclntsh.so.10.1'].OCIFormatTText
    OCIFormatTText.argtypes = []
    OCIFormatTText.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7581
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTDouble'):
    OCIFormatTDouble = _libs['libclntsh.so.10.1'].OCIFormatTDouble
    OCIFormatTDouble.argtypes = []
    OCIFormatTDouble.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7582
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTDvoid'):
    OCIFormatTDvoid = _libs['libclntsh.so.10.1'].OCIFormatTDvoid
    OCIFormatTDvoid.argtypes = []
    OCIFormatTDvoid.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7583
if hasattr(_libs['libclntsh.so.10.1'], 'OCIFormatTEnd'):
    OCIFormatTEnd = _libs['libclntsh.so.10.1'].OCIFormatTEnd
    OCIFormatTEnd.argtypes = []
    OCIFormatTEnd.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7596
if hasattr(_libs['libclntsh.so.10.1'], 'xaosvch'):
    xaosvch = _libs['libclntsh.so.10.1'].xaosvch
    xaosvch.argtypes = [POINTER(OraText)]
    xaosvch.restype = POINTER(OCISvcCtx)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7611
if hasattr(_libs['libclntsh.so.10.1'], 'xaoSvcCtx'):
    xaoSvcCtx = _libs['libclntsh.so.10.1'].xaoSvcCtx
    xaoSvcCtx.argtypes = [POINTER(OraText)]
    xaoSvcCtx.restype = POINTER(OCISvcCtx)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7626
if hasattr(_libs['libclntsh.so.10.1'], 'xaoEnv'):
    xaoEnv = _libs['libclntsh.so.10.1'].xaoEnv
    xaoEnv.argtypes = [POINTER(OraText)]
    xaoEnv.restype = POINTER(OCIEnv)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7635
if hasattr(_libs['libclntsh.so.10.1'], 'xaosterr'):
    xaosterr = _libs['libclntsh.so.10.1'].xaosterr
    xaosterr.argtypes = [POINTER(OCISvcCtx), sb4]
    xaosterr.restype = c_int

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7721
if hasattr(_libs['libclntsh.so.10.1'], 'OCINlsGetInfo'):
    OCINlsGetInfo = _libs['libclntsh.so.10.1'].OCINlsGetInfo
    OCINlsGetInfo.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OraText), c_size_t, ub2]
    OCINlsGetInfo.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7750
if hasattr(_libs['libclntsh.so.10.1'], 'OCINlsNumericInfoGet'):
    OCINlsNumericInfoGet = _libs['libclntsh.so.10.1'].OCINlsNumericInfoGet
    OCINlsNumericInfoGet.argtypes = [POINTER(None), POINTER(OCIError), POINTER(sb4), ub2]
    OCINlsNumericInfoGet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7768
if hasattr(_libs['libclntsh.so.10.1'], 'OCINlsCharSetNameToId'):
    OCINlsCharSetNameToId = _libs['libclntsh.so.10.1'].OCINlsCharSetNameToId
    OCINlsCharSetNameToId.argtypes = [POINTER(None), POINTER(oratext)]
    OCINlsCharSetNameToId.restype = ub2

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7791
if hasattr(_libs['libclntsh.so.10.1'], 'OCINlsCharSetIdToName'):
    OCINlsCharSetIdToName = _libs['libclntsh.so.10.1'].OCINlsCharSetIdToName
    OCINlsCharSetIdToName.argtypes = [POINTER(None), POINTER(oratext), c_size_t, ub2]
    OCINlsCharSetIdToName.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7828
if hasattr(_libs['libclntsh.so.10.1'], 'OCINlsNameMap'):
    OCINlsNameMap = _libs['libclntsh.so.10.1'].OCINlsNameMap
    OCINlsNameMap.argtypes = [POINTER(None), POINTER(oratext), c_size_t, POINTER(oratext), ub4]
    OCINlsNameMap.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7851
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMultiByteToWideChar'):
    OCIMultiByteToWideChar = _libs['libclntsh.so.10.1'].OCIMultiByteToWideChar
    OCIMultiByteToWideChar.argtypes = [POINTER(None), POINTER(OCIWchar), POINTER(OraText), POINTER(c_size_t)]
    OCIMultiByteToWideChar.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7886
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMultiByteInSizeToWideChar'):
    OCIMultiByteInSizeToWideChar = _libs['libclntsh.so.10.1'].OCIMultiByteInSizeToWideChar
    OCIMultiByteInSizeToWideChar.argtypes = [POINTER(None), POINTER(OCIWchar), c_size_t, POINTER(OraText), c_size_t, POINTER(c_size_t)]
    OCIMultiByteInSizeToWideChar.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7911
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharToMultiByte'):
    OCIWideCharToMultiByte = _libs['libclntsh.so.10.1'].OCIWideCharToMultiByte
    OCIWideCharToMultiByte.argtypes = [POINTER(None), POINTER(OraText), POINTER(OCIWchar), POINTER(c_size_t)]
    OCIWideCharToMultiByte.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7946
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharInSizeToMultiByte'):
    OCIWideCharInSizeToMultiByte = _libs['libclntsh.so.10.1'].OCIWideCharInSizeToMultiByte
    OCIWideCharInSizeToMultiByte.argtypes = [POINTER(None), POINTER(OraText), c_size_t, POINTER(OCIWchar), c_size_t, POINTER(c_size_t)]
    OCIWideCharInSizeToMultiByte.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7965
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharIsAlnum'):
    OCIWideCharIsAlnum = _libs['libclntsh.so.10.1'].OCIWideCharIsAlnum
    OCIWideCharIsAlnum.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharIsAlnum.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7981
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharIsAlpha'):
    OCIWideCharIsAlpha = _libs['libclntsh.so.10.1'].OCIWideCharIsAlpha
    OCIWideCharIsAlpha.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharIsAlpha.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 7997
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharIsCntrl'):
    OCIWideCharIsCntrl = _libs['libclntsh.so.10.1'].OCIWideCharIsCntrl
    OCIWideCharIsCntrl.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharIsCntrl.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8013
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharIsDigit'):
    OCIWideCharIsDigit = _libs['libclntsh.so.10.1'].OCIWideCharIsDigit
    OCIWideCharIsDigit.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharIsDigit.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8031
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharIsGraph'):
    OCIWideCharIsGraph = _libs['libclntsh.so.10.1'].OCIWideCharIsGraph
    OCIWideCharIsGraph.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharIsGraph.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8047
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharIsLower'):
    OCIWideCharIsLower = _libs['libclntsh.so.10.1'].OCIWideCharIsLower
    OCIWideCharIsLower.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharIsLower.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8063
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharIsPrint'):
    OCIWideCharIsPrint = _libs['libclntsh.so.10.1'].OCIWideCharIsPrint
    OCIWideCharIsPrint.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharIsPrint.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8079
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharIsPunct'):
    OCIWideCharIsPunct = _libs['libclntsh.so.10.1'].OCIWideCharIsPunct
    OCIWideCharIsPunct.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharIsPunct.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8097
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharIsSpace'):
    OCIWideCharIsSpace = _libs['libclntsh.so.10.1'].OCIWideCharIsSpace
    OCIWideCharIsSpace.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharIsSpace.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8113
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharIsUpper'):
    OCIWideCharIsUpper = _libs['libclntsh.so.10.1'].OCIWideCharIsUpper
    OCIWideCharIsUpper.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharIsUpper.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8129
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharIsXdigit'):
    OCIWideCharIsXdigit = _libs['libclntsh.so.10.1'].OCIWideCharIsXdigit
    OCIWideCharIsXdigit.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharIsXdigit.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8146
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharIsSingleByte'):
    OCIWideCharIsSingleByte = _libs['libclntsh.so.10.1'].OCIWideCharIsSingleByte
    OCIWideCharIsSingleByte.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharIsSingleByte.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8163
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharToLower'):
    OCIWideCharToLower = _libs['libclntsh.so.10.1'].OCIWideCharToLower
    OCIWideCharToLower.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharToLower.restype = OCIWchar

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8180
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharToUpper'):
    OCIWideCharToUpper = _libs['libclntsh.so.10.1'].OCIWideCharToUpper
    OCIWideCharToUpper.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharToUpper.restype = OCIWchar

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8208
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharStrcmp'):
    OCIWideCharStrcmp = _libs['libclntsh.so.10.1'].OCIWideCharStrcmp
    OCIWideCharStrcmp.argtypes = [POINTER(None), POINTER(OCIWchar), POINTER(OCIWchar), c_int]
    OCIWideCharStrcmp.restype = c_int

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8242
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharStrncmp'):
    OCIWideCharStrncmp = _libs['libclntsh.so.10.1'].OCIWideCharStrncmp
    OCIWideCharStrncmp.argtypes = [POINTER(None), POINTER(OCIWchar), c_size_t, POINTER(OCIWchar), c_size_t, c_int]
    OCIWideCharStrncmp.restype = c_int

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8265
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharStrcat'):
    OCIWideCharStrcat = _libs['libclntsh.so.10.1'].OCIWideCharStrcat
    OCIWideCharStrcat.argtypes = [POINTER(None), POINTER(OCIWchar), POINTER(OCIWchar)]
    OCIWideCharStrcat.restype = c_size_t

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8286
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharStrchr'):
    OCIWideCharStrchr = _libs['libclntsh.so.10.1'].OCIWideCharStrchr
    OCIWideCharStrchr.argtypes = [POINTER(None), POINTER(OCIWchar), OCIWchar]
    OCIWideCharStrchr.restype = POINTER(OCIWchar)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8307
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharStrcpy'):
    OCIWideCharStrcpy = _libs['libclntsh.so.10.1'].OCIWideCharStrcpy
    OCIWideCharStrcpy.argtypes = [POINTER(None), POINTER(OCIWchar), POINTER(OCIWchar)]
    OCIWideCharStrcpy.restype = c_size_t

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8326
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharStrlen'):
    OCIWideCharStrlen = _libs['libclntsh.so.10.1'].OCIWideCharStrlen
    OCIWideCharStrlen.argtypes = [POINTER(None), POINTER(OCIWchar)]
    OCIWideCharStrlen.restype = c_size_t

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8350
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharStrncat'):
    OCIWideCharStrncat = _libs['libclntsh.so.10.1'].OCIWideCharStrncat
    OCIWideCharStrncat.argtypes = [POINTER(None), POINTER(OCIWchar), POINTER(OCIWchar), c_size_t]
    OCIWideCharStrncat.restype = c_size_t

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8374
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharStrncpy'):
    OCIWideCharStrncpy = _libs['libclntsh.so.10.1'].OCIWideCharStrncpy
    OCIWideCharStrncpy.argtypes = [POINTER(None), POINTER(OCIWchar), POINTER(OCIWchar), c_size_t]
    OCIWideCharStrncpy.restype = c_size_t

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8395
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharStrrchr'):
    OCIWideCharStrrchr = _libs['libclntsh.so.10.1'].OCIWideCharStrrchr
    OCIWideCharStrrchr.argtypes = [POINTER(None), POINTER(OCIWchar), OCIWchar]
    OCIWideCharStrrchr.restype = POINTER(OCIWchar)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8423
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharStrCaseConversion'):
    OCIWideCharStrCaseConversion = _libs['libclntsh.so.10.1'].OCIWideCharStrCaseConversion
    OCIWideCharStrCaseConversion.argtypes = [POINTER(None), POINTER(OCIWchar), POINTER(OCIWchar), ub4]
    OCIWideCharStrCaseConversion.restype = c_size_t

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8442
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharDisplayLength'):
    OCIWideCharDisplayLength = _libs['libclntsh.so.10.1'].OCIWideCharDisplayLength
    OCIWideCharDisplayLength.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharDisplayLength.restype = c_size_t

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8459
if hasattr(_libs['libclntsh.so.10.1'], 'OCIWideCharMultiByteLength'):
    OCIWideCharMultiByteLength = _libs['libclntsh.so.10.1'].OCIWideCharMultiByteLength
    OCIWideCharMultiByteLength.argtypes = [POINTER(None), OCIWchar]
    OCIWideCharMultiByteLength.restype = c_size_t

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8487
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMultiByteStrcmp'):
    OCIMultiByteStrcmp = _libs['libclntsh.so.10.1'].OCIMultiByteStrcmp
    OCIMultiByteStrcmp.argtypes = [POINTER(None), POINTER(OraText), POINTER(OraText), c_int]
    OCIMultiByteStrcmp.restype = c_int

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8521
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMultiByteStrncmp'):
    OCIMultiByteStrncmp = _libs['libclntsh.so.10.1'].OCIMultiByteStrncmp
    OCIMultiByteStrncmp.argtypes = [POINTER(None), POINTER(OraText), c_size_t, POINTER(OraText), c_size_t, c_int]
    OCIMultiByteStrncmp.restype = c_int

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8544
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMultiByteStrcat'):
    OCIMultiByteStrcat = _libs['libclntsh.so.10.1'].OCIMultiByteStrcat
    OCIMultiByteStrcat.argtypes = [POINTER(None), POINTER(OraText), POINTER(OraText)]
    OCIMultiByteStrcat.restype = c_size_t

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8566
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMultiByteStrcpy'):
    OCIMultiByteStrcpy = _libs['libclntsh.so.10.1'].OCIMultiByteStrcpy
    OCIMultiByteStrcpy.argtypes = [POINTER(None), POINTER(OraText), POINTER(OraText)]
    OCIMultiByteStrcpy.restype = c_size_t

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8583
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMultiByteStrlen'):
    OCIMultiByteStrlen = _libs['libclntsh.so.10.1'].OCIMultiByteStrlen
    OCIMultiByteStrlen.argtypes = [POINTER(None), POINTER(OraText)]
    OCIMultiByteStrlen.restype = c_size_t

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8607
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMultiByteStrncat'):
    OCIMultiByteStrncat = _libs['libclntsh.so.10.1'].OCIMultiByteStrncat
    OCIMultiByteStrncat.argtypes = [POINTER(None), POINTER(OraText), POINTER(OraText), c_size_t]
    OCIMultiByteStrncat.restype = c_size_t

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8632
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMultiByteStrncpy'):
    OCIMultiByteStrncpy = _libs['libclntsh.so.10.1'].OCIMultiByteStrncpy
    OCIMultiByteStrncpy.argtypes = [POINTER(None), POINTER(OraText), POINTER(OraText), c_size_t]
    OCIMultiByteStrncpy.restype = c_size_t

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8653
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMultiByteStrnDisplayLength'):
    OCIMultiByteStrnDisplayLength = _libs['libclntsh.so.10.1'].OCIMultiByteStrnDisplayLength
    OCIMultiByteStrnDisplayLength.argtypes = [POINTER(None), POINTER(OraText), c_size_t]
    OCIMultiByteStrnDisplayLength.restype = c_size_t

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8680
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMultiByteStrCaseConversion'):
    OCIMultiByteStrCaseConversion = _libs['libclntsh.so.10.1'].OCIMultiByteStrCaseConversion
    OCIMultiByteStrCaseConversion.argtypes = [POINTER(None), POINTER(OraText), POINTER(OraText), ub4]
    OCIMultiByteStrCaseConversion.restype = c_size_t

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8711
if hasattr(_libs['libclntsh.so.10.1'], 'OCICharSetToUnicode'):
    OCICharSetToUnicode = _libs['libclntsh.so.10.1'].OCICharSetToUnicode
    OCICharSetToUnicode.argtypes = [POINTER(None), POINTER(ub2), c_size_t, POINTER(OraText), c_size_t, POINTER(c_size_t)]
    OCICharSetToUnicode.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8745
if hasattr(_libs['libclntsh.so.10.1'], 'OCIUnicodeToCharSet'):
    OCIUnicodeToCharSet = _libs['libclntsh.so.10.1'].OCIUnicodeToCharSet
    OCIUnicodeToCharSet.argtypes = [POINTER(None), POINTER(OraText), c_size_t, POINTER(ub2), c_size_t, POINTER(c_size_t)]
    OCIUnicodeToCharSet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8791
if hasattr(_libs['libclntsh.so.10.1'], 'OCINlsCharSetConvert'):
    OCINlsCharSetConvert = _libs['libclntsh.so.10.1'].OCINlsCharSetConvert
    OCINlsCharSetConvert.argtypes = [POINTER(None), POINTER(OCIError), ub2, POINTER(None), c_size_t, ub2, POINTER(None), c_size_t, POINTER(c_size_t)]
    OCINlsCharSetConvert.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8813
if hasattr(_libs['libclntsh.so.10.1'], 'OCICharSetConversionIsReplacementUsed'):
    OCICharSetConversionIsReplacementUsed = _libs['libclntsh.so.10.1'].OCICharSetConversionIsReplacementUsed
    OCICharSetConversionIsReplacementUsed.argtypes = [POINTER(None)]
    OCICharSetConversionIsReplacementUsed.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8851
if hasattr(_libs['libclntsh.so.10.1'], 'OCINlsEnvironmentVariableGet'):
    OCINlsEnvironmentVariableGet = _libs['libclntsh.so.10.1'].OCINlsEnvironmentVariableGet
    OCINlsEnvironmentVariableGet.argtypes = [POINTER(None), c_size_t, ub2, ub2, POINTER(c_size_t)]
    OCINlsEnvironmentVariableGet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8898
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMessageOpen'):
    OCIMessageOpen = _libs['libclntsh.so.10.1'].OCIMessageOpen
    OCIMessageOpen.argtypes = [POINTER(None), POINTER(OCIError), POINTER(POINTER(OCIMsg)), POINTER(OraText), POINTER(OraText), OCIDuration]
    OCIMessageOpen.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8928
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMessageGet'):
    OCIMessageGet = _libs['libclntsh.so.10.1'].OCIMessageGet
    OCIMessageGet.argtypes = [POINTER(OCIMsg), ub4, POINTER(OraText), c_size_t]
    OCIMessageGet.restype = POINTER(OraText)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 8950
if hasattr(_libs['libclntsh.so.10.1'], 'OCIMessageClose'):
    OCIMessageClose = _libs['libclntsh.so.10.1'].OCIMessageClose
    OCIMessageClose.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIMsg)]
    OCIMessageClose.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10077
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadProcessInit'):
    OCIThreadProcessInit = _libs['libclntsh.so.10.1'].OCIThreadProcessInit
    OCIThreadProcessInit.argtypes = []
    OCIThreadProcessInit.restype = None

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10079
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadInit'):
    OCIThreadInit = _libs['libclntsh.so.10.1'].OCIThreadInit
    OCIThreadInit.argtypes = [POINTER(None), POINTER(OCIError)]
    OCIThreadInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10081
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadTerm'):
    OCIThreadTerm = _libs['libclntsh.so.10.1'].OCIThreadTerm
    OCIThreadTerm.argtypes = [POINTER(None), POINTER(OCIError)]
    OCIThreadTerm.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10083
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadIsMulti'):
    OCIThreadIsMulti = _libs['libclntsh.so.10.1'].OCIThreadIsMulti
    OCIThreadIsMulti.argtypes = []
    OCIThreadIsMulti.restype = boolean

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10085
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadMutexInit'):
    OCIThreadMutexInit = _libs['libclntsh.so.10.1'].OCIThreadMutexInit
    OCIThreadMutexInit.argtypes = [POINTER(None), POINTER(OCIError), POINTER(POINTER(OCIThreadMutex))]
    OCIThreadMutexInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10088
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadMutexDestroy'):
    OCIThreadMutexDestroy = _libs['libclntsh.so.10.1'].OCIThreadMutexDestroy
    OCIThreadMutexDestroy.argtypes = [POINTER(None), POINTER(OCIError), POINTER(POINTER(OCIThreadMutex))]
    OCIThreadMutexDestroy.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10091
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadMutexAcquire'):
    OCIThreadMutexAcquire = _libs['libclntsh.so.10.1'].OCIThreadMutexAcquire
    OCIThreadMutexAcquire.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIThreadMutex)]
    OCIThreadMutexAcquire.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10094
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadMutexRelease'):
    OCIThreadMutexRelease = _libs['libclntsh.so.10.1'].OCIThreadMutexRelease
    OCIThreadMutexRelease.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIThreadMutex)]
    OCIThreadMutexRelease.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10097
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadKeyInit'):
    OCIThreadKeyInit = _libs['libclntsh.so.10.1'].OCIThreadKeyInit
    OCIThreadKeyInit.argtypes = [POINTER(None), POINTER(OCIError), POINTER(POINTER(OCIThreadKey)), OCIThreadKeyDestFunc]
    OCIThreadKeyInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10100
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadKeyDestroy'):
    OCIThreadKeyDestroy = _libs['libclntsh.so.10.1'].OCIThreadKeyDestroy
    OCIThreadKeyDestroy.argtypes = [POINTER(None), POINTER(OCIError), POINTER(POINTER(OCIThreadKey))]
    OCIThreadKeyDestroy.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10103
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadKeyGet'):
    OCIThreadKeyGet = _libs['libclntsh.so.10.1'].OCIThreadKeyGet
    OCIThreadKeyGet.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIThreadKey), POINTER(POINTER(None))]
    OCIThreadKeyGet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10106
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadKeySet'):
    OCIThreadKeySet = _libs['libclntsh.so.10.1'].OCIThreadKeySet
    OCIThreadKeySet.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIThreadKey), POINTER(None)]
    OCIThreadKeySet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10109
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadIdInit'):
    OCIThreadIdInit = _libs['libclntsh.so.10.1'].OCIThreadIdInit
    OCIThreadIdInit.argtypes = [POINTER(None), POINTER(OCIError), POINTER(POINTER(OCIThreadId))]
    OCIThreadIdInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10111
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadIdDestroy'):
    OCIThreadIdDestroy = _libs['libclntsh.so.10.1'].OCIThreadIdDestroy
    OCIThreadIdDestroy.argtypes = [POINTER(None), POINTER(OCIError), POINTER(POINTER(OCIThreadId))]
    OCIThreadIdDestroy.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10113
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadIdSet'):
    OCIThreadIdSet = _libs['libclntsh.so.10.1'].OCIThreadIdSet
    OCIThreadIdSet.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIThreadId), POINTER(OCIThreadId)]
    OCIThreadIdSet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10116
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadIdSetNull'):
    OCIThreadIdSetNull = _libs['libclntsh.so.10.1'].OCIThreadIdSetNull
    OCIThreadIdSetNull.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIThreadId)]
    OCIThreadIdSetNull.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10118
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadIdGet'):
    OCIThreadIdGet = _libs['libclntsh.so.10.1'].OCIThreadIdGet
    OCIThreadIdGet.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIThreadId)]
    OCIThreadIdGet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10120
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadIdSame'):
    OCIThreadIdSame = _libs['libclntsh.so.10.1'].OCIThreadIdSame
    OCIThreadIdSame.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIThreadId), POINTER(OCIThreadId), POINTER(boolean)]
    OCIThreadIdSame.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10124
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadIdNull'):
    OCIThreadIdNull = _libs['libclntsh.so.10.1'].OCIThreadIdNull
    OCIThreadIdNull.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIThreadId), POINTER(boolean)]
    OCIThreadIdNull.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10127
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadHndInit'):
    OCIThreadHndInit = _libs['libclntsh.so.10.1'].OCIThreadHndInit
    OCIThreadHndInit.argtypes = [POINTER(None), POINTER(OCIError), POINTER(POINTER(OCIThreadHandle))]
    OCIThreadHndInit.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10129
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadHndDestroy'):
    OCIThreadHndDestroy = _libs['libclntsh.so.10.1'].OCIThreadHndDestroy
    OCIThreadHndDestroy.argtypes = [POINTER(None), POINTER(OCIError), POINTER(POINTER(OCIThreadHandle))]
    OCIThreadHndDestroy.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10131
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadCreate'):
    OCIThreadCreate = _libs['libclntsh.so.10.1'].OCIThreadCreate
    OCIThreadCreate.argtypes = [POINTER(None), POINTER(OCIError), CFUNCTYPE(UNCHECKED(None), POINTER(None)), POINTER(None), POINTER(OCIThreadId), POINTER(OCIThreadHandle)]
    OCIThreadCreate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10135
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadJoin'):
    OCIThreadJoin = _libs['libclntsh.so.10.1'].OCIThreadJoin
    OCIThreadJoin.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIThreadHandle)]
    OCIThreadJoin.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10137
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadClose'):
    OCIThreadClose = _libs['libclntsh.so.10.1'].OCIThreadClose
    OCIThreadClose.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIThreadHandle)]
    OCIThreadClose.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10139
if hasattr(_libs['libclntsh.so.10.1'], 'OCIThreadHandleGet'):
    OCIThreadHandleGet = _libs['libclntsh.so.10.1'].OCIThreadHandleGet
    OCIThreadHandleGet.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIThreadHandle)]
    OCIThreadHandleGet.restype = sword

OCIBindRowCallback = CFUNCTYPE(UNCHECKED(sword), POINTER(None)) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10144

OCIFetchRowCallback = CFUNCTYPE(UNCHECKED(sword), POINTER(None)) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10145

OCISubscriptionNotify = CFUNCTYPE(UNCHECKED(ub4), POINTER(None), POINTER(OCISubscription), POINTER(None), ub4, POINTER(None), ub4) # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10151

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10155
if hasattr(_libs['libclntsh.so.10.1'], 'OCISubscriptionRegister'):
    OCISubscriptionRegister = _libs['libclntsh.so.10.1'].OCISubscriptionRegister
    OCISubscriptionRegister.argtypes = [POINTER(OCISvcCtx), POINTER(POINTER(OCISubscription)), ub2, POINTER(OCIError), ub4]
    OCISubscriptionRegister.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10159
if hasattr(_libs['libclntsh.so.10.1'], 'OCISubscriptionPost'):
    OCISubscriptionPost = _libs['libclntsh.so.10.1'].OCISubscriptionPost
    OCISubscriptionPost.argtypes = [POINTER(OCISvcCtx), POINTER(POINTER(OCISubscription)), ub2, POINTER(OCIError), ub4]
    OCISubscriptionPost.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10162
if hasattr(_libs['libclntsh.so.10.1'], 'OCISubscriptionUnRegister'):
    OCISubscriptionUnRegister = _libs['libclntsh.so.10.1'].OCISubscriptionUnRegister
    OCISubscriptionUnRegister.argtypes = [POINTER(OCISvcCtx), POINTER(OCISubscription), POINTER(OCIError), ub4]
    OCISubscriptionUnRegister.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10165
if hasattr(_libs['libclntsh.so.10.1'], 'OCISubscriptionDisable'):
    OCISubscriptionDisable = _libs['libclntsh.so.10.1'].OCISubscriptionDisable
    OCISubscriptionDisable.argtypes = [POINTER(OCISubscription), POINTER(OCIError), ub4]
    OCISubscriptionDisable.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10168
if hasattr(_libs['libclntsh.so.10.1'], 'OCISubscriptionEnable'):
    OCISubscriptionEnable = _libs['libclntsh.so.10.1'].OCISubscriptionEnable
    OCISubscriptionEnable.argtypes = [POINTER(OCISubscription), POINTER(OCIError), ub4]
    OCISubscriptionEnable.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10175
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeGetTime'):
    OCIDateTimeGetTime = _libs['libclntsh.so.10.1'].OCIDateTimeGetTime
    OCIDateTimeGetTime.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIDateTime), POINTER(ub1), POINTER(ub1), POINTER(ub1), POINTER(ub4)]
    OCIDateTimeGetTime.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10178
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeGetDate'):
    OCIDateTimeGetDate = _libs['libclntsh.so.10.1'].OCIDateTimeGetDate
    OCIDateTimeGetDate.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIDateTime), POINTER(sb2), POINTER(ub1), POINTER(ub1)]
    OCIDateTimeGetDate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10181
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeGetTimeZoneOffset'):
    OCIDateTimeGetTimeZoneOffset = _libs['libclntsh.so.10.1'].OCIDateTimeGetTimeZoneOffset
    OCIDateTimeGetTimeZoneOffset.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIDateTime), POINTER(sb1), POINTER(sb1)]
    OCIDateTimeGetTimeZoneOffset.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10185
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeConstruct'):
    OCIDateTimeConstruct = _libs['libclntsh.so.10.1'].OCIDateTimeConstruct
    OCIDateTimeConstruct.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIDateTime), sb2, ub1, ub1, ub1, ub1, ub1, ub4, POINTER(OraText), c_size_t]
    OCIDateTimeConstruct.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10189
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeSysTimeStamp'):
    OCIDateTimeSysTimeStamp = _libs['libclntsh.so.10.1'].OCIDateTimeSysTimeStamp
    OCIDateTimeSysTimeStamp.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIDateTime)]
    OCIDateTimeSysTimeStamp.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10192
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeAssign'):
    OCIDateTimeAssign = _libs['libclntsh.so.10.1'].OCIDateTimeAssign
    OCIDateTimeAssign.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIDateTime), POINTER(OCIDateTime)]
    OCIDateTimeAssign.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10195
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeToText'):
    OCIDateTimeToText = _libs['libclntsh.so.10.1'].OCIDateTimeToText
    OCIDateTimeToText.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIDateTime), POINTER(OraText), ub1, ub1, POINTER(OraText), c_size_t, POINTER(ub4), POINTER(OraText)]
    OCIDateTimeToText.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10200
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeFromText'):
    OCIDateTimeFromText = _libs['libclntsh.so.10.1'].OCIDateTimeFromText
    OCIDateTimeFromText.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OraText), c_size_t, POINTER(OraText), ub1, POINTER(OraText), c_size_t, POINTER(OCIDateTime)]
    OCIDateTimeFromText.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10204
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeCompare'):
    OCIDateTimeCompare = _libs['libclntsh.so.10.1'].OCIDateTimeCompare
    OCIDateTimeCompare.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIDateTime), POINTER(OCIDateTime), POINTER(sword)]
    OCIDateTimeCompare.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10207
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeCheck'):
    OCIDateTimeCheck = _libs['libclntsh.so.10.1'].OCIDateTimeCheck
    OCIDateTimeCheck.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIDateTime), POINTER(ub4)]
    OCIDateTimeCheck.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10210
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeConvert'):
    OCIDateTimeConvert = _libs['libclntsh.so.10.1'].OCIDateTimeConvert
    OCIDateTimeConvert.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIDateTime), POINTER(OCIDateTime)]
    OCIDateTimeConvert.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10213
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeSubtract'):
    OCIDateTimeSubtract = _libs['libclntsh.so.10.1'].OCIDateTimeSubtract
    OCIDateTimeSubtract.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIDateTime), POINTER(OCIDateTime), POINTER(OCIInterval)]
    OCIDateTimeSubtract.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10216
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeIntervalAdd'):
    OCIDateTimeIntervalAdd = _libs['libclntsh.so.10.1'].OCIDateTimeIntervalAdd
    OCIDateTimeIntervalAdd.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIDateTime), POINTER(OCIInterval), POINTER(OCIDateTime)]
    OCIDateTimeIntervalAdd.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10219
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeIntervalSub'):
    OCIDateTimeIntervalSub = _libs['libclntsh.so.10.1'].OCIDateTimeIntervalSub
    OCIDateTimeIntervalSub.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIDateTime), POINTER(OCIInterval), POINTER(OCIDateTime)]
    OCIDateTimeIntervalSub.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10222
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalSubtract'):
    OCIIntervalSubtract = _libs['libclntsh.so.10.1'].OCIIntervalSubtract
    OCIIntervalSubtract.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIInterval), POINTER(OCIInterval), POINTER(OCIInterval)]
    OCIIntervalSubtract.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10225
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalAdd'):
    OCIIntervalAdd = _libs['libclntsh.so.10.1'].OCIIntervalAdd
    OCIIntervalAdd.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIInterval), POINTER(OCIInterval), POINTER(OCIInterval)]
    OCIIntervalAdd.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10228
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalMultiply'):
    OCIIntervalMultiply = _libs['libclntsh.so.10.1'].OCIIntervalMultiply
    OCIIntervalMultiply.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIInterval), POINTER(OCINumber), POINTER(OCIInterval)]
    OCIIntervalMultiply.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10231
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalDivide'):
    OCIIntervalDivide = _libs['libclntsh.so.10.1'].OCIIntervalDivide
    OCIIntervalDivide.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIInterval), POINTER(OCINumber), POINTER(OCIInterval)]
    OCIIntervalDivide.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10234
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalCompare'):
    OCIIntervalCompare = _libs['libclntsh.so.10.1'].OCIIntervalCompare
    OCIIntervalCompare.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIInterval), POINTER(OCIInterval), POINTER(sword)]
    OCIIntervalCompare.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10237
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalFromNumber'):
    OCIIntervalFromNumber = _libs['libclntsh.so.10.1'].OCIIntervalFromNumber
    OCIIntervalFromNumber.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIInterval), POINTER(OCINumber)]
    OCIIntervalFromNumber.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10240
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalFromText'):
    OCIIntervalFromText = _libs['libclntsh.so.10.1'].OCIIntervalFromText
    OCIIntervalFromText.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OraText), c_size_t, POINTER(OCIInterval)]
    OCIIntervalFromText.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10243
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalToText'):
    OCIIntervalToText = _libs['libclntsh.so.10.1'].OCIIntervalToText
    OCIIntervalToText.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIInterval), ub1, ub1, POINTER(OraText), c_size_t, POINTER(c_size_t)]
    OCIIntervalToText.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10247
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalToNumber'):
    OCIIntervalToNumber = _libs['libclntsh.so.10.1'].OCIIntervalToNumber
    OCIIntervalToNumber.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIInterval), POINTER(OCINumber)]
    OCIIntervalToNumber.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10250
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalCheck'):
    OCIIntervalCheck = _libs['libclntsh.so.10.1'].OCIIntervalCheck
    OCIIntervalCheck.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIInterval), POINTER(ub4)]
    OCIIntervalCheck.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10253
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalAssign'):
    OCIIntervalAssign = _libs['libclntsh.so.10.1'].OCIIntervalAssign
    OCIIntervalAssign.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIInterval), POINTER(OCIInterval)]
    OCIIntervalAssign.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10256
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalSetYearMonth'):
    OCIIntervalSetYearMonth = _libs['libclntsh.so.10.1'].OCIIntervalSetYearMonth
    OCIIntervalSetYearMonth.argtypes = [POINTER(None), POINTER(OCIError), sb4, sb4, POINTER(OCIInterval)]
    OCIIntervalSetYearMonth.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10259
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalGetYearMonth'):
    OCIIntervalGetYearMonth = _libs['libclntsh.so.10.1'].OCIIntervalGetYearMonth
    OCIIntervalGetYearMonth.argtypes = [POINTER(None), POINTER(OCIError), POINTER(sb4), POINTER(sb4), POINTER(OCIInterval)]
    OCIIntervalGetYearMonth.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10262
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalSetDaySecond'):
    OCIIntervalSetDaySecond = _libs['libclntsh.so.10.1'].OCIIntervalSetDaySecond
    OCIIntervalSetDaySecond.argtypes = [POINTER(None), POINTER(OCIError), sb4, sb4, sb4, sb4, sb4, POINTER(OCIInterval)]
    OCIIntervalSetDaySecond.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10265
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalGetDaySecond'):
    OCIIntervalGetDaySecond = _libs['libclntsh.so.10.1'].OCIIntervalGetDaySecond
    OCIIntervalGetDaySecond.argtypes = [POINTER(None), POINTER(OCIError), POINTER(sb4), POINTER(sb4), POINTER(sb4), POINTER(sb4), POINTER(sb4), POINTER(OCIInterval)]
    OCIIntervalGetDaySecond.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10268
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeToArray'):
    OCIDateTimeToArray = _libs['libclntsh.so.10.1'].OCIDateTimeToArray
    OCIDateTimeToArray.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIDateTime), POINTER(OCIInterval), POINTER(ub1), POINTER(ub4), ub1]
    OCIDateTimeToArray.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10272
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeFromArray'):
    OCIDateTimeFromArray = _libs['libclntsh.so.10.1'].OCIDateTimeFromArray
    OCIDateTimeFromArray.argtypes = [POINTER(None), POINTER(OCIError), POINTER(ub1), ub4, ub1, POINTER(OCIDateTime), POINTER(OCIInterval), ub1]
    OCIDateTimeFromArray.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10276
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDateTimeGetTimeZoneName'):
    OCIDateTimeGetTimeZoneName = _libs['libclntsh.so.10.1'].OCIDateTimeGetTimeZoneName
    OCIDateTimeGetTimeZoneName.argtypes = [POINTER(None), POINTER(OCIError), POINTER(OCIDateTime), POINTER(ub1), POINTER(ub4)]
    OCIDateTimeGetTimeZoneName.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10280
if hasattr(_libs['libclntsh.so.10.1'], 'OCIIntervalFromTZ'):
    OCIIntervalFromTZ = _libs['libclntsh.so.10.1'].OCIIntervalFromTZ
    OCIIntervalFromTZ.argtypes = [POINTER(None), POINTER(OCIError), POINTER(oratext), c_size_t, POINTER(OCIInterval)]
    OCIIntervalFromTZ.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10286
if hasattr(_libs['libclntsh.so.10.1'], 'OCIConnectionPoolCreate'):
    OCIConnectionPoolCreate = _libs['libclntsh.so.10.1'].OCIConnectionPoolCreate
    OCIConnectionPoolCreate.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCICPool), POINTER(POINTER(OraText)), POINTER(sb4), POINTER(OraText), sb4, ub4, ub4, ub4, POINTER(OraText), sb4, POINTER(OraText), sb4, ub4]
    OCIConnectionPoolCreate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10294
if hasattr(_libs['libclntsh.so.10.1'], 'OCIConnectionPoolDestroy'):
    OCIConnectionPoolDestroy = _libs['libclntsh.so.10.1'].OCIConnectionPoolDestroy
    OCIConnectionPoolDestroy.argtypes = [POINTER(OCICPool), POINTER(OCIError), ub4]
    OCIConnectionPoolDestroy.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10301
if hasattr(_libs['libclntsh.so.10.1'], 'OCISessionPoolCreate'):
    OCISessionPoolCreate = _libs['libclntsh.so.10.1'].OCISessionPoolCreate
    OCISessionPoolCreate.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(OCISPool), POINTER(POINTER(OraText)), POINTER(ub4), POINTER(OraText), ub4, ub4, ub4, ub4, POINTER(OraText), ub4, POINTER(OraText), ub4, ub4]
    OCISessionPoolCreate.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10309
if hasattr(_libs['libclntsh.so.10.1'], 'OCISessionPoolDestroy'):
    OCISessionPoolDestroy = _libs['libclntsh.so.10.1'].OCISessionPoolDestroy
    OCISessionPoolDestroy.argtypes = [POINTER(OCISPool), POINTER(OCIError), ub4]
    OCISessionPoolDestroy.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10313
if hasattr(_libs['libclntsh.so.10.1'], 'OCISessionGet'):
    OCISessionGet = _libs['libclntsh.so.10.1'].OCISessionGet
    OCISessionGet.argtypes = [POINTER(OCIEnv), POINTER(OCIError), POINTER(POINTER(OCISvcCtx)), POINTER(OCIAuthInfo), POINTER(OraText), ub4, POINTER(OraText), ub4, POINTER(POINTER(OraText)), POINTER(ub4), POINTER(boolean), ub4]
    OCISessionGet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10320
if hasattr(_libs['libclntsh.so.10.1'], 'OCISessionRelease'):
    OCISessionRelease = _libs['libclntsh.so.10.1'].OCISessionRelease
    OCISessionRelease.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OraText), ub4, ub4]
    OCISessionRelease.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10329
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAppCtxSet'):
    OCIAppCtxSet = _libs['libclntsh.so.10.1'].OCIAppCtxSet
    OCIAppCtxSet.argtypes = [POINTER(None), POINTER(None), ub4, POINTER(None), ub4, POINTER(None), ub4, POINTER(OCIError), ub4]
    OCIAppCtxSet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10334
if hasattr(_libs['libclntsh.so.10.1'], 'OCIAppCtxClearAll'):
    OCIAppCtxClearAll = _libs['libclntsh.so.10.1'].OCIAppCtxClearAll
    OCIAppCtxClearAll.argtypes = [POINTER(None), POINTER(None), ub4, POINTER(OCIError), ub4]
    OCIAppCtxClearAll.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10338
if hasattr(_libs['libclntsh.so.10.1'], 'OCIPing'):
    OCIPing = _libs['libclntsh.so.10.1'].OCIPing
    OCIPing.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), ub4]
    OCIPing.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10342
if hasattr(_libs['libclntsh.so.10.1'], 'OCIKerbAttrSet'):
    OCIKerbAttrSet = _libs['libclntsh.so.10.1'].OCIKerbAttrSet
    OCIKerbAttrSet.argtypes = [POINTER(OCISession), ub4, POINTER(ub1), ub4, POINTER(ub1), ub4, ub2, ub4, sb4, sb4, sb4, sb4, POINTER(oratext), ub4, POINTER(oratext), ub4, POINTER(OCIError)]
    OCIKerbAttrSet.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10355
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDBStartup'):
    OCIDBStartup = _libs['libclntsh.so.10.1'].OCIDBStartup
    OCIDBStartup.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAdmin), ub4, ub4]
    OCIDBStartup.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10361
if hasattr(_libs['libclntsh.so.10.1'], 'OCIDBShutdown'):
    OCIDBShutdown = _libs['libclntsh.so.10.1'].OCIDBShutdown
    OCIDBShutdown.argtypes = [POINTER(OCISvcCtx), POINTER(OCIError), POINTER(OCIAdmin), ub4]
    OCIDBShutdown.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10369
if hasattr(_libs['libclntsh.so.10.1'], 'OCIClientVersion'):
    OCIClientVersion = _libs['libclntsh.so.10.1'].OCIClientVersion
    OCIClientVersion.argtypes = [POINTER(sword), POINTER(sword), POINTER(sword), POINTER(sword), POINTER(sword)]
    OCIClientVersion.restype = None

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ociap.h: 10378
if hasattr(_libs['libclntsh.so.10.1'], 'OCIInitEventHandle'):
    OCIInitEventHandle = _libs['libclntsh.so.10.1'].OCIInitEventHandle
    OCIInitEventHandle.argtypes = [POINTER(OCIError), POINTER(OCIEvent), POINTER(text), ub4]
    OCIInitEventHandle.restype = sword

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 46
try:
    MAXSB1MINVAL = (-127)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oratypes.h: 124
try:
    MINUB4MAXVAL = 4294967295L
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 116
try:
    HDA_SIZE = 256
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 122
try:
    CDA_SIZE = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 159
try:
    OCI_EV_DEF = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 160
try:
    OCI_EV_TSF = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 163
try:
    OCI_LM_DEF = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 164
try:
    OCI_LM_NBL = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 175
try:
    OCI_ONE_PIECE = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 176
try:
    OCI_FIRST_PIECE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 177
try:
    OCI_NEXT_PIECE = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 178
try:
    OCI_LAST_PIECE = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 184
try:
    SQLT_CHR = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 185
try:
    SQLT_NUM = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 186
try:
    SQLT_INT = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 187
try:
    SQLT_FLT = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 188
try:
    SQLT_STR = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 189
try:
    SQLT_VNU = 6
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 190
try:
    SQLT_PDN = 7
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 191
try:
    SQLT_LNG = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 192
try:
    SQLT_VCS = 9
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 193
try:
    SQLT_NON = 10
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 194
try:
    SQLT_RID = 11
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 195
try:
    SQLT_DAT = 12
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 196
try:
    SQLT_VBI = 15
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 197
try:
    SQLT_BFLOAT = 21
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 198
try:
    SQLT_BDOUBLE = 22
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 199
try:
    SQLT_BIN = 23
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 200
try:
    SQLT_LBI = 24
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 201
try:
    SQLT_UIN = 68
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 202
try:
    SQLT_SLS = 91
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 203
try:
    SQLT_LVC = 94
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 204
try:
    SQLT_LVB = 95
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 205
try:
    SQLT_AFC = 96
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 206
try:
    SQLT_AVC = 97
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 207
try:
    SQLT_IBFLOAT = 100
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 208
try:
    SQLT_IBDOUBLE = 101
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 209
try:
    SQLT_CUR = 102
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 210
try:
    SQLT_RDD = 104
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 211
try:
    SQLT_LAB = 105
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 212
try:
    SQLT_OSL = 106
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 214
try:
    SQLT_NTY = 108
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 215
try:
    SQLT_REF = 110
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 216
try:
    SQLT_CLOB = 112
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 217
try:
    SQLT_BLOB = 113
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 218
try:
    SQLT_BFILEE = 114
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 219
try:
    SQLT_CFILEE = 115
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 220
try:
    SQLT_RSET = 116
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 221
try:
    SQLT_NCO = 122
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 222
try:
    SQLT_VST = 155
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 223
try:
    SQLT_ODT = 156
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 226
try:
    SQLT_DATE = 184
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 227
try:
    SQLT_TIME = 185
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 228
try:
    SQLT_TIME_TZ = 186
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 229
try:
    SQLT_TIMESTAMP = 187
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 230
try:
    SQLT_TIMESTAMP_TZ = 188
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 231
try:
    SQLT_INTERVAL_YM = 189
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 232
try:
    SQLT_INTERVAL_DS = 190
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 233
try:
    SQLT_TIMESTAMP_LTZ = 232
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 235
try:
    SQLT_PNTY = 241
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 239
try:
    SQLT_FILE = SQLT_BFILEE
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 240
try:
    SQLT_CFILE = SQLT_CFILEE
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 241
try:
    SQLT_BFILE = SQLT_BFILEE
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 244
try:
    SQLCS_IMPLICIT = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 245
try:
    SQLCS_NCHAR = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 246
try:
    SQLCS_EXPLICIT = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 247
try:
    SQLCS_FLEXIBLE = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 248
try:
    SQLCS_LIT_NULL = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 783
try:
    OCI_HTYPE_FIRST = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 784
try:
    OCI_HTYPE_ENV = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 785
try:
    OCI_HTYPE_ERROR = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 786
try:
    OCI_HTYPE_SVCCTX = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 787
try:
    OCI_HTYPE_STMT = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 788
try:
    OCI_HTYPE_BIND = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 789
try:
    OCI_HTYPE_DEFINE = 6
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 790
try:
    OCI_HTYPE_DESCRIBE = 7
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 791
try:
    OCI_HTYPE_SERVER = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 792
try:
    OCI_HTYPE_SESSION = 9
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 793
try:
    OCI_HTYPE_AUTHINFO = OCI_HTYPE_SESSION
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 794
try:
    OCI_HTYPE_TRANS = 10
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 795
try:
    OCI_HTYPE_COMPLEXOBJECT = 11
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 796
try:
    OCI_HTYPE_SECURITY = 12
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 797
try:
    OCI_HTYPE_SUBSCRIPTION = 13
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 798
try:
    OCI_HTYPE_DIRPATH_CTX = 14
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 799
try:
    OCI_HTYPE_DIRPATH_COLUMN_ARRAY = 15
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 800
try:
    OCI_HTYPE_DIRPATH_STREAM = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 801
try:
    OCI_HTYPE_PROC = 17
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 802
try:
    OCI_HTYPE_DIRPATH_FN_CTX = 18
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 803
try:
    OCI_HTYPE_DIRPATH_FN_COL_ARRAY = 19
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 804
try:
    OCI_HTYPE_XADSESSION = 20
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 805
try:
    OCI_HTYPE_XADTABLE = 21
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 806
try:
    OCI_HTYPE_XADFIELD = 22
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 807
try:
    OCI_HTYPE_XADGRANULE = 23
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 808
try:
    OCI_HTYPE_XADRECORD = 24
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 809
try:
    OCI_HTYPE_XADIO = 25
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 810
try:
    OCI_HTYPE_CPOOL = 26
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 811
try:
    OCI_HTYPE_SPOOL = 27
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 812
try:
    OCI_HTYPE_ADMIN = 28
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 813
try:
    OCI_HTYPE_EVENT = 29
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 815
try:
    OCI_HTYPE_LAST = 29
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 822
try:
    OCI_DTYPE_FIRST = 50
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 823
try:
    OCI_DTYPE_LOB = 50
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 824
try:
    OCI_DTYPE_SNAP = 51
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 825
try:
    OCI_DTYPE_RSET = 52
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 826
try:
    OCI_DTYPE_PARAM = 53
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 827
try:
    OCI_DTYPE_ROWID = 54
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 828
try:
    OCI_DTYPE_COMPLEXOBJECTCOMP = 55
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 830
try:
    OCI_DTYPE_FILE = 56
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 831
try:
    OCI_DTYPE_AQENQ_OPTIONS = 57
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 832
try:
    OCI_DTYPE_AQDEQ_OPTIONS = 58
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 833
try:
    OCI_DTYPE_AQMSG_PROPERTIES = 59
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 834
try:
    OCI_DTYPE_AQAGENT = 60
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 835
try:
    OCI_DTYPE_LOCATOR = 61
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 836
try:
    OCI_DTYPE_INTERVAL_YM = 62
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 837
try:
    OCI_DTYPE_INTERVAL_DS = 63
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 838
try:
    OCI_DTYPE_AQNFY_DESCRIPTOR = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 839
try:
    OCI_DTYPE_DATE = 65
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 840
try:
    OCI_DTYPE_TIME = 66
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 841
try:
    OCI_DTYPE_TIME_TZ = 67
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 842
try:
    OCI_DTYPE_TIMESTAMP = 68
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 843
try:
    OCI_DTYPE_TIMESTAMP_TZ = 69
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 844
try:
    OCI_DTYPE_TIMESTAMP_LTZ = 70
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 845
try:
    OCI_DTYPE_UCB = 71
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 846
try:
    OCI_DTYPE_SRVDN = 72
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 847
try:
    OCI_DTYPE_SIGNATURE = 73
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 848
try:
    OCI_DTYPE_RESERVED_1 = 74
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 849
try:
    OCI_DTYPE_AQLIS_OPTIONS = 75
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 850
try:
    OCI_DTYPE_AQLIS_MSG_PROPERTIES = 76
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 851
try:
    OCI_DTYPE_CHDES = 77
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 852
try:
    OCI_DTYPE_TABLE_CHDES = 78
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 853
try:
    OCI_DTYPE_ROW_CHDES = 79
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 854
try:
    OCI_DTYPE_LAST = 79
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 859
try:
    OCI_TEMP_BLOB = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 860
try:
    OCI_TEMP_CLOB = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 864
try:
    OCI_OTYPE_NAME = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 865
try:
    OCI_OTYPE_REF = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 866
try:
    OCI_OTYPE_PTR = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 881
try:
    OCI_ATTR_FNCODE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 882
try:
    OCI_ATTR_OBJECT = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 883
try:
    OCI_ATTR_NONBLOCKING_MODE = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 884
try:
    OCI_ATTR_SQLCODE = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 885
try:
    OCI_ATTR_ENV = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 886
try:
    OCI_ATTR_SERVER = 6
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 887
try:
    OCI_ATTR_SESSION = 7
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 888
try:
    OCI_ATTR_TRANS = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 889
try:
    OCI_ATTR_ROW_COUNT = 9
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 890
try:
    OCI_ATTR_SQLFNCODE = 10
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 891
try:
    OCI_ATTR_PREFETCH_ROWS = 11
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 892
try:
    OCI_ATTR_NESTED_PREFETCH_ROWS = 12
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 893
try:
    OCI_ATTR_PREFETCH_MEMORY = 13
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 894
try:
    OCI_ATTR_NESTED_PREFETCH_MEMORY = 14
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 895
try:
    OCI_ATTR_CHAR_COUNT = 15
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 897
try:
    OCI_ATTR_PDSCL = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 898
try:
    OCI_ATTR_FSPRECISION = OCI_ATTR_PDSCL
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 900
try:
    OCI_ATTR_PDPRC = 17
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 901
try:
    OCI_ATTR_LFPRECISION = OCI_ATTR_PDPRC
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 903
try:
    OCI_ATTR_PARAM_COUNT = 18
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 904
try:
    OCI_ATTR_ROWID = 19
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 905
try:
    OCI_ATTR_CHARSET = 20
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 906
try:
    OCI_ATTR_NCHAR = 21
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 907
try:
    OCI_ATTR_USERNAME = 22
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 908
try:
    OCI_ATTR_PASSWORD = 23
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 909
try:
    OCI_ATTR_STMT_TYPE = 24
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 910
try:
    OCI_ATTR_INTERNAL_NAME = 25
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 911
try:
    OCI_ATTR_EXTERNAL_NAME = 26
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 912
try:
    OCI_ATTR_XID = 27
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 913
try:
    OCI_ATTR_TRANS_LOCK = 28
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 914
try:
    OCI_ATTR_TRANS_NAME = 29
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 915
try:
    OCI_ATTR_HEAPALLOC = 30
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 916
try:
    OCI_ATTR_CHARSET_ID = 31
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 917
try:
    OCI_ATTR_CHARSET_FORM = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 918
try:
    OCI_ATTR_MAXDATA_SIZE = 33
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 919
try:
    OCI_ATTR_CACHE_OPT_SIZE = 34
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 920
try:
    OCI_ATTR_CACHE_MAX_SIZE = 35
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 921
try:
    OCI_ATTR_PINOPTION = 36
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 922
try:
    OCI_ATTR_ALLOC_DURATION = 37
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 924
try:
    OCI_ATTR_PIN_DURATION = 38
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 925
try:
    OCI_ATTR_FDO = 39
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 926
try:
    OCI_ATTR_POSTPROCESSING_CALLBACK = 40
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 928
try:
    OCI_ATTR_POSTPROCESSING_CONTEXT = 41
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 930
try:
    OCI_ATTR_ROWS_RETURNED = 42
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 932
try:
    OCI_ATTR_FOCBK = 43
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 933
try:
    OCI_ATTR_IN_V8_MODE = 44
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 934
try:
    OCI_ATTR_LOBEMPTY = 45
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 935
try:
    OCI_ATTR_SESSLANG = 46
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 937
try:
    OCI_ATTR_VISIBILITY = 47
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 938
try:
    OCI_ATTR_RELATIVE_MSGID = 48
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 939
try:
    OCI_ATTR_SEQUENCE_DEVIATION = 49
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 941
try:
    OCI_ATTR_CONSUMER_NAME = 50
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 942
try:
    OCI_ATTR_DEQ_MODE = 51
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 943
try:
    OCI_ATTR_NAVIGATION = 52
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 944
try:
    OCI_ATTR_WAIT = 53
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 945
try:
    OCI_ATTR_DEQ_MSGID = 54
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 947
try:
    OCI_ATTR_PRIORITY = 55
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 948
try:
    OCI_ATTR_DELAY = 56
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 949
try:
    OCI_ATTR_EXPIRATION = 57
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 950
try:
    OCI_ATTR_CORRELATION = 58
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 951
try:
    OCI_ATTR_ATTEMPTS = 59
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 952
try:
    OCI_ATTR_RECIPIENT_LIST = 60
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 953
try:
    OCI_ATTR_EXCEPTION_QUEUE = 61
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 954
try:
    OCI_ATTR_ENQ_TIME = 62
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 955
try:
    OCI_ATTR_MSG_STATE = 63
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 957
try:
    OCI_ATTR_AGENT_NAME = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 958
try:
    OCI_ATTR_AGENT_ADDRESS = 65
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 959
try:
    OCI_ATTR_AGENT_PROTOCOL = 66
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 960
try:
    OCI_ATTR_USER_PROPERTY = 67
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 961
try:
    OCI_ATTR_SENDER_ID = 68
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 962
try:
    OCI_ATTR_ORIGINAL_MSGID = 69
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 964
try:
    OCI_ATTR_QUEUE_NAME = 70
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 965
try:
    OCI_ATTR_NFY_MSGID = 71
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 966
try:
    OCI_ATTR_MSG_PROP = 72
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 968
try:
    OCI_ATTR_NUM_DML_ERRORS = 73
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 969
try:
    OCI_ATTR_DML_ROW_OFFSET = 74
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 972
try:
    OCI_ATTR_AQ_NUM_ERRORS = OCI_ATTR_NUM_DML_ERRORS
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 973
try:
    OCI_ATTR_AQ_ERROR_INDEX = OCI_ATTR_DML_ROW_OFFSET
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 975
try:
    OCI_ATTR_DATEFORMAT = 75
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 976
try:
    OCI_ATTR_BUF_ADDR = 76
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 977
try:
    OCI_ATTR_BUF_SIZE = 77
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 981
try:
    OCI_ATTR_NUM_ROWS = 81
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 985
try:
    OCI_ATTR_COL_COUNT = 82
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 987
try:
    OCI_ATTR_STREAM_OFFSET = 83
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 988
try:
    OCI_ATTR_SHARED_HEAPALLOC = 84
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 990
try:
    OCI_ATTR_SERVER_GROUP = 85
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 992
try:
    OCI_ATTR_MIGSESSION = 86
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 994
try:
    OCI_ATTR_NOCACHE = 87
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 996
try:
    OCI_ATTR_MEMPOOL_SIZE = 88
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 997
try:
    OCI_ATTR_MEMPOOL_INSTNAME = 89
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 998
try:
    OCI_ATTR_MEMPOOL_APPNAME = 90
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 999
try:
    OCI_ATTR_MEMPOOL_HOMENAME = 91
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1000
try:
    OCI_ATTR_MEMPOOL_MODEL = 92
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1001
try:
    OCI_ATTR_MODES = 93
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1003
try:
    OCI_ATTR_SUBSCR_NAME = 94
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1004
try:
    OCI_ATTR_SUBSCR_CALLBACK = 95
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1005
try:
    OCI_ATTR_SUBSCR_CTX = 96
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1006
try:
    OCI_ATTR_SUBSCR_PAYLOAD = 97
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1007
try:
    OCI_ATTR_SUBSCR_NAMESPACE = 98
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1009
try:
    OCI_ATTR_PROXY_CREDENTIALS = 99
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1010
try:
    OCI_ATTR_INITIAL_CLIENT_ROLES = 100
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1012
try:
    OCI_ATTR_UNK = 101
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1013
try:
    OCI_ATTR_NUM_COLS = 102
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1014
try:
    OCI_ATTR_LIST_COLUMNS = 103
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1015
try:
    OCI_ATTR_RDBA = 104
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1016
try:
    OCI_ATTR_CLUSTERED = 105
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1017
try:
    OCI_ATTR_PARTITIONED = 106
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1018
try:
    OCI_ATTR_INDEX_ONLY = 107
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1019
try:
    OCI_ATTR_LIST_ARGUMENTS = 108
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1020
try:
    OCI_ATTR_LIST_SUBPROGRAMS = 109
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1021
try:
    OCI_ATTR_REF_TDO = 110
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1022
try:
    OCI_ATTR_LINK = 111
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1023
try:
    OCI_ATTR_MIN = 112
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1024
try:
    OCI_ATTR_MAX = 113
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1025
try:
    OCI_ATTR_INCR = 114
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1026
try:
    OCI_ATTR_CACHE = 115
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1027
try:
    OCI_ATTR_ORDER = 116
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1028
try:
    OCI_ATTR_HW_MARK = 117
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1029
try:
    OCI_ATTR_TYPE_SCHEMA = 118
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1030
try:
    OCI_ATTR_TIMESTAMP = 119
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1031
try:
    OCI_ATTR_NUM_ATTRS = 120
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1032
try:
    OCI_ATTR_NUM_PARAMS = 121
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1033
try:
    OCI_ATTR_OBJID = 122
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1034
try:
    OCI_ATTR_PTYPE = 123
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1035
try:
    OCI_ATTR_PARAM = 124
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1036
try:
    OCI_ATTR_OVERLOAD_ID = 125
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1037
try:
    OCI_ATTR_TABLESPACE = 126
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1038
try:
    OCI_ATTR_TDO = 127
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1039
try:
    OCI_ATTR_LTYPE = 128
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1040
try:
    OCI_ATTR_PARSE_ERROR_OFFSET = 129
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1041
try:
    OCI_ATTR_IS_TEMPORARY = 130
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1042
try:
    OCI_ATTR_IS_TYPED = 131
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1043
try:
    OCI_ATTR_DURATION = 132
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1044
try:
    OCI_ATTR_IS_INVOKER_RIGHTS = 133
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1045
try:
    OCI_ATTR_OBJ_NAME = 134
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1046
try:
    OCI_ATTR_OBJ_SCHEMA = 135
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1047
try:
    OCI_ATTR_OBJ_ID = 136
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1052
try:
    OCI_ATTR_TRANS_TIMEOUT = 142
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1053
try:
    OCI_ATTR_SERVER_STATUS = 143
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1054
try:
    OCI_ATTR_STATEMENT = 144
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1058
try:
    OCI_ATTR_DEQCOND = 146
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1059
try:
    OCI_ATTR_RESERVED_2 = 147
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1062
try:
    OCI_ATTR_SUBSCR_RECPT = 148
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1063
try:
    OCI_ATTR_SUBSCR_RECPTPROTO = 149
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1067
try:
    OCI_ATTR_LDAP_HOST = 153
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1068
try:
    OCI_ATTR_LDAP_PORT = 154
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1069
try:
    OCI_ATTR_BIND_DN = 155
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1070
try:
    OCI_ATTR_LDAP_CRED = 156
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1071
try:
    OCI_ATTR_WALL_LOC = 157
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1072
try:
    OCI_ATTR_LDAP_AUTH = 158
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1073
try:
    OCI_ATTR_LDAP_CTX = 159
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1074
try:
    OCI_ATTR_SERVER_DNS = 160
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1076
try:
    OCI_ATTR_DN_COUNT = 161
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1077
try:
    OCI_ATTR_SERVER_DN = 162
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1079
try:
    OCI_ATTR_MAXCHAR_SIZE = 163
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1081
try:
    OCI_ATTR_CURRENT_POSITION = 164
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1084
try:
    OCI_ATTR_RESERVED_3 = 165
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1085
try:
    OCI_ATTR_RESERVED_4 = 166
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1089
try:
    OCI_ATTR_DIGEST_ALGO = 168
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1090
try:
    OCI_ATTR_CERTIFICATE = 169
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1091
try:
    OCI_ATTR_SIGNATURE_ALGO = 170
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1092
try:
    OCI_ATTR_CANONICAL_ALGO = 171
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1093
try:
    OCI_ATTR_PRIVATE_KEY = 172
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1094
try:
    OCI_ATTR_DIGEST_VALUE = 173
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1095
try:
    OCI_ATTR_SIGNATURE_VAL = 174
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1096
try:
    OCI_ATTR_SIGNATURE = 175
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1099
try:
    OCI_ATTR_STMTCACHESIZE = 176
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1102
try:
    OCI_ATTR_CONN_NOWAIT = 178
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1103
try:
    OCI_ATTR_CONN_BUSY_COUNT = 179
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1104
try:
    OCI_ATTR_CONN_OPEN_COUNT = 180
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1105
try:
    OCI_ATTR_CONN_TIMEOUT = 181
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1106
try:
    OCI_ATTR_STMT_STATE = 182
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1107
try:
    OCI_ATTR_CONN_MIN = 183
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1108
try:
    OCI_ATTR_CONN_MAX = 184
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1109
try:
    OCI_ATTR_CONN_INCR = 185
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1113
try:
    OCI_ATTR_NUM_OPEN_STMTS = 188
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1114
try:
    OCI_ATTR_DESCRIBE_NATIVE = 189
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1116
try:
    OCI_ATTR_BIND_COUNT = 190
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1117
try:
    OCI_ATTR_HANDLE_POSITION = 191
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1118
try:
    OCI_ATTR_RESERVED_5 = 192
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1119
try:
    OCI_ATTR_SERVER_BUSY = 193
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1124
try:
    OCI_ATTR_SUBSCR_RECPTPRES = 195
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1125
try:
    OCI_ATTR_TRANSFORMATION = 196
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1127
try:
    OCI_ATTR_ROWS_FETCHED = 197
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1130
try:
    OCI_ATTR_SCN_BASE = 198
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1131
try:
    OCI_ATTR_SCN_WRAP = 199
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1134
try:
    OCI_ATTR_RESERVED_6 = 200
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1135
try:
    OCI_ATTR_READONLY_TXN = 201
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1136
try:
    OCI_ATTR_RESERVED_7 = 202
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1137
try:
    OCI_ATTR_ERRONEOUS_COLUMN = 203
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1138
try:
    OCI_ATTR_RESERVED_8 = 204
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1142
try:
    OCI_ATTR_INST_TYPE = 207
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1145
try:
    OCI_ATTR_ENV_UTF16 = 209
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1146
try:
    OCI_ATTR_RESERVED_9 = 210
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1147
try:
    OCI_ATTR_RESERVED_10 = 211
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1151
try:
    OCI_ATTR_RESERVED_12 = 214
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1152
try:
    OCI_ATTR_RESERVED_13 = 215
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1153
try:
    OCI_ATTR_IS_EXTERNAL = 216
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1158
try:
    OCI_ATTR_RESERVED_15 = 217
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1159
try:
    OCI_ATTR_STMT_IS_RETURNING = 218
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1160
try:
    OCI_ATTR_RESERVED_16 = 219
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1161
try:
    OCI_ATTR_RESERVED_17 = 220
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1162
try:
    OCI_ATTR_RESERVED_18 = 221
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1165
try:
    OCI_ATTR_RESERVED_19 = 222
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1166
try:
    OCI_ATTR_RESERVED_20 = 223
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1167
try:
    OCI_ATTR_CURRENT_SCHEMA = 224
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1168
try:
    OCI_ATTR_RESERVED_21 = 415
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1171
try:
    OCI_ATTR_SUBSCR_QOSFLAGS = 225
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1172
try:
    OCI_ATTR_SUBSCR_PAYLOADCBK = 226
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1173
try:
    OCI_ATTR_SUBSCR_TIMEOUT = 227
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1174
try:
    OCI_ATTR_SUBSCR_NAMESPACE_CTX = 228
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1177
try:
    OCI_ATTR_BIND_ROWCBK = 301
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1178
try:
    OCI_ATTR_BIND_ROWCTX = 302
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1179
try:
    OCI_ATTR_SKIP_BUFFER = 303
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1182
try:
    OCI_ATTR_CHNF_TABLENAMES = 401
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1183
try:
    OCI_ATTR_CHNF_ROWIDS = 402
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1184
try:
    OCI_ATTR_CHNF_OPERATIONS = 403
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1185
try:
    OCI_ATTR_CHNF_CHANGELAG = 404
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1188
try:
    OCI_ATTR_CHDES_DBNAME = 405
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1189
try:
    OCI_ATTR_CHDES_NFYTYPE = 406
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1190
try:
    OCI_ATTR_CHDES_XID = 407
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1191
try:
    OCI_ATTR_CHDES_TABLE_CHANGES = 408
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1193
try:
    OCI_ATTR_CHDES_TABLE_NAME = 409
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1194
try:
    OCI_ATTR_CHDES_TABLE_OPFLAGS = 410
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1195
try:
    OCI_ATTR_CHDES_TABLE_ROW_CHANGES = 411
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1196
try:
    OCI_ATTR_CHDES_ROW_ROWID = 412
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1197
try:
    OCI_ATTR_CHDES_ROW_OPFLAGS = 413
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1200
try:
    OCI_ATTR_CHNF_REGHANDLE = 414
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1203
try:
    OCI_ATTR_PROXY_CLIENT = 416
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1208
try:
    OCI_ATTR_TABLE_ENC = 417
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1209
try:
    OCI_ATTR_TABLE_ENC_ALG = 418
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1210
try:
    OCI_ATTR_TABLE_ENC_ALG_ID = 419
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1213
try:
    OCI_ATTR_STMTCACHE_CBKCTX = 420
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1214
try:
    OCI_ATTR_STMTCACHE_CBK = 421
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1218
try:
    OCI_ATTR_RESERVED_26 = 422
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1221
try:
    OCI_EVENT_NONE = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1222
try:
    OCI_EVENT_STARTUP = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1223
try:
    OCI_EVENT_SHUTDOWN = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1224
try:
    OCI_EVENT_SHUTDOWN_ANY = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1225
try:
    OCI_EVENT_DROP_DB = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1226
try:
    OCI_EVENT_DEREG = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1227
try:
    OCI_EVENT_OBJCHANGE = 6
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1230
try:
    OCI_OPCODE_ALLROWS = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1231
try:
    OCI_OPCODE_ALLOPS = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1232
try:
    OCI_OPCODE_INSERT = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1233
try:
    OCI_OPCODE_UPDATE = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1234
try:
    OCI_OPCODE_DELETE = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1235
try:
    OCI_OPCODE_ALTER = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1236
try:
    OCI_OPCODE_DROP = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1237
try:
    OCI_OPCODE_UNKNOWN = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1240
try:
    OCI_ATTR_ENV_CHARSET_ID = OCI_ATTR_CHARSET_ID
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1241
try:
    OCI_ATTR_ENV_NCHARSET_ID = OCI_ATTR_NCHARSET_ID
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1244
try:
    OCI_ATTR_EVTCBK = 304
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1245
try:
    OCI_ATTR_EVTCTX = 305
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1248
try:
    OCI_ATTR_USER_MEMORY = 306
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1251
try:
    OCI_ATTR_SUBSCR_PORTNO = 390
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1254
try:
    OCI_SUBSCR_PROTO_OCI = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1255
try:
    OCI_SUBSCR_PROTO_MAIL = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1256
try:
    OCI_SUBSCR_PROTO_SERVER = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1257
try:
    OCI_SUBSCR_PROTO_HTTP = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1258
try:
    OCI_SUBSCR_PROTO_MAX = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1261
try:
    OCI_SUBSCR_PRES_DEFAULT = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1262
try:
    OCI_SUBSCR_PRES_XML = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1263
try:
    OCI_SUBSCR_PRES_MAX = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1266
try:
    OCI_SUBSCR_QOS_RELIABLE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1267
try:
    OCI_SUBSCR_QOS_PAYLOAD = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1268
try:
    OCI_SUBSCR_QOS_REPLICATE = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1269
try:
    OCI_SUBSCR_QOS_SECURE = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1270
try:
    OCI_SUBSCR_QOS_PURGE_ON_NTFN = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1271
try:
    OCI_SUBSCR_QOS_MULTICBK = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1274
try:
    OCI_UCS2ID = 1000
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1275
try:
    OCI_UTF16ID = 1000
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1282
try:
    OCI_SERVER_NOT_CONNECTED = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1283
try:
    OCI_SERVER_NORMAL = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1288
try:
    OCI_SUBSCR_NAMESPACE_ANONYMOUS = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1289
try:
    OCI_SUBSCR_NAMESPACE_AQ = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1290
try:
    OCI_SUBSCR_NAMESPACE_DBCHANGE = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1291
try:
    OCI_SUBSCR_NAMESPACE_MAX = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1295
try:
    OCI_CRED_RDBMS = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1296
try:
    OCI_CRED_EXT = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1297
try:
    OCI_CRED_PROXY = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1298
try:
    OCI_CRED_RESERVED_1 = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1299
try:
    OCI_CRED_RESERVED_2 = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1303
try:
    OCI_SUCCESS = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1304
try:
    OCI_SUCCESS_WITH_INFO = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1305
try:
    OCI_RESERVED_FOR_INT_USE = 200
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1306
try:
    OCI_NO_DATA = 100
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1307
try:
    OCI_ERROR = (-1)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1308
try:
    OCI_INVALID_HANDLE = (-2)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1309
try:
    OCI_NEED_DATA = 99
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1310
try:
    OCI_STILL_EXECUTING = (-3123)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1314
try:
    OCI_CONTINUE = (-24200)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1315
try:
    OCI_ROWCBK_DONE = (-24201)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1321
try:
    OCI_DT_INVALID_DAY = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1322
try:
    OCI_DT_DAY_BELOW_VALID = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1323
try:
    OCI_DT_INVALID_MONTH = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1324
try:
    OCI_DT_MONTH_BELOW_VALID = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1325
try:
    OCI_DT_INVALID_YEAR = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1326
try:
    OCI_DT_YEAR_BELOW_VALID = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1327
try:
    OCI_DT_INVALID_HOUR = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1328
try:
    OCI_DT_HOUR_BELOW_VALID = 128
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1329
try:
    OCI_DT_INVALID_MINUTE = 256
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1330
try:
    OCI_DT_MINUTE_BELOW_VALID = 512
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1331
try:
    OCI_DT_INVALID_SECOND = 1024
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1332
try:
    OCI_DT_SECOND_BELOW_VALID = 2048
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1333
try:
    OCI_DT_DAY_MISSING_FROM_1582 = 4096
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1335
try:
    OCI_DT_YEAR_ZERO = 8192
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1336
try:
    OCI_DT_INVALID_TIMEZONE = 16384
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1337
try:
    OCI_DT_INVALID_FORMAT = 32768
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1341
try:
    OCI_INTER_INVALID_DAY = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1342
try:
    OCI_INTER_DAY_BELOW_VALID = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1343
try:
    OCI_INTER_INVALID_MONTH = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1344
try:
    OCI_INTER_MONTH_BELOW_VALID = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1345
try:
    OCI_INTER_INVALID_YEAR = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1346
try:
    OCI_INTER_YEAR_BELOW_VALID = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1347
try:
    OCI_INTER_INVALID_HOUR = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1348
try:
    OCI_INTER_HOUR_BELOW_VALID = 128
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1349
try:
    OCI_INTER_INVALID_MINUTE = 256
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1350
try:
    OCI_INTER_MINUTE_BELOW_VALID = 512
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1352
try:
    OCI_INTER_INVALID_SECOND = 1024
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1353
try:
    OCI_INTER_SECOND_BELOW_VALID = 2048
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1355
try:
    OCI_INTER_INVALID_FRACSEC = 4096
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1356
try:
    OCI_INTER_FRACSEC_BELOW_VALID = 8192
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1361
try:
    OCI_V7_SYNTAX = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1362
try:
    OCI_V8_SYNTAX = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1363
try:
    OCI_NTV_SYNTAX = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1371
try:
    OCI_FETCH_CURRENT = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1372
try:
    OCI_FETCH_NEXT = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1373
try:
    OCI_FETCH_FIRST = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1374
try:
    OCI_FETCH_LAST = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1375
try:
    OCI_FETCH_PRIOR = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1376
try:
    OCI_FETCH_ABSOLUTE = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1377
try:
    OCI_FETCH_RELATIVE = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1378
try:
    OCI_FETCH_RESERVED_1 = 128
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1379
try:
    OCI_FETCH_RESERVED_2 = 256
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1380
try:
    OCI_FETCH_RESERVED_3 = 512
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1381
try:
    OCI_FETCH_RESERVED_4 = 1024
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1382
try:
    OCI_FETCH_RESERVED_5 = 2048
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1387
try:
    OCI_SB2_IND_PTR = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1388
try:
    OCI_DATA_AT_EXEC = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1389
try:
    OCI_DYNAMIC_FETCH = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1390
try:
    OCI_PIECEWISE = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1391
try:
    OCI_DEFINE_RESERVED_1 = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1392
try:
    OCI_BIND_RESERVED_2 = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1393
try:
    OCI_DEFINE_RESERVED_2 = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1394
try:
    OCI_BIND_SOFT = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1395
try:
    OCI_DEFINE_SOFT = 128
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1396
try:
    OCI_BIND_RESERVED_3 = 256
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1400
try:
    OCI_DEFAULT = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1403
try:
    OCI_THREADED = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1404
try:
    OCI_OBJECT = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1405
try:
    OCI_EVENTS = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1406
try:
    OCI_RESERVED1 = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1407
try:
    OCI_SHARED = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1408
try:
    OCI_RESERVED2 = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1410
try:
    OCI_NO_UCB = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1411
try:
    OCI_NO_MUTEX = 128
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1413
try:
    OCI_SHARED_EXT = 256
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1415
try:
    OCI_ALWAYS_BLOCKING = 1024
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1417
try:
    OCI_USE_LDAP = 4096
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1418
try:
    OCI_REG_LDAPONLY = 8192
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1419
try:
    OCI_UTF16 = 16384
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1420
try:
    OCI_AFC_PAD_ON = 32768
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1422
try:
    OCI_ENVCR_RESERVED3 = 65536
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1423
try:
    OCI_NEW_LENGTH_SEMANTICS = 131072
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1425
try:
    OCI_NO_MUTEX_STMT = 262144
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1426
try:
    OCI_MUTEX_ENV_ONLY = 524288
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1427
try:
    OCI_SUPPRESS_NLS_VALIDATION = 1048576
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1428
try:
    OCI_MUTEX_TRY = 2097152
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1429
try:
    OCI_NCHAR_LITERAL_REPLACE_ON = 4194304
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1430
try:
    OCI_NCHAR_LITERAL_REPLACE_OFF = 8388608
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1436
try:
    OCI_CPOOL_REINITIALIZE = 273
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1441
try:
    OCI_LOGON2_SPOOL = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1442
try:
    OCI_LOGON2_CPOOL = OCI_CPOOL
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1443
try:
    OCI_LOGON2_STMTCACHE = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1444
try:
    OCI_LOGON2_PROXY = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1449
try:
    OCI_SPC_REINITIALIZE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1450
try:
    OCI_SPC_HOMOGENEOUS = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1451
try:
    OCI_SPC_STMTCACHE = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1456
try:
    OCI_SESSGET_SPOOL = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1457
try:
    OCI_SESSGET_CPOOL = OCI_CPOOL
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1458
try:
    OCI_SESSGET_STMTCACHE = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1459
try:
    OCI_SESSGET_CREDPROXY = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1460
try:
    OCI_SESSGET_CREDEXT = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1461
try:
    OCI_SESSGET_SPOOL_MATCHANY = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1462
try:
    OCI_SESSGET_SYSDBA = 256
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1466
try:
    OCI_SPOOL_ATTRVAL_WAIT = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1467
try:
    OCI_SPOOL_ATTRVAL_NOWAIT = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1468
try:
    OCI_SPOOL_ATTRVAL_FORCEGET = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1473
try:
    OCI_SESSRLS_DROPSESS = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1474
try:
    OCI_SESSRLS_RETAG = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1479
try:
    OCI_SPD_FORCE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1486
try:
    OCI_STMT_STATE_INITIALIZED = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1487
try:
    OCI_STMT_STATE_EXECUTED = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1488
try:
    OCI_STMT_STATE_END_OF_FETCH = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1493
try:
    OCI_MEM_INIT = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1494
try:
    OCI_MEM_CLN = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1495
try:
    OCI_MEM_FLUSH = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1496
try:
    OCI_DUMP_HEAP = 128
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1498
try:
    OCI_CLIENT_STATS = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1499
try:
    OCI_SERVER_STATS = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1505
try:
    OCI_ENV_NO_UCB = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1507
try:
    OCI_ENV_NO_MUTEX = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1513
try:
    OCI_NO_SHARING = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1514
try:
    OCI_PREP_RESERVED_1 = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1515
try:
    OCI_PREP_AFC_PAD_ON = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1516
try:
    OCI_PREP_AFC_PAD_OFF = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1522
try:
    OCI_BATCH_MODE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1523
try:
    OCI_EXACT_FETCH = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1525
try:
    OCI_STMT_SCROLLABLE_READONLY = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1527
try:
    OCI_DESCRIBE_ONLY = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1528
try:
    OCI_COMMIT_ON_SUCCESS = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1529
try:
    OCI_NON_BLOCKING = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1530
try:
    OCI_BATCH_ERRORS = 128
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1531
try:
    OCI_PARSE_ONLY = 256
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1532
try:
    OCI_EXACT_FETCH_RESERVED_1 = 512
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1533
try:
    OCI_SHOW_DML_WARNINGS = 1024
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1535
try:
    OCI_EXEC_RESERVED_2 = 2048
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1536
try:
    OCI_DESC_RESERVED_1 = 4096
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1537
try:
    OCI_EXEC_RESERVED_3 = 8192
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1538
try:
    OCI_EXEC_RESERVED_4 = 16384
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1539
try:
    OCI_EXEC_RESERVED_5 = 32768
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1540
try:
    OCI_EXEC_RESERVED_6 = 65536
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1545
try:
    OCI_MIGRATE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1546
try:
    OCI_SYSDBA = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1547
try:
    OCI_SYSOPER = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1548
try:
    OCI_PRELIM_AUTH = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1549
try:
    OCIP_ICACHE = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1550
try:
    OCI_AUTH_RESERVED_1 = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1551
try:
    OCI_STMT_CACHE = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1552
try:
    OCI_STATELESS_CALL = 128
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1553
try:
    OCI_STATELESS_TXN = 256
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1554
try:
    OCI_STATELESS_APP = 512
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1555
try:
    OCI_AUTH_RESERVED_2 = 1024
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1556
try:
    OCI_AUTH_RESERVED_3 = 2048
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1557
try:
    OCI_AUTH_RESERVED_4 = 4096
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1558
try:
    OCI_AUTH_RESERVED_5 = 8192
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1559
try:
    OCI_SYSASM = 32768
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1564
try:
    OCI_SESSEND_RESERVED_1 = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1565
try:
    OCI_SESSEND_RESERVED_2 = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1574
try:
    OCI_FASTPATH = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1575
try:
    OCI_ATCH_RESERVED_1 = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1576
try:
    OCI_ATCH_RESERVED_2 = 128
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1577
try:
    OCI_ATCH_RESERVED_3 = 256
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1578
try:
    OCI_CPOOL = 512
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1579
try:
    OCI_ATCH_RESERVED_4 = 1024
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1580
try:
    OCI_ATCH_RESERVED_5 = 8192
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1582
try:
    OCI_SRVATCH_RESERVED5 = 16777216
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1585
try:
    OCI_PREP2_CACHE_SEARCHONLY = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1586
try:
    OCI_PREP2_GET_PLSQL_WARNINGS = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1587
try:
    OCI_PREP2_RESERVED_1 = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1590
try:
    OCI_STRLS_CACHE_DELETE = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1593
try:
    OCI_STM_RESERVED4 = 1048576
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1598
try:
    OCI_PARAM_IN = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1599
try:
    OCI_PARAM_OUT = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1604
try:
    OCI_TRANS_NEW = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1605
try:
    OCI_TRANS_JOIN = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1606
try:
    OCI_TRANS_RESUME = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1607
try:
    OCI_TRANS_STARTMASK = 255
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1609
try:
    OCI_TRANS_READONLY = 256
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1610
try:
    OCI_TRANS_READWRITE = 512
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1611
try:
    OCI_TRANS_SERIALIZABLE = 1024
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1613
try:
    OCI_TRANS_ISOLMASK = 65280
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1615
try:
    OCI_TRANS_LOOSE = 65536
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1616
try:
    OCI_TRANS_TIGHT = 131072
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1617
try:
    OCI_TRANS_TYPEMASK = 983040
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1619
try:
    OCI_TRANS_NOMIGRATE = 1048576
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1620
try:
    OCI_TRANS_SEPARABLE = 2097152
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1621
try:
    OCI_TRANS_OTSRESUME = 4194304
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1627
try:
    OCI_TRANS_TWOPHASE = 16777216
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1628
try:
    OCI_TRANS_WRITEBATCH = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1629
try:
    OCI_TRANS_WRITEIMMED = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1630
try:
    OCI_TRANS_WRITEWAIT = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1631
try:
    OCI_TRANS_WRITENOWAIT = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1640
try:
    OCI_ENQ_IMMEDIATE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1641
try:
    OCI_ENQ_ON_COMMIT = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1644
try:
    OCI_DEQ_BROWSE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1645
try:
    OCI_DEQ_LOCKED = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1646
try:
    OCI_DEQ_REMOVE = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1647
try:
    OCI_DEQ_REMOVE_NODATA = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1648
try:
    OCI_DEQ_GETSIG = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1651
try:
    OCI_DEQ_FIRST_MSG = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1652
try:
    OCI_DEQ_NEXT_MSG = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1653
try:
    OCI_DEQ_NEXT_TRANSACTION = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1654
try:
    OCI_DEQ_MULT_TRANSACTION = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1657
try:
    OCI_DEQ_RESERVED_1 = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1660
try:
    OCI_MSG_WAITING = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1661
try:
    OCI_MSG_READY = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1662
try:
    OCI_MSG_PROCESSED = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1663
try:
    OCI_MSG_EXPIRED = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1666
try:
    OCI_ENQ_BEFORE = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1667
try:
    OCI_ENQ_TOP = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1670
try:
    OCI_DEQ_IMMEDIATE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1671
try:
    OCI_DEQ_ON_COMMIT = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1674
try:
    OCI_DEQ_WAIT_FOREVER = (-1)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1675
try:
    OCI_DEQ_NO_WAIT = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1678
try:
    OCI_MSG_NO_DELAY = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1681
try:
    OCI_MSG_NO_EXPIRATION = (-1)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1683
try:
    OCI_MSG_PERSISTENT_OR_BUFFERED = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1684
try:
    OCI_MSG_BUFFERED = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1685
try:
    OCI_MSG_PERSISTENT = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1688
try:
    OCI_AQ_RESERVED_1 = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1689
try:
    OCI_AQ_RESERVED_2 = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1690
try:
    OCI_AQ_RESERVED_3 = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1691
try:
    OCI_AQ_RESERVED_4 = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1700
try:
    OCI_OTYPE_UNK = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1701
try:
    OCI_OTYPE_TABLE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1702
try:
    OCI_OTYPE_VIEW = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1703
try:
    OCI_OTYPE_SYN = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1704
try:
    OCI_OTYPE_PROC = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1705
try:
    OCI_OTYPE_FUNC = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1706
try:
    OCI_OTYPE_PKG = 6
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1707
try:
    OCI_OTYPE_STMT = 7
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1717
try:
    OCI_ATTR_DATA_SIZE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1718
try:
    OCI_ATTR_DATA_TYPE = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1719
try:
    OCI_ATTR_DISP_SIZE = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1720
try:
    OCI_ATTR_NAME = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1721
try:
    OCI_ATTR_PRECISION = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1722
try:
    OCI_ATTR_SCALE = 6
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1723
try:
    OCI_ATTR_IS_NULL = 7
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1724
try:
    OCI_ATTR_TYPE_NAME = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1726
try:
    OCI_ATTR_SCHEMA_NAME = 9
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1727
try:
    OCI_ATTR_SUB_NAME = 10
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1728
try:
    OCI_ATTR_POSITION = 11
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1731
try:
    OCI_ATTR_COMPLEXOBJECTCOMP_TYPE = 50
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1732
try:
    OCI_ATTR_COMPLEXOBJECTCOMP_TYPE_LEVEL = 51
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1733
try:
    OCI_ATTR_COMPLEXOBJECT_LEVEL = 52
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1734
try:
    OCI_ATTR_COMPLEXOBJECT_COLL_OUTOFLINE = 53
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1737
try:
    OCI_ATTR_DISP_NAME = 100
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1738
try:
    OCI_ATTR_ENCC_SIZE = 101
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1739
try:
    OCI_ATTR_COL_ENC = 102
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1740
try:
    OCI_ATTR_COL_ENC_SALT = 103
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1743
try:
    OCI_ATTR_OVERLOAD = 210
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1744
try:
    OCI_ATTR_LEVEL = 211
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1745
try:
    OCI_ATTR_HAS_DEFAULT = 212
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1746
try:
    OCI_ATTR_IOMODE = 213
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1747
try:
    OCI_ATTR_RADIX = 214
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1748
try:
    OCI_ATTR_NUM_ARGS = 215
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1751
try:
    OCI_ATTR_TYPECODE = 216
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1752
try:
    OCI_ATTR_COLLECTION_TYPECODE = 217
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1753
try:
    OCI_ATTR_VERSION = 218
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1754
try:
    OCI_ATTR_IS_INCOMPLETE_TYPE = 219
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1755
try:
    OCI_ATTR_IS_SYSTEM_TYPE = 220
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1756
try:
    OCI_ATTR_IS_PREDEFINED_TYPE = 221
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1757
try:
    OCI_ATTR_IS_TRANSIENT_TYPE = 222
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1758
try:
    OCI_ATTR_IS_SYSTEM_GENERATED_TYPE = 223
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1759
try:
    OCI_ATTR_HAS_NESTED_TABLE = 224
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1760
try:
    OCI_ATTR_HAS_LOB = 225
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1761
try:
    OCI_ATTR_HAS_FILE = 226
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1762
try:
    OCI_ATTR_COLLECTION_ELEMENT = 227
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1763
try:
    OCI_ATTR_NUM_TYPE_ATTRS = 228
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1764
try:
    OCI_ATTR_LIST_TYPE_ATTRS = 229
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1765
try:
    OCI_ATTR_NUM_TYPE_METHODS = 230
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1766
try:
    OCI_ATTR_LIST_TYPE_METHODS = 231
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1767
try:
    OCI_ATTR_MAP_METHOD = 232
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1768
try:
    OCI_ATTR_ORDER_METHOD = 233
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1771
try:
    OCI_ATTR_NUM_ELEMS = 234
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1774
try:
    OCI_ATTR_ENCAPSULATION = 235
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1775
try:
    OCI_ATTR_IS_SELFISH = 236
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1776
try:
    OCI_ATTR_IS_VIRTUAL = 237
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1777
try:
    OCI_ATTR_IS_INLINE = 238
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1778
try:
    OCI_ATTR_IS_CONSTANT = 239
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1779
try:
    OCI_ATTR_HAS_RESULT = 240
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1780
try:
    OCI_ATTR_IS_CONSTRUCTOR = 241
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1781
try:
    OCI_ATTR_IS_DESTRUCTOR = 242
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1782
try:
    OCI_ATTR_IS_OPERATOR = 243
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1783
try:
    OCI_ATTR_IS_MAP = 244
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1784
try:
    OCI_ATTR_IS_ORDER = 245
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1785
try:
    OCI_ATTR_IS_RNDS = 246
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1786
try:
    OCI_ATTR_IS_RNPS = 247
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1787
try:
    OCI_ATTR_IS_WNDS = 248
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1788
try:
    OCI_ATTR_IS_WNPS = 249
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1790
try:
    OCI_ATTR_DESC_PUBLIC = 250
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1793
try:
    OCI_ATTR_CACHE_CLIENT_CONTEXT = 251
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1794
try:
    OCI_ATTR_UCI_CONSTRUCT = 252
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1795
try:
    OCI_ATTR_UCI_DESTRUCT = 253
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1796
try:
    OCI_ATTR_UCI_COPY = 254
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1797
try:
    OCI_ATTR_UCI_PICKLE = 255
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1798
try:
    OCI_ATTR_UCI_UNPICKLE = 256
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1799
try:
    OCI_ATTR_UCI_REFRESH = 257
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1802
try:
    OCI_ATTR_IS_SUBTYPE = 258
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1803
try:
    OCI_ATTR_SUPERTYPE_SCHEMA_NAME = 259
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1804
try:
    OCI_ATTR_SUPERTYPE_NAME = 260
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1807
try:
    OCI_ATTR_LIST_OBJECTS = 261
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1810
try:
    OCI_ATTR_NCHARSET_ID = 262
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1811
try:
    OCI_ATTR_LIST_SCHEMAS = 263
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1812
try:
    OCI_ATTR_MAX_PROC_LEN = 264
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1813
try:
    OCI_ATTR_MAX_COLUMN_LEN = 265
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1814
try:
    OCI_ATTR_CURSOR_COMMIT_BEHAVIOR = 266
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1815
try:
    OCI_ATTR_MAX_CATALOG_NAMELEN = 267
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1816
try:
    OCI_ATTR_CATALOG_LOCATION = 268
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1817
try:
    OCI_ATTR_SAVEPOINT_SUPPORT = 269
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1818
try:
    OCI_ATTR_NOWAIT_SUPPORT = 270
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1819
try:
    OCI_ATTR_AUTOCOMMIT_DDL = 271
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1820
try:
    OCI_ATTR_LOCKING_MODE = 272
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1823
try:
    OCI_ATTR_APPCTX_SIZE = 273
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1824
try:
    OCI_ATTR_APPCTX_LIST = 274
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1825
try:
    OCI_ATTR_APPCTX_NAME = 275
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1826
try:
    OCI_ATTR_APPCTX_ATTR = 276
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1827
try:
    OCI_ATTR_APPCTX_VALUE = 277
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1830
try:
    OCI_ATTR_CLIENT_IDENTIFIER = 278
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1833
try:
    OCI_ATTR_IS_FINAL_TYPE = 279
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1834
try:
    OCI_ATTR_IS_INSTANTIABLE_TYPE = 280
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1835
try:
    OCI_ATTR_IS_FINAL_METHOD = 281
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1836
try:
    OCI_ATTR_IS_INSTANTIABLE_METHOD = 282
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1837
try:
    OCI_ATTR_IS_OVERRIDING_METHOD = 283
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1839
try:
    OCI_ATTR_DESC_SYNBASE = 284
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1842
try:
    OCI_ATTR_CHAR_USED = 285
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1843
try:
    OCI_ATTR_CHAR_SIZE = 286
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1846
try:
    OCI_ATTR_IS_JAVA_TYPE = 287
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1849
try:
    OCI_ATTR_DISTINGUISHED_NAME = 300
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1850
try:
    OCI_ATTR_KERBEROS_TICKET = 301
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1853
try:
    OCI_ATTR_ORA_DEBUG_JDWP = 302
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1855
try:
    OCI_ATTR_RESERVED_14 = 303
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1863
try:
    OCI_ATTR_SPOOL_TIMEOUT = 308
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1864
try:
    OCI_ATTR_SPOOL_GETMODE = 309
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1865
try:
    OCI_ATTR_SPOOL_BUSY_COUNT = 310
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1866
try:
    OCI_ATTR_SPOOL_OPEN_COUNT = 311
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1867
try:
    OCI_ATTR_SPOOL_MIN = 312
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1868
try:
    OCI_ATTR_SPOOL_MAX = 313
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1869
try:
    OCI_ATTR_SPOOL_INCR = 314
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1870
try:
    OCI_ATTR_SPOOL_STMTCACHESIZE = 208
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1874
try:
    OCI_ATTR_IS_XMLTYPE = 315
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1875
try:
    OCI_ATTR_XMLSCHEMA_NAME = 316
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1876
try:
    OCI_ATTR_XMLELEMENT_NAME = 317
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1877
try:
    OCI_ATTR_XMLSQLTYPSCH_NAME = 318
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1878
try:
    OCI_ATTR_XMLSQLTYPE_NAME = 319
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1879
try:
    OCI_ATTR_XMLTYPE_STORED_OBJ = 320
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1883
try:
    OCI_ATTR_HAS_SUBTYPES = 321
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1884
try:
    OCI_ATTR_NUM_SUBTYPES = 322
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1885
try:
    OCI_ATTR_LIST_SUBTYPES = 323
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1888
try:
    OCI_ATTR_XML_HRCHY_ENABLED = 324
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1891
try:
    OCI_ATTR_IS_OVERRIDDEN_METHOD = 325
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1896
try:
    OCI_ATTR_OBJ_SUBS = 336
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1901
try:
    OCI_ATTR_XADFIELD_RESERVED_1 = 339
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1902
try:
    OCI_ATTR_XADFIELD_RESERVED_2 = 340
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1904
try:
    OCI_ATTR_KERBEROS_CID = 341
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1908
try:
    OCI_ATTR_CONDITION = 342
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1909
try:
    OCI_ATTR_COMMENT = 343
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1910
try:
    OCI_ATTR_VALUE = 344
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1911
try:
    OCI_ATTR_EVAL_CONTEXT_OWNER = 345
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1912
try:
    OCI_ATTR_EVAL_CONTEXT_NAME = 346
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1913
try:
    OCI_ATTR_EVALUATION_FUNCTION = 347
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1914
try:
    OCI_ATTR_VAR_TYPE = 348
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1915
try:
    OCI_ATTR_VAR_VALUE_FUNCTION = 349
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1916
try:
    OCI_ATTR_VAR_METHOD_FUNCTION = 350
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1917
try:
    OCI_ATTR_ACTION_CONTEXT = 351
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1918
try:
    OCI_ATTR_LIST_TABLE_ALIASES = 352
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1919
try:
    OCI_ATTR_LIST_VARIABLE_TYPES = 353
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1920
try:
    OCI_ATTR_TABLE_NAME = 356
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1924
try:
    OCI_ATTR_MESSAGE_CSCN = 360
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1925
try:
    OCI_ATTR_MESSAGE_DSCN = 361
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1928
try:
    OCI_ATTR_AUDIT_SESSION_ID = 362
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1931
try:
    OCI_ATTR_KERBEROS_KEY = 363
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1932
try:
    OCI_ATTR_KERBEROS_CID_KEY = 364
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1935
try:
    OCI_ATTR_TRANSACTION_NO = 365
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1938
try:
    OCI_ATTR_MODULE = 366
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1939
try:
    OCI_ATTR_ACTION = 367
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1940
try:
    OCI_ATTR_CLIENT_INFO = 368
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1941
try:
    OCI_ATTR_COLLECT_CALL_TIME = 369
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1942
try:
    OCI_ATTR_CALL_TIME = 370
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1943
try:
    OCI_ATTR_ECONTEXT_ID = 371
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1944
try:
    OCI_ATTR_ECONTEXT_SEQ = 372
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1948
try:
    OCI_ATTR_SESSION_STATE = 373
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1949
try:
    OCI_SESSION_STATELESS = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1950
try:
    OCI_SESSION_STATEFUL = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1952
try:
    OCI_ATTR_SESSION_STATETYPE = 374
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1953
try:
    OCI_SESSION_STATELESS_DEF = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1954
try:
    OCI_SESSION_STATELESS_CAL = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1955
try:
    OCI_SESSION_STATELESS_TXN = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1956
try:
    OCI_SESSION_STATELESS_APP = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1958
try:
    OCI_ATTR_SESSION_STATE_CLEARED = 376
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1959
try:
    OCI_ATTR_SESSION_MIGRATED = 377
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1960
try:
    OCI_ATTR_SESSION_PRESERVE_STATE = 388
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1964
try:
    OCI_ATTR_ADMIN_PFILE = 389
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1969
try:
    OCI_ATTR_HOSTNAME = 390
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1970
try:
    OCI_ATTR_DBNAME = 391
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1971
try:
    OCI_ATTR_INSTNAME = 392
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1972
try:
    OCI_ATTR_SERVICENAME = 393
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1973
try:
    OCI_ATTR_INSTSTARTTIME = 394
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1974
try:
    OCI_ATTR_HA_TIMESTAMP = 395
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1975
try:
    OCI_ATTR_RESERVED_22 = 396
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1976
try:
    OCI_ATTR_RESERVED_23 = 397
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1977
try:
    OCI_ATTR_RESERVED_24 = 398
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1978
try:
    OCI_ATTR_DBDOMAIN = 399
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1980
try:
    OCI_ATTR_EVENTTYPE = 400
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1981
try:
    OCI_EVENTTYPE_HA = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1983
try:
    OCI_ATTR_HA_SOURCE = 401
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1985
try:
    OCI_HA_SOURCE_INSTANCE = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1986
try:
    OCI_HA_SOURCE_DATABASE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1987
try:
    OCI_HA_SOURCE_NODE = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1988
try:
    OCI_HA_SOURCE_SERVICE = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1989
try:
    OCI_HA_SOURCE_SERVICE_MEMBER = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1990
try:
    OCI_HA_SOURCE_ASM_INSTANCE = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1991
try:
    OCI_HA_SOURCE_SERVICE_PRECONNECT = 6
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1993
try:
    OCI_ATTR_HA_STATUS = 402
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1994
try:
    OCI_HA_STATUS_DOWN = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1995
try:
    OCI_HA_STATUS_UP = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1997
try:
    OCI_ATTR_HA_SRVFIRST = 403
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 1999
try:
    OCI_ATTR_HA_SRVNEXT = 404
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2002
try:
    OCI_ATTR_TAF_ENABLED = 405
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2005
try:
    OCI_ATTR_NFY_FLAGS = 406
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2007
try:
    OCI_ATTR_MSG_DELIVERY_MODE = 407
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2008
try:
    OCI_ATTR_DB_CHARSET_ID = 416
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2009
try:
    OCI_ATTR_DB_NCHARSET_ID = 417
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2010
try:
    OCI_ATTR_RESERVED_25 = 418
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2020
try:
    OCI_DIRPATH_STREAM_VERSION_1 = 100
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2021
try:
    OCI_DIRPATH_STREAM_VERSION_2 = 200
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2022
try:
    OCI_DIRPATH_STREAM_VERSION_3 = 300
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2025
try:
    OCI_ATTR_DIRPATH_MODE = 78
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2026
try:
    OCI_ATTR_DIRPATH_NOLOG = 79
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2027
try:
    OCI_ATTR_DIRPATH_PARALLEL = 80
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2029
try:
    OCI_ATTR_DIRPATH_SORTED_INDEX = 137
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2032
try:
    OCI_ATTR_DIRPATH_INDEX_MAINT_METHOD = 138
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2036
try:
    OCI_ATTR_DIRPATH_FILE = 139
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2037
try:
    OCI_ATTR_DIRPATH_STORAGE_INITIAL = 140
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2038
try:
    OCI_ATTR_DIRPATH_STORAGE_NEXT = 141
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2040
try:
    OCI_ATTR_DIRPATH_SKIPINDEX_METHOD = 145
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2043
try:
    OCI_ATTR_DIRPATH_EXPR_TYPE = 150
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2050
try:
    OCI_ATTR_DIRPATH_INPUT = 151
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2051
try:
    OCI_DIRPATH_INPUT_TEXT = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2052
try:
    OCI_DIRPATH_INPUT_STREAM = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2053
try:
    OCI_DIRPATH_INPUT_OCI = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2054
try:
    OCI_DIRPATH_INPUT_UNKNOWN = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2056
try:
    OCI_ATTR_DIRPATH_FN_CTX = 167
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2058
try:
    OCI_ATTR_DIRPATH_OID = 187
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2059
try:
    OCI_ATTR_DIRPATH_SID = 194
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2060
try:
    OCI_ATTR_DIRPATH_OBJ_CONSTR = 206
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2063
try:
    OCI_ATTR_DIRPATH_STREAM_VERSION = 212
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2065
try:
    OCIP_ATTR_DIRPATH_VARRAY_INDEX = 213
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2068
try:
    OCI_ATTR_DIRPATH_DCACHE_NUM = 303
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2069
try:
    OCI_ATTR_DIRPATH_DCACHE_SIZE = 304
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2070
try:
    OCI_ATTR_DIRPATH_DCACHE_MISSES = 305
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2071
try:
    OCI_ATTR_DIRPATH_DCACHE_HITS = 306
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2072
try:
    OCI_ATTR_DIRPATH_DCACHE_DISABLE = 307
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2079
try:
    OCI_ATTR_DIRPATH_RESERVED_7 = 326
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2080
try:
    OCI_ATTR_DIRPATH_RESERVED_8 = 327
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2081
try:
    OCI_ATTR_DIRPATH_CONVERT = 328
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2082
try:
    OCI_ATTR_DIRPATH_BADROW = 329
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2083
try:
    OCI_ATTR_DIRPATH_BADROW_LENGTH = 330
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2084
try:
    OCI_ATTR_DIRPATH_WRITE_ORDER = 331
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2085
try:
    OCI_ATTR_DIRPATH_GRANULE_SIZE = 332
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2086
try:
    OCI_ATTR_DIRPATH_GRANULE_OFFSET = 333
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2087
try:
    OCI_ATTR_DIRPATH_RESERVED_1 = 334
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2088
try:
    OCI_ATTR_DIRPATH_RESERVED_2 = 335
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2091
try:
    OCI_ATTR_DIRPATH_RESERVED_3 = 337
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2092
try:
    OCI_ATTR_DIRPATH_RESERVED_4 = 338
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2093
try:
    OCI_ATTR_DIRPATH_RESERVED_5 = 357
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2094
try:
    OCI_ATTR_DIRPATH_RESERVED_6 = 358
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2096
try:
    OCI_ATTR_DIRPATH_LOCK_WAIT = 359
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2098
try:
    OCI_ATTR_DIRPATH_RESERVED_9 = 2000
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2101
try:
    OCI_ATTR_DIRPATH_RESERVED_10 = 2001
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2102
try:
    OCI_ATTR_DIRPATH_RESERVED_11 = 2002
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2105
try:
    OCI_ATTR_CURRENT_ERRCOL = 2003
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2107
try:
    OCI_ATTR_DIRPATH_RESERVED_12 = 2004
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2112
try:
    OCI_ATTR_DIRPATH_RESERVED_17 = 2010
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2122
try:
    OCI_CURSOR_OPEN = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2123
try:
    OCI_CURSOR_CLOSED = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2126
try:
    OCI_CL_START = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2127
try:
    OCI_CL_END = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2130
try:
    OCI_SP_SUPPORTED = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2131
try:
    OCI_SP_UNSUPPORTED = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2134
try:
    OCI_NW_SUPPORTED = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2135
try:
    OCI_NW_UNSUPPORTED = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2138
try:
    OCI_AC_DDL = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2139
try:
    OCI_NO_AC_DDL = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2142
try:
    OCI_LOCK_IMMEDIATE = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2143
try:
    OCI_LOCK_DELAYED = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2146
try:
    OCI_INSTANCE_TYPE_UNKNOWN = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2147
try:
    OCI_INSTANCE_TYPE_RDBMS = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2148
try:
    OCI_INSTANCE_TYPE_OSM = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2153
try:
    OCI_AUTH = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2157
try:
    OCI_MAX_FNS = 100
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2158
try:
    OCI_SQLSTATE_SIZE = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2159
try:
    OCI_ERROR_MAXMSG_SIZE = 1024
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2160
try:
    OCI_LOBMAXSIZE = MINUB4MAXVAL
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2161
try:
    OCI_ROWID_LEN = 23
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2165
try:
    OCI_FO_END = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2166
try:
    OCI_FO_ABORT = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2167
try:
    OCI_FO_REAUTH = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2168
try:
    OCI_FO_BEGIN = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2169
try:
    OCI_FO_ERROR = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2173
try:
    OCI_FO_RETRY = 25410
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2177
try:
    OCI_FO_NONE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2178
try:
    OCI_FO_SESSION = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2179
try:
    OCI_FO_SELECT = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2180
try:
    OCI_FO_TXNAL = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2184
try:
    OCI_FNCODE_INITIALIZE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2185
try:
    OCI_FNCODE_HANDLEALLOC = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2186
try:
    OCI_FNCODE_HANDLEFREE = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2187
try:
    OCI_FNCODE_DESCRIPTORALLOC = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2188
try:
    OCI_FNCODE_DESCRIPTORFREE = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2189
try:
    OCI_FNCODE_ENVINIT = 6
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2190
try:
    OCI_FNCODE_SERVERATTACH = 7
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2191
try:
    OCI_FNCODE_SERVERDETACH = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2193
try:
    OCI_FNCODE_SESSIONBEGIN = 10
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2194
try:
    OCI_FNCODE_SESSIONEND = 11
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2195
try:
    OCI_FNCODE_PASSWORDCHANGE = 12
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2196
try:
    OCI_FNCODE_STMTPREPARE = 13
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2198
try:
    OCI_FNCODE_BINDDYNAMIC = 17
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2199
try:
    OCI_FNCODE_BINDOBJECT = 18
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2201
try:
    OCI_FNCODE_BINDARRAYOFSTRUCT = 20
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2202
try:
    OCI_FNCODE_STMTEXECUTE = 21
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2204
try:
    OCI_FNCODE_DEFINEOBJECT = 25
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2205
try:
    OCI_FNCODE_DEFINEDYNAMIC = 26
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2206
try:
    OCI_FNCODE_DEFINEARRAYOFSTRUCT = 27
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2207
try:
    OCI_FNCODE_STMTFETCH = 28
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2208
try:
    OCI_FNCODE_STMTGETBIND = 29
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2210
try:
    OCI_FNCODE_DESCRIBEANY = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2211
try:
    OCI_FNCODE_TRANSSTART = 33
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2212
try:
    OCI_FNCODE_TRANSDETACH = 34
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2213
try:
    OCI_FNCODE_TRANSCOMMIT = 35
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2215
try:
    OCI_FNCODE_ERRORGET = 37
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2216
try:
    OCI_FNCODE_LOBOPENFILE = 38
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2217
try:
    OCI_FNCODE_LOBCLOSEFILE = 39
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2220
try:
    OCI_FNCODE_LOBCOPY = 42
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2221
try:
    OCI_FNCODE_LOBAPPEND = 43
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2222
try:
    OCI_FNCODE_LOBERASE = 44
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2223
try:
    OCI_FNCODE_LOBLENGTH = 45
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2224
try:
    OCI_FNCODE_LOBTRIM = 46
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2225
try:
    OCI_FNCODE_LOBREAD = 47
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2226
try:
    OCI_FNCODE_LOBWRITE = 48
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2228
try:
    OCI_FNCODE_SVCCTXBREAK = 50
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2229
try:
    OCI_FNCODE_SERVERVERSION = 51
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2231
try:
    OCI_FNCODE_KERBATTRSET = 52
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2235
try:
    OCI_FNCODE_ATTRGET = 54
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2236
try:
    OCI_FNCODE_ATTRSET = 55
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2237
try:
    OCI_FNCODE_PARAMSET = 56
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2238
try:
    OCI_FNCODE_PARAMGET = 57
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2239
try:
    OCI_FNCODE_STMTGETPIECEINFO = 58
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2240
try:
    OCI_FNCODE_LDATOSVCCTX = 59
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2242
try:
    OCI_FNCODE_STMTSETPIECEINFO = 61
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2243
try:
    OCI_FNCODE_TRANSFORGET = 62
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2244
try:
    OCI_FNCODE_TRANSPREPARE = 63
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2245
try:
    OCI_FNCODE_TRANSROLLBACK = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2246
try:
    OCI_FNCODE_DEFINEBYPOS = 65
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2247
try:
    OCI_FNCODE_BINDBYPOS = 66
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2248
try:
    OCI_FNCODE_BINDBYNAME = 67
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2249
try:
    OCI_FNCODE_LOBASSIGN = 68
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2250
try:
    OCI_FNCODE_LOBISEQUAL = 69
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2251
try:
    OCI_FNCODE_LOBISINIT = 70
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2253
try:
    OCI_FNCODE_LOBENABLEBUFFERING = 71
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2254
try:
    OCI_FNCODE_LOBCHARSETID = 72
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2255
try:
    OCI_FNCODE_LOBCHARSETFORM = 73
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2256
try:
    OCI_FNCODE_LOBFILESETNAME = 74
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2257
try:
    OCI_FNCODE_LOBFILEGETNAME = 75
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2258
try:
    OCI_FNCODE_LOGON = 76
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2259
try:
    OCI_FNCODE_LOGOFF = 77
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2260
try:
    OCI_FNCODE_LOBDISABLEBUFFERING = 78
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2261
try:
    OCI_FNCODE_LOBFLUSHBUFFER = 79
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2262
try:
    OCI_FNCODE_LOBLOADFROMFILE = 80
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2264
try:
    OCI_FNCODE_LOBOPEN = 81
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2265
try:
    OCI_FNCODE_LOBCLOSE = 82
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2266
try:
    OCI_FNCODE_LOBISOPEN = 83
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2267
try:
    OCI_FNCODE_LOBFILEISOPEN = 84
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2268
try:
    OCI_FNCODE_LOBFILEEXISTS = 85
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2269
try:
    OCI_FNCODE_LOBFILECLOSEALL = 86
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2270
try:
    OCI_FNCODE_LOBCREATETEMP = 87
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2271
try:
    OCI_FNCODE_LOBFREETEMP = 88
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2272
try:
    OCI_FNCODE_LOBISTEMP = 89
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2274
try:
    OCI_FNCODE_AQENQ = 90
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2275
try:
    OCI_FNCODE_AQDEQ = 91
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2276
try:
    OCI_FNCODE_RESET = 92
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2277
try:
    OCI_FNCODE_SVCCTXTOLDA = 93
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2278
try:
    OCI_FNCODE_LOBLOCATORASSIGN = 94
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2280
try:
    OCI_FNCODE_UBINDBYNAME = 95
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2282
try:
    OCI_FNCODE_AQLISTEN = 96
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2284
try:
    OCI_FNCODE_SVC2HST = 97
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2285
try:
    OCI_FNCODE_SVCRH = 98
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2288
try:
    OCI_FNCODE_TRANSMULTIPREPARE = 99
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2290
try:
    OCI_FNCODE_CPOOLCREATE = 100
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2291
try:
    OCI_FNCODE_CPOOLDESTROY = 101
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2292
try:
    OCI_FNCODE_LOGON2 = 102
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2293
try:
    OCI_FNCODE_ROWIDTOCHAR = 103
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2295
try:
    OCI_FNCODE_SPOOLCREATE = 104
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2296
try:
    OCI_FNCODE_SPOOLDESTROY = 105
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2297
try:
    OCI_FNCODE_SESSIONGET = 106
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2298
try:
    OCI_FNCODE_SESSIONRELEASE = 107
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2299
try:
    OCI_FNCODE_STMTPREPARE2 = 108
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2300
try:
    OCI_FNCODE_STMTRELEASE = 109
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2301
try:
    OCI_FNCODE_AQENQARRAY = 110
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2302
try:
    OCI_FNCODE_AQDEQARRAY = 111
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2303
try:
    OCI_FNCODE_LOBCOPY2 = 112
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2304
try:
    OCI_FNCODE_LOBERASE2 = 113
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2305
try:
    OCI_FNCODE_LOBLENGTH2 = 114
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2306
try:
    OCI_FNCODE_LOBLOADFROMFILE2 = 115
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2307
try:
    OCI_FNCODE_LOBREAD2 = 116
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2308
try:
    OCI_FNCODE_LOBTRIM2 = 117
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2309
try:
    OCI_FNCODE_LOBWRITE2 = 118
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2310
try:
    OCI_FNCODE_LOBGETSTORAGELIMIT = 119
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2311
try:
    OCI_FNCODE_DBSTARTUP = 120
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2312
try:
    OCI_FNCODE_DBSHUTDOWN = 121
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2313
try:
    OCI_FNCODE_LOBARRAYREAD = 122
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2314
try:
    OCI_FNCODE_LOBARRAYWRITE = 123
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2316
try:
    OCI_FNCODE_MAXFCN = 123
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2319
try:
    OCI_CBK_STMTCACHE_STMTPURGE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2378
try:
    OCI_INTHR_UNK = 24
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2381
try:
    OCI_ADJUST_UNK = 10
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2382
try:
    OCI_ORACLE_DATE = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2383
try:
    OCI_ANSI_DATE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2446
try:
    OCI_FILE_READONLY = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2449
try:
    OCI_LOB_READONLY = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2450
try:
    OCI_LOB_READWRITE = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2453
try:
    OCI_LOB_BUFFER_FREE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2454
try:
    OCI_LOB_BUFFER_NOFREE = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2459
try:
    OCI_STMT_SELECT = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2460
try:
    OCI_STMT_UPDATE = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2461
try:
    OCI_STMT_DELETE = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2462
try:
    OCI_STMT_INSERT = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2463
try:
    OCI_STMT_CREATE = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2464
try:
    OCI_STMT_DROP = 6
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2465
try:
    OCI_STMT_ALTER = 7
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2466
try:
    OCI_STMT_BEGIN = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2467
try:
    OCI_STMT_DECLARE = 9
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2471
try:
    OCI_PTYPE_UNK = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2472
try:
    OCI_PTYPE_TABLE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2473
try:
    OCI_PTYPE_VIEW = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2474
try:
    OCI_PTYPE_PROC = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2475
try:
    OCI_PTYPE_FUNC = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2476
try:
    OCI_PTYPE_PKG = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2477
try:
    OCI_PTYPE_TYPE = 6
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2478
try:
    OCI_PTYPE_SYN = 7
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2479
try:
    OCI_PTYPE_SEQ = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2480
try:
    OCI_PTYPE_COL = 9
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2481
try:
    OCI_PTYPE_ARG = 10
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2482
try:
    OCI_PTYPE_LIST = 11
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2483
try:
    OCI_PTYPE_TYPE_ATTR = 12
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2484
try:
    OCI_PTYPE_TYPE_COLL = 13
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2485
try:
    OCI_PTYPE_TYPE_METHOD = 14
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2486
try:
    OCI_PTYPE_TYPE_ARG = 15
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2487
try:
    OCI_PTYPE_TYPE_RESULT = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2488
try:
    OCI_PTYPE_SCHEMA = 17
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2489
try:
    OCI_PTYPE_DATABASE = 18
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2490
try:
    OCI_PTYPE_RULE = 19
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2491
try:
    OCI_PTYPE_RULE_SET = 20
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2492
try:
    OCI_PTYPE_EVALUATION_CONTEXT = 21
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2493
try:
    OCI_PTYPE_TABLE_ALIAS = 22
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2494
try:
    OCI_PTYPE_VARIABLE_TYPE = 23
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2495
try:
    OCI_PTYPE_NAME_VALUE = 24
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2500
try:
    OCI_LTYPE_UNK = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2501
try:
    OCI_LTYPE_COLUMN = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2502
try:
    OCI_LTYPE_ARG_PROC = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2503
try:
    OCI_LTYPE_ARG_FUNC = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2504
try:
    OCI_LTYPE_SUBPRG = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2505
try:
    OCI_LTYPE_TYPE_ATTR = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2506
try:
    OCI_LTYPE_TYPE_METHOD = 6
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2507
try:
    OCI_LTYPE_TYPE_ARG_PROC = 7
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2508
try:
    OCI_LTYPE_TYPE_ARG_FUNC = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2509
try:
    OCI_LTYPE_SCH_OBJ = 9
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2510
try:
    OCI_LTYPE_DB_SCH = 10
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2511
try:
    OCI_LTYPE_TYPE_SUBTYPE = 11
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2512
try:
    OCI_LTYPE_TABLE_ALIAS = 12
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2513
try:
    OCI_LTYPE_VARIABLE_TYPE = 13
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2514
try:
    OCI_LTYPE_NAME_VALUE = 14
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2519
try:
    OCI_MEMORY_CLEARED = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2536
try:
    OCI_UCBTYPE_ENTRY = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2537
try:
    OCI_UCBTYPE_EXIT = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2538
try:
    OCI_UCBTYPE_REPLACE = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2543
try:
    OCI_NLS_DAYNAME1 = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2544
try:
    OCI_NLS_DAYNAME2 = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2545
try:
    OCI_NLS_DAYNAME3 = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2546
try:
    OCI_NLS_DAYNAME4 = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2547
try:
    OCI_NLS_DAYNAME5 = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2548
try:
    OCI_NLS_DAYNAME6 = 6
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2549
try:
    OCI_NLS_DAYNAME7 = 7
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2550
try:
    OCI_NLS_ABDAYNAME1 = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2551
try:
    OCI_NLS_ABDAYNAME2 = 9
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2552
try:
    OCI_NLS_ABDAYNAME3 = 10
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2553
try:
    OCI_NLS_ABDAYNAME4 = 11
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2554
try:
    OCI_NLS_ABDAYNAME5 = 12
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2555
try:
    OCI_NLS_ABDAYNAME6 = 13
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2556
try:
    OCI_NLS_ABDAYNAME7 = 14
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2557
try:
    OCI_NLS_MONTHNAME1 = 15
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2558
try:
    OCI_NLS_MONTHNAME2 = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2559
try:
    OCI_NLS_MONTHNAME3 = 17
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2560
try:
    OCI_NLS_MONTHNAME4 = 18
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2561
try:
    OCI_NLS_MONTHNAME5 = 19
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2562
try:
    OCI_NLS_MONTHNAME6 = 20
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2563
try:
    OCI_NLS_MONTHNAME7 = 21
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2564
try:
    OCI_NLS_MONTHNAME8 = 22
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2565
try:
    OCI_NLS_MONTHNAME9 = 23
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2566
try:
    OCI_NLS_MONTHNAME10 = 24
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2567
try:
    OCI_NLS_MONTHNAME11 = 25
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2568
try:
    OCI_NLS_MONTHNAME12 = 26
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2569
try:
    OCI_NLS_ABMONTHNAME1 = 27
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2570
try:
    OCI_NLS_ABMONTHNAME2 = 28
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2571
try:
    OCI_NLS_ABMONTHNAME3 = 29
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2572
try:
    OCI_NLS_ABMONTHNAME4 = 30
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2573
try:
    OCI_NLS_ABMONTHNAME5 = 31
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2574
try:
    OCI_NLS_ABMONTHNAME6 = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2575
try:
    OCI_NLS_ABMONTHNAME7 = 33
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2576
try:
    OCI_NLS_ABMONTHNAME8 = 34
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2577
try:
    OCI_NLS_ABMONTHNAME9 = 35
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2578
try:
    OCI_NLS_ABMONTHNAME10 = 36
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2579
try:
    OCI_NLS_ABMONTHNAME11 = 37
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2580
try:
    OCI_NLS_ABMONTHNAME12 = 38
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2581
try:
    OCI_NLS_YES = 39
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2582
try:
    OCI_NLS_NO = 40
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2583
try:
    OCI_NLS_AM = 41
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2584
try:
    OCI_NLS_PM = 42
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2585
try:
    OCI_NLS_AD = 43
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2586
try:
    OCI_NLS_BC = 44
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2587
try:
    OCI_NLS_DECIMAL = 45
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2588
try:
    OCI_NLS_GROUP = 46
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2589
try:
    OCI_NLS_DEBIT = 47
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2590
try:
    OCI_NLS_CREDIT = 48
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2591
try:
    OCI_NLS_DATEFORMAT = 49
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2592
try:
    OCI_NLS_INT_CURRENCY = 50
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2593
try:
    OCI_NLS_LOC_CURRENCY = 51
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2594
try:
    OCI_NLS_LANGUAGE = 52
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2595
try:
    OCI_NLS_ABLANGUAGE = 53
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2596
try:
    OCI_NLS_TERRITORY = 54
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2597
try:
    OCI_NLS_CHARACTER_SET = 55
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2598
try:
    OCI_NLS_LINGUISTIC_NAME = 56
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2599
try:
    OCI_NLS_CALENDAR = 57
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2600
try:
    OCI_NLS_DUAL_CURRENCY = 78
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2601
try:
    OCI_NLS_WRITINGDIR = 79
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2602
try:
    OCI_NLS_ABTERRITORY = 80
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2603
try:
    OCI_NLS_DDATEFORMAT = 81
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2604
try:
    OCI_NLS_DTIMEFORMAT = 82
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2605
try:
    OCI_NLS_SFDATEFORMAT = 83
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2606
try:
    OCI_NLS_SFTIMEFORMAT = 84
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2607
try:
    OCI_NLS_NUMGROUPING = 85
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2608
try:
    OCI_NLS_LISTSEP = 86
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2609
try:
    OCI_NLS_MONDECIMAL = 87
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2610
try:
    OCI_NLS_MONGROUP = 88
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2611
try:
    OCI_NLS_MONGROUPING = 89
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2612
try:
    OCI_NLS_INT_CURRENCYSEP = 90
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2613
try:
    OCI_NLS_CHARSET_MAXBYTESZ = 91
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2614
try:
    OCI_NLS_CHARSET_FIXEDWIDTH = 92
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2615
try:
    OCI_NLS_CHARSET_ID = 93
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2616
try:
    OCI_NLS_NCHARSET_ID = 94
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2618
try:
    OCI_NLS_MAXBUFSZ = 100
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2620
try:
    OCI_NLS_BINARY = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2621
try:
    OCI_NLS_LINGUISTIC = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2622
try:
    OCI_NLS_CASE_INSENSITIVE = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2624
try:
    OCI_NLS_UPPERCASE = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2625
try:
    OCI_NLS_LOWERCASE = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2627
try:
    OCI_NLS_CS_IANA_TO_ORA = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2628
try:
    OCI_NLS_CS_ORA_TO_IANA = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2629
try:
    OCI_NLS_LANG_ISO_TO_ORA = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2630
try:
    OCI_NLS_LANG_ORA_TO_ISO = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2631
try:
    OCI_NLS_TERR_ISO_TO_ORA = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2632
try:
    OCI_NLS_TERR_ORA_TO_ISO = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2633
try:
    OCI_NLS_TERR_ISO3_TO_ORA = 6
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2635
try:
    OCI_NLS_TERR_ORA_TO_ISO3 = 7
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2641
try:
    OCI_XMLTYPE_CREATE_OCISTRING = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2642
try:
    OCI_XMLTYPE_CREATE_CLOB = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2643
try:
    OCI_XMLTYPE_CREATE_BLOB = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2646
try:
    OCI_KERBCRED_PROXY = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2647
try:
    OCI_KERBCRED_CLIENT_IDENTIFIER = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2650
try:
    OCI_DBSTARTUPFLAG_FORCE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2651
try:
    OCI_DBSTARTUPFLAG_RESTRICT = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2654
try:
    OCI_DBSHUTDOWN_TRANSACTIONAL = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2655
try:
    OCI_DBSHUTDOWN_TRANSACTIONAL_LOCAL = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2656
try:
    OCI_DBSHUTDOWN_IMMEDIATE = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2657
try:
    OCI_DBSHUTDOWN_ABORT = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2658
try:
    OCI_DBSHUTDOWN_FINAL = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2661
try:
    OCI_MAJOR_VERSION = 10
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2662
try:
    OCI_MINOR_VERSION = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 296
try:
    OCI_IND_NOTNULL = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 297
try:
    OCI_IND_NULL = (-1)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 298
try:
    OCI_IND_BADNULL = (-2)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 299
try:
    OCI_IND_NOTNULLABLE = (-3)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 306
try:
    OCI_ATTR_OBJECT_DETECTCHANGE = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 312
try:
    OCI_ATTR_OBJECT_NEWNOTNULL = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 318
try:
    OCI_ATTR_CACHE_ARRAYFLUSH = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 405
try:
    OCI_DURATION_INVALID = 65535
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 406
try:
    OCI_DURATION_BEGIN = 10
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 408
try:
    OCI_DURATION_NULL = (OCI_DURATION_BEGIN - 1)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 410
try:
    OCI_DURATION_DEFAULT = (OCI_DURATION_BEGIN - 2)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 411
try:
    OCI_DURATION_USER_CALLBACK = (OCI_DURATION_BEGIN - 3)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 412
try:
    OCI_DURATION_NEXT = (OCI_DURATION_BEGIN - 4)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 414
try:
    OCI_DURATION_SESSION = OCI_DURATION_BEGIN
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 416
try:
    OCI_DURATION_TRANS = (OCI_DURATION_BEGIN + 1)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 422
try:
    OCI_DURATION_CALL = (OCI_DURATION_BEGIN + 2)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 424
try:
    OCI_DURATION_STATEMENT = (OCI_DURATION_BEGIN + 3)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 429
try:
    OCI_DURATION_CALLOUT = (OCI_DURATION_BEGIN + 4)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 431
try:
    OCI_DURATION_LAST = OCI_DURATION_CALLOUT
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 439
try:
    OCI_DURATION_PROCESS = (OCI_DURATION_BEGIN - 5)
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 525
try:
    OCI_OBJECTCOPY_NOREF = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 534
try:
    OCI_OBJECTFREE_FORCE = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 535
try:
    OCI_OBJECTFREE_NONULL = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 536
try:
    OCI_OBJECTFREE_HEADER = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 549
try:
    OCI_OBJECTPROP_LIFETIME = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 550
try:
    OCI_OBJECTPROP_SCHEMA = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 551
try:
    OCI_OBJECTPROP_TABLE = 3
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 552
try:
    OCI_OBJECTPROP_PIN_DURATION = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 553
try:
    OCI_OBJECTPROP_ALLOC_DURATION = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 554
try:
    OCI_OBJECTPROP_LOCK = 6
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 555
try:
    OCI_OBJECTPROP_MARKSTATUS = 7
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 556
try:
    OCI_OBJECTPROP_VIEW = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 582
try:
    OCI_OBJECT_NEW = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 583
try:
    OCI_OBJECT_DELETED = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 584
try:
    OCI_OBJECT_UPDATED = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 616
try:
    OCI_TYPECODE_REF = SQLT_REF
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 617
try:
    OCI_TYPECODE_DATE = SQLT_DAT
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 618
try:
    OCI_TYPECODE_SIGNED8 = 27
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 619
try:
    OCI_TYPECODE_SIGNED16 = 28
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 620
try:
    OCI_TYPECODE_SIGNED32 = 29
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 621
try:
    OCI_TYPECODE_REAL = 21
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 622
try:
    OCI_TYPECODE_DOUBLE = 22
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 623
try:
    OCI_TYPECODE_BFLOAT = SQLT_IBFLOAT
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 624
try:
    OCI_TYPECODE_BDOUBLE = SQLT_IBDOUBLE
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 625
try:
    OCI_TYPECODE_FLOAT = SQLT_FLT
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 626
try:
    OCI_TYPECODE_NUMBER = SQLT_NUM
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 627
try:
    OCI_TYPECODE_DECIMAL = SQLT_PDN
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 629
try:
    OCI_TYPECODE_UNSIGNED8 = SQLT_BIN
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 631
try:
    OCI_TYPECODE_UNSIGNED16 = 25
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 632
try:
    OCI_TYPECODE_UNSIGNED32 = 26
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 633
try:
    OCI_TYPECODE_OCTET = 245
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 634
try:
    OCI_TYPECODE_SMALLINT = 246
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 635
try:
    OCI_TYPECODE_INTEGER = SQLT_INT
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 636
try:
    OCI_TYPECODE_RAW = SQLT_LVB
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 637
try:
    OCI_TYPECODE_PTR = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 638
try:
    OCI_TYPECODE_VARCHAR2 = SQLT_VCS
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 640
try:
    OCI_TYPECODE_CHAR = SQLT_AFC
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 641
try:
    OCI_TYPECODE_VARCHAR = SQLT_CHR
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 643
try:
    OCI_TYPECODE_MLSLABEL = SQLT_LAB
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 644
try:
    OCI_TYPECODE_VARRAY = 247
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 645
try:
    OCI_TYPECODE_TABLE = 248
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 646
try:
    OCI_TYPECODE_OBJECT = SQLT_NTY
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 647
try:
    OCI_TYPECODE_OPAQUE = 58
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 648
try:
    OCI_TYPECODE_NAMEDCOLLECTION = SQLT_NCO
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 650
try:
    OCI_TYPECODE_BLOB = SQLT_BLOB
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 651
try:
    OCI_TYPECODE_BFILE = SQLT_BFILE
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 652
try:
    OCI_TYPECODE_CLOB = SQLT_CLOB
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 653
try:
    OCI_TYPECODE_CFILE = SQLT_CFILE
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 656
try:
    OCI_TYPECODE_TIME = SQLT_TIME
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 657
try:
    OCI_TYPECODE_TIME_TZ = SQLT_TIME_TZ
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 658
try:
    OCI_TYPECODE_TIMESTAMP = SQLT_TIMESTAMP
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 659
try:
    OCI_TYPECODE_TIMESTAMP_TZ = SQLT_TIMESTAMP_TZ
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 661
try:
    OCI_TYPECODE_TIMESTAMP_LTZ = SQLT_TIMESTAMP_LTZ
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 663
try:
    OCI_TYPECODE_INTERVAL_YM = SQLT_INTERVAL_YM
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 664
try:
    OCI_TYPECODE_INTERVAL_DS = SQLT_INTERVAL_DS
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 665
try:
    OCI_TYPECODE_UROWID = SQLT_RDD
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 668
try:
    OCI_TYPECODE_OTMFIRST = 228
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 669
try:
    OCI_TYPECODE_OTMLAST = 320
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 670
try:
    OCI_TYPECODE_SYSFIRST = 228
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 671
try:
    OCI_TYPECODE_SYSLAST = 235
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 672
try:
    OCI_TYPECODE_PLS_INTEGER = 266
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 682
try:
    OCI_TYPECODE_NCHAR = 286
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 683
try:
    OCI_TYPECODE_NVARCHAR2 = 287
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 684
try:
    OCI_TYPECODE_NCLOB = 288
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 688
try:
    OCI_TYPECODE_NONE = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 691
try:
    OCI_TYPECODE_ERRHP = 283
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 859
try:
    OCI_NUMBER_DEFAULTPREC = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 860
try:
    OCI_NUMBER_DEFAULTSCALE = MAXSB1MINVAL
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 865
try:
    OCI_VARRAY_MAXSIZE = 4000
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 867
try:
    OCI_STRING_MAXLEN = 4000
except:
    pass

OCICoherency = OCIRefreshOpt # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 877

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 878
try:
    OCI_COHERENCY_NONE = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 879
try:
    OCI_COHERENCY_NULL = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 880
try:
    OCI_COHERENCY_ALWAYS = 5
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2582
try:
    OCI_TYPEELEM_REF = 32768
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2583
try:
    OCI_TYPEPARAM_REQUIRED = 2048
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2586
def OCI_TYPEELEM_IS_REF(elem_flag):
    return ((elem_flag & OCI_TYPEELEM_REF) != 0)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 2588
def OCI_TYPEPARAM_IS_REQUIRED(param_flag):
    return ((param_flag & OCI_TYPEPARAM_REQUIRED) != 0)

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 478
try:
    OCI_NUMBER_SIZE = 22
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 939
try:
    OCI_NUMBER_UNSIGNED = 0
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 940
try:
    OCI_NUMBER_SIGNED = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2167
try:
    OCI_DATE_INVALID_DAY = 1
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2168
try:
    OCI_DATE_DAY_BELOW_VALID = 2
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2169
try:
    OCI_DATE_INVALID_MONTH = 4
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2170
try:
    OCI_DATE_MONTH_BELOW_VALID = 8
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2171
try:
    OCI_DATE_INVALID_YEAR = 16
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2172
try:
    OCI_DATE_YEAR_BELOW_VALID = 32
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2173
try:
    OCI_DATE_INVALID_HOUR = 64
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2174
try:
    OCI_DATE_HOUR_BELOW_VALID = 128
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2175
try:
    OCI_DATE_INVALID_MINUTE = 256
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2176
try:
    OCI_DATE_MINUTE_BELOW_VALID = 512
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2178
try:
    OCI_DATE_INVALID_SECOND = 1024
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2179
try:
    OCI_DATE_SECOND_BELOW_VALID = 2048
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2181
try:
    OCI_DATE_DAY_MISSING_FROM_1582 = 4096
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2183
try:
    OCI_DATE_YEAR_ZERO = 8192
except:
    pass

# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2184
try:
    OCI_DATE_INVALID_FORMAT = 32768
except:
    pass

cda_head = struct_cda_head # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 82

cda_def = struct_cda_def # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ocidfn.h: 126

OCIEnv = struct_OCIEnv # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2324

OCIError = struct_OCIError # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2325

OCISvcCtx = struct_OCISvcCtx # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2326

OCIStmt = struct_OCIStmt # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2327

OCIBind = struct_OCIBind # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2328

OCIDefine = struct_OCIDefine # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2329

OCIDescribe = struct_OCIDescribe # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2330

OCIServer = struct_OCIServer # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2331

OCISession = struct_OCISession # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2332

OCIComplexObject = struct_OCIComplexObject # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2333

OCITrans = struct_OCITrans # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2334

OCISecurity = struct_OCISecurity # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2335

OCISubscription = struct_OCISubscription # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2336

OCICPool = struct_OCICPool # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2338

OCISPool = struct_OCISPool # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2339

OCIAuthInfo = struct_OCIAuthInfo # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2340

OCIAdmin = struct_OCIAdmin # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2341

OCIEvent = struct_OCIEvent # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2342

OCISnapshot = struct_OCISnapshot # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2345

OCIResult = struct_OCIResult # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2346

OCILobLocator = struct_OCILobLocator # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2347

OCIParam = struct_OCIParam # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2348

OCIComplexObjectComp = struct_OCIComplexObjectComp # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2349

OCIRowid = struct_OCIRowid # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2351

OCIDateTime = struct_OCIDateTime # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2353

OCIInterval = struct_OCIInterval # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2354

OCIUcb = struct_OCIUcb # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2356

OCIServerDNs = struct_OCIServerDNs # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2357

OCIAQEnqOptions = struct_OCIAQEnqOptions # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2360

OCIAQDeqOptions = struct_OCIAQDeqOptions # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2361

OCIAQMsgProperties = struct_OCIAQMsgProperties # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2362

OCIAQAgent = struct_OCIAQAgent # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2363

OCIAQNfyDescriptor = struct_OCIAQNfyDescriptor # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2364

OCIAQSignature = struct_OCIAQSignature # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2365

OCIAQListenOpts = struct_OCIAQListenOpts # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2366

OCIAQLisMsgProps = struct_OCIAQLisMsgProps # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2367

OCIPicklerTdsCtx = struct_OCIPicklerTdsCtx # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2522

OCIPicklerTds = struct_OCIPicklerTds # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2523

OCIPicklerImage = struct_OCIPicklerImage # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2524

OCIPicklerFdo = struct_OCIPicklerFdo # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2525

OCIAnyData = struct_OCIAnyData # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2528

OCIAnyDataSet = struct_OCIAnyDataSet # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2530

OCIAnyDataCtx = struct_OCIAnyDataCtx # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2531

OCIMsg = struct_OCIMsg # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oci.h: 2638

OCIRef = struct_OCIRef # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/oro.h: 278

OCIType = struct_OCIType # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 694

OCITypeElem = struct_OCITypeElem # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 714

OCITypeMethod = struct_OCITypeMethod # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 731

OCITypeIter = struct_OCITypeIter # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/ort.h: 746

OCINumber = struct_OCINumber # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 479

OCITime = struct_OCITime # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1695

OCIDate = struct_OCIDate # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 1711

OCIString = struct_OCIString # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2276

OCIRaw = struct_OCIRaw # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2436

OCIColl = struct_OCIColl # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2807

OCIIter = struct_OCIIter # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 2816

OCIXMLType = struct_OCIXMLType # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3623

OCIDOMDocument = struct_OCIDOMDocument # /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_10_2/sdk/include/orl.h: 3626

# No inserted files

