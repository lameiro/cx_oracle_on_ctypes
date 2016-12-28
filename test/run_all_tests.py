import subprocess
import sys
import os

if sys.version_info.major == 2:
    suffix = ''
else:
    suffix = '3'

pypy_binary_name = 'pypy%s' % suffix

pypy_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pypy%d/bin/%s' % (sys.version_info.major, pypy_binary_name)))

for instant_client_version in ('10_2', '11_2', '12_1'):
    for python_path in (sys.executable, pypy_path):
        subprocess.check_call(['python', 'test/run_tests.py', instant_client_version, str(sys.version_info.major), python_path, 'True', 'False'])
