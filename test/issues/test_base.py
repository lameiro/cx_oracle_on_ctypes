import os
import cx_Oracle
import unittest

USER = os.environ['CX_ORACLE_USERNAME']
PASSWORD = os.environ['CX_ORACLE_PASSWORD']
SID = os.environ['CX_ORACLE_TNSENTRY']

class TestBase(unittest.TestCase):
    def get_connection(self):
        return cx_Oracle.connect(USER, PASSWORD, SID)
    def get_cursor(self):
        connection = self.get_connection()
        return connection.cursor()
