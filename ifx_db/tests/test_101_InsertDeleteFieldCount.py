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

  def test_101_InsertDeleteFieldCount(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_101)

  def run_test_101(self):
    conn = ifx_db.connect(config.database, config.user, config.password)
    if conn:
      result = ifx_db.exec_immediate(conn,"insert into t_string values(123,1.222333,'one to one')")
      if result:
        cols = ifx_db.num_fields(result)
        print "col: %d" % cols
        rows = ifx_db.num_rows(result)
        print "affected row: %d" % rows
      result = ifx_db.exec_immediate(conn,"delete from t_string where a=123")
      if result:
        cols = ifx_db.num_fields(result)
        print "col: %d" % cols
        rows = ifx_db.num_rows(result)
        print "affected row: %d" % rows
    else:
      print "no connection";    

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
