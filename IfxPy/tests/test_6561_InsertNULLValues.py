# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_6561_InsertNULLValues(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_6561)

  def run_test_6561(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_OFF)

      stmt = IfxPy.exec_immediate(conn, "INSERT INTO animals (id, breed, name, weight) VALUES (null, null, null, null)")
      statement = "SELECT count(id) FROM animals"
      result = IfxPy.exec_immediate(conn, statement)
      if ( (not result) and IfxPy.stmt_error() ):
        print "ERROR: %s" % (IfxPy.stmt_errormsg(), )

      row = IfxPy.fetch_tuple(result)
      while ( row ):
        for i in row:
            print i
        row = IfxPy.fetch_tuple(result)
    
      IfxPy.rollback(conn)
      IfxPy.close(conn)
      
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
