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

  def test_063_Tables_04(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_063)

  def run_test_063(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
      
    result = IfxPy.tables(conn, None, "SYSIBM", "", "VIEW")
    
    if (type(result) == IfxPy.IFXStatement):
      print "Resource is a IFX Statement"
      
    IfxPy.free_result(result)

#__END__
#__IDS_EXPECTED__
#Resource is a IFX Statement
