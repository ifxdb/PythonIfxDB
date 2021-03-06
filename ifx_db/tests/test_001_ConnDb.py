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

  def test_001_ConnDb(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_001)

  def run_test_001(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
      
    if conn:
      print "Connection succeeded."
      ifx_db.close(conn)
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#Connection succeeded.
#__ZOS_EXPECTED__
#Connection succeeded.
#__SYSTEMI_EXPECTED__
#Connection succeeded.
#__IDS_EXPECTED__
#Connection succeeded.
