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

  def test_147_PrepareWithWrongType(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_147)

  def run_test_147(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      ifx_db.autocommit(conn, ifx_db.SQL_AUTOCOMMIT_OFF)

      stmt = ifx_db.prepare(conn, "INSERT INTO animals (id, breed, name) VALUES (?, ?, ?)")
    
      id = "\"999\""
      breed = None
      name = 'PythonDS'
      try:
          ifx_db.bind_param(stmt, 1, id)
          ifx_db.bind_param(stmt, 2, breed)
          ifx_db.bind_param(stmt, 3, name)
       
          error = ifx_db.execute(stmt)
          print "Should not make it this far"
      except:
          excp = sys.exc_info()
          # slot 1 contains error message
          print excp[1]
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#Statement Execute Failed: [IBM][CLI Driver] CLI0112E  Error in assignment. SQLSTATE=22005 SQLCODE=-99999
#__ZOS_EXPECTED__
#Statement Execute Failed: [IBM][CLI Driver] CLI0112E  Error in assignment. SQLSTATE=22005 SQLCODE=-99999
#__SYSTEMI_EXPECTED__
#Statement Execute Failed: [IBM][CLI Driver] CLI0112E  Error in assignment. SQLSTATE=22005 SQLCODE=-99999
#__IDS_EXPECTED__
#Statement Execute Failed: [IBM][CLI Driver] CLI0112E  Error in assignment. SQLSTATE=22005 SQLCODE=-99999
