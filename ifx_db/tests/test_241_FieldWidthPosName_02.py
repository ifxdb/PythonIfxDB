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

  def test_241_FieldWidthPosName_02(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_241)

  def run_test_241(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    
    result = ifx_db.exec_immediate(conn, "select * from sales")
    result2 = ifx_db.exec_immediate(conn, "select * from staff")
    result3 = ifx_db.exec_immediate(conn, "select * from emp_photo")
    
    for i in range(0, ifx_db.num_fields(result)):
      print str(ifx_db.field_width(result,i))
    
    print "\n-----"
    
    for i in range(0, ifx_db.num_fields(result2)):
      print str(ifx_db.field_width(result2,ifx_db.field_name(result2,i)))

#__END__
#__LUW_EXPECTED__
#10
#15
#15
#11
#
#-----
#6
#9
#6
#5
#6
#9
#9
#__ZOS_EXPECTED__
#10
#15
#15
#11
#
#-----
#6
#9
#6
#5
#6
#9
#9
#__SYSTEMI_EXPECTED__
#10
#15
#15
#11
#
#-----
#6
#9
#6
#5
#6
#9
#9
#__IDS_EXPECTED__
#6
#15
#15
#4
#
#-----
#2
#9
#2
#5
#2
#9
#9
