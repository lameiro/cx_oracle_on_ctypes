import ctypes
from ctypes import byref

from variable_type import VariableType
import oci
from utils import python3_or_better
from buffer import cxBuffer
from variable import Variable
from externallobvar import LOB
from descriptor_manager import DescriptorManager

class CLOB(Variable):
    pass

class NCLOB(Variable):
    pass

class BLOB(Variable):
    pass

class BFILE(Variable):
    pass

class BaseLobVariableType(VariableType):
    def __init__(self):
        VariableType.__init__(self)
        self.oci_type = oci.POINTER(oci.OCILobLocator)
        
        self.initialize_proc = self.initialize
        self.finalize_proc = self.finalize
        self.pre_define_proc = None
        self.post_define_proc = None
        self.pre_fetch_proc = self.pre_fetch
        self.is_null_proc = None
        self.set_value_proc = self.set_value
        self.get_value_proc = self.get_value
        self.get_buffer_size_proc = None
        
        #self.python_type = None
        #self.oracle_type = None
        #self.charset_form = None
        self.size = ctypes.sizeof(self.oci_type)
        #self.is_character_data = None
        self.is_variable_length = False
        self.can_be_copied = False
        self.can_be_in_array = False
        
        self.descriptor_manager = DescriptorManager()
    
    def initialize(self, var, cursor):
        var.connection = cursor.connection
        self.descriptor_manager.initialize(self, var, cursor, oci.OCI_DTYPE_LOB, "LobVar_Initialize()")
    
    def finalize(self, var):
        self.pre_fetch(var)
        self.descriptor_manager.finalize(self, var, oci.OCI_DTYPE_LOB)
    
    def pre_fetch(self, var):
        """Free temporary LOBs prior to fetch."""
        typed_data = self.get_typed_data(var)
        
        for i in xrange(var.allocelems):
            if typed_data[i]:
                c_is_temporary = ctypes.c_int()
                status = oci.OCILobIsTemporary(var.environment.handle,
                        var.environment.error_handle, typed_data[i], byref(c_is_temporary))
                var.environment.check_for_error(status, "LobVar_PreFetch(): is temporary LOB?")
                is_temporary = c_is_temporary.value

                 # connection can be closed already, therefore we need to check for a non-null handle
                if is_temporary and var.connection.handle:
                    status = oci.OCILobFreeTemporary(var.connection.handle, var.environment.error_handle,
                                                 typed_data[i])
                    var.environment.check_for_error(status, "LobVar_PreFetch(): free temporary LOB")

    def set_value(self, var, pos, value):
        # make sure have temporary LOBs set up
        typed_data = self.get_typed_data(var)
        c_is_temporary = ctypes.c_int()
        status = oci.OCILobIsTemporary(var.environment.handle, var.environment.error_handle,
                                       typed_data[pos], byref(c_is_temporary))
        var.environment.check_for_error(status, "LobVar_SetValue(): is temporary?")
        is_temporary = c_is_temporary.value
        if not is_temporary:
            if var.type.oracle_type == oci.SQLT_BLOB:
                lob_type = oci.OCI_TEMP_BLOB
            else:
                lob_type = oci.OCI_TEMP_CLOB
            
            status = oci.OCILobCreateTemporary(var.connection.handle,
                    var.environment.error_handle, typed_data[pos],
                    oci.OCI_DEFAULT, var.type.charset_form, lob_type, 0,
                    oci.OCI_DURATION_SESSION)
            
            var.environment.check_for_error(status, "LobVar_SetValue(): create temporary")
            
    
        # trim the current value
        status = oci.OCILobTrim(var.connection.handle, var.environment.error_handle,
                                typed_data[pos], 0)
        
        var.environment.check_for_error(status, "LobVar_SetValue(): trim")
    
        # set the current value
        self._write(var, pos, value, 1)
        
    def _write(self, var, pos, data_obj, offset):
        """Write data to the LOB variable."""
        
        # verify the data type
        var_type = var.type
        if var_type == vt_BFILE:
            raise TypeError("BFILEs are read only")
        
        if var_type == vt_BLOB:
            buffer = cxBuffer.new_from_object(data_obj, var.environment.encoding)
            amount = buffer.size
        elif not python3_or_better() and var_type == vt_NCLOB:
            buffer = cxBuffer.new_from_object(data_obj, var.environment.nencoding)
            amount = buffer.size
        else:
            buffer = cxBuffer.new_from_object(data_obj, var.environment.encoding)
            if var.environment.fixedWidth and var.environment.maxBytesPerCharacter > 1:
                amount = buffer.size / var.environment.maxBytesPerCharacter
            else:
                amount = buffer.size
    
        # nothing to do if no data to write
        if amount == 0:
            return amount
        
        typed_data = self.get_typed_data(var)
        c_amount = oci.ub4(amount)
        callback_lob_write_type = oci.OCILobWrite.argtypes[9]
        null_oci_callback = callback_lob_write_type()
        status = oci.OCILobWrite(var.connection.handle,
                var.environment.error_handle, typed_data[pos], byref(c_amount), offset,
                buffer.ptr, buffer.size, oci.OCI_ONE_PIECE, None, null_oci_callback, 0,
                var.type.charset_form)

        var.environment.check_for_error(status, "LobVar_Write()")
        amount = c_amount.value # not sure if the write can change it, i dont think so, but just for correctness
        
        return amount
    
    def get_value(self, var, pos):
        return LOB(var, pos)

class CLOBVariableType(BaseLobVariableType):
    def __init__(self):
        BaseLobVariableType.__init__(self)
        self.python_type = CLOB
        self.oracle_type = oci.SQLT_CLOB
        self.charset_form = oci.SQLCS_IMPLICIT
        self.is_character_data = True
    
    def initialize(self, var, cursor):
        BaseLobVariableType.initialize(self, var, cursor)
        var.is_file = False

class NCLOBVariableType(BaseLobVariableType):
    def __init__(self):
        BaseLobVariableType.__init__(self)
        self.python_type = NCLOB
        self.oracle_type = oci.SQLT_CLOB
        self.charset_form = oci.SQLCS_NCHAR
        self.is_character_data = True
        
    def initialize(self, var, cursor):
        BaseLobVariableType.initialize(self, var, cursor)
        var.is_file = False

class BLOBVariableType(BaseLobVariableType):
    def __init__(self):
        BaseLobVariableType.__init__(self)
        self.python_type = BLOB
        self.oracle_type = oci.SQLT_BLOB
        self.charset_form = oci.SQLCS_IMPLICIT
        self.is_character_data = False
    
    def initialize(self, var, cursor):
        BaseLobVariableType.initialize(self, var, cursor)
        var.is_file = False

class BFILEVariableType(BaseLobVariableType):
    def __init__(self):
        BaseLobVariableType.__init__(self)
        self.python_type = BFILE
        self.oracle_type = oci.SQLT_BFILE
        self.charset_form = oci.SQLCS_IMPLICIT
        self.is_character_data = False
        
    def initialize(self, var, cursor):
        BaseLobVariableType.initialize(self, var, cursor)
        var.is_file = True

vt_NCLOB = NCLOBVariableType()
vt_CLOB = CLOBVariableType()
vt_BLOB = BLOBVariableType()
vt_BFILE = BFILEVariableType()
