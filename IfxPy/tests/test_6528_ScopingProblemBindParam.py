# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_6528_ScopingProblemBindParam(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_6528)

  def checked_db2_execute(self, stmt):
    IfxPy.execute(stmt)
    row = IfxPy.fetch_tuple(stmt)
    for i in row:
      print i
     
  def run_test_6528(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    server = IfxPy.server_info( conn )
    
    if conn:
      if (server.DBMS_NAME[0:3] == 'Inf'):
        sql = "SELECT TRIM(TRAILING FROM name) FROM animals WHERE breed = ?"
      else:
        sql = "SELECT RTRIM(name) FROM animals WHERE breed = ?"
      stmt = IfxPy.prepare(conn, sql)
      var = "cat"
      IfxPy.bind_param(stmt, 1, var, IfxPy.SQL_PARAM_INPUT)
      self.checked_db2_execute(stmt)
      IfxPy.close(conn)
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
