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

  def test_092_ConnmsgWrongPwd(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_092)

  def run_test_092(self):
    try:
      conn = ifx_db.connect(config.ConnStr, config.user, "z")
      print "??? No way."
    except:
      err = ifx_db.conn_errormsg()
      print err[0:68]

#__END__
#__IDS_EXPECTED__
#[Informix][Informix ODBC Driver][Informix]Incorrect password or user
