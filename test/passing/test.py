"""Runs all defined unit tests."""

import cx_Oracle
import imp
import os
import sys
import unittest
import time

print "Running tests for cx_Oracle version", cx_Oracle.version

import TestEnv

inSetup = (os.path.basename(sys.argv[0]).lower() == "setup.py")

if len(sys.argv) > 1 and not inSetup:
    moduleNames = [os.path.splitext(v)[0] for v in sys.argv[1:]]
else:
    moduleNames = [
            "Connection",
            "uConnection",
            "Cursor",
            "uCursor",
            "CursorVar",
            "uCursorVar",
            "DateTimeVar",
            "uDateTimeVar",
            "IntervalVar",
            "uIntervalVar",
            "LobVar",
            "uLobVar",
            "LongVar",
            "uLongVar",
            "NumberVar",
            "uNumberVar",
           # "ObjectVar",
            #"uObjectVar",
            #"SessionPool",
            #"uSessionPool",
            "StringVar",
            "uStringVar",
            "TimestampVar",
            "uTimestampVar",
            "UnicodeVar"
    ]

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        global cx_Oracle
        self.connection = cx_Oracle.connect(TestEnv.USERNAME,
                TestEnv.PASSWORD, TestEnv.TNSENTRY)
        self.cursor = self.connection.cursor()
        self.cursor.arraysize = TestEnv.ARRAY_SIZE

    def tearDown(self):
        self.connection.close()
        del self.cursor
        del self.connection
        import gc
        for i in range(5):
            gc.collect()



loader = unittest.TestLoader()
runner = unittest.TextTestRunner(verbosity = 2)
failures = []
for name in moduleNames:
    fileName = name + ".py"
    print
    print "Running tests in", fileName
    if inSetup:
        fileName = os.path.join("test", fileName)
    module = imp.new_module(name)
    setattr(module, "USERNAME", TestEnv.USERNAME)
    setattr(module, "PASSWORD", TestEnv.PASSWORD)
    setattr(module, "TNSENTRY", TestEnv.TNSENTRY)
    setattr(module, "ARRAY_SIZE", TestEnv.ARRAY_SIZE)
    setattr(module, "TestCase", unittest.TestCase)
    setattr(module, "BaseTestCase", BaseTestCase)
    setattr(module, "cx_Oracle", cx_Oracle)
    exec(open(fileName).read(), module.__dict__)
    tests = loader.loadTestsFromModule(module)
    result = runner.run(tests)
    if not result.wasSuccessful():
        failures.append(name)
    time.sleep(5)
if failures:
    print "***** Some tests in the following modules failed. *****"
    for name in failures:
        print "      %s" % name
    sys.exit(1)

