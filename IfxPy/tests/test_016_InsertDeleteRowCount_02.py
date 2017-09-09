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

  def test_016_InsertDeleteRowCount_02(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_016)

  def run_test_016(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    if conn:
      result = IfxPy.exec_immediate(conn,"insert into t_string values(123,1.222333,'one to one')")
      if result:
        cols = IfxPy.num_fields(result)
        print "col:", cols
        rows = IfxPy.num_rows(result)
        print "affected row:", rows
      else:
        print IfxPy.stmt_errormsg()
      result = IfxPy.exec_immediate(conn,"delete from t_string where a=123")
      if result:
        cols = IfxPy.num_fields(result)
        print "col:", cols
        rows = IfxPy.num_rows(result)
        print "affected row:", rows
      else:
        print IfxPy.stmt_errormsg()
      IfxPy.close(conn)
    else:
      print "no connection:", IfxPy.conn_errormsg()

#__END__
#__LUW_EXPECTED__
#col: 0
#affected row: 1
#col: 0
#affected row: 1
#__ZOS_EXPECTED__
#col: 0
#affected row: 1
#col: 0
#affected row: 1
#__SYSTEMI_EXPECTED__
#col: 0
#affected row: 1
#col: 0
#affected row: 1
#__IDS_EXPECTED__
#col: 0
#affected row: 1
#col: 0
#affected row: 1
