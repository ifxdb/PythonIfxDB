# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_116_ConnActive(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_116)

  def run_test_116(self):
    conn = None
    is_alive = IfxPy.active(conn)
    if is_alive:
      print("Is active")
    else:
      print("Is not active")

    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    is_alive = IfxPy.active(conn)
    if is_alive:
      print("Is active")
    else:
      print("Is not active")

    IfxPy.close(conn)
    is_alive = IfxPy.active(conn)
    if is_alive:
      print("Is active")
    else:
      print("Is not active")

    # Executing active method multiple times to reproduce a customer reported defect
    print(IfxPy.active(conn))
    print(IfxPy.active(conn))
    print(IfxPy.active(conn))
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    print(IfxPy.active(conn))
    print(IfxPy.active(conn))
    print(IfxPy.active(conn))

#__END__
#__LUW_EXPECTED__
#Is not active
#Is active
#Is not active
#False
#False
#False
#True
#True
#True
#__ZOS_EXPECTED__
#Is not active
#Is active
#Is not active
#False
#False
#False
#True
#True
#True
#__SYSTEMI_EXPECTED__
#Is not active
#Is active
#Is not active
#False
#False
#False
#True
#True
#True
#__IDS_EXPECTED__
#Is not active
#Is active
#Is not active
#False
#False
#False
#True
#True
#True
