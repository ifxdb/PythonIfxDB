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

  def test_017_selectRowcountPrefetchSTMTOpt(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_017)

  def run_test_017(self):
    conn = ifx_db.connect(config.database, config.user, config.password)
    if conn:
      result = ifx_db.exec_immediate(conn,"SELECT * from animals WHERE weight < 10.0", { ifx_db.SQL_ATTR_CURSOR_TYPE : ifx_db.SQL_CURSOR_KEYSET_DRIVEN})
      if result:
        rows = ifx_db.num_rows(result)
        print "affected row:", rows
      else:
        print ifx_db.stmt_errormsg()
      result = ifx_db.exec_immediate(conn,"SELECT * from animals WHERE weight < 10.0", {ifx_db.SQL_ATTR_CURSOR_TYPE : ifx_db.SQL_CURSOR_FORWARD_ONLY})
      if result:
        rows = ifx_db.num_rows(result)
        print "affected row:", rows
      else:
        print ifx_db.stmt_errormsg()
      result = ifx_db.exec_immediate(conn,"SELECT * from animals WHERE weight < 10.0", {ifx_db.SQL_ATTR_ROWCOUNT_PREFETCH : ifx_db.SQL_ROWCOUNT_PREFETCH_ON})
      if result:
        rows = ifx_db.num_rows(result)
        print "affected row:", rows
      else:
        print ifx_db.stmt_errormsg()
      result = ifx_db.exec_immediate(conn,"SELECT * from animals WHERE weight < 10.0", {ifx_db.SQL_ATTR_ROWCOUNT_PREFETCH : ifx_db.SQL_ROWCOUNT_PREFETCH_OFF})
      if result:
        rows = ifx_db.num_rows(result)
        print "affected row:", rows
      else:
        print ifx_db.stmt_errormsg()


      ifx_db.close(conn)
    else:
      print "no connection:", ifx_db.conn_errormsg()

#__END__
#__LUW_EXPECTED__
#affected row: 4
#affected row: -1
#affected row: 4
#affected row: -1
#__ZOS_EXPECTED__
#affected row: 4
#affected row: -1
#affected row: 4
#affected row: -1
#__SYSTEMI_EXPECTED__
#affected row: 4
#affected row: -1
#affected row: 4
#affected row: -1
#__IDS_EXPECTED__
#affected row: 4
#affected row: -1
#affected row: 4
#affected row: -1
