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

  def test_019_selectRowcountPrefetchPrepOpt(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_019)

  def run_test_019(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    ifx_db.autocommit(conn, ifx_db.SQL_AUTOCOMMIT_ON)
    if conn:
      stmt = ifx_db.prepare(conn, "SELECT * from animals WHERE weight < 10.0", {ifx_db.SQL_ATTR_ROWCOUNT_PREFETCH : ifx_db.SQL_ROWCOUNT_PREFETCH_ON} )
      result = ifx_db.execute(stmt)
      if result:
        rows = ifx_db.num_rows(stmt)
        print "affected row:", rows
        ifx_db.free_result(stmt)
      else:
        print ifx_db.stmt_errormsg()

      ifx_db.close(conn)
    else:
      print "no connection:", ifx_db.conn_errormsg()

#__END__
#__LUW_EXPECTED__
#affected row: 4
#__ZOS_EXPECTED__
#affected row: 4
#__SYSTEMI_EXPECTED__
#affected row: 4
#__IDS_EXPECTED__
#affected row: 4
