# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_240_FieldWidthPosName_01(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_240)

  def run_test_240(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    result = IfxPy.exec_immediate(conn, "select * from sales")
    result2 = IfxPy.exec_immediate(conn, "select * from staff")
    result3 = IfxPy.exec_immediate(conn, "select * from emp_photo")
    
    for i in range(0, IfxPy.num_fields(result)):
      print str(i) + ":" + str(IfxPy.field_width(result,i))
    
    print "\n-----"
    
    for i in range(0, IfxPy.num_fields(result2)):
      print str(i) + ":" + str(IfxPy.field_width(result2,IfxPy.field_name(result2,i)))
          
    print "\n-----"
    
    for i in range(0, 3):
      print str(i) + ":" + str(IfxPy.field_width(result3,i)) + "," + str(IfxPy.field_display_size(result3,i))
    
    print "\n-----"
    print "region:%s" % IfxPy.field_type(result,'region')
    
    print "5:%s" % IfxPy.field_type(result2,5)

#__END__
#__LUW_EXPECTED__
#0:10
#1:15
#2:15
#3:11
#
#-----
#0:6
#1:9
#2:6
#3:5
#4:6
#5:9
#6:9
#
#-----
#0:6,6
#1:10,10
#2:1048576,2097152
#
#-----
#region:False
#5:decimal
#__ZOS_EXPECTED__
#0:10
#1:15
#2:15
#3:11
#
#-----
#0:6
#1:9
#2:6
#3:5
#4:6
#5:9
#6:9
#
#-----
#0:6,6
#1:10,10
#2:1048576,2097152
#
#-----
#region:False
#5:decimal
#__SYSTEMI_EXPECTED__
#0:10
#1:15
#2:15
#3:11
#
#-----
#0:6
#1:9
#2:6
#3:5
#4:6
#5:9
#6:9
#
#-----
#0:6,6
#1:10,10
#2:1048576,2097152
#
#-----
#region:False
#5:decimal
#__IDS_EXPECTED__
#0:6
#1:15
#2:15
#3:4
#
#-----
#0:2
#1:9
#2:2
#3:5
#4:2
#5:9
#6:9
#
#-----
#0:6,6
#1:10,10
#2:2147483647,2147483647
#
#-----
#region:string
#5:decimal
