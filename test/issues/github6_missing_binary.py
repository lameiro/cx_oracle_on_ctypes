import cx_Oracle
from test_base import TestBase

class Github6(TestBase):
    def test_expected(self):
        expected_oracle_11 = {'ATTR_PURITY_DEFAULT', 'ATTR_PURITY_NEW', 'ATTR_PURITY_SELF', 'BFILE', 'BINARY', 'BLOB', 'Binary',
                              'CLOB', 'CURSOR', 'Connection', 'Cursor', 'DATETIME', 'DBSHUTDOWN_ABORT', 'DBSHUTDOWN_FINAL',
                              'DBSHUTDOWN_IMMEDIATE', 'DBSHUTDOWN_TRANSACTIONAL', 'DBSHUTDOWN_TRANSACTIONAL_LOCAL', 'DataError',
                              'DatabaseError', 'Date', 'DateFromTicks', 'EVENT_DEREG', 'EVENT_NONE', 'EVENT_OBJCHANGE',
                              'EVENT_SHUTDOWN', 'EVENT_SHUTDOWN_ANY', 'EVENT_STARTUP', 'Error', 'FIXED_CHAR', 'FIXED_UNICODE',
                              'FNCODE_BINDBYNAME', 'FNCODE_BINDBYPOS', 'FNCODE_DEFINEBYPOS', 'FNCODE_STMTEXECUTE',
                              'FNCODE_STMTFETCH', 'FNCODE_STMTPREPARE', 'INTERVAL', 'IntegrityError', 'InterfaceError',
                              'InternalError', 'LOB', 'LONG_BINARY', 'LONG_STRING', 'LONG_UNICODE', 'NATIVE_FLOAT', 'NCLOB',
                              'NUMBER', 'NotSupportedError', 'OBJECT', 'OPCODE_ALLOPS', 'OPCODE_ALLROWS', 'OPCODE_ALTER',
                              'OPCODE_DELETE', 'OPCODE_DROP', 'OPCODE_INSERT', 'OPCODE_UPDATE', 'OperationalError',
                              'PRELIM_AUTH', 'ProgrammingError', 'ROWID', 'SPOOL_ATTRVAL_FORCEGET', 'SPOOL_ATTRVAL_NOWAIT',
                              'SPOOL_ATTRVAL_WAIT', 'STRING', 'SUBSCR_NAMESPACE_DBCHANGE', 'SUBSCR_PROTO_HTTP',
                              'SUBSCR_PROTO_MAIL', 'SUBSCR_PROTO_OCI', 'SUBSCR_PROTO_SERVER', 'SYSDBA', 'SYSOPER',
                              'SessionPool', 'TIMESTAMP', 'Time', 'TimeFromTicks', 'Timestamp', 'TimestampFromTicks',
                              'UCBTYPE_ENTRY', 'UCBTYPE_EXIT', 'UCBTYPE_REPLACE', 'UNICODE', 'Warning', '_Error', '__doc__',
                              '__file__', '__name__', '__package__', 'apilevel', 'buildtime', 'clientversion', 'connect',
                              'makedsn', 'paramstyle', 'threadsafety', 'version'}

        if cx_Oracle.ORACLE_VERSION == cx_Oracle.ORACLE_VERSION_11G:
            assert expected_oracle_11.difference(set(dir(cx_Oracle))) == {'OBJECT', 'SessionPool', 'LONG_UNICODE',
                                                               'NATIVE_FLOAT'}
