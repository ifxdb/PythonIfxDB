# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_011_DeleteRowCount(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_011)

  def run_test_011(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
      
    if conn:
      IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_OFF)
      stmt = IfxPy.exec_immediate(conn, "DELETE FROM animals WHERE weight > 10.0")
      print "Number of affected rows: %d" % IfxPy.num_rows( stmt )
      IfxPy.rollback(conn)
      IfxPy.close(conn)
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
