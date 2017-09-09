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

  def test_019_selectRowcountPrefetchPrepOpt(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_019)

  def run_test_019(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_ON)
    if conn:
      stmt = IfxPy.prepare(conn, "SELECT * from animals WHERE weight < 10.0", {IfxPy.SQL_ATTR_ROWCOUNT_PREFETCH : IfxPy.SQL_ROWCOUNT_PREFETCH_ON} )
      result = IfxPy.execute(stmt)
      if result:
        rows = IfxPy.num_rows(stmt)
        print "affected row:", rows
        IfxPy.free_result(stmt)
      else:
        print IfxPy.stmt_errormsg()

      IfxPy.close(conn)
    else:
      print "no connection:", IfxPy.conn_errormsg()

#__END__
#__LUW_EXPECTED__
#affected row: 4
#__ZOS_EXPECTED__
#affected row: 4
#__SYSTEMI_EXPECTED__
#affected row: 4
#__IDS_EXPECTED__
#affected row: 4
