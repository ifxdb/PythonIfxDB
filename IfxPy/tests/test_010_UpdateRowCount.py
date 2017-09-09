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
  
  def test_010_UpdateRowCount(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_010)

  def run_test_010(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
     
    if conn:
      IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_OFF)
      stmt = IfxPy.exec_immediate(conn, "UPDATE animals SET name = 'flyweight' WHERE weight < 10.0")
      print "Number of affected rows: %d" % IfxPy.num_rows( stmt )
      IfxPy.rollback(conn)
      IfxPy.close(conn)
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#Number of affected rows: 4
#__ZOS_EXPECTED__
#Number of affected rows: 4
#__SYSTEMI_EXPECTED__
#Number of affected rows: 4
#__IDS_EXPECTED__
#Number of affected rows: 4
