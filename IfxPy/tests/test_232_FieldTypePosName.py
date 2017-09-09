# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_232_FieldTypePosName(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_232)

  def run_test_232(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)

    result = IfxPy.exec_immediate(conn, "select * from sales")
     
    for i in range(0, IfxPy.num_fields(result) + 1):
      field_name = IfxPy.field_name(result,i)
      field_type = IfxPy.field_type(result, IfxPy.field_name(result,i))
      print str(IfxPy.field_name(result, i)) + ":" + str(IfxPy.field_type(result, IfxPy.field_name(result, i)))
          
    print "-----"
    
    t = IfxPy.field_type(result,99)
    print t
    
    t1 = IfxPy.field_type(result, "HELMUT")
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
