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

  def test_6561_InsertNULLValues(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_6561)

  def run_test_6561(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      ifx_db.autocommit(conn, ifx_db.SQL_AUTOCOMMIT_OFF)

      stmt = ifx_db.exec_immediate(conn, "INSERT INTO animals (id, breed, name, weight) VALUES (null, null, null, null)")
      statement = "SELECT count(id) FROM animals"
      result = ifx_db.exec_immediate(conn, statement)
      if ( (not result) and ifx_db.stmt_error() ):
        print "ERROR: %s" % (ifx_db.stmt_errormsg(), )

      row = ifx_db.fetch_tuple(result)
      while ( row ):
        for i in row:
            print i
        row = ifx_db.fetch_tuple(result)
    
      ifx_db.rollback(conn)
      ifx_db.close(conn)
      
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#7
#__ZOS_EXPECTED__
#7
#__SYSTEMI_EXPECTED__
#7
#__IDS_EXPECTED__
#7
