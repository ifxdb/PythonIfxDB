# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_102_NumFieldsSelect_01(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_102)

  def run_test_102(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    if (not conn):
      print IfxPy.conn_errormsg()
    
    server = IfxPy.server_info( conn )
    if ((server.DBMS_NAME[0:2] != "AS") and (server.DBMS_NAME != "DB2") and (server.DBMS_NAME[0:3] != "Inf")):
      result = IfxPy.exec_immediate(conn, "VALUES(1)")
      #throw :unsupported unless result
      if (not result):
        raise Exception('Unsupported')
      print IfxPy.num_fields(result)
    else:
      print '1'
    IfxPy.close(conn)

#__END__
#__LUW_EXPECTED__
#1
#__ZOS_EXPECTED__
#1
#__SYSTEMI_EXPECTED__
#1
#__IDS_EXPECTED__
#1
