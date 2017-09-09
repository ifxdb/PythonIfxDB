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

  def test_115_NumericTest_02(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_115)

  def run_test_115(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)

    server = IfxPy.server_info( conn )
    if (server.DBMS_NAME[0:3] == 'Inf'):
      op = {IfxPy.ATTR_CASE: IfxPy.CASE_UPPER}
      IfxPy.set_option(conn, op, 1)
    
    if conn:
      drop = "drop table numericliteral"
      try:
        IfxPy.exec_immediate( conn, drop )
      except:
        pass

      create = "create table numericliteral ( id INTEGER, data VARCHAR(50) )"
      IfxPy.exec_immediate(conn, create)

      insert = "INSERT INTO numericliteral (id, data) values (12, 'NUMERIC LITERAL TEST')"
      IfxPy.exec_immediate(conn, insert)

      stmt = IfxPy.prepare(conn, "SELECT data FROM numericliteral")
      IfxPy.execute(stmt)
      
#      NOTE: This is a workaround
#      function fetch_object() to be implemented...
#      row = IfxPy.fetch_object(stmt, 0)
      
      class Row:
          pass
      
      row = Row()
      IfxPy.fetch_row(stmt, 0)
      if (server.DBMS_NAME[0:3] != 'Inf'):
        row.DATA = IfxPy.result(stmt, 'DATA')
      else:
        row.DATA = IfxPy.result(stmt, 'data')
      print row.DATA

      insert = "UPDATE numericliteral SET data = '@@@@@@@@@@' WHERE id = '12'"
      IfxPy.exec_immediate(conn, insert)

      stmt = IfxPy.prepare(conn, "SELECT data FROM numericliteral")
      IfxPy.execute(stmt)
      
#      row = IfxPy.fetch_object(stmt, 0)
      IfxPy.fetch_row(stmt, 0)
      if (server.DBMS_NAME[0:3] != 'Inf'):
        row.DATA = IfxPy.result(stmt, 'DATA')
      else:
        row.DATA = IfxPy.result(stmt, 'data')
      print row.DATA
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#NUMERIC LITERAL TEST
#@@@@@@@@@@
#__ZOS_EXPECTED__
#NUMERIC LITERAL TEST
#@@@@@@@@@@
#__SYSTEMI_EXPECTED__
#NUMERIC LITERAL TEST
#@@@@@@@@@@
#__IDS_EXPECTED__
#NUMERIC LITERAL TEST
#@@@@@@@@@@
