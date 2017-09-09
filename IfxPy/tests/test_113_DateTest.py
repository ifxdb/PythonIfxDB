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

  def test_113_DateTest(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_113)

  def run_test_113(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      drop = "DROP TABLE datetest"
      try:
        IfxPy.exec_immediate( conn, drop )
      except:
        pass
      
      create = "CREATE TABLE datetest ( id INTEGER, mydate DATE )"
      IfxPy.exec_immediate(conn, create)

      insert = "INSERT INTO datetest (id, mydate) VALUES (1,'03-27-1982')"
      IfxPy.exec_immediate(conn, insert)
      insert = "INSERT INTO datetest (id, mydate) VALUES (2,'07-08-1981')"
      IfxPy.exec_immediate(conn, insert)
      
      stmt = IfxPy.prepare(conn, "SELECT * FROM datetest")
      IfxPy.execute(stmt)

      result = IfxPy.fetch_row( stmt )
      while ( result ):
        row0 = IfxPy.result(stmt, 0)
        row1 = IfxPy.result(stmt, 1)
        print row0
        print row1
        result = IfxPy.fetch_row( stmt )
    else:
      print "Connection failed."

#__END__
#__IDS_EXPECTED__
#1
#1982-03-27
#2
#1981-07-08
