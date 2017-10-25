
import IfxPyDbi as dbapi2

ConStr = "SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;SERVICE=9088;UID=informix;PWD=xxxxx;"

# netstat -a | findstr  9088
conn = dbapi2.connect( ConStr, "", "")

cur = conn.cursor()

try:
    stmt = cur.execute('drop table t1;')
except:
    print ('FYI: drop table failed')

cur.execute('create table t1 ( c1 int, c2 char(20), c3 int, c4 int ) ')

# example that inserts many records at a time
days = [ (1, 'Sunday',  101, 201),
         (2, 'Monday',  102, 202),
         (3, 'Tuesday', 103, 203),
         (4, 'Wednesday', 104, 204),
         (5, 'Thursday', 105, 205),
         (6, 'Friday', 106, 206),
         (7, 'Saturday', 1027, 207),
       ]
cur.executemany('INSERT INTO t1 VALUES (?,?,?,?)', days)

conn.commit ()

cur.execute ("SELECT * FROM t1")
rows = cur.fetchall()
for i, row in enumerate(rows):
    print ("Row", i, "value = ", row)

cur.close()

conn.close()
print ("Done")

