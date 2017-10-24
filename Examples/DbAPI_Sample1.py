
import IfxPyi as dbapi2

ConStr = "SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;SERVICE=9088;UID=informix;PWD=xxxx;"

# netstat -a | findstr  9088
conn = dbapi2.connect( ConStr, "", "")

cur = conn.cursor()

try:
    stmt = cur.execute('drop table t1;')
except:
    print ('FYI: drop table failed')

cur.execute('create table t1 ( c1 int, c2 char(20), c3 int, c4 int ) ')

cur.execute("insert into t1 values( 1, 'Sunday', 101, 201 )")
cur.execute("insert into t1 values( 2, 'Monday', 102, 202 )")
cur.execute("insert into t1 values( 3, 'Tuesday', 103, 203 )")
cur.execute("insert into t1 values( 4, 'Wednesday', 104, 204 )")
cur.execute("insert into t1 values( 5, 'Thursday', 105, 2005 )")
cur.execute("insert into t1 values( 6, 'Friday', 106, 206 )")
cur.execute("insert into t1 values( 7, 'Saturday', 107, 207 )")

conn.commit ()

cur.execute ("SELECT * FROM t1")
rows = cur.fetchall()
for i, row in enumerate(rows):
    print ("Row", i, "value = ", row)

cur.close()

conn.close()
print ("Done")

