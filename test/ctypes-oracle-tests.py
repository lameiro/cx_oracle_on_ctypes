import cx_Oracle
import unittest

#BaseTestCase  = unittest.TestCase
class TestModule(BaseTestCase):
    def test_timestamp_exists(self):
        self.assertTrue(cx_Oracle.TIMESTAMP)