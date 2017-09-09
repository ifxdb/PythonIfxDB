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

  def test_145_BindRetrieveNoneEmptyString(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_145)

  def run_test_145(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)

    if conn:
      IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_OFF)

      stmt = IfxPy.prepare(conn, "INSERT INTO animals (id, breed, name) VALUES (?, ?, ?)")

      id = 999
      breed = None
      name = 'PythonDS'
      IfxPy.bind_param(stmt, 1, id)
      IfxPy.bind_param(stmt, 2, breed)
      IfxPy.bind_param(stmt, 3, name)

      # After this statement, we expect that the BREED column will contain
      # an SQL NULL value, while the NAME column contains an empty string

      IfxPy.execute(stmt)

      # After this statement, we expect that the BREED column will contain
      # an SQL NULL value, while the NAME column contains an empty string.
      # Use the dynamically bound parameters to ensure that the code paths
      # for both IfxPy.bind_param and IfxPy.execute treat Python Nones and empty
      # strings the right way.

      IfxPy.execute(stmt, (1000, None, 'PythonDS'))

      result = IfxPy.exec_immediate(conn, "SELECT id, breed, name FROM animals WHERE breed IS NULL")
      row = IfxPy.fetch_tuple(result)
      while ( row ): 
        for i in row:
          print i
        row = IfxPy.fetch_tuple(result)

      IfxPy.rollback(conn)
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#999
#None
#PythonDS        
#1000
#None
#PythonDS        
#__ZOS_EXPECTED__
#999
#None
#PythonDS        
#1000
#None
#PythonDS        
#__SYSTEMI_EXPECTED__
#999
#None
#PythonDS        
#1000
#None
#PythonDS        
#__IDS_EXPECTED__
#999
#None
#PythonDS        
#1000
#None
#PythonDS        
