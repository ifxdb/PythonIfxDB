# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_001_ConnDb(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_001)

  def run_test_001(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
      
    if conn:
      print("Connection succeeded.")
      IfxPy.close(conn)
    else:
      print("Connection failed.")

#__END__
#__LUW_EXPECTED__
#Connection succeeded.
#__ZOS_EXPECTED__
#Connection succeeded.
#__SYSTEMI_EXPECTED__
#Connection succeeded.
#__IDS_EXPECTED__
#Connection succeeded.
