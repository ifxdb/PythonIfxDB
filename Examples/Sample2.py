# Sample2.py
import IfxPy


def my_Sample():
    ConStr = "SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;SERVICE=9088;UID=informix;PWD=xxxxx;"

    try:
        # netstat -a | findstr  9088
        conn = IfxPy.connect( ConStr, "", "")
    except Exception as e:
        print ('ERROR: Connect failed')
        print ( e )
        quit()


    try:
        sql = "drop table t1;"
        print ( sql )
        stmt = IfxPy.exec_immediate(conn, sql)
    except:
        print ('FYI: drop table failed')

    sql = "create table t1 ( c1 int, c2 char(20), c3 int, c4 int ) ;"
    stmt = IfxPy.exec_immediate(conn, sql)


    sql = "INSERT INTO t1 (c1, c2, c3, c4) VALUES ( ?, ?, ?, ? )"
    stmt = IfxPy.prepare(conn, sql)

    c1 = None
    c2 = None
    c3 = None
    c4 = None
    # Create bindings for the parameter
    IfxPy.bind_param(stmt, 1, c1, IfxPy.SQL_PARAM_INPUT, IfxPy.SQL_INTEGER)
    IfxPy.bind_param(stmt, 2, c2, IfxPy.SQL_PARAM_INPUT, IfxPy.SQL_CHAR)
    IfxPy.bind_param(stmt, 3, c1, IfxPy.SQL_PARAM_INPUT, IfxPy.SQL_INTEGER)
    IfxPy.bind_param(stmt, 4, c1, IfxPy.SQL_PARAM_INPUT, IfxPy.SQL_INTEGER)

    print("Inserting Recors ......")
    i = 0
    while i < 10:
        i += 1
        c1 = 100 + i
        c2 = "Testing {0}".format(i)
        c3 = 20000 + i
        c4 = 50000 + i
        # supply new values as a tuple
        IfxPy.execute(stmt, (c1, c2, c3, c4) )


    # Try select those rows we have just inserted
    print("Selecting Recors ......")
    sql = "SELECT * FROM t1"
    stmt = IfxPy.exec_immediate(conn, sql)
    tu = IfxPy.fetch_tuple(stmt)
    rc = 0
    while tu != False:
        rc += 1
        print( tu )
        tu = IfxPy.fetch_tuple(stmt)

    print()
    print( "Total Record Inserted {}".format(i) )
    print( "Total Record Selected {}".format(rc) )

    # Free up memory used by result and then stmt too
    IfxPy.free_result(stmt)
    IfxPy.free_stmt (stmt)

    # close the connection
    IfxPy.close(conn)

    print ("Done")

####### Run the sample function ######
my_Sample()
