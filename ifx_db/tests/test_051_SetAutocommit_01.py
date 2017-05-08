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

  def test_051_SetAutocommit_01(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_051)

  def run_test_051(self):
    options = { ifx_db.SQL_ATTR_AUTOCOMMIT:  ifx_db.SQL_AUTOCOMMIT_OFF }
      
    conn = ifx_db.connect(config.database, config.user, config.password, options)
      
    ac = ifx_db.autocommit(conn)
      
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
