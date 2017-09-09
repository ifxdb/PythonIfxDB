# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_091_ConnmsgWrongUser(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_091)

  def run_test_091(self):
    try:
      conn = IfxPy.connect(config.ConnStr, "y", config.password)
      print "??? No way."
    except:
      err = IfxPy.conn_errormsg()
      print err[0:68]

#__END__
#__LUW_EXPECTED__
#__IDS_EXPECTED__
#[Informix][Informix ODBC Driver][Informix]Incorrect password or user
