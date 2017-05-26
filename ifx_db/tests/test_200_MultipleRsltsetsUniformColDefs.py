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

  def test_200_MultipleRsltsetsUniformColDefs(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_200)

  def run_test_200(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    serverinfo = ifx_db.server_info( conn )
   
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
       ifx_db.exec_immediate(conn, 'DROP PROCEDURE multiResults')
     except:
       pass
     ifx_db.exec_immediate(conn, procedure)
     stmt = ifx_db.exec_immediate(conn, 'CALL multiResults()')
    
     print "Fetching first result set"
     row = ifx_db.fetch_tuple(stmt)
     while ( row ):
       for i in row:
         print i
       row = ifx_db.fetch_tuple(stmt)
    
     ifx_db.close(conn)
    else:
      print "Connection failed."

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
