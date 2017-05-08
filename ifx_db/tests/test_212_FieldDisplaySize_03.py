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

  def test_212_FieldDisplaySize_03(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_212)

  def run_test_212(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    server = ifx_db.server_info( conn )

    result = ifx_db.exec_immediate(conn, "select * from sales")
    
    if (server.DBMS_NAME[0:3] == 'IDS'):
      i = "sales_person"
    else:
      i = "SALES_PERSON"
    
    print "%s size %d" % (i, ifx_db.field_display_size(result,i))
    
    i = 2
    print "%d size %d" % (i, ifx_db.field_display_size(result,i))

#__END__
#__LUW_EXPECTED__
#SALES_PERSON size 15
#2 size 15
#__ZOS_EXPECTED__
#SALES_PERSON size 15
#2 size 15
#__SYSTEMI_EXPECTED__
#SALES_PERSON size 15
#2 size 15
#__IDS_EXPECTED__
#sales_person size 15
#2 size 15
