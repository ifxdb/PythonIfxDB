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

  def test_051_SetAutocommit_01(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_051)

  def run_test_051(self):
    options = { IfxPy.SQL_ATTR_AUTOCOMMIT:  IfxPy.SQL_AUTOCOMMIT_OFF }
      
    conn = IfxPy.connect(config.ConnStr, config.user, config.password, options)
      
    ac = IfxPy.autocommit(conn)
      
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
