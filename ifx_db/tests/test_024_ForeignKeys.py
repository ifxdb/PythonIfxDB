# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#
# NOTE: IDS requires that you pass the schema name (cannot pass None)

import unittest, sys
import ifx_db
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_024_ForeignKeys(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_024)

  def run_test_024(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    server = ifx_db.server_info( conn )
     
    if conn != 0:
      drop = 'DROP TABLE test_primary_keys'
      try:
        result = ifx_db.exec_immediate(conn, drop)
      except:
        pass
      drop = 'DROP TABLE test_keys'
      try:
        result = ifx_db.exec_immediate(conn, drop)
      except:
        pass
      drop = 'DROP TABLE test_foreign_keys'
      try:
        result = ifx_db.exec_immediate(conn, drop)
      except:
        pass

      statement = 'CREATE TABLE test_primary_keys (id INTEGER NOT NULL, PRIMARY KEY(id))'
      result = ifx_db.exec_immediate(conn, statement)
      statement = "INSERT INTO test_primary_keys VALUES (1)"
      result = ifx_db.exec_immediate(conn, statement)
      statement = 'CREATE TABLE test_keys (name VARCHAR(30) NOT NULL, idf INTEGER NOT NULL, FOREIGN KEY(idf) REFERENCES test_primary_keys(id), \
                   PRIMARY KEY(name))'
      result = ifx_db.exec_immediate(conn, statement)
      statement = "INSERT INTO test_keys VALUES ('vince', 1)"
      result = ifx_db.exec_immediate(conn, statement)
      statement = 'CREATE TABLE test_foreign_keys (namef VARCHAR(30) NOT NULL, id INTEGER NOT NULL, FOREIGN KEY(namef) REFERENCES test_keys(name))'
      result = ifx_db.exec_immediate(conn, statement)
      statement = "INSERT INTO test_foreign_keys VALUES ('vince', 1)"
      result = ifx_db.exec_immediate(conn, statement)

      stmt = ifx_db.foreign_keys(conn, None, config.user, 'test_primary_keys')
      
      row = ifx_db.fetch_tuple(stmt)
      print row[2]
      print row[3]
      print row[6]
      print row[7]

      stmt = ifx_db.foreign_keys(conn, None, None, None, None, config.user, 'test_keys')
      row = ifx_db.fetch_tuple(stmt)
      print row[2]
      print row[3]
      print row[6]
      print row[7]

      stmt = ifx_db.foreign_keys(conn, None, config.user, 'test_keys', None, None, None)
      row = ifx_db.fetch_tuple(stmt)
      print row[2]
      print row[3]
      print row[6]
      print row[7]

      stmt = ifx_db.foreign_keys(conn, None, config.user, 'test_keys', None, config.user, 'test_foreign_keys')
      row = ifx_db.fetch_tuple(stmt)
      print row[2]
      print row[3]
      print row[6]
      print row[7]

      try:
        stmt = ifx_db.foreign_keys(conn, None, None, None, None, None, None)
        row = ifx_db.fetch_tuple(stmt)
      except:
        if (not stmt):
          print ifx_db.stmt_errormsg()


      stmt = ifx_db.foreign_keys(conn, None, config.user, 'test_keys', None, 'dummy_schema')
      row = ifx_db.fetch_tuple(stmt)
      if(not row):
        print "No Data Found"
      else:
        print row[2]
        print row[3]
        print row[6]
        print row[7]
      ifx_db.close(conn)
    else:
      print ifx_db.conn_errormsg()
      print "Connection failed\n"

#__END__
#__LUW_EXPECTED__
#TEST_PRIMARY_KEYS
#ID
#TEST_KEYS
#IDF
#TEST_PRIMARY_KEYS
#ID
#TEST_KEYS
#IDF
#TEST_KEYS
#NAME
#TEST_FOREIGN_KEYS
#NAMEF
#TEST_KEYS
#NAME
#TEST_FOREIGN_KEYS
#NAMEF
#[IBM][CLI Driver] CLI0124E  Invalid argument value. SQLSTATE=HY009 SQLCODE=-99999
#No Data Found
#__ZOS_EXPECTED__
#TEST_PRIMARY_KEYS
#ID
#TEST_KEYS
#IDF
#TEST_PRIMARY_KEYS
#ID
#TEST_KEYS
#IDF
#TEST_KEYS
#NAME
#TEST_FOREIGN_KEYS
#NAMEF
#TEST_KEYS
#NAME
#TEST_FOREIGN_KEYS
#NAMEF
#[IBM][CLI Driver] CLI0124E  Invalid argument value. SQLSTATE=HY009 SQLCODE=-99999
#No Data Found
#__SYSTEMI_EXPECTED__
#TEST_PRIMARY_KEYS
#ID
#TEST_KEYS
#IDF
#TEST_PRIMARY_KEYS
#ID
#TEST_KEYS
#IDF
#TEST_KEYS
#NAME
#TEST_FOREIGN_KEYS
#NAMEF
#TEST_KEYS
#NAME
#TEST_FOREIGN_KEYS
#NAMEF
#[IBM][CLI Driver] CLI0124E  Invalid argument value. SQLSTATE=HY009 SQLCODE=-99999
#__IDS_EXPECTED__
#test_primary_keys
#id
#test_keys
#idf
#test_primary_keys
#id
#test_keys
#idf
#test_keys
#name
#test_foreign_keys
#namef
#test_keys
#name
#test_foreign_keys
#namef
#[Microsoft][ODBC Driver Manager] Invalid use of null pointer SQLCODE=0
#test_keys
#name
#test_foreign_keys
#namef