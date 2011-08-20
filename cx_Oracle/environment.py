from ctypes import byref, CFUNCTYPE
import ctypes
import oci
from buffer import cxBuffer
from error import Error
from custom_exceptions import IntegrityError, OperationalError, DatabaseError
from utils import MAX_STRING_CHARS, MAX_BINARY_BYTES


class Environment(object):
    def __init__(self, handle):
        self.handle = handle
        self.error_handle = oci.POINTER(oci.OCIError)()
        
        self.fixedWidth = self.maxBytesPerCharacter = 1
        self.maxStringBytes = MAX_STRING_CHARS
        self.cloneEnv = None

        self.numberToStringFormatBuffer = cxBuffer()
        self.numberFromStringFormatBuffer = cxBuffer()
        self.nlsNumericCharactersBuffer = cxBuffer()

        # create the error handle
        null_ptr_type = oci.OCIHandleAlloc.argtypes[-1]
        null_ptr = null_ptr_type()
        status = oci.OCIHandleAlloc(handle, byref(self.error_handle), oci.OCI_HTYPE_ERROR, 0, 0)
        self.check_for_error(status, "Environment_New(): create error handle")


    @staticmethod
    def new_from_scratch(threaded, events, encoding, nencoding):
        mode = oci.OCI_OBJECT
        if threaded:
            mode |= oci.OCI_THREADED
        #TODO: if EVENTS_SUPPORTED:
        #    if events:
        #        mode |= ociap.OCI_EVENTS
        
        handle = oci.POINTER(oci.OCIEnv)()
        malocfp_type = CFUNCTYPE(oci.UNCHECKED(oci.POINTER(None)), oci.POINTER(None), oci.c_size_t)
        null_malocfp = malocfp_type()

        ralocfp_type = CFUNCTYPE(oci.UNCHECKED(oci.POINTER(None)), oci.POINTER(None), oci.POINTER(None), oci.c_size_t)
        null_ralocfp = ralocfp_type()

        mfreefp_type = CFUNCTYPE(oci.UNCHECKED(None), oci.POINTER(None), oci.POINTER(None))
        null_mfreefp = mfreefp_type()

        status = oci.OCIEnvNlsCreate(byref(handle), mode, oci.POINTER(None)(), null_malocfp, null_ralocfp, null_mfreefp, 0, None, 0, 0)

        if not handle or (status != oci.OCI_SUCCESS and status != oci.OCI_SUCCESS_WITH_INFO):
            raise InterfaceErrorException("Unable to acquire Oracle environment handle")

        env = Environment(handle)

        c_maxBytesPerCharacter = oci.sb4()
        status = oci.OCINlsNumericInfoGet(handle, env.error_handle, byref(c_maxBytesPerCharacter), oci.OCI_NLS_CHARSET_MAXBYTESZ)
        env.check_for_error(status, "Environment_New(): get max bytes per character")
        env.maxBytesPerCharacter = c_maxBytesPerCharacter.value
        

        env.maxStringBytes = MAX_STRING_CHARS * env.maxBytesPerCharacter

        # acquire whether character set is fixed width
        c_fixedWidth = oci.sb4()
        status = oci.OCINlsNumericInfoGet(handle, env.error_handle, byref(c_fixedWidth), oci.OCI_NLS_CHARSET_FIXEDWIDTH)
        env.check_for_error(status, "Environment_New(): determine if charset fixed width")
        env.fixedWidth = c_fixedWidth.value
        
        # determine encodings to use for Unicode values
        env.encoding = env.get_characterset_name(oci.OCI_ATTR_ENV_CHARSET_ID, encoding)
        env.nencoding = env.get_characterset_name(oci.OCI_ATTR_ENV_NCHARSET_ID, nencoding)

        # fill buffers for number formats
        env.numberToStringFormatBuffer = Environment.set_buffer("TM9", env.encoding)
        env.numberFromStringFormatBuffer = Environment.set_buffer("999999999999999999999999999999999999999999999999999999999999999", env.encoding)
        env.nlsNumericCharactersBuffer = Environment.set_buffer("NLS_NUMERIC_CHARACTERS='.,'", env.encoding)

        return env

    @staticmethod
    def set_buffer(value, encoding):
        if value is None:
            raise # TODO: what?
        return cxBuffer.new_from_object(value, encoding)

    def check_for_error(self, status, context):
        if status != oci.OCI_SUCCESS and status != oci.OCI_SUCCESS_WITH_INFO:
            if status != oci.OCI_INVALID_HANDLE:
                self.raise_error(context)
            
            error = Error(self, context, 0)
            error.code = 0
            error.message = "Invalid handle!"

            raise DatabaseError(error)

    def raise_error(self, context):
        error = Error(self, context, 1)
        if error.code in (1, 1400, 2290, 2291, 2292):
            raise IntegrityError(error)
        elif error.code in (22, 378, 602, 603, 604, 609, 1012, 1013, 1033, 1034, 1041, 1043, 1089, 1090, 1092, 3113, 3114, 3122, 3135, 12153, 12203, 12500, 12571, 27146, 28511):
            raise OperationalError(error)
        else:
            raise DatabaseError(error)


    def get_characterset_name(self, attribute, override_value):
        """Retrieve and store the IANA character set name for the attribute."""

        # if override value specified, use it
        if override_value:
            return override_value

        # get character set id
        c_charset_id = oci.ub2()
        status = oci.OCIAttrGet(self.handle, oci.OCI_HTYPE_ENV, byref(c_charset_id), None, attribute, self.error_handle)
        self.check_for_error(status, "Environment_GetCharacterSetName(): get charset id")

        # get character set name
        c_charset_name = ctypes.create_string_buffer(oci.OCI_NLS_MAXBUFSZ)
        status = oci.OCINlsCharSetIdToName(self.handle, c_charset_name, oci.OCI_NLS_MAXBUFSZ, c_charset_id)
        self.check_for_error(status, "Environment_GetCharacterSetName(): get Oracle charset name")

        # get IANA character set name
        c_iana_charset_name = ctypes.create_string_buffer(oci.OCI_NLS_MAXBUFSZ)
        status = oci.OCINlsNameMap(self.handle, c_iana_charset_name, oci.OCI_NLS_MAXBUFSZ, c_charset_name, oci.OCI_NLS_CS_ORA_TO_IANA)
        self.check_for_error(status, "Environment_GetCharacterSetName(): translate NLS charset")
        
        return c_iana_charset_name.value
