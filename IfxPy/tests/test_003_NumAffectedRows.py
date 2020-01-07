# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_003_NumAffectedRows(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_003)
    
  def run_test_003(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
      
    if conn:
      IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_OFF)
      sql = 'UPDATE animals SET id = 9'
      res = IfxPy.exec_immediate(conn, sql)
      print("Number of affected rows: %d" % IfxPy.num_rows(res))
      IfxPy.rollback(conn)
      IfxPy.close(conn)
    else:
      print("Connection failed.")

#__END__
#__LUW_EXPECTED__
#Number of affected rows: 7
#__ZOS_EXPECTED__
#Number of affected rows: 7
#__SYSTEMI_EXPECTED__
#Number of affected rows: 7
#__IDS_EXPECTED__
#Number of affected rows: 7
