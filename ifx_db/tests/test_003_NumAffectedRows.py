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

  def test_003_NumAffectedRows(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_003)
    
  def run_test_003(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
      
    if conn:
      ifx_db.autocommit(conn, ifx_db.SQL_AUTOCOMMIT_OFF)
      sql = 'UPDATE animals SET id = 9'
      res = ifx_db.exec_immediate(conn, sql)
      print "Number of affected rows: %d" % ifx_db.num_rows(res)
      ifx_db.rollback(conn)
      ifx_db.close(conn)
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#Number of affected rows: 7
#__ZOS_EXPECTED__
#Number of affected rows: 7
#__SYSTEMI_EXPECTED__
#Number of affected rows: 7
#__IDS_EXPECTED__
#Number of affected rows: 7
