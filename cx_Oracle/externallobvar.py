import ctypes
from ctypes import byref

import oci
from utils import bytes, cxString_from_encoded_string
from custom_exceptions import ProgrammingError

class LOB(object):
    def size(self):
        self._verify()
        return self._internal_size()

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()
    
    def read(self, offset=-1, amount=-1):
        self._verify()
        return self._value(offset, amount)
    
    def write(self, data, offset=-1):
        raise NotImplementedError()

    def trim(self, newSize=0):
        self._verify()
        typed_data = self._get_lobvar_typed_data()
        status = oci.OCILobTrim(self.lob_var.connection.handle,
            self.lob_var.environment.error_handle, typed_data[self.pos],
            newSize)
        
        self.lob_var.environment.check_for_error(status, "ExternalLobVar_Trim()")
    
    def getchunksize(self):
        raise NotImplementedError()
    
    def isopen(self):
        raise NotImplementedError()
    
    def getfilename(self):
        raise NotImplementedError()
    
    def setfilename(self):
        raise NotImplementedError()
    
    def fileexists(self):
        raise NotImplementedError()
    
    def __reduce__(self):
        raise NotImplementedError()
    
    def __init__(self, var, pos):
        """Create a new external LOB variable."""
        self.pos = pos
        self.internal_fetch_num = var.internal_fetch_num
        self.lob_var = var
        
    def _value(self, offset, amount):
        from lobvar import vt_CLOB, vt_NCLOB
        """Return a portion (or all) of the data in the external LOB variable."""
        lob_type = self.lob_var.type
        
        # modify the arguments
        if offset < 0:
            offset = 1
        
        if amount < 0:
            amount = self._internal_size()
            amount = amount - offset + 1;
            if amount <= 0:
                amount = 1
        
        length = amount
        
        if lob_type == vt_CLOB:
            buffer_size = amount * self.lob_var.environment.maxBytesPerCharacter
        elif lob_type == vt_NCLOB:
            buffer_size = amount * 2
        else:
            buffer_size = amount
    
        buffer, length = self._internal_read(offset)
        
        if lob_type == vt_CLOB:
            if var.lob_var.environment.fixedWidth:
                length = length * self.lob_var.environment.maxBytesPerCharacter
            result = cxString_from_encoded_string(buffer, self.lob_var.environment.encoding)
        elif lob_type == vt_NCLOB:
            result = buffer.decode(self.lob_var.environment.encoding)
        else:
            result = bytes(buffer, length)

        return result
    
    def _verify(self):
        if self.internal_fetch_num != self.lob_var.internal_fetch_num:
            raise ProgrammingError("LOB variable no longer valid after subsequent fetch")
        
    def _internal_size(self, ):
        c_length = oci.ub4()
        typed_data = self._get_lobvar_typed_data()
        status = oci.OCILobGetLength(self.lob_var.connection.handle, self.lob_var.environment.error_handle,
                                     typed_data[self.pos], byref(c_length))
    
        self.lob_var.environment.check_for_error(status, "ExternalLobVar_InternalSize()")

        return c_length.value
    
    def _get_lobvar_typed_data(self):
        return self.lob_var.type.get_typed_data(self.lob_var)