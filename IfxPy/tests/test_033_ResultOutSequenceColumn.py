# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_033_ResultOutSequenceColumn(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_033)
	  
  def run_test_033(self): 
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    server = IfxPy.server_info( conn )
      
    if conn:
      stmt = IfxPy.exec_immediate(conn, "SELECT id, breed, name, weight FROM animals WHERE id = 0")
        
      while (IfxPy.fetch_row(stmt)):
        weight = IfxPy.result(stmt, 3)
        print "string(%d) \"%s\"" % (len(str(weight)), weight)
        breed = IfxPy.result(stmt, 1)
        print "string(%d) \"%s\"" % (len(breed), breed)
        name = IfxPy.result(stmt, "name")
        print "string(%d) \"%s\"" % (len(name), name)
      IfxPy.close(conn)
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#string(4) "3.20"
#string(3) "cat"
#string(16) "Pook            "
#__ZOS_EXPECTED__
#string(4) "3.20"
#string(3) "cat"
#string(16) "Pook            "
#__SYSTEMI_EXPECTED__
#string(4) "3.20"
#string(3) "cat"
#string(16) "Pook            "
#__IDS_EXPECTED__
#string(4) "3.20"
#string(3) "cat"
#string(16) "Pook            "
