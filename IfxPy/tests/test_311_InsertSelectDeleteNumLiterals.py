#
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_311_InsertSelectDeleteNumLiterals(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_311)

  def run_test_311(self):
    # Make a connection
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)

    if conn:
       IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_ON )

       # Drop the tab_num_literals table, in case it exists
       drop = 'DROP TABLE tab_num_literals'
       result = ''
       try:
         result = IfxPy.exec_immediate(conn, drop)
       except:
         pass
       # Create the animal table
       create = "CREATE TABLE tab_num_literals (col1 INTEGER, col2 FLOAT, col3 DECIMAL(7,2))"
       result = IfxPy.exec_immediate(conn, create)
   
       insert = "INSERT INTO tab_num_literals values ('11.22', '33.44', '55.66')"
       res = IfxPy.exec_immediate(conn, insert)
       print "Number of inserted rows:", IfxPy.num_rows(res)

       stmt = IfxPy.prepare(conn, "SELECT col1, col2, col3 FROM tab_num_literals WHERE col1 = '11'")
       IfxPy.execute(stmt)
       data = IfxPy.fetch_both(stmt)
       while ( data ):
         print data[0]
         print data[1]
         print data[2]
         data = IfxPy.fetch_both(stmt)

       sql = "UPDATE tab_num_literals SET col1 = 77 WHERE col2 = 33.44"
       res = IfxPy.exec_immediate(conn, sql)
       print "Number of updated rows:", IfxPy.num_rows(res)

       stmt = IfxPy.prepare(conn, "SELECT col1, col2, col3 FROM tab_num_literals WHERE col2 > '33'")
       IfxPy.execute(stmt)
       data = IfxPy.fetch_both(stmt)
       while ( data ):
         print data[0]
         print data[1]
         print data[2]
         data = IfxPy.fetch_both(stmt)
	 
       sql = "DELETE FROM tab_num_literals WHERE col1 > '10.0'"
       res = IfxPy.exec_immediate(conn, sql)
       print "Number of deleted rows:", IfxPy.num_rows(res)

       stmt = IfxPy.prepare(conn, "SELECT col1, col2, col3 FROM tab_num_literals WHERE col3 < '56'")
       IfxPy.execute(stmt)
       data = IfxPy.fetch_both(stmt)
       while ( data ):
         print data[0]
         print data[1]
         print data[2]
         data = IfxPy.fetch_both(stmt)

       IfxPy.rollback(conn)
       IfxPy.close(conn)

#__END__
#__LUW_EXPECTED__
#Number of inserted rows: 1
#11
#33.44
#55.66
#Number of updated rows: 1
#77
#33.44
#55.66
#Number of deleted rows: 1
#__ZOS_EXPECTED__
#Number of inserted rows: 1
#11
#33.44
#55.66
#Number of updated rows: 1
#77
#33.44
#55.66
#Number of deleted rows: 1
#__SYSTEMI_EXPECTED__
#Number of inserted rows: 1
#11
#33.44
#55.66
#Number of updated rows: 1
#77
#33.44
#55.66
#Number of deleted rows: 1
#__IDS_EXPECTED__
#Number of inserted rows: 1
#11
#33.44
#55.66
#Number of updated rows: 1
#77
#33.44
#55.66
#Number of deleted rows: 1
