What
----

cx_Oracle written in 100% pure-Python, on top of ctypes. 100% API-compatible with cx_Oracle.

Why?!
-----

cx_Oracle is great code, but as many CPython extensions, it is not compatible with other Python implementations. I rewrote it in pure-Python to be able to use PyPy and possibly Jython and IronPython. Also, ctypes is the recommended way to integrate C code with PyPy, as it can benefit from the JIT and no CPython emulation must be done.

How good is it?
---------------

Most of the Oracle datatypes are implemented and most of tests from cx_Oracle pass. Django works.

License
-------

3-clause BSD, like cx_Oracle.
For cx_Oracle license, see: http://cx-oracle.sourceforge.net/html/license.html

Differences
-----------

cx_oracle_on_ctypes is 100% API compatible with cx_Oracle. If you find any missing functionality, even if it is not in the DB-API specification, report a bug.
