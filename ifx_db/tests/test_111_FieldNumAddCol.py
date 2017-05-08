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

  def test_111_FieldNumAddCol(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_111)

  def run_test_111(self):
    conn = ifx_db.connect(config.database, config.user, config.password)
    server = ifx_db.server_info( conn )

    if conn:
      ifx_db.autocommit(conn, ifx_db.SQL_AUTOCOMMIT_OFF)

      insert = "INSERT INTO animals values (7, 'cat', 'Benji', 5.1)"
      ifx_db.exec_immediate(conn, insert)
      
      stmt = ifx_db.exec_immediate(conn, "SELECT breed, COUNT(breed) AS number FROM animals GROUP BY breed ORDER BY breed")
    
      if (server.DBMS_NAME[0:3] == 'IDS'):
        num1 = ifx_db.field_num(stmt, "id")
        num2 = ifx_db.field_num(stmt, "breed")
        num3 = ifx_db.field_num(stmt, "number")
        num4 = ifx_db.field_num(stmt, "NUMBER")
        num5 = ifx_db.field_num(stmt, "bREED")
        num6 = ifx_db.field_num(stmt, 8)
        num7 = ifx_db.field_num(stmt, 1)
        num8 = ifx_db.field_num(stmt, "WEIGHT")
      else:
        num1 = ifx_db.field_num(stmt, "ID")
        num2 = ifx_db.field_num(stmt, "BREED")
        num3 = ifx_db.field_num(stmt, "NUMBER")
        num4 = ifx_db.field_num(stmt, "number")
        num5 = ifx_db.field_num(stmt, "Breed")
        num6 = ifx_db.field_num(stmt, 8)
        num7 = ifx_db.field_num(stmt, 1)
        num8 = ifx_db.field_num(stmt, "weight")
  
      print "%s" % num1
      print "int(%d)" % num2
      print "int(%d)" % num3
      print "%s" % num4
      
      print "%s" % num5
      print "%s" % num6
      print "int(%d)" % num7
      print "%s" % num8

      ifx_db.rollback(conn)
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#False
#int(0)
#int(1)
#False
#False
#False
#int(1)
#False
#__ZOS_EXPECTED__
#False
#int(0)
#int(1)
#False
#False
#False
#int(1)
#False
#__SYSTEMI_EXPECTED__
#False
#int(0)
#int(1)
#False
#False
#False
#int(1)
#False
#__IDS_EXPECTED__
#False
#int(0)
#int(1)
#False
#False
#False
#int(1)
#False
