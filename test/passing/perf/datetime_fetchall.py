import cx_Oracle, time, sys, gc
connection = cx_Oracle.connect('cx_Oracle', 'dev', 'localhost')
cursor = connection.cursor()

for i in xrange(50000):
    if i == 2000:
        print "starting"
        start = time.time()

    cursor.execute("select * From TestDates order by IntCol")
    cursor.fetchall()
print "ended", time.time()-start

#import ctypes
#import time
#
#class AStruct(ctypes.Structure):
#    _fields_ = [
#        ('an_int', ctypes.c_int),
#        ('a_string', ctypes.c_char_p),
#    ]
#
#
#a = AStruct(1, 'abc')
#
#for i in xrange(5000000):
#    if i == 2000:
#        print "starting"
#        start = time.time()
#
#    a.an_int
#
#print "ended", time.time()-start