# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_132_ExecuteStatementArrayMultipleParams(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_132)

  def run_test_132(self):
    sql =  "SELECT id, breed, name, weight FROM animals WHERE id = ? AND name = ?"
    
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      stmt = IfxPy.prepare(conn, sql)
    
      if (IfxPy.execute(stmt, (0, 'Pook'))):
        row = IfxPy.fetch_tuple(stmt)
        while ( row ):
          #row.each { |child| print child }
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
