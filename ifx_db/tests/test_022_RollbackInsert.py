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

  def test_022_RollbackInsert(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_022)

  def run_test_022(self):
    conn = ifx_db.connect(config.database, config.user, config.password)
      
    if conn:
      stmt = ifx_db.exec_immediate(conn, "SELECT count(*) FROM animals")
      res = ifx_db.fetch_tuple(stmt)
      rows = res[0]
      print rows
        
      ifx_db.autocommit(conn, 0)
      ac = ifx_db.autocommit(conn)
      if ac != 0:
        print "Cannot set ifx_db.AUTOCOMMIT_OFF\nCannot run test"
        #continue
        
      ifx_db.exec_immediate(conn, "INSERT INTO animals values (7,'bug','Brain Bug',10000.1)")
        
      stmt = ifx_db.exec_immediate(conn, "SELECT count(*) FROM animals")
      res = ifx_db.fetch_tuple(stmt)
      rows = res[0]
      print rows
        
      ifx_db.rollback(conn)
      
      stmt = ifx_db.exec_immediate(conn, "SELECT count(*) FROM animals")
      res = ifx_db.fetch_tuple(stmt)
      rows = res[0]
      print rows
      ifx_db.close(conn)
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
