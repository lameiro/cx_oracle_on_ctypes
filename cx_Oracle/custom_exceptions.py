from utils import python3_or_better

if python3_or_better():
    CXORA_BASE_EXCEPTION = Exception
    CXORA_TYPE_ERROR = 'expecting string or bytes object'
else:
    CXORA_BASE_EXCEPTION = StandardError
    CXORA_TYPE_ERROR = 'expecting string, unicode or buffer object'

class Warning(CXORA_BASE_EXCEPTION):
    pass

class Error(CXORA_BASE_EXCEPTION):
    pass

class InterfaceError(Error):
    pass

class DatabaseError(Error):
    pass

class DataError(DatabaseError):
    pass

class OperationalError(DatabaseError):
    pass

class IntegrityError(DatabaseError):
    pass

class InternalError(DatabaseError):
    pass

class ProgrammingError(DatabaseError):
    pass

class NotSupportedError(DatabaseError):
    pass
