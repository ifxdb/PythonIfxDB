
import ifx_db

# in case of connection problem check the service port mapped to which ip
# for example the port you configured is 9088 then
#
# netstat -a | findstr  9088
#ConStr = "SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;PROTOCOL=onsoctcp;SERVICE=9088;UID=TestUser1;PWD=MySimplePass1;"
ConStr = "SERVER=ids1210;DATABASE=stores7;UID=informix;PWD=ximrofni;"
conn = ifx_db.connect( ConStr, "", "")


SetupSqlSet = [
    "drop table t1;", 
    "create table t1 ( c1 int, c2 char(20), c3 int, c4 int ) ;", 
    "insert into t1 values( 1, 'Sunday', 101, 201 );",
    "insert into t1 values( 2, 'Monday', 102, 202 );",
    "insert into t1 values( 3, 'Tuesday', 103, 203 );",
    "insert into t1 values( 4, 'Wednesday', 104, 204 );",
    "insert into t1 values( 5, 'Thursday', 105, 2005 );",
    "insert into t1 values( 6, 'Friday', 106, 206 );",
    "insert into t1 values( 7, 'Saturday', 107, 207 );"
]


for sql in SetupSqlSet:
    print sql
    stmt = ifx_db.exec_immediate(conn, sql)


sql = "SELECT * FROM t1"
stmt2 = ifx_db.exec_immediate(conn, sql)
dictionary = ifx_db.fetch_both(stmt2)

rc = 0
while dictionary != False:
    rc = rc + 1
    print "--  Record {0} --".format(rc)
    print "c1 is : ",  dictionary[0]
    print "c2 is : ", dictionary[1]
    print "c3 is : ", dictionary["c3"]
    print "c4 is : ", dictionary[3]
    print " "
    dictionary = ifx_db.fetch_both(stmt2)

ifx_db.close(conn)

print "Done"

