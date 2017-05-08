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

  def test_054_CursorType(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_054)

  def run_test_054(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    serverinfo = ifx_db.server_info( conn )

    stmt = ifx_db.exec_immediate(conn, "SELECT * FROM animals")
    val = ifx_db.get_option(stmt, ifx_db.SQL_ATTR_CURSOR_TYPE, 0)
    print val

    op = {ifx_db.SQL_ATTR_CURSOR_TYPE: ifx_db.SQL_CURSOR_FORWARD_ONLY}
    stmt = ifx_db.exec_immediate(conn, "SELECT * FROM animals", op)
    val = ifx_db.get_option(stmt, ifx_db.SQL_ATTR_CURSOR_TYPE, 0)
    print val

    if (serverinfo.DBMS_NAME[0:3] != 'IDS'):
      op = {ifx_db.SQL_ATTR_CURSOR_TYPE: ifx_db.SQL_CURSOR_KEYSET_DRIVEN}
    else:
      op = {ifx_db.SQL_ATTR_CURSOR_TYPE: ifx_db.SQL_CURSOR_STATIC}
    stmt = ifx_db.exec_immediate(conn, "SELECT * FROM animals", op)
    val = ifx_db.get_option(stmt, ifx_db.SQL_ATTR_CURSOR_TYPE, 0)
    print val

    op = {ifx_db.SQL_ATTR_CURSOR_TYPE: ifx_db.SQL_CURSOR_STATIC}
    stmt = ifx_db.exec_immediate(conn, "SELECT * FROM animals", op)
    val = ifx_db.get_option(stmt, ifx_db.SQL_ATTR_CURSOR_TYPE, 0)
    print val

#__END__
#__LUW_EXPECTED__
#0
#0
#1
#3
#__ZOS_EXPECTED__
#0
#0
#1
#3
#__SYSTEMI_EXPECTED__
#0
#0
#3
#3
#__IDS_EXPECTED__
#0
#0
#3
#3
#
