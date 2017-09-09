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

  def test_110_FieldNum(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_110)

  def run_test_110(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    server = IfxPy.server_info( conn )
    
    if conn:
      stmt = IfxPy.exec_immediate(conn, "SELECT * FROM animals ORDER BY breed")
    
      num1 = IfxPy.field_num(stmt, "id")
      num2 = IfxPy.field_num(stmt, "breed")
      num3 = IfxPy.field_num(stmt, "name")
      num4 = IfxPy.field_num(stmt, "weight")
      num5 = IfxPy.field_num(stmt, "test")
      num6 = IfxPy.field_num(stmt, 8)
      num7 = IfxPy.field_num(stmt, 1)
      num8 = IfxPy.field_num(stmt, "WEIGHT")
      
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
