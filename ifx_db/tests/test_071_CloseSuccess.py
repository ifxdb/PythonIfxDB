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

  def test_071_CloseSuccess(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_071)

  def run_test_071(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      rc = ifx_db.close(conn)
      if (rc == True):
        print "ifx_db.close succeeded"
      else:
        print "ifx_db.close FAILED\n"
    else:
      print "%s" % ifx_db.conn_errormsg()
      print ",sqlstate=%s" % ifx_db.conn_error()
      print "%s" % ifx_db.conn_errormsg()
      print "%s" % ifx_db.conn_errormsg()
      print "%s" % ifx_db.conn_errormsg()
      print "%s" % ifx_db.conn_errormsg()

#__END__
#__LUW_EXPECTED__
#ifx_db.close succeeded
#__ZOS_EXPECTED__
#ifx_db.close succeeded
#__SYSTEMI_EXPECTED__
#ifx_db.close succeeded
#__IDS_EXPECTED__
#ifx_db.close succeeded
