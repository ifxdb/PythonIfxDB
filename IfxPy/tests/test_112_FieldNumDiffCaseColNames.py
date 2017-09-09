# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import ifx_db
import config
import os
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_112_FieldNumDiffCaseColNames(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_112)

  def run_test_112(self):
    os.environ['DELIMIDENT'] = 'y'
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)

    if conn:
      drop = "DROP TABLE ftest"
      try:
        ifx_db.exec_immediate( conn, drop )
      except:
        pass
      
      create = "CREATE TABLE ftest ( \"TEST\" INTEGER, \"test\" INTEGER, \"Test\" INTEGER  )"
      ifx_db.exec_immediate(conn, create)
      
      insert = "INSERT INTO ftest VALUES (1,2,3)"
      ifx_db.exec_immediate(conn, insert)
      
      stmt = ifx_db.exec_immediate(conn, "SELECT * FROM ftest")
    
      num1 = ifx_db.field_num(stmt, "TEST")
      num2 = ifx_db.field_num(stmt, 'test')
      num3 = ifx_db.field_num(stmt, 'Test')
      
      print "int(%d)" % num1
      print "int(%d)" % num2
      print "int(%d)" % num3
      
    else:
      print "Connection failed."

#__END__
#__IDS_EXPECTED__
#int(0)
#int(1)
#int(2)
