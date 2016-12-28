from cx_Oracle import Connection
import time
import sys

while True:
    time.sleep(0.2)
    try:
        c = Connection('cx_Oracle/dev@localhost')
        c.close()
        sys.stdout.write('.')
        sys.stdout.flush()
    except Exception, e:
        print e
        sys.stdout.write('x')
        sys.stdout.flush()
