# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import ifx_db
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_115_NumericTest_02(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_115)

  def run_test_115(self):
    conn = ifx_db.connect(config.database, config.user, config.password)

    server = ifx_db.server_info( conn )
    if (server.DBMS_NAME[0:3] == 'IDS'):
      op = {ifx_db.ATTR_CASE: ifx_db.CASE_UPPER}
      ifx_db.set_option(conn, op, 1)
    
    if conn:
      drop = "drop table numericliteral"
      try:
        ifx_db.exec_immediate( conn, drop )
      except:
        pass

      create = "create table numericliteral ( id INTEGER, data VARCHAR(50) )"
      ifx_db.exec_immediate(conn, create)

      insert = "INSERT INTO numericliteral (id, data) values (12, 'NUMERIC LITERAL TEST')"
      ifx_db.exec_immediate(conn, insert)

      stmt = ifx_db.prepare(conn, "SELECT data FROM numericliteral")
      ifx_db.execute(stmt)
      
#      NOTE: This is a workaround
#      function fetch_object() to be implemented...
#      row = ifx_db.fetch_object(stmt, 0)
      
      class Row:
          pass
      
      row = Row()
      ifx_db.fetch_row(stmt, 0)
      if (server.DBMS_NAME[0:3] != 'IDS'):
        row.DATA = ifx_db.result(stmt, 'DATA')
      else:
        row.DATA = ifx_db.result(stmt, 'data')
      print row.DATA

      insert = "UPDATE numericliteral SET data = '@@@@@@@@@@' WHERE id = '12'"
      ifx_db.exec_immediate(conn, insert)

      stmt = ifx_db.prepare(conn, "SELECT data FROM numericliteral")
      ifx_db.execute(stmt)
      
#      row = ifx_db.fetch_object(stmt, 0)
      ifx_db.fetch_row(stmt, 0)
      if (server.DBMS_NAME[0:3] != 'IDS'):
        row.DATA = ifx_db.result(stmt, 'DATA')
      else:
        row.DATA = ifx_db.result(stmt, 'data')
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
