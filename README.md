What
----

cx_Oracle re-written in Python, using ctypes to interface with Oracle native code. 100% API-compatible with cx_Oracle.

Why?!
-----

cx_Oracle is great code, but as many CPython extensions, it is not compatible with other Python implementations. I rewrote it in Python to be able to use PyPy and possibly Jython and IronPython. Also, ctypes is the recommended way to integrate C code with PyPy, as it can benefit from the JIT and no CPython emulation must be done.

How good is it?
---------------

Most of the Oracle datatypes are implemented and most of tests from cx_Oracle pass. Django works. Tested with Oracle 10 and 11.
The performance is not as good as cx_Oracle yet, but it improves fast as PyPy's JIT improves.

Installation
------------

As in cx_Oracle, you need the binary library from Oracle ( the instant client will suffice ) and you need to setup the environment variables so that Python can find it. As an example, take a look into https://github.com/lameiro/cx_oracle_on_ctypes/blob/master/test/setup_test_env_10.sh and adapt accordingly.

To install the python module, just put the cx_Oracle dir in your PYTHONPATH.

License
-------

3-clause BSD, like cx_Oracle. See http://opensource.org/licenses/BSD-3-Clause

Differences
-----------

cx_oracle_on_ctypes is 100% API compatible with cx_Oracle. If you find any missing functionality, even if it is not in the DB-API specification, report a bug.

Contributing
------------

Feedback and patches are welcome. Send them through the issue tracker or by e-mail.
