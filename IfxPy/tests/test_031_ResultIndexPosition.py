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

  def test_031_ResultIndexPosition(self):
     obj = IfxPyTestFunctions()
     obj.assert_expect(self.run_test_031)

  def run_test_031(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
      
    if conn:
      stmt = IfxPy.exec_immediate(conn, "SELECT id, breed, name, weight FROM animals WHERE id = 0")
        
      while (IfxPy.fetch_row(stmt)):
        id = IfxPy.result(stmt, 0)
        print "int(%d)" % id
        breed = IfxPy.result(stmt, 1)
        print "string(%d) \"%s\"" % (len(breed), breed)
        name = IfxPy.result(stmt, 2)
        print "string(%d) \"%s\"" % (len(name), name)
        weight = IfxPy.result(stmt, 3)
        print "string(%d) \"%s\"" % (len(str(weight)), weight)
      IfxPy.close(conn)
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#int(0)
#string(3) "cat"
#string(16) "Pook            "
#string(4) "3.20"
#__ZOS_EXPECTED__
#int(0)
#string(3) "cat"
#string(16) "Pook            "
#string(4) "3.20"
#__SYSTEMI_EXPECTED__
#int(0)
#string(3) "cat"
#string(16) "Pook            "
#string(4) "3.20"
#__IDS_EXPECTED__
#int(0)
#string(3) "cat"
#string(16) "Pook            "
#string(4) "3.20"
