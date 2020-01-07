# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_200_MultipleRsltsetsUniformColDefs(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_200)

  def run_test_200(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    serverinfo = IfxPy.server_info( conn )
   
    procedure = """
  	CREATE FUNCTION multiResults()
  	 RETURNING CHAR(16), INT;
  			
  	 DEFINE p_name CHAR(16);
  	 DEFINE p_id INT;
  		   
  	 FOREACH c1 FOR
  		 SELECT name, id
  		  INTO p_name, p_id
  		   FROM animals
  		   ORDER BY name
  		  RETURN p_name, p_id WITH RESUME;
  	 END FOREACH;
  			
    END FUNCTION;
    """
    
    if conn:
     try:
       IfxPy.exec_immediate(conn, 'DROP PROCEDURE multiResults')
     except:
       pass
     IfxPy.exec_immediate(conn, procedure)
     stmt = IfxPy.exec_immediate(conn, 'CALL multiResults()')
    
     print("Fetching first result set")
     row = IfxPy.fetch_tuple(stmt)
     while ( row ):
       for i in row:
         print(i)
       row = IfxPy.fetch_tuple(stmt)
    
     IfxPy.close(conn)
    else:
      print("Connection failed.")

#__END__
#__IDS_EXPECTED__
#Fetching first result set
#Bubbles         
#3
#Gizmo           
#4
#Peaches         
#1
#Pook            
#0
#Rickety Ride    
#5
#Smarty          
#2
#Sweater         
#6
