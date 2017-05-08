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

  def test_145_BindRetrieveNoneEmptyString(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_145)

  def run_test_145(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)

    if conn:
      ifx_db.autocommit(conn, ifx_db.SQL_AUTOCOMMIT_OFF)

      stmt = ifx_db.prepare(conn, "INSERT INTO animals (id, breed, name) VALUES (?, ?, ?)")

      id = 999
      breed = None
      name = 'PythonDS'
      ifx_db.bind_param(stmt, 1, id)
      ifx_db.bind_param(stmt, 2, breed)
      ifx_db.bind_param(stmt, 3, name)

      # After this statement, we expect that the BREED column will contain
      # an SQL NULL value, while the NAME column contains an empty string

      ifx_db.execute(stmt)

      # After this statement, we expect that the BREED column will contain
      # an SQL NULL value, while the NAME column contains an empty string.
      # Use the dynamically bound parameters to ensure that the code paths
      # for both ifx_db.bind_param and ifx_db.execute treat Python Nones and empty
      # strings the right way.

      ifx_db.execute(stmt, (1000, None, 'PythonDS'))

      result = ifx_db.exec_immediate(conn, "SELECT id, breed, name FROM animals WHERE breed IS NULL")
      row = ifx_db.fetch_tuple(result)
      while ( row ): 
        for i in row:
          print i
        row = ifx_db.fetch_tuple(result)

      ifx_db.rollback(conn)
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
