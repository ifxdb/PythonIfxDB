# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_142_BindParamSelectStmtMultipleParams_02(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_142)

  def run_test_142(self):
    sql = "SELECT id, breed, name, weight FROM animals WHERE weight < ? AND weight > ?"
    
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      stmt = IfxPy.prepare(conn, sql)
    
      weight = 200.05
      mass = 2.0
      
      IfxPy.bind_param(stmt, 1, weight, IfxPy.SQL_PARAM_INPUT)
      IfxPy.bind_param(stmt, 2, mass, IfxPy.SQL_PARAM_INPUT)
    
      result = IfxPy.execute(stmt) 
      if ( result ):
        row = IfxPy.fetch_tuple(stmt)
        while ( row ):
          #row.each { |child| print child }
          for i in row:
            print(i)
          row = IfxPy.fetch_tuple(stmt)
      IfxPy.close(conn)
    else:
      print("Connection failed.")

#__END__
#__LUW_EXPECTED__
#0
#cat
#Pook            
#3.20
#1
#dog
#Peaches         
#12.30
#5
#goat
#Rickety Ride    
#9.70
#6
#llama
#Sweater         
#150.00
#__ZOS_EXPECTED__
#0
#cat
#Pook            
#3.20
#1
#dog
#Peaches         
#12.30
#5
#goat
#Rickety Ride    
#9.70
#6
#llama
#Sweater         
#150.00
#__SYSTEMI_EXPECTED__
#0
#cat
#Pook            
#3.20
#1
#dog
#Peaches         
#12.30
#5
#goat
#Rickety Ride    
#9.70
#6
#llama
#Sweater         
#150.00
#__IDS_EXPECTED__
#0
#cat
#Pook            
#3.20
#1
#dog
#Peaches         
#12.30
#5
#goat
#Rickety Ride    
#9.70
#6
#llama
#Sweater         
#150.00
