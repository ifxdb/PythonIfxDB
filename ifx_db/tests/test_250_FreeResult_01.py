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

  def test_250_FreeResult_01(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_250)

  def run_test_250(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    
    result = ifx_db.exec_immediate(conn, "select * from sales")
    result2 = ifx_db.exec_immediate(conn, "select * from staff")
    result3 = ifx_db.exec_immediate(conn, "select * from emp_photo")
    
    r1 = ifx_db.free_result(result)
    r2 = ifx_db.free_result(result2)
    r3 = ifx_db.free_result(result3)
    
    print r1
    print r2
    print r3

#__END__
#__LUW_EXPECTED__
#True
#True
#True
#__ZOS_EXPECTED__
#True
#True
#True
#__SYSTEMI_EXPECTED__
#True
#True
#True
#__IDS_EXPECTED__
#True
#True
#True
