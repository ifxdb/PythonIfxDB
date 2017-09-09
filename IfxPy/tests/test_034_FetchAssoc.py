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

  def test_034_FetchAssoc(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_034)

  def run_test_034(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)

    server = ifx_db.server_info( conn )
    op = {ifx_db.ATTR_CASE: ifx_db.CASE_UPPER}
    ifx_db.set_option(conn, op, 1)

    result = ifx_db.exec_immediate(conn, "select * from staff")
    row = ifx_db.fetch_assoc(result)
    if( row ):
      #printf("%5d  ",row['ID'])
      #printf("%-10s ",row['NAME'])
      #printf("%5d ",row['DEPT'])
      #printf("%-7s ",row['JOB'])
      #printf("%5d ", row['YEARS'])
      #printf("%15s ", row['SALARY'])
      #printf("%10s ", row['COMM'])
      #puts ""
      print "%5d %-10s %5d %-7s %5d %15s %10s" % (row['ID'], row['NAME'], row['DEPT'], row['JOB'], row['YEARS'], row['SALARY'], row['COMM'])
    
    ifx_db.close(conn)

#__END__
#__LUW_EXPECTED__
#   10 Sanders       20 Mgr         7        18357.50       None
#__ZOS_EXPECTED__
#   10 Sanders       20 Mgr         7        18357.50       None
#__SYSTEMI_EXPECTED__
#   10 Sanders       20 Mgr         7        18357.50       None
#__IDS_EXPECTED__
#   10 Sanders       20 Mgr         7        18357.50       None
