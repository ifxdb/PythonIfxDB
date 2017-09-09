# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#
# NOTE: IDS requires that you pass the schema name (cannot pass None)

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_025_PrimaryKeys(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_025)

  def run_test_025(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    server = IfxPy.server_info( conn )
      
    if (conn != 0):
      drop = 'DROP TABLE test_primary_keys'
      try:
        result = IfxPy.exec_immediate(conn, drop)
      except:
        pass
      drop = 'DROP TABLE test_foreign_keys'
      try:
        result = IfxPy.exec_immediate(conn, drop)
      except:
        pass
      statement = 'CREATE TABLE test_primary_keys (id INTEGER NOT NULL, PRIMARY KEY(id))'
      result = IfxPy.exec_immediate(conn, statement)
      statement = "INSERT INTO test_primary_keys VALUES (1)"
      result = IfxPy.exec_immediate(conn, statement)
      statement = 'CREATE TABLE test_foreign_keys (idf INTEGER NOT NULL, FOREIGN KEY(idf) REFERENCES test_primary_keys(id))'
      result = IfxPy.exec_immediate(conn, statement)
      statement = "INSERT INTO test_foreign_keys VALUES (1)"
      result = IfxPy.exec_immediate(conn, statement)
      
      if (server.DBMS_NAME[0:3] == 'Inf'):
        stmt = IfxPy.primary_keys(conn, None, config.user, 'test_primary_keys')
      else:
        stmt = IfxPy.primary_keys(conn, None, None, 'TEST_PRIMARY_KEYS')
      row = IfxPy.fetch_tuple(stmt)
      print row[2]
      print row[3]
      print row[4]
      IfxPy.close(conn)
    else:
      print IfxPy.conn_errormsg()
      print "Connection failed\n"

#__END__
#__LUW_EXPECTED__
#TEST_PRIMARY_KEYS
#ID
#1
#__ZOS_EXPECTED__
#TEST_PRIMARY_KEYS
#ID
#1
#__SYSTEMI_EXPECTED__
#TEST_PRIMARY_KEYS
#ID
#1
#__IDS_EXPECTED__
#test_primary_keys
#id
#1
