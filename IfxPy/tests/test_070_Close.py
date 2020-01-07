# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_070_Close(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_070)

  def run_test_070(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      if (type(conn) == IfxPy.IFXConnection):
        print("Resource is a Ifx Connection")
      
      rc = IfxPy.close(conn)
      
      print(rc)
    else:
      print("Connection failed.")

#__END__
#__IDS_EXPECTED__
#Resource is a Ifx Connection
#True
