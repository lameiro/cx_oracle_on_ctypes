#!/usr/local/python
from __future__ import print_function
import os
import sys
import pprint
import subprocess

instant_client_version, python_version, python_path = sys.argv[1:4]

if len(sys.argv) >= 6:
    run_cx_oracle_tests = eval(sys.argv[4])
    run_github_tests = eval(sys.argv[5])
else:
    run_cx_oracle_tests = True
    run_github_tests = True

instant_client_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'instantclient_%s' % instant_client_version))
cx_oracle_on_ctypes_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

print('Running tests for instant client %s, python %s' % (instant_client_version, python_version) )

os.environ['LD_LIBRARY_PATH']=instant_client_path
os.environ['DYLD_LIBRARY_PATH']=instant_client_path
os.environ['PYTHONPATH']=cx_oracle_on_ctypes_path
os.environ['NLS_LANG']='.UTF8'
os.environ['CX_ORACLE_USERNAME']='cx_Oracle'
os.environ['CX_ORACLE_PASSWORD']='dev'
os.environ['CX_ORACLE_TNSENTRY']='(DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = localhost)(PORT = 1521))) (CONNECT_DATA = (SID = XE)))'
os.environ['CX_ORACLE_ARRAY_SIZE']=str(1024)

if python_version == '3':
    suffix = '3k'
else:
    suffix = ''

if run_cx_oracle_tests:
    print('Running C cx_Oracle tests')
    os.chdir(os.path.join(os.path.dirname(__file__), 'passing'))
    subprocess.call([python_path, 'test%s.py' % suffix])

if run_github_tests:
    print('Running cx_oracle_on_ctypes github tests')
    os.chdir(os.path.join(os.path.dirname(__file__), 'issues'))
    subprocess.call([python_path, '-m', 'unittest', 'discover', '-v', '-p' 'github*.py'])

