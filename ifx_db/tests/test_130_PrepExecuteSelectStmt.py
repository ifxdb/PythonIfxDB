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

  def test_130_PrepExecuteSelectStmt(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_130)

  def run_test_130(self):
    conn = ifx_db.connect(config.database, config.user, config.password)
    
    if conn:
      stmt = ifx_db.prepare(conn, "SELECT id, breed, name, weight FROM animals WHERE id = 0")
    
      if ifx_db.execute(stmt):
        row = ifx_db.fetch_tuple(stmt)
        while ( row ):
          for i in row:
            print i
            row = ifx_db.fetch_tuple(stmt)
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#0
#cat
#Pook            
#3.20
#__ZOS_EXPECTED__
#0
#cat
#Pook            
#3.20
#__SYSTEMI_EXPECTED__
#0
#cat
#Pook            
#3.20
#__IDS_EXPECTED__
#0
#cat
#Pook            
#3.20
