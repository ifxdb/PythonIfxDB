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

  def test_052_SetAutocommit_02(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_052)
	  
  def run_test_052(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
      
    ifx_db.autocommit(conn, 0)
      
    ac = ifx_db.autocommit(conn)
      
    print ac

#__END__
#__LUW_EXPECTED__
#0
#__ZOS_EXPECTED__
#0
#__SYSTEMI_EXPECTED__
#0
#__IDS_EXPECTED__
#0
