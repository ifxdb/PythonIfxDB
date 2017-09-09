#

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_053_AttrThruConn(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_053)

  def run_test_053(self):
    print "Client attributes passed through conection string:"

    options1 = {IfxPy.SQL_ATTR_INFO_USERID: 'db2inst1'}
    conn1 = IfxPy.connect(config.ConnStr, config.user, config.password, options1)
    val = IfxPy.get_option(conn1, IfxPy.SQL_ATTR_INFO_USERID, 1)
    print val

    options2 = {IfxPy.SQL_ATTR_INFO_ACCTSTR: 'account'}
    conn2 = IfxPy.connect(config.ConnStr, config.user, config.password, options2)
    val = IfxPy.get_option(conn2, IfxPy.SQL_ATTR_INFO_ACCTSTR, 1)
    print val

    options3 = {IfxPy.SQL_ATTR_INFO_APPLNAME: 'myapp'}
    conn3 = IfxPy.connect(config.ConnStr, config.user, config.password, options3)
    val = IfxPy.get_option(conn3, IfxPy.SQL_ATTR_INFO_APPLNAME, 1)
    print val

    options4 = {IfxPy.SQL_ATTR_INFO_WRKSTNNAME: 'workstation'}
    conn4 = IfxPy.connect(config.ConnStr, config.user, config.password, options4)
    val = IfxPy.get_option(conn4, IfxPy.SQL_ATTR_INFO_WRKSTNNAME, 1)
    print val

    options5 = {IfxPy.SQL_ATTR_INFO_USERID: 'kfb',
                IfxPy.SQL_ATTR_INFO_WRKSTNNAME: 'kfbwork',
                IfxPy.SQL_ATTR_INFO_ACCTSTR: 'kfbacc',
                IfxPy.SQL_ATTR_INFO_APPLNAME: 'kfbapp'}
    conn5 = IfxPy.connect(config.ConnStr, config.user, config.password, options5)
    val = IfxPy.get_option(conn5, IfxPy.SQL_ATTR_INFO_USERID, 1)
    print val
    val = IfxPy.get_option(conn5, IfxPy.SQL_ATTR_INFO_ACCTSTR, 1)
    print val
    val = IfxPy.get_option(conn5, IfxPy.SQL_ATTR_INFO_APPLNAME, 1)
    print val
    val = IfxPy.get_option(conn5, IfxPy.SQL_ATTR_INFO_WRKSTNNAME, 1)
    print val

    print "Client attributes passed post-conection:"

    options5 = {IfxPy.SQL_ATTR_INFO_USERID: 'db2inst1'}
    conn5 = IfxPy.connect(config.ConnStr, config.user, config.password)
    rc = IfxPy.set_option(conn5, options5, 1)
    val = IfxPy.get_option(conn5, IfxPy.SQL_ATTR_INFO_USERID, 1)
    print val

    options6 = {IfxPy.SQL_ATTR_INFO_ACCTSTR: 'account'}
    conn6 = IfxPy.connect(config.ConnStr, config.user, config.password)
    rc = IfxPy.set_option(conn6, options6, 1)
    val = IfxPy.get_option(conn6, IfxPy.SQL_ATTR_INFO_ACCTSTR, 1)
    print val

    options7 = {IfxPy.SQL_ATTR_INFO_APPLNAME: 'myapp'}
    conn7 = IfxPy.connect(config.ConnStr, config.user, config.password)
    rc = IfxPy.set_option(conn7, options7, 1)
    val = IfxPy.get_option(conn7, IfxPy.SQL_ATTR_INFO_APPLNAME, 1)
    print val

    options8 = {IfxPy.SQL_ATTR_INFO_WRKSTNNAME: 'workstation'}
    conn8 = IfxPy.connect(config.ConnStr, config.user, config.password)
    rc = IfxPy.set_option(conn8, options8, 1)
    val = IfxPy.get_option(conn8, IfxPy.SQL_ATTR_INFO_WRKSTNNAME, 1)
    print val

#__END__
#__LUW_EXPECTED__
#Client attributes passed through conection string:
#db2inst1
#account
#myapp
#workstation
#kfb
#kfbacc
#kfbapp
#kfbwork
#Client attributes passed post-conection:
#db2inst1
#account
#myapp
#workstation
#__ZOS_EXPECTED__
#Client attributes passed through conection string:
#db2inst1
#account
#myapp
#workstation
#kfb
#kfbacc
#kfbapp
#kfbwork
#Client attributes passed post-conection:
#db2inst1
#account
#myapp
#workstation
#__SYSTEMI_EXPECTED__
#Client attributes passed through conection string:
#db2inst1
#account
#myapp
#workstation
#kfb
#kfbacc
#kfbapp
#kfbwork
#Client attributes passed post-conection:
#db2inst1
#account
#myapp
#workstation
#__IDS_EXPECTED__
#Client attributes passed through conection string:
#db2inst1
#account
#myapp
#workstation
#kfb
#kfbacc
#kfbapp
#kfbwork
#Client attributes passed post-conection:
#db2inst1
#account
#myapp
#workstation
