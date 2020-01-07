# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_250_FreeResult_01(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_250)

  def run_test_250(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    result = IfxPy.exec_immediate(conn, "select * from sales")
    result2 = IfxPy.exec_immediate(conn, "select * from staff")
    result3 = IfxPy.exec_immediate(conn, "select * from emp_photo")
    
    r1 = IfxPy.free_result(result)
    r2 = IfxPy.free_result(result2)
    r3 = IfxPy.free_result(result3)
    
    print(r1)
    print(r2)
    print(r3)

#__END__
#__LUW_EXPECTED__
#True
#True
#True
#__ZOS_EXPECTED__
#True
#True
#True
#__SYSTEMI_EXPECTED__
#True
#True
#True
#__IDS_EXPECTED__
#True
#True
#True
