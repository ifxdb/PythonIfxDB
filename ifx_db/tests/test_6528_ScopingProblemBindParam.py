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

  def test_6528_ScopingProblemBindParam(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_6528)

  def checked_db2_execute(self, stmt):
    ifx_db.execute(stmt)
    row = ifx_db.fetch_tuple(stmt)
    for i in row:
      print i
     
  def run_test_6528(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    server = ifx_db.server_info( conn )
    
    if conn:
      if (server.DBMS_NAME[0:3] == 'IDS'):
        sql = "SELECT TRIM(TRAILING FROM name) FROM animals WHERE breed = ?"
      else:
        sql = "SELECT RTRIM(name) FROM animals WHERE breed = ?"
      stmt = ifx_db.prepare(conn, sql)
      var = "cat"
      ifx_db.bind_param(stmt, 1, var, ifx_db.SQL_PARAM_INPUT)
      self.checked_db2_execute(stmt)
      ifx_db.close(conn)
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#Pook
#__ZOS_EXPECTED__
#Pook
#__SYSTEMI_EXPECTED__
#Pook
#__IDS_EXPECTED__
#Pook
