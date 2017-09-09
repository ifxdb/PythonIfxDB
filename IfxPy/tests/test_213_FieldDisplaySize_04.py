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

  def test_213_FieldDisplaySize_04(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_213)

  def run_test_213(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    result = IfxPy.exec_immediate(conn, "select * from sales")
    
    i = "sales_person"
    
    print "%s size %d\n" % (i, (IfxPy.field_display_size(result,i) or 0))
    
    i = "REGION"
    
    print "%s size %d\n" % (i, (IfxPy.field_display_size(result,i) or 0))
    
    i = "REgion"
    
    print "%s size %d\n" % (i, (IfxPy.field_display_size(result,i) or 0))
    
    i = "HELMUT"
    
    print "%s size %d\n" % (i, (IfxPy.field_display_size(result,i) or 0))
    
    t = IfxPy.field_display_size(result,"")
    
    print t
    
    t = IfxPy.field_display_size(result,"HELMUT")
    
    print t
    
    t = IfxPy.field_display_size(result,"Region")
    
    print t
    
    t = IfxPy.field_display_size(result,"SALES_DATE")
    
    print t

#__END__
#__LUW_EXPECTED__
#sales_person size 0
#REGION size 15
#REgion size 0
#HELMUT size 0
#False
#False
#False
#10
#__ZOS_EXPECTED__
#sales_person size 0
#REGION size 15
#REgion size 0
#HELMUT size 0
#False
#False
#False
#10
#__SYSTEMI_EXPECTED__
#sales_person size 0
#REGION size 15
#REgion size 0
#HELMUT size 0
#False
#False
#False
#10
#__IDS_EXPECTED__
#sales_person size 15
#REGION size 0
#REgion size 0
#HELMUT size 0
#False
#False
#False
#False
