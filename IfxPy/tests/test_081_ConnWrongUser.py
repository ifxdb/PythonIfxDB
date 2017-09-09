# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import ifx_db
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_081_ConnWrongUser(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_081)

  def run_test_081(self):
    try:
      conn = ifx_db.connect(config.ConnStr, "y", config.password)
      print "??? No way."
    except:
      print ifx_db.conn_error()

    #if conn:
    #  print "??? No way."
    #else:
    #  err = ifx_db.conn_error 
    #  print err

#__END__
#__IDS_EXPECTED__
#28000