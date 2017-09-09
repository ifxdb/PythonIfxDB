# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxDbTestCase(unittest.TestCase):
  
  def test_006_ConnPassingOpts(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_006)
	  
  def run_test_006(self):    

    options1 = {IfxPy.SQL_ATTR_CURSOR_TYPE:  IfxPy.SQL_CURSOR_KEYSET_DRIVEN}
    options2 = {IfxPy.SQL_ATTR_CURSOR_TYPE: IfxPy.SQL_CURSOR_FORWARD_ONLY}
      
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
  
    if conn:
      serverinfo = IfxPy.server_info( conn )

      if (serverinfo.DBMS_NAME[0:3] == 'Inf'):
        options1 = options2

      stmt = IfxPy.prepare(conn, "SELECT name FROM animals WHERE weight < 10.0", options2)
      IfxPy.execute(stmt)
      data = IfxPy.fetch_both(stmt)
      while ( data ):
        print data[0]
        data = IfxPy.fetch_both(stmt)
      
      print ""

      stmt = IfxPy.prepare(conn, "SELECT name FROM animals WHERE weight < 10.0", options1)
      IfxPy.execute(stmt)
      data = IfxPy.fetch_both(stmt)
      while ( data ):
        print data[0]
        data = IfxPy.fetch_both(stmt)
    
      IfxPy.close(conn)
    else:
      print "Connection failed."

#__END__
#__IDS_EXPECTED__
#Pook            
#Bubbles         
#Gizmo           
#Rickety Ride    
#
#Pook            
#Bubbles         
#Gizmo           
#Rickety Ride    
