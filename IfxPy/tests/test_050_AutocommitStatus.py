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

  def test_050_AutocommitStatus(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_050)

  def run_test_050(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
     
    ac = IfxPy.autocommit(conn)
      
    print ac

#__END__
#__LUW_EXPECTED__
#1
#__ZOS_EXPECTED__
#1
#__SYSTEMI_EXPECTED__
#1
#__IDS_EXPECTED__
#1
