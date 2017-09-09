# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_147_PrepareWithWrongType(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_147)

  def run_test_147(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_OFF)

      stmt = IfxPy.prepare(conn, "INSERT INTO animals (id, breed, name) VALUES (?, ?, ?)")
    
      id = "\"999\""
      breed = None
      name = 'PythonDS'
      try:
          IfxPy.bind_param(stmt, 1, id)
          IfxPy.bind_param(stmt, 2, breed)
          IfxPy.bind_param(stmt, 3, name)
       
          error = IfxPy.execute(stmt)
          print "Should not make it this far"
      except:
          excp = sys.exc_info()
          # slot 1 contains error message
          print excp[1]
    else:
      print "Connection failed."

#__END__
#__IDS_EXPECTED__
#Statement Execute Failed: [Informix][Informix ODBC Driver]Invalid character value for cast specification. SQLCODE=-11106
