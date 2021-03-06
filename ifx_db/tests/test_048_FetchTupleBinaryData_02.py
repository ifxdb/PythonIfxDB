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

  def test_048_FetchTupleBinaryData_02(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_048)

  def run_test_048(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    if (not conn):
      print "Could not make a connection." 
      return 0
    server = ifx_db.server_info( conn )
    
    fp = open("tests/spook_out.png", "wb")
    result = ifx_db.exec_immediate(conn, "SELECT picture FROM animal_pics WHERE name = 'Spook'")
    if (not result):
      print "Could not execute SELECT statement."
      return 0
    row = ifx_db.fetch_tuple(result)
    if row:
      fp.write(row[0])
    else:
      print ifx_db.stmt_errormsg()
    fp.close()
    cmp = (open('tests/spook_out.png', "rb").read() == open('tests/spook.png', "rb").read())
    print "Are the files the same:", cmp

#__END__
#__LUW_EXPECTED__
#Are the files the same: True
#__ZOS_EXPECTED__
#Are the files the same: True
#__SYSTEMI_EXPECTED__
#Are the files the same: True
#__IDS_EXPECTED__
#Are the files the same: True
