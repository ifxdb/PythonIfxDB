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

  def test_011_DeleteRowCount(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_011)

  def run_test_011(self):
    conn = ifx_db.connect(config.database, config.user, config.password)
      
    if conn:
      ifx_db.autocommit(conn, ifx_db.SQL_AUTOCOMMIT_OFF)
      stmt = ifx_db.exec_immediate(conn, "DELETE FROM animals WHERE weight > 10.0")
      print "Number of affected rows: %d" % ifx_db.num_rows( stmt )
      ifx_db.rollback(conn)
      ifx_db.close(conn)
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#Number of affected rows: 3
#__ZOS_EXPECTED__
#Number of affected rows: 3
#__SYSTEMI_EXPECTED__
#Number of affected rows: 3
#__IDS_EXPECTED__
#Number of affected rows: 3
