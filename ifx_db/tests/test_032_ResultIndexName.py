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

  def test_032_ResultIndexName(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_032)

  def run_test_032(self):
      conn = ifx_db.connect(config.database, config.user, config.password)
      server = ifx_db.server_info( conn )

      if conn:
        stmt = ifx_db.exec_immediate(conn, "SELECT id, breed, name, weight FROM animals WHERE id = 6")
        
        while (ifx_db.fetch_row(stmt)):
          if (server.DBMS_NAME[0:3] == 'IDS'):
            id = ifx_db.result(stmt, "id")
            breed = ifx_db.result(stmt, "breed")
            name = ifx_db.result(stmt, "name")
            weight = ifx_db.result(stmt, "weight")
          else:
            id = ifx_db.result(stmt, "ID")
            breed = ifx_db.result(stmt, "BREED")
            name = ifx_db.result(stmt, "NAME")
            weight = ifx_db.result(stmt, "WEIGHT")
          print "int(%d)" % id
          print "string(%d) \"%s\"" % (len(breed), breed)
          print "string(%d) \"%s\"" % (len(name), name)
          print "string(%d) \"%s\"" % (len(str(weight)), weight)
        ifx_db.close(conn)
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
