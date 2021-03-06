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

  def test_082_ConnWrongPwd(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_082)

  def run_test_082(self):
    try:
      conn = ifx_db.connect(config.ConnStr, config.user, "z")
      print "??? No way."
    except:
      err = ifx_db.conn_error()
      print err

#__END__
#__IDS_EXPECTED__
#28000
