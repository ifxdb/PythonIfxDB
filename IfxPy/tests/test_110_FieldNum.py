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

  def test_110_FieldNum(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_110)

  def run_test_110(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    server = ifx_db.server_info( conn )
    
    if conn:
      stmt = ifx_db.exec_immediate(conn, "SELECT * FROM animals ORDER BY breed")
    
      num1 = ifx_db.field_num(stmt, "id")
      num2 = ifx_db.field_num(stmt, "breed")
      num3 = ifx_db.field_num(stmt, "name")
      num4 = ifx_db.field_num(stmt, "weight")
      num5 = ifx_db.field_num(stmt, "test")
      num6 = ifx_db.field_num(stmt, 8)
      num7 = ifx_db.field_num(stmt, 1)
      num8 = ifx_db.field_num(stmt, "WEIGHT")
      
      print "int(%d)" % num1
      print "int(%d)" % num2
      print "int(%d)" % num3
      print "int(%d)" % num4
      
      print "%s" % num5
      print "%s" % num6
      print "int(%d)" % num7
      print "%s" % num8
    else:
      print "Connection failed."

#__END__
#__IDS_EXPECTED__
#int(0)
#int(1)
#int(2)
#int(3)
#False
#False
#int(1)
#False
