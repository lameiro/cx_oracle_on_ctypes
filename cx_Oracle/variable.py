from ctypes import byref
import ctypes
import sys

from utils import python3_or_better
from custom_exceptions import NotSupportedError, DatabaseError
from error import Error
from buffer import cxBuffer

import oci

class Variable(object):
    def __init__(self, cursor, num_elements, type, size):
        self.environment = cursor.connection.environment

        self.bind_handle = oci.POINTER(oci.OCIBind)()
        self.define_handle = oci.POINTER(oci.OCIDefine)()
        self.bound_cursor_handle = oci.POINTER(oci.OCIStmt)()
        self.bound_name = None
        self.inconverter = None # public
        self.outconverter = None  # public
        self.bound_pos = 0

        if num_elements < 1:
            self.numElements = self.allocelems = 1
        else:
            self.numElements = self.allocelems = num_elements
        
        # the OCI will keep a ref to this across multiple calls, so we have to keep one too.
        # to avoid duplication of python-level vs c-level fields, self.actual_elements is a property
        self.c_actual_elements = oci.ub4(0)
        self.internal_fetch_num = 0
        self.is_array = False
        self.is_allocated_internally = True
        self.type = type
        self.actual_length = oci.POINTER(oci.ub2)()
        self.return_code = oci.POINTER(oci.ub2)()

        # set the maximum length of the variable, ensure that a minimum of
        # 2 bytes is allocated to ensure that the array size check works
        self.size = type.size
        if type.is_variable_length:
            if size < ctypes.sizeof(oci.ub2):
                size = ctypes.sizeof(oci.ub2)
            self.size = size

        # allocate the data for the variable
        self.allocate_data()

        # allocate the indicator for the variable
        self.indicator = (self.numElements * oci.sb2)()

        # ensure that all variable values start out NULL
        for i in xrange(self.numElements):
            self.indicator[i] = oci.OCI_IND_NULL

        # for variable length data, also allocate the return code
        if type.is_variable_length:
            self.return_code = (self.numElements * oci.ub2)()

        # perform extended initialization
        if self.type.initialize_proc:
            self.type.initialize_proc(self, cursor)
            
    def get_actual_elements(self):
        return self.c_actual_elements.value
    
    def set_actual_elements(self, value):
        #TODO: PyCharm says it is read-only. Is it right?
        self.c_actual_elements.value = value
        
    actual_elements = property(get_actual_elements, set_actual_elements)
    
    # the two names are good, the property is here just to avoid losing sync
    def get_maxlength(self):
        return self.bufferSize
    
    def set_maxlength(self, value):
        self.bufferSize = value
        
    maxlength = property(get_maxlength, set_maxlength)

    def allocate_data(self):
        """Allocate the data for the variable."""

        # set the buffer size for the variable
        # bufferSize is public
        if self.type.get_buffer_size_proc: # if we could change this to something like get_buffer_type
            self.bufferSize = self.type.get_buffer_size_proc(self)
        else:
            self.bufferSize = self.size

        # allocate the data as long as it is small enough
        data_length = self.numElements * self.bufferSize
        if data_length > sys.maxint:
            raise ValueError("array size too large")

        self.data = ctypes.create_string_buffer(data_length) # TODO: then, would be nicer to use a typed array here.
    
    def get_single_value(self, array_pos):
        """Return the value of the variable at the given position."""

        # ensure we do not exceed the number of allocated elements
        if array_pos >= self.numElements:
            raise(IndexError, "Variable_GetSingleValue: array size exceeded")

        # check for a NULL value
        if self.type.is_null_proc:
            is_null = self.type.is_null_proc(self, array_pos)
        else:
            is_null = self.indicator[array_pos] == oci.OCI_IND_NULL

        if is_null:
            return None

        # check for truncation or other problems on retrieve
        self.verify_fetch(array_pos)

        # calculate value to return
        value = self.type.get_value_proc(self, array_pos)
        if self.outconverter is not None:
            result = self.outconverter(value)
            return result

        return value
    
    def _get_value(self, array_pos):
        """Return the value of the variable."""
        if self.is_array:
            return self.get_array_value(self.actual_elements)
        return self.get_single_value(array_pos)
    
    def getvalue(self, pos=0):
        """Return the value of the variable at the given position."""
        # TODO: Type check like cx_oracle
        return self._get_value(pos)

    def verify_fetch(self, array_pos):
        """Verifies that truncation or other problems did not take place on retrieve."""
        if self.type.is_variable_length:
            if self.return_code[array_pos] != 0:
                error = Error(self.environment, "Variable_VerifyFetch()", 0)
                error.code = self.return_code[array_pos]
                error.message = "column at array pos %d fetched with error: %d" % (array_pos, self.return_code[array_pos])

                raise DatabaseError(error)

    def get_array_value(self, num_elements):
        """Return the value of the variable as an array."""
        return [self.get_single_value(i) for i in xrange(num_elements)]

    def bind(self, cursor, name, pos):
        """Allocate a variable and bind it to the given statement."""

        # nothing to do if already bound
        if self.bind_handle and name == self.bound_name and pos == self.bound_pos:
            return

        # set the instance variables specific for binding
        self.bound_pos = pos
        self.bound_cursor_handle = cursor.handle
        self.bound_name = name

        # perform the bind
        self.internal_bind()
    
    def internal_bind(self):
        """Allocate a variable and bind it to the given statement."""

        if self.is_array:
            alloc_elems = self.allocelems
            actual_elements_ref = byref(self.c_actual_elements)
        else:
            alloc_elems = 0
            actual_elements_ref = oci.POINTER(oci.ub4)()
        
        # perform the bind
        if self.bound_name:
            buffer = cxBuffer.new_from_object(self.bound_name, self.environment.encoding)
            status = oci.OCIBindByName(self.bound_cursor_handle, byref(self.bind_handle),
                        self.environment.error_handle, buffer.cast_ptr,
                        buffer.size, self.data, self.bufferSize,
                        self.type.oracle_type, self.indicator, self.actual_length,
                        self.return_code, alloc_elems,
                        actual_elements_ref, oci.OCI_DEFAULT)
        else:
            status = oci.OCIBindByPos(self.bound_cursor_handle, byref(self.bind_handle),
                        self.environment.error_handle, self.bound_pos, self.data,
                        self.bufferSize, self.type.oracle_type, self.indicator,
                        self.actual_length, self.return_code, alloc_elems,
                        actual_elements_ref, oci.OCI_DEFAULT)
        
        self.environment.check_for_error(status, "Variable_InternalBind()")

        if not python3_or_better():
            # set the charset form and id if applicable
            if self.type.charset_form != oci.SQLCS_IMPLICIT:
                c_charset_form = oci.ub1(self.type.charset_form)
                status = oci.OCIAttrSet(self.bind_handle, oci.OCI_HTYPE_BIND,
                        byref(c_charset_form), 0, oci.OCI_ATTR_CHARSET_FORM,
                        self.environment.error_handle)
                self.environment.check_for_error(status, "Variable_InternalBind(): set charset form")
                self.type.charset_form = c_charset_form.value
                
                c_buffer_size = oci.ub4(self.bufferSize)
                status = oci.OCIAttrSet(self.bind_handle, oci.OCI_HTYPE_BIND,
                        byref(c_buffer_size), 0, oci.OCI_ATTR_MAXDATA_SIZE,
                        self.environment.error_handle)
                self.environment.check_for_error(status, "Variable_InternalBind(): set max data size")
                self.bufferSize = self.maxlength = c_buffer_size.value

        # set the max data size for strings
        self.set_max_data_size()
        
    def set_max_data_size(self):
        pass

    def make_array(self):
        """Make the variable an array, ensuring that the type supports arrays."""
        if not self.type.can_be_in_array:
            raise NotSupportedError("Variable_MakeArray(): type does not support arrays")

        self.is_array = True

    def set_value(self, array_pos, value):
        """Set the value of the variable."""
        if self.is_array:
            if array_pos > 0:
                raise NotSupportedError("arrays of arrays are not supported by the OCI")

            return self.set_array_value(value)

        return self.set_single_value(array_pos, value)
    
    setvalue = set_value # TODO: Type check like cx_oracle

    def set_single_value(self, array_pos, value):
        """Set a single value in the variable."""

        # ensure we do not exceed the number of allocated elements
        if array_pos >= self.numElements:
            raise IndexError("Variable_SetSingleValue: array size exceeded")

        # convert value, if necessary
        if self.inconverter is not None:
            value = self.inconverter(value)

        # check for a NULL value
        if value is None:
            self.indicator[array_pos] = oci.OCI_IND_NULL
            return None

        self.indicator[array_pos] = oci.OCI_IND_NOTNULL
        if self.type.is_variable_length:
            self.return_code[array_pos] = 0
        
        self.type.set_value_proc(self, array_pos, value)

    def set_array_value(self, value):
        """Set all of the array values for the variable."""

        # ensure we have an array to set
        if not isinstance(value, list):
            raise TypeError("expecting array data")

        # ensure we haven't exceeded the number of allocated elements
        num_elements = len(value)
        if num_elements > self.numElements:
            raise IndexError("Variable_SetArrayValue: array size exceeded")

        # set all of the values
        self.actual_elements = num_elements

        for i, element_value in enumerate(value):
            self.set_single_value(i, element_value)
            
    def resize(self, size):
        """Resize the variable."""
        
        # allocate the data for the new array
        orig_data = self.data
        orig_buffer_size = self.bufferSize
        self.size = size
        
        self.allocate_data()
    
        # copy the data from the original array to the new array
        for i in xrange(self.allocelems):
            to = ctypes.c_void_p(ctypes.addressof(self.data) + self.bufferSize*i)
            frm = ctypes.c_void_p(ctypes.addressof(orig_data) + orig_buffer_size*i)
            #ctypes.memmove(byref(self.data, self.bufferSize*i),
            #               byref(orig_data, orig_buffer_size * i),
            #               orig_buffer_size)
            
            ctypes.memmove(to, frm, orig_buffer_size)
    
        # force rebinding
        if self.bound_name or self.bound_pos > 0:
            self.internal_bind()
    
    @staticmethod
    def lookup_precision_and_scale(environment, param):
        return 0, 0
    
    @staticmethod
    def get_display_size(precision, scale, char_size, internal_size):
        return -1
    
    def __del__(self):
        if self.is_allocated_internally:
            if self.type.finalize_proc:
                self.type.finalize_proc(self)
    
    #def __repr__(self):
        #if self.is_array:
            #value = self.get_array_value(self.actual_elements)
        #elif self.allocelems == 1:
            #value = self.get_single_value(0)
        #else:
            #value = self.get_array_value(self.allocelems)
        
        #return '<%s.%s with value %s>' % (type(self).__module__, type(self).__name__, 'TODO')