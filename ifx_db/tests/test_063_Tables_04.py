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

  def test_063_Tables_04(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_063)

  def run_test_063(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
      
    result = ifx_db.tables(conn, None, "SYSIBM", "", "VIEW")
    
    if (type(result) == ifx_db.IBM_DBStatement):
      print "Resource is a DB2 Statement"
      
    ifx_db.free_result(result)

#__END__
#__LUW_EXPECTED__
#Resource is a DB2 Statement
#__ZOS_EXPECTED__
#Resource is a DB2 Statement
#__SYSTEMI_EXPECTED__
#Resource is a DB2 Statement
#__IDS_EXPECTED__
#Resource is a DB2 Statement
