# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_018_selectRowcountPrefetchSetOpt(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_018)

  def run_test_018(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_ON)
    if conn:
      stmt = IfxPy.prepare(conn, "SELECT * from animals WHERE weight < 10.0" )
      IfxPy.set_option(stmt, {IfxPy.SQL_ATTR_ROWCOUNT_PREFETCH : IfxPy.SQL_ROWCOUNT_PREFETCH_ON}, 2)
      result = IfxPy.execute(stmt)
      if result:
        rows = IfxPy.num_rows(stmt)
        print "affected row:", rows
        IfxPy.free_result(stmt)
      else:
        print IfxPy.stmt_errormsg()

      IfxPy.set_option(stmt, {IfxPy.SQL_ATTR_ROWCOUNT_PREFETCH : IfxPy.SQL_ROWCOUNT_PREFETCH_OFF}, 2)
      result = IfxPy.execute(stmt)
      if result:
        rows = IfxPy.num_rows(stmt)
        print "affected row:", rows
        IfxPy.free_result(stmt)
      else:
        print IfxPy.stmt_errormsg()

      IfxPy.set_option(stmt, {IfxPy.SQL_ATTR_ROWCOUNT_PREFETCH : IfxPy.SQL_ROWCOUNT_PREFETCH_ON}, 2)
      result = IfxPy.execute(stmt)
      if result:
        rows = IfxPy.num_rows(stmt)
        print "affected row:", rows
      else:
        print IfxPy.stmt_errormsg()

      IfxPy.close(conn)
    else:
      print "no connection:", IfxPy.conn_errormsg()

#__END__
#__LUW_EXPECTED__
#affected row: 4
#affected row: -1
#affected row: 4
#__ZOS_EXPECTED__
#affected row: 4
#affected row: -1
#affected row: 4
#__SYSTEMI_EXPECTED__
#affected row: 4
#affected row: -1
#affected row: 4
#__IDS_EXPECTED__
#affected row: 4
#affected row: -1
#affected row: 4
