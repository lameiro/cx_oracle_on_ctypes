import cx_Oracle

con = cx_Oracle.Connection('lameiro', 'lameiro', 'localhost')
print "Open connection OK"

cursor = con.cursor()
cursor.execute("select * from dual")
print cursor.fetchone()
con.close()
print "Close connection OK"
