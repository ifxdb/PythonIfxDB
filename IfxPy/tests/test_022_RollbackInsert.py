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

  def test_022_RollbackInsert(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_022)

  def run_test_022(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
      
    if conn:
      stmt = IfxPy.exec_immediate(conn, "SELECT count(*) FROM animals")
      res = IfxPy.fetch_tuple(stmt)
      rows = res[0]
      print rows
        
      IfxPy.autocommit(conn, 0)
      ac = IfxPy.autocommit(conn)
      if ac != 0:
        print "Cannot set IfxPy.AUTOCOMMIT_OFF\nCannot run test"
        #continue
        
      IfxPy.exec_immediate(conn, "INSERT INTO animals values (7,'bug','Brain Bug',10000.1)")
        
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
#8
#7
#__ZOS_EXPECTED__
#7
#8
#7
#__SYSTEMI_EXPECTED__
#7
#8
#7
#__IDS_EXPECTED__
#7
#8
#7
