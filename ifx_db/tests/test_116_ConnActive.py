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

  def test_116_ConnActive(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_116)

  def run_test_116(self):
    conn = None
    is_alive = ifx_db.active(conn)
    if is_alive:
      print "Is active"
    else:
      print "Is not active"

    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    is_alive = ifx_db.active(conn)
    if is_alive:
      print "Is active"
    else:
      print "Is not active"

    ifx_db.close(conn)
    is_alive = ifx_db.active(conn)
    if is_alive:
      print "Is active"
    else:
      print "Is not active"

    # Executing active method multiple times to reproduce a customer reported defect
    print ifx_db.active(conn)
    print ifx_db.active(conn)
    print ifx_db.active(conn)
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    print ifx_db.active(conn)
    print ifx_db.active(conn)
    print ifx_db.active(conn)

#__END__
#__LUW_EXPECTED__
#Is not active
#Is active
#Is not active
#False
#False
#False
#True
#True
#True
#__ZOS_EXPECTED__
#Is not active
#Is active
#Is not active
#False
#False
#False
#True
#True
#True
#__SYSTEMI_EXPECTED__
#Is not active
#Is active
#Is not active
#False
#False
#False
#True
#True
#True
#__IDS_EXPECTED__
#Is not active
#Is active
#Is not active
#False
#False
#False
#True
#True
#True
