
import ifx_db

# Fetching rows or columns from result sets
# https://www.ibm.com/support/knowledgecenter/en/SSEPGG_9.5.0/com.ibm.db2.luw.apdv.python.doc/doc/t0054388.html

# in case of connection problem check the service port mapped to which ip
# for example the port you configured is 9088 then
#
# netstat -a | findstr  9088
ConStr = "SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;PROTOCOL=onsoctcp;SERVICE=9088;UID=TestUser1;PWD=MySimplePass1;"

conn = ifx_db.connect( ConStr, "", "")


SetupSqlSet = [
    "drop table t1;", 
    "create table t1 ( c1 int, c2 char(20), c3 int, c4 int ) ;", 
    "insert into t1 values( 1, 'val 1', 101, 201 );",
    "insert into t1 values( 2, 'val 2', 102, 202 );",
    "insert into t1 values( 3, 'val 3', 103, 203 );",
    "insert into t1 values( 4, 'val 4', 104, 204 );",
    "insert into t1 values( 5, 'val 5', 105, 2005 );"
]

for sql in SetupSqlSet:
    print sql
    stmt = ifx_db.exec_immediate(conn, sql)


sql = "SELECT * FROM t1"
stmt = ifx_db.exec_immediate(conn, sql)
dictionary = ifx_db.fetch_both(stmt)
while dictionary != False:
    print "c1 is : ",  dictionary["c1"]
    print "c2 is : ", dictionary[1]
    print "c3 is : ", dictionary[2]
    print "c4 is : ", dictionary["c4"]
    print "Going for next rec"
    print " "
    dictionary = ifx_db.fetch_both(stmt)

conn.close()

print "Done"
