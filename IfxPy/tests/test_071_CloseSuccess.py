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

  def test_071_CloseSuccess(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_071)

  def run_test_071(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      rc = IfxPy.close(conn)
      if (rc == True):
        print "IfxPy.close succeeded"
      else:
        print "IfxPy.close FAILED\n"
    else:
      print "%s" % IfxPy.conn_errormsg()
      print ",sqlstate=%s" % IfxPy.conn_error()
      print "%s" % IfxPy.conn_errormsg()
      print "%s" % IfxPy.conn_errormsg()
      print "%s" % IfxPy.conn_errormsg()
      print "%s" % IfxPy.conn_errormsg()

#__END__
#__LUW_EXPECTED__
#IfxPy.close succeeded
#__ZOS_EXPECTED__
#IfxPy.close succeeded
#__SYSTEMI_EXPECTED__
#IfxPy.close succeeded
#__IDS_EXPECTED__
#IfxPy.close succeeded
