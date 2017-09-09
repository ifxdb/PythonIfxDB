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

  def test_251_FreeResult_02(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_251)

  def run_test_251(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    result = IfxPy.exec_immediate(conn, "select * from sales")
    
    r1 = IfxPy.free_result(result)
    r2 = IfxPy.free_result(result)
    r3 = ''
    try:
      r3 = IfxPy.free_result(result99)
    except:
      r3 = None
    
    print r1
    print r2
    print r3

#__END__
#__LUW_EXPECTED__
#True
#True
#None
#__ZOS_EXPECTED__
#True
#True
#None
#__SYSTEMI_EXPECTED__
#True
#True
#None
#__IDS_EXPECTED__
#True
#True
#None
