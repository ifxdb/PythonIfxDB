# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_035_FetchRow_01(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_035)

  def run_test_035(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
      
    result = IfxPy.exec_immediate(conn, "select * from staff")
    i=0
    
    row = IfxPy.fetch_row(result)
    while ( row ):
      print "%d, " % i
      i+=1
      row = IfxPy.fetch_row(result)
    IfxPy.close(conn)

#__END__
#__LUW_EXPECTED__
#0, 
#1, 
#2, 
#3, 
#4, 
#5, 
#6, 
#7, 
#8, 
#9, 
#10, 
#11, 
#12, 
#13, 
#14, 
#15, 
#16, 
#17, 
#18, 
#19, 
#20, 
#21, 
#22, 
#23, 
#24, 
#25, 
#26, 
#27, 
#28, 
#29, 
#30, 
#31, 
#32, 
#33, 
#34, 
#__ZOS_EXPECTED__
#0, 
#1, 
#2, 
#3, 
#4, 
#5, 
#6, 
#7, 
#8, 
#9, 
#10, 
#11, 
#12, 
#13, 
#14, 
#15, 
#16, 
#17, 
#18, 
#19, 
#20, 
#21, 
#22, 
#23, 
#24, 
#25, 
#26, 
#27, 
#28, 
#29, 
#30, 
#31, 
#32, 
#33, 
#34, 
#__SYSTEMI_EXPECTED__
#0, 
#1, 
#2, 
#3, 
#4, 
#5, 
#6, 
#7, 
#8, 
#9, 
#10, 
#11, 
#12, 
#13, 
#14, 
#15, 
#16, 
#17, 
#18, 
#19, 
#20, 
#21, 
#22, 
#23, 
#24, 
#25, 
#26, 
#27, 
#28, 
#29, 
#30, 
#31, 
#32, 
#33, 
#34, 
#__IDS_EXPECTED__
#0, 
#1, 
#2, 
#3, 
#4, 
#5, 
#6, 
#7, 
#8, 
#9, 
#10, 
#11, 
#12, 
#13, 
#14, 
#15, 
#16, 
#17, 
#18, 
#19, 
#20, 
#21, 
#22, 
#23, 
#24, 
#25, 
#26, 
#27, 
#28, 
#29, 
#30, 
#31, 
#32, 
#33, 
#34, 
