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

  def test_221_100PersistentConns(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_221)

  def run_test_221(self):
    pconn = range(100)
    
    for i in range(100):
      pconn[i] = ifx_db.pconnect(config.database, config.user, config.password)
    
    if pconn[33]:
      conn = pconn[22]
      ifx_db.autocommit(conn, ifx_db.SQL_AUTOCOMMIT_OFF)
      stmt = ifx_db.exec_immediate(pconn[33], "UPDATE animals SET name = 'flyweight' WHERE weight < 10.0")
      print "Number of affected rows:", ifx_db.num_rows( stmt )
      ifx_db.rollback(conn)
      ifx_db.close(pconn[33])
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#Number of affected rows: 4
#__ZOS_EXPECTED__
#Number of affected rows: 4
#__SYSTEMI_EXPECTED__
#Number of affected rows: 4
#__IDS_EXPECTED__
#Number of affected rows: 4
