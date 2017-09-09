# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_032_ResultIndexName(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_032)

  def run_test_032(self):
      conn = IfxPy.connect(config.ConnStr, config.user, config.password)
      server = IfxPy.server_info( conn )

      if conn:
        stmt = IfxPy.exec_immediate(conn, "SELECT id, breed, name, weight FROM animals WHERE id = 6")
        
        while (IfxPy.fetch_row(stmt)):
          id = IfxPy.result(stmt, "id")
          breed = IfxPy.result(stmt, "breed")
          name = IfxPy.result(stmt, "name")
          weight = IfxPy.result(stmt, "weight")
          print "int(%d)" % id
          print "string(%d) \"%s\"" % (len(breed), breed)
          print "string(%d) \"%s\"" % (len(name), name)
          print "string(%d) \"%s\"" % (len(str(weight)), weight)
        IfxPy.close(conn)
      else:
        print "Connection failed."

#__END__
#__LUW_EXPECTED__
#int(6)
#string(5) "llama"
#string(16) "Sweater         "
#string(6) "150.00"
#__ZOS_EXPECTED__
#int(6)
#string(5) "llama"
#string(16) "Sweater         "
#string(6) "150.00"
#__SYSTEMI_EXPECTED__
#int(6)
#string(5) "llama"
#string(16) "Sweater         "
#string(6) "150.00"
#__IDS_EXPECTED__
#int(6)
#string(5) "llama"
#string(16) "Sweater         "
#string(6) "150.00"
