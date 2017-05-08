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

  def test_053_AttrThruConn(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_053)

  def run_test_053(self):
    print "Client attributes passed through conection string:"

    options1 = {ifx_db.SQL_ATTR_INFO_USERID: 'db2inst1'}
    conn1 = ifx_db.connect(config.database, config.user, config.password, options1)
    val = ifx_db.get_option(conn1, ifx_db.SQL_ATTR_INFO_USERID, 1)
    print val

    options2 = {ifx_db.SQL_ATTR_INFO_ACCTSTR: 'account'}
    conn2 = ifx_db.connect(config.database, config.user, config.password, options2)
    val = ifx_db.get_option(conn2, ifx_db.SQL_ATTR_INFO_ACCTSTR, 1)
    print val

    options3 = {ifx_db.SQL_ATTR_INFO_APPLNAME: 'myapp'}
    conn3 = ifx_db.connect(config.database, config.user, config.password, options3)
    val = ifx_db.get_option(conn3, ifx_db.SQL_ATTR_INFO_APPLNAME, 1)
    print val

    options4 = {ifx_db.SQL_ATTR_INFO_WRKSTNNAME: 'workstation'}
    conn4 = ifx_db.connect(config.database, config.user, config.password, options4)
    val = ifx_db.get_option(conn4, ifx_db.SQL_ATTR_INFO_WRKSTNNAME, 1)
    print val

    options5 = {ifx_db.SQL_ATTR_INFO_USERID: 'kfb',
                ifx_db.SQL_ATTR_INFO_WRKSTNNAME: 'kfbwork',
                ifx_db.SQL_ATTR_INFO_ACCTSTR: 'kfbacc',
                ifx_db.SQL_ATTR_INFO_APPLNAME: 'kfbapp'}
    conn5 = ifx_db.connect(config.database, config.user, config.password, options5)
    val = ifx_db.get_option(conn5, ifx_db.SQL_ATTR_INFO_USERID, 1)
    print val
    val = ifx_db.get_option(conn5, ifx_db.SQL_ATTR_INFO_ACCTSTR, 1)
    print val
    val = ifx_db.get_option(conn5, ifx_db.SQL_ATTR_INFO_APPLNAME, 1)
    print val
    val = ifx_db.get_option(conn5, ifx_db.SQL_ATTR_INFO_WRKSTNNAME, 1)
    print val

    print "Client attributes passed post-conection:"

    options5 = {ifx_db.SQL_ATTR_INFO_USERID: 'db2inst1'}
    conn5 = ifx_db.connect(config.database, config.user, config.password)
    rc = ifx_db.set_option(conn5, options5, 1)
    val = ifx_db.get_option(conn5, ifx_db.SQL_ATTR_INFO_USERID, 1)
    print val

    options6 = {ifx_db.SQL_ATTR_INFO_ACCTSTR: 'account'}
    conn6 = ifx_db.connect(config.database, config.user, config.password)
    rc = ifx_db.set_option(conn6, options6, 1)
    val = ifx_db.get_option(conn6, ifx_db.SQL_ATTR_INFO_ACCTSTR, 1)
    print val

    options7 = {ifx_db.SQL_ATTR_INFO_APPLNAME: 'myapp'}
    conn7 = ifx_db.connect(config.database, config.user, config.password)
    rc = ifx_db.set_option(conn7, options7, 1)
    val = ifx_db.get_option(conn7, ifx_db.SQL_ATTR_INFO_APPLNAME, 1)
    print val

    options8 = {ifx_db.SQL_ATTR_INFO_WRKSTNNAME: 'workstation'}
    conn8 = ifx_db.connect(config.database, config.user, config.password)
    rc = ifx_db.set_option(conn8, options8, 1)
    val = ifx_db.get_option(conn8, ifx_db.SQL_ATTR_INFO_WRKSTNNAME, 1)
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
