# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_052_SetAutocommit_02(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_052)
	  
  def run_test_052(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
      
    IfxPy.autocommit(conn, 0)
      
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
