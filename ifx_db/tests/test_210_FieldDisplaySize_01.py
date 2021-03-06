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

  def test_210_FieldDisplaySize_01(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_210)

  def run_test_210(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    
    result = ifx_db.exec_immediate(conn, "select * from staff")
    cols = ifx_db.num_fields(result)
    
    for i in range(0, cols):
      size = ifx_db.field_display_size(result,i)
      print "col:%d and size: %d" % (i, size)
    
    ifx_db.close(conn)

#__END__
#__LUW_EXPECTED__
#col:0 and size: 6
#col:1 and size: 9
#col:2 and size: 6
#col:3 and size: 5
#col:4 and size: 6
#col:5 and size: 9
#col:6 and size: 9
#__ZOS_EXPECTED__
#col:0 and size: 6
#col:1 and size: 9
#col:2 and size: 6
#col:3 and size: 5
#col:4 and size: 6
#col:5 and size: 9
#col:6 and size: 9
#__SYSTEMI_EXPECTED__
#col:0 and size: 6
#col:1 and size: 9
#col:2 and size: 6
#col:3 and size: 5
#col:4 and size: 6
#col:5 and size: 9
#col:6 and size: 9
#__IDS_EXPECTED__
#col:0 and size: 6
#col:1 and size: 9
#col:2 and size: 6
#col:3 and size: 5
#col:4 and size: 6
#col:5 and size: 9
#col:6 and size: 9
