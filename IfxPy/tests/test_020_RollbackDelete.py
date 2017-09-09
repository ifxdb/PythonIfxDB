# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_020_RollbackDelete(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_020)

  def run_test_020(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
      
    if conn:
        
      stmt = IfxPy.exec_immediate(conn, "SELECT count(*) FROM animals")
      res = IfxPy.fetch_tuple(stmt)
      rows = res[0]
      print rows
      
      IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_OFF)
      ac = IfxPy.autocommit(conn)
      if ac != 0:
        print "Cannot set IfxPy.SQL_AUTOCOMMIT_OFF\nCannot run test"
        #continue 
      
      IfxPy.exec_immediate(conn, "DELETE FROM animals")
      
      stmt = IfxPy.exec_immediate(conn, "SELECT count(*) FROM animals")
      res = IfxPy.fetch_tuple(stmt)
      rows = res[0]
      print rows
       
      IfxPy.rollback(conn)
       
      stmt = IfxPy.exec_immediate(conn, "SELECT count(*) FROM animals")
      res = IfxPy.fetch_tuple(stmt)
      rows = res[0]
      print rows
      IfxPy.close(conn)
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#7
#0
#7
#__ZOS_EXPECTED__
#7
#0
#7
#__SYSTEMI_EXPECTED__
#7
#0
#7
#__IDS_EXPECTED__
#7
#0
#7
