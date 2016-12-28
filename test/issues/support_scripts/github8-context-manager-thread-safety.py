import cx_Oracle
from threading import Thread
CNT = 40

class TSelector(Thread):
    def run(self):
        con = cx_Oracle.connect('cx_Oracle/dev@localhost')
        cur = cur_acc = con.cursor()
        cur.execute('SELECT 1 FROM DUAL')
        for row in cur:
            print('Thread: %s Got row: %s' % (id(self), row,))
        cur.close()
        con.close()

threads = [TSelector() for _ in range(CNT)]
[t.start() for t in threads]
[t.join() for t in threads]
