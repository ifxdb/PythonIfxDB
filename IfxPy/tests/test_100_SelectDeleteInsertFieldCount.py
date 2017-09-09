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

  def test_100_SelectDeleteInsertFieldCount(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_100)

  def run_test_100(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_OFF)

      stmt = IfxPy.exec_immediate(conn, "SELECT * FROM animals ORDER BY breed")
    
      fields1 = IfxPy.num_fields(stmt)
      
      print "int(%d)" % fields1
      
      stmt = IfxPy.exec_immediate(conn, "SELECT name, breed FROM animals ORDER BY breed")
      fields2 = IfxPy.num_fields(stmt)
      
      print "int(%d)" % fields2
      
      stmt = IfxPy.exec_immediate(conn, "DELETE FROM animals")
      fields3 = IfxPy.num_fields(stmt)
      
      print "int(%d)" % fields3
      
      stmt = IfxPy.exec_immediate(conn, "INSERT INTO animals values (0, 'cat', 'Pook', 3.2)")
      fields4 = IfxPy.num_fields(stmt)
        
      print "int(%d)" % fields4
      
      stmt = IfxPy.exec_immediate(conn, "SELECT name, breed, 'TEST' FROM animals")
      fields5 = IfxPy.num_fields(stmt)
        
      print "int(%d)" % fields5

      IfxPy.rollback(conn)
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
