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

  def test_100_SelectDeleteInsertFieldCount(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_100)

  def run_test_100(self):
    conn = ifx_db.connect(config.database, config.user, config.password)
    
    if conn:
      ifx_db.autocommit(conn, ifx_db.SQL_AUTOCOMMIT_OFF)

      stmt = ifx_db.exec_immediate(conn, "SELECT * FROM animals ORDER BY breed")
    
      fields1 = ifx_db.num_fields(stmt)
      
      print "int(%d)" % fields1
      
      stmt = ifx_db.exec_immediate(conn, "SELECT name, breed FROM animals ORDER BY breed")
      fields2 = ifx_db.num_fields(stmt)
      
      print "int(%d)" % fields2
      
      stmt = ifx_db.exec_immediate(conn, "DELETE FROM animals")
      fields3 = ifx_db.num_fields(stmt)
      
      print "int(%d)" % fields3
      
      stmt = ifx_db.exec_immediate(conn, "INSERT INTO animals values (0, 'cat', 'Pook', 3.2)")
      fields4 = ifx_db.num_fields(stmt)
        
      print "int(%d)" % fields4
      
      stmt = ifx_db.exec_immediate(conn, "SELECT name, breed, 'TEST' FROM animals")
      fields5 = ifx_db.num_fields(stmt)
        
      print "int(%d)" % fields5

      ifx_db.rollback(conn)
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#int(4)
#int(2)
#int(0)
#int(0)
#int(3)
#__ZOS_EXPECTED__
#int(4)
#int(2)
#int(0)
#int(0)
#int(3)
#__SYSTEMI_EXPECTED__
#int(4)
#int(2)
#int(0)
#int(0)
#int(3)
#__IDS_EXPECTED__
#int(4)
#int(2)
#int(0)
#int(0)
#int(3)
