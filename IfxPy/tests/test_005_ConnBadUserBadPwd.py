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

  def test_005_ConnBadUserBadPwd(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_005)

  def run_test_005(self):
    baduser = "non_user"
    badpass = "invalid_password"
    dsn = "DATABASE=" + config.ConnStr + ";UID=" + baduser + ";PWD=" + badpass + ";"
    try:
      conn = ifx_db.connect(dsn, "", "")
      print "odd, ifx_db.connect succeeded with an invalid user / password"
      ifx_db.close(conn)
    except: 
      print "Ooops"

#__END__
#__LUW_EXPECTED__
#Ooops
#__ZOS_EXPECTED__
#Ooops
#__SYSTEMI_EXPECTED__
#Ooops
#__IDS_EXPECTED__
#Ooops
