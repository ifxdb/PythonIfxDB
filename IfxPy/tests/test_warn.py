#
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2016
#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):
    def test_warn(self):
        obj = IfxDbTestFunctions()
        obj.assert_expect(self.run_test_warn)

    def run_test_warn(self):
        conn = IfxPy.connect(config.ConnStr, config.user, config.password)
            
        if conn:

            drop = "DROP TABLE TEST1"
            try:
                result = IfxPy.exec_immediate(conn,drop)
            except:
                pass

            # Create the table test1

            create = "CREATE TABLE TEST1 (COL1 CHAR(5))"
            result = IfxPy.exec_immediate(conn, create)

            # Insert a string longer than 5 characters to force an error 
            # IfxPy.stmt_warn() API

            query = 'INSERT INTO TEST1 VALUES (?)'
            stmt = IfxPy.prepare(conn, query)
            try:
                IfxPy.execute(stmt, ('ABCDEF',))
            except:
                pass
				
            print(IfxPy.stmt_warn(stmt))
			
            IfxPy.close(conn)
        else:
            print ("Connection failed.")

#__END__
#__IDS_EXPECTED__
#[Informix][Informix ODBC Driver]String data right truncation. SQLCODE=-11023
