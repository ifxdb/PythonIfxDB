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

  def test_232_FieldTypePosName(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_232)

  def run_test_232(self):
    conn = ifx_db.connect(config.database, config.user, config.password)

    result = ifx_db.exec_immediate(conn, "select * from sales")
     
    for i in range(0, ifx_db.num_fields(result) + 1):
      field_name = ifx_db.field_name(result,i)
      field_type = ifx_db.field_type(result, ifx_db.field_name(result,i))
      print str(ifx_db.field_name(result, i)) + ":" + str(ifx_db.field_type(result, ifx_db.field_name(result, i)))
          
    print "-----"
    
    t = ifx_db.field_type(result,99)
    print t
    
    t1 = ifx_db.field_type(result, "HELMUT")
    print t1

#__END__
#__LUW_EXPECTED__
#SALES_DATE:date
#SALES_PERSON:string
#REGION:string
#SALES:int
#False:False
#-----
#False
#False
#__ZOS_EXPECTED__
#SALES_DATE:date
#SALES_PERSON:string
#REGION:string
#SALES:int
#False:False
#-----
#False
#False
#__SYSTEMI_EXPECTED__
#SALES_DATE:date
#SALES_PERSON:string
#REGION:string
#SALES:int
#False:False
#-----
#False
#False
#__IDS_EXPECTED__
#sales_date:date
#sales_person:string
#region:string
#sales:int
#False:False
#-----
#False
#False
