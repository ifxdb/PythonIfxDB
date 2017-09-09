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

  def test_050_AutocommitStatus(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_050)

  def run_test_050(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
     
    ac = ifx_db.autocommit(conn)
      
    print ac

#__END__
#__LUW_EXPECTED__
#1
#__ZOS_EXPECTED__
#1
#__SYSTEMI_EXPECTED__
#1
#__IDS_EXPECTED__
#1
