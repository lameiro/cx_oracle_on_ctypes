import cx_Oracle

connection = cx_Oracle.connect('cx_Oracle', 'dev', 'localhost')
print "Open connection OK"

cursor = connection.cursor()

cursor.execute("truncate table TestExecuteMany")
rows = [ ( 1, "First" ),
         ( 2, "Second" ),
         ( 3, "Third" ),
         ( 4, "Fourth" ),
         ( 5, "Fifth" ),
         ( 6, "Sixth" ),
         ( 7, "Seventh" ) ]
cursor.bindarraysize = 5
cursor.setinputsizes(int, 100)
sql = "insert into TestExecuteMany (IntCol, StringCol) values (:1, :2)"
cursor.executemany(sql, rows)
var = cursor.bindvars[1]
cursor.execute("select count(*) from TestExecuteMany")
count, = cursor.fetchone()
print count == len(rows)
print var.maxlength == 100
print var.maxlength
print var