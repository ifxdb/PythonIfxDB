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

  def test_070_Close(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_070)

  def run_test_070(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      if (type(conn) == ifx_db.IFX_DBConnection):
        print "Resource is a Ifx Connection"
      
      rc = ifx_db.close(conn)
      
      print rc
    else:
      print "Connection failed."

#__END__
#__IDS_EXPECTED__
#Resource is a Ifx Connection
#True
