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

  def test_213_FieldDisplaySize_04(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_213)

  def run_test_213(self):
    conn = ifx_db.connect(config.database, config.user, config.password)
    
    result = ifx_db.exec_immediate(conn, "select * from sales")
    
    i = "sales_person"
    
    print "%s size %d\n" % (i, (ifx_db.field_display_size(result,i) or 0))
    
    i = "REGION"
    
    print "%s size %d\n" % (i, (ifx_db.field_display_size(result,i) or 0))
    
    i = "REgion"
    
    print "%s size %d\n" % (i, (ifx_db.field_display_size(result,i) or 0))
    
    i = "HELMUT"
    
    print "%s size %d\n" % (i, (ifx_db.field_display_size(result,i) or 0))
    
    t = ifx_db.field_display_size(result,"")
    
    print t
    
    t = ifx_db.field_display_size(result,"HELMUT")
    
    print t
    
    t = ifx_db.field_display_size(result,"Region")
    
    print t
    
    t = ifx_db.field_display_size(result,"SALES_DATE")
    
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
