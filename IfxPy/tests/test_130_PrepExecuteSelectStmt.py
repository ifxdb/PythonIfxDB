# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_130_PrepExecuteSelectStmt(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_130)

  def run_test_130(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      stmt = IfxPy.prepare(conn, "SELECT id, breed, name, weight FROM animals WHERE id = 0")
    
      if IfxPy.execute(stmt):
        row = IfxPy.fetch_tuple(stmt)
        while ( row ):
          for i in row:
            print(i)
            row = IfxPy.fetch_tuple(stmt)
    else:
      print("Connection failed.")

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
