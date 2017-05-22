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

  def test_102_NumFieldsSelect_01(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_102)

  def run_test_102(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    
    if (not conn):
      print ifx_db.conn_errormsg()
    
    server = ifx_db.server_info( conn )
    if ((server.DBMS_NAME[0:2] != "AS") and (server.DBMS_NAME != "DB2") and (server.DBMS_NAME[0:3] != "Inf")):
      result = ifx_db.exec_immediate(conn, "VALUES(1)")
      #throw :unsupported unless result
      if (not result):
        raise Exception('Unsupported')
      print ifx_db.num_fields(result)
    else:
      print '1'
    ifx_db.close(conn)

#__END__
#__LUW_EXPECTED__
#1
#__ZOS_EXPECTED__
#1
#__SYSTEMI_EXPECTED__
#1
#__IDS_EXPECTED__
#1
