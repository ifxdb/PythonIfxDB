#

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_054_CursorType(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_054)

  def run_test_054(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    serverinfo = IfxPy.server_info( conn )

    stmt = IfxPy.exec_immediate(conn, "SELECT * FROM animals")
    val = IfxPy.get_option(stmt, IfxPy.SQL_ATTR_CURSOR_TYPE, 0)
    print val

    op = {IfxPy.SQL_ATTR_CURSOR_TYPE: IfxPy.SQL_CURSOR_FORWARD_ONLY}
    stmt = IfxPy.exec_immediate(conn, "SELECT * FROM animals", op)
    val = IfxPy.get_option(stmt, IfxPy.SQL_ATTR_CURSOR_TYPE, 0)
    print val

    op = {IfxPy.SQL_ATTR_CURSOR_TYPE: IfxPy.SQL_CURSOR_KEYSET_DRIVEN}
    stmt = IfxPy.exec_immediate(conn, "SELECT * FROM animals", op)
    val = IfxPy.get_option(stmt, IfxPy.SQL_ATTR_CURSOR_TYPE, 0)
    print val

    op = {IfxPy.SQL_ATTR_CURSOR_TYPE: IfxPy.SQL_CURSOR_STATIC}
    stmt = IfxPy.exec_immediate(conn, "SELECT * FROM animals", op)
    val = IfxPy.get_option(stmt, IfxPy.SQL_ATTR_CURSOR_TYPE, 0)
    print val

#__END__
#__IDS_EXPECTED__
#0
#0
#0
#0
#
