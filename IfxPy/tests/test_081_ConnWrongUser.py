# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_081_ConnWrongUser(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_081)

  def run_test_081(self):
    try:
      conn = IfxPy.connect(config.ConnStr, "y", config.password)
      print("??? No way.")
    except:
      print(IfxPy.conn_error())

    #if conn:
    #  print "??? No way."
    #else:
    #  err = IfxPy.conn_error 
    #  print err

#__END__
#__IDS_EXPECTED__
#28000