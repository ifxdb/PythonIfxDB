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

  def test_111_FieldNumAddCol(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_111)

  def run_test_111(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    server = IfxPy.server_info( conn )
    if conn:
      IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_OFF)

      insert = "INSERT INTO animals values (7, 'cat', 'Benji', 5.1)"
      IfxPy.exec_immediate(conn, insert)
      
      stmt = IfxPy.exec_immediate(conn, "SELECT breed, COUNT(breed) AS number FROM animals GROUP BY breed ORDER BY breed")
    
      if (server.DBMS_NAME[0:3] == 'Inf'):
        num1 = IfxPy.field_num(stmt, "id")
        num2 = IfxPy.field_num(stmt, "breed")
        num3 = IfxPy.field_num(stmt, "number")
        num4 = IfxPy.field_num(stmt, "NUMBER")
        num5 = IfxPy.field_num(stmt, "bREED")
        num6 = IfxPy.field_num(stmt, 8)
        num7 = IfxPy.field_num(stmt, 1)
        num8 = IfxPy.field_num(stmt, "WEIGHT")
      else:
        num1 = IfxPy.field_num(stmt, "ID")
        num2 = IfxPy.field_num(stmt, "BREED")
        num3 = IfxPy.field_num(stmt, "NUMBER")
        num4 = IfxPy.field_num(stmt, "number")
        num5 = IfxPy.field_num(stmt, "Breed")
        num6 = IfxPy.field_num(stmt, 8)
        num7 = IfxPy.field_num(stmt, 1)
        num8 = IfxPy.field_num(stmt, "weight")
  
      print "%s" % num1
      print "int(%d)" % num2
      print "int(%d)" % num3
      print "%s" % num4
      
      print "%s" % num5
      print "%s" % num6
      print "int(%d)" % num7
      print "%s" % num8

      IfxPy.rollback(conn)
    else:
      print "Connection failed."

#__END__
#__IDS_EXPECTED__
#False
#int(0)
#int(1)
#False
#False
#False
#int(1)
#False
