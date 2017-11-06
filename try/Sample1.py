
import IfxPy

ConStr = "SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;SERVICE=9088;UID=informix;PWD=Blue4You;"

# netstat -a | findstr  9088
conn = IfxPy.connect( ConStr, "", "")

SetupSqlSet = [
    "create table t1 ( c1 int, c2 char(20), c3 int, c4 int ) ;", 
    "insert into t1 values( 1, 'Sunday', 101, 201 );",
    "insert into t1 values( 2, 'Monday', 102, 202 );",
    "insert into t1 values( 3, 'Tuesday', 103, 203 );",
    "insert into t1 values( 4, 'Wednesday', 104, 204 );",
    "insert into t1 values( 5, 'Thursday', 105, 2005 );",
    "insert into t1 values( 6, 'Friday', 106, 206 );",
    "insert into t1 values( 7, 'Saturday', 107, 207 );"
]

try:
    sql = "drop table t1;"
    print ( sql )
    stmt = IfxPy.exec_immediate(conn, sql)
except:
    print ('FYI: drop table failed')
	
for sql in SetupSqlSet:
    print (sql)
    stmt = IfxPy.exec_immediate(conn, sql)


sql = "SELECT * FROM t1"
stmt = IfxPy.exec_immediate(conn, sql)
dictionary = IfxPy.fetch_both(stmt)

rc = 0
while dictionary != False:
    rc = rc + 1
    print ("--  Record {0} --".format(rc))
    print ("c1 is : ",  dictionary[0])
    print ("c2 is : ", dictionary[1])
    print ("c3 is : ", dictionary["c3"])
    print ("c4 is : ", dictionary[3])
    print (" ")
    dictionary = IfxPy.fetch_both(stmt)

IfxPy.close(conn)

print ("Done")
