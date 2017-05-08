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
      print err

#__END__
#__LUW_EXPECTED__
#[IBM][CLI Driver] SQL30082N  Security processing failed with reason "24" ("USERNAME AND/OR PASSWORD INVALID").  SQLSTATE=08001 SQLCODE=-30082
#__ZOS_EXPECTED__
#[IBM][CLI Driver] SQL30082N  Security processing failed with reason "15" ("PROCESSING FAILURE").  SQLSTATE=08001 SQLCODE=-30082
#__SYSTEMI_EXPECTED__
#[IBM][CLI Driver] SQL30082N  Security processing failed with reason "24" ("USERNAME AND/OR PASSWORD INVALID").  SQLSTATE=08001 SQLCODE=-30082
#__IDS_EXPECTED__
#[IBM][CLI Driver] SQL30082N  Security processing failed with reason "24" ("USERNAME AND/OR PASSWORD INVALID").  SQLSTATE=08001 SQLCODE=-30082
