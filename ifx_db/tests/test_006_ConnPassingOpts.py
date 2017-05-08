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
  
  def test_006_ConnPassingOpts(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_006)
	  
  def run_test_006(self):    

    options1 = {ifx_db.SQL_ATTR_CURSOR_TYPE:  ifx_db.SQL_CURSOR_KEYSET_DRIVEN}
    options2 = {ifx_db.SQL_ATTR_CURSOR_TYPE: ifx_db.SQL_CURSOR_FORWARD_ONLY}
      
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
  
    if conn:
      serverinfo = ifx_db.server_info( conn )

      if (serverinfo.DBMS_NAME[0:3] == 'IDS'):
        options1 = options2

      stmt = ifx_db.prepare(conn, "SELECT name FROM animals WHERE weight < 10.0", options2)
      ifx_db.execute(stmt)
      data = ifx_db.fetch_both(stmt)
      while ( data ):
        print data[0]
        data = ifx_db.fetch_both(stmt)
      
      print ""

      stmt = ifx_db.prepare(conn, "SELECT name FROM animals WHERE weight < 10.0", options1)
      ifx_db.execute(stmt)
      data = ifx_db.fetch_both(stmt)
      while ( data ):
        print data[0]
        data = ifx_db.fetch_both(stmt)
    
      ifx_db.close(conn)
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#Pook            
#Bubbles         
#Gizmo           
#Rickety Ride    
#
#Pook            
#Bubbles         
#Gizmo           
#Rickety Ride    
#__ZOS_EXPECTED__
#Pook            
#Bubbles         
#Gizmo           
#Rickety Ride    
#
#Pook            
#Bubbles         
#Gizmo           
#Rickety Ride    
#__SYSTEMI_EXPECTED__
#Pook            
#Bubbles         
#Gizmo           
#Rickety Ride    
#
#Pook            
#Bubbles         
#Gizmo           
#Rickety Ride    
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
