# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_211_FieldDisplaySize_02(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_211)

  def run_test_211(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    result = IfxPy.exec_immediate(conn, "select * from sales")
    
    i = 1
    
    while (i <= IfxPy.num_fields(result)):
      #printf("%d size %d\n",i, IfxPy.field_display_size(result,i) || 0)
      print "%d size %d" % (i, IfxPy.field_display_size(result,i) or 0)
      i += 1
    
    IfxPy.close(conn)

#__END__
#__LUW_EXPECTED__
#1 size 15
#2 size 15
#3 size 11
#4 size 0
#__ZOS_EXPECTED__
#1 size 15
#2 size 15
#3 size 11
#4 size 0
#__SYSTEMI_EXPECTED__
#1 size 15
#2 size 15
#3 size 11
#4 size 0
#__IDS_EXPECTED__
#1 size 15
#2 size 15
#3 size 11
#4 size 0
