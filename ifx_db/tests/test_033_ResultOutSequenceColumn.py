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

  def test_033_ResultOutSequenceColumn(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_033)
	  
  def run_test_033(self): 
    conn = ifx_db.connect(config.database, config.user, config.password)
    server = ifx_db.server_info( conn )
      
    if conn:
      stmt = ifx_db.exec_immediate(conn, "SELECT id, breed, name, weight FROM animals WHERE id = 0")
        
      while (ifx_db.fetch_row(stmt)):
        weight = ifx_db.result(stmt, 3)
        print "string(%d) \"%s\"" % (len(str(weight)), weight)
        breed = ifx_db.result(stmt, 1)
        print "string(%d) \"%s\"" % (len(breed), breed)
        if (server.DBMS_NAME[0:3] == 'IDS'):
          name = ifx_db.result(stmt, "name")
        else:
          name = ifx_db.result(stmt, "NAME")
        print "string(%d) \"%s\"" % (len(name), name)
      ifx_db.close(conn)
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
