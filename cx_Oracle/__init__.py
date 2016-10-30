from decimal import Decimal

from datetime import datetime, date

from ctypes import c_int, byref

from cx_Oracle.custom_exceptions import Warning, Error, InterfaceError, DatabaseError, DataError, OperationalError, IntegrityError, InternalError, ProgrammingError, NotSupportedError

from cx_Oracle.utils import python3_or_better

# set up the types that are available
from cx_Oracle.utils import cxBinary as Binary
from cx_Oracle.connection import Connection
from cx_Oracle.cursor import Cursor
from datetime import datetime as Timestamp
from datetime import date as Date
# TODO: Sessionpool
from cx_Oracle.error import Error as _Error
connect = Connection # the name "connect" is required by the DB API

# create the basic data types for setting input sizes
from cx_Oracle.numbervar import NUMBER #, NATIVE_FLOAT
from cx_Oracle.stringvar import STRING, BINARY, FIXED_CHAR, ROWID

if not python3_or_better():
    from cx_Oracle.stringvar import UNICODE, FIXED_UNICODE

from cx_Oracle.longvar import LONG_BINARY, LONG_STRING
from cx_Oracle.datetimevar import DATETIME
from cx_Oracle.lobvar import NCLOB, CLOB, BLOB, BFILE
from cx_Oracle.externallobvar import LOB
from cx_Oracle.timestampvar import TIMESTAMP
from cx_Oracle.intervalvar import INTERVAL
from cx_Oracle.cursorvar import CURSOR
from cx_Oracle.oci import ORACLE_10G, ORACLE_10GR2, ORACLE_11, ORACLE_12

def makedsn(host, port, sid='', service_name=''):
    if sid == '' and service_name == '':
        raise TypeError('makedsn requires either sid or servicename, but both were passed empty')

    if sid:
        connect_data_obj = sid
        dsn_format = "(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=%s)(PORT=%s)))(CONNECT_DATA=(SID=%s)))"
    else:
        connect_data_obj = service_name
        dsn_format = "(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=%s)(PORT=%s)))(CONNECT_DATA=(SERVICE_NAME=%s)))"

    return dsn_format % (host, port, connect_data_obj)

ORACLE_VERSION_10G, ORACLE_VERSION_10GR2, ORACLE_VERSION_11G, ORACLE_VERSION_12 = range(4)
ORACLE_VERSION = int(ORACLE_10GR2) + int(ORACLE_11) + int(ORACLE_12)

# broken end! can we try to run the clientversion method instead? apparently, it does not exist for oracle 10g, but if that is the only case, it is still OK
if ORACLE_VERSION >= ORACLE_VERSION_10GR2:
    def clientversion():
        major_version, minor_version, update_num, patch_num, port_update_num = c_int(), c_int(), c_int(), c_int(), c_int()
        oci.OCIClientVersion(byref(major_version), byref(minor_version), byref(update_num), byref(patch_num), byref(port_update_num))

        return (major_version.value, minor_version.value, update_num.value, patch_num.value, port_update_num.value)

def Time(*args):
    raise NotSupportedError("Oracle does not support time only variables")

TimeFromTicks = Time

def DateFromTicks(args):
    return date.fromtimestamp(args)

def TimestampFromTicks(args):
    return datetime.fromtimestamp(args)

apilevel = '2.0'
threadsafety = 2
paramstyle = 'named'
buildtime = '' # TODO: Find out what cx_oracle puts here
version = '0.1'

# add constants for registering callbacks
from cx_Oracle.oci import \
    OCI_SYSDBA                  as SYSDBA, \
    OCI_SYSOPER                 as SYSOPER,\
    OCI_FNCODE_BINDBYNAME       as FNCODE_BINDBYNAME, \
    OCI_FNCODE_BINDBYPOS        as FNCODE_BINDBYPOS, \
    OCI_FNCODE_DEFINEBYPOS      as FNCODE_DEFINEBYPOS, \
    OCI_FNCODE_STMTEXECUTE      as FNCODE_STMTEXECUTE, \
    OCI_FNCODE_STMTFETCH        as FNCODE_STMTFETCH, \
    OCI_FNCODE_STMTPREPARE      as FNCODE_STMTPREPARE, \
    OCI_UCBTYPE_ENTRY           as UCBTYPE_ENTRY, \
    OCI_UCBTYPE_EXIT            as UCBTYPE_EXIT, \
    OCI_UCBTYPE_REPLACE         as UCBTYPE_REPLACE, \
    OCI_SPOOL_ATTRVAL_WAIT      as SPOOL_ATTRVAL_WAIT, \
    OCI_SPOOL_ATTRVAL_NOWAIT    as SPOOL_ATTRVAL_NOWAIT, \
    OCI_SPOOL_ATTRVAL_FORCEGET  as SPOOL_ATTRVAL_FORCEGET

if ORACLE_VERSION >= ORACLE_VERSION_10GR2:
    from cx_Oracle.oci import \
        OCI_PRELIM_AUTH                     as PRELIM_AUTH, \
        OCI_DBSHUTDOWN_ABORT                as DBSHUTDOWN_ABORT, \
        OCI_DBSHUTDOWN_FINAL                as DBSHUTDOWN_FINAL, \
        OCI_DBSHUTDOWN_IMMEDIATE            as DBSHUTDOWN_IMMEDIATE, \
        OCI_DBSHUTDOWN_TRANSACTIONAL        as DBSHUTDOWN_TRANSACTIONAL, \
        OCI_DBSHUTDOWN_TRANSACTIONAL_LOCAL  as DBSHUTDOWN_TRANSACTIONAL_LOCAL, \
        OCI_EVENT_NONE                      as EVENT_NONE, \
        OCI_EVENT_STARTUP                   as EVENT_STARTUP, \
        OCI_EVENT_SHUTDOWN                  as EVENT_SHUTDOWN, \
        OCI_EVENT_SHUTDOWN_ANY              as EVENT_SHUTDOWN_ANY, \
        OCI_EVENT_DEREG                     as EVENT_DEREG, \
        OCI_EVENT_OBJCHANGE                 as EVENT_OBJCHANGE, \
        OCI_OPCODE_ALLOPS                   as OPCODE_ALLOPS, \
        OCI_OPCODE_ALLROWS                  as OPCODE_ALLROWS, \
        OCI_OPCODE_INSERT                   as OPCODE_INSERT, \
        OCI_OPCODE_UPDATE                   as OPCODE_UPDATE, \
        OCI_OPCODE_DELETE                   as OPCODE_DELETE, \
        OCI_OPCODE_ALTER                    as OPCODE_ALTER, \
        OCI_OPCODE_DROP                     as OPCODE_DROP, \
        OCI_SUBSCR_NAMESPACE_DBCHANGE       as SUBSCR_NAMESPACE_DBCHANGE, \
        OCI_SUBSCR_PROTO_OCI                as SUBSCR_PROTO_OCI, \
        OCI_SUBSCR_PROTO_MAIL               as SUBSCR_PROTO_MAIL, \
        OCI_SUBSCR_PROTO_SERVER             as SUBSCR_PROTO_SERVER, \
        OCI_SUBSCR_PROTO_HTTP               as SUBSCR_PROTO_HTTP
        #OCI_SUBSCR_QOS_RELIABLE             as SUBSCR_QOS_RELIABLE, \
        #OCI_SUBSCR_QOS_PAYLOAD              as SUBSCR_QOS_PAYLOAD, \
        #OCI_SUBSCR_QOS_REPLICATE            as SUBSCR_QOS_REPLICATE, \
        #OCI_SUBSCR_QOS_SECURE               as SUBSCR_QOS_SECURE, \
        #OCI_SUBSCR_QOS_PURGE_ON_NTFN        as SUBSCR_QOS_PURGE_ON_NTFN, \
        #OCI_SUBSCR_QOS_MULTICB              as SUBSCR_QOS_MULTICBK

if ORACLE_VERSION >= ORACLE_VERSION_11G:
    from cx_Oracle.oci import \
        OCI_ATTR_PURITY_DEFAULT as ATTR_PURITY_DEFAULT,\
        OCI_ATTR_PURITY_NEW as ATTR_PURITY_NEW, \
        OCI_ATTR_PURITY_SELF as ATTR_PURITY_SELF

# TODO: add all exceptions, imported classes etc
__all__ = ['connect', 'makedsn', 'Time', 'DateFromTicks', 'TimeFromTicks', 'TimestampFromTicks', 'Binary'] # just to hide ancilliary names like "python3_or_better"
if ORACLE_VERSION >= ORACLE_VERSION_10GR2:
    __all__ += ['clientversion']
