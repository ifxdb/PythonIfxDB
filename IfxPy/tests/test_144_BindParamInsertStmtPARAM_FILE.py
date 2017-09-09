# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys, os
import ifx_db
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_144_BindParamInsertStmtPARAM_FILE(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_144)

  def run_test_144(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      # Drop the test table, in case it exists
      drop = 'DROP TABLE pictures'
      try:
        result = ifx_db.exec_immediate(conn, drop)
      except:
        pass
      
      # Create the test table
      create = 'CREATE TABLE pictures (id INTEGER, picture BLOB)'
      result = ifx_db.exec_immediate(conn, create)
      
      stmt = ifx_db.prepare(conn, "INSERT INTO pictures VALUES (0, ?)")
      
      picture = os.path.dirname(os.path.abspath(__file__)) + "/pic1.jpg"
      rc = ifx_db.bind_param(stmt, 1, picture, ifx_db.SQL_PARAM_INPUT, ifx_db.SQL_BINARY)
    
      rc = ifx_db.execute(stmt)
      
      num = ifx_db.num_rows(stmt)
      
      print num
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#1
#__ZOS_EXPECTED__
#1
#__SYSTEMI_EXPECTED__
#1
#__IDS_EXPECTED__
#1
