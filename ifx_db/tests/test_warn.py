#
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2016
#

import unittest, sys
import ifx_db
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):
    def test_warn(self):
        obj = IfxDbTestFunctions()
        obj.assert_expect(self.run_test_warn)

    def run_test_warn(self):
        conn = ifx_db.connect(config.database, config.user, config.password)
        
        # Get the server type
        serverinfo = ifx_db.server_info( conn )
    
        if conn:

            drop = "DROP TABLE WITH_CLOB"
            try:
                result = ifx_db.exec_immediate(conn,drop)
            except:
                pass

            # Create the table with_clob

            if (serverinfo.DBMS_NAME[0:3] != 'IDS'): 
                create = "CREATE TABLE WITH_CLOB (id SMALLINT NOT NULL, clob_col CLOB(1k))"
            else:
                create = "CREATE TABLE WITH_CLOB (id SMALLINT NOT NULL, clob_col CLOB(smart))"
            result = ifx_db.exec_immediate(conn, create)

            # Select the result from the table. This is just to verify we get appropriate warning using
            # ifx_db.stmt_warn() API

            query = 'SELECT * FROM WITH_CLOB'
            if (serverinfo.DBMS_NAME[0:3] != 'IDS'):
                stmt = ifx_db.prepare(conn, query, {ifx_db.SQL_ATTR_CURSOR_TYPE: ifx_db.SQL_CURSOR_KEYSET_DRIVEN})
            else:
               stmt = ifx_db.prepare(conn, query)

            ifx_db.execute(stmt)
            data = ifx_db.fetch_both( stmt )
            if data:
                print("Success")
            else:
                print("No Data")
                print(ifx_db.stmt_warn(stmt))
            ifx_db.close(conn)
        else:
            print ("Connection failed.")

#__END__
#__LUW_EXPECTED__
#No Data[IBM][CLI Driver][DB2%s] SQL0100W  No row was found for FETCH, UPDATE or DELETE; or the result of a query is an empty table.  SQLSTATE=02000 SQLCODE=100
#__ZOS_EXPECTED__
#No Data[IBM][CLI Driver][DB2]
# SQL0100W  No row was found for FETCH, UPDATE or DELETE; or the result of a query is an empty table.  SQLSTATE=02000 SQLCODE=100
#__SYSTEMI_EXPECTED__
#No Data
#__IDS_EXPECTED__
#No Data
#[IBM][CLI Driver][IDS/%s] SQL0100W  No row was found for FETCH, UPDATE or DELETE; or the result of a query is an empty table.  SQLSTATE=02000 SQLCODE=100
