# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_114_NumericTest_01(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_114)

  def run_test_114(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      drop = "drop table numericliteral"

      try:
        IfxPy.exec_immediate( conn, drop )
      except:
        pass
      
      create = "create table numericliteral ( id INTEGER, num INTEGER )"
      IfxPy.exec_immediate(conn, create)
      
      insert = "INSERT INTO numericliteral (id, num) values (1,5)"
      IfxPy.exec_immediate(conn, insert)

      insert = "UPDATE numericliteral SET num = '10' WHERE num = '5'"
      IfxPy.exec_immediate(conn, insert)
      
      stmt = IfxPy.prepare(conn, "SELECT * FROM numericliteral")
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
#__LUW_EXPECTED__
#1
#10
#__ZOS_EXPECTED__
#1
#10
#__SYSTEMI_EXPECTED__
#1
#10
#__IDS_EXPECTED__
#1
#10
