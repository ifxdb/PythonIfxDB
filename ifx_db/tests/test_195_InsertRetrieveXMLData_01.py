# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#
# NOTE: IDS does not support XML as a native datatype (test is invalid for IDS)

import unittest, sys
import ifx_db
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_195_InsertRetrieveXMLData_01(self):
    obj = IfxDbTestFunctions()
    obj.assert_expectf(self.run_test_195)

  def run_test_195(self):
    conn = ifx_db.connect(config.database, config.user, config.password)
    server = ifx_db.server_info( conn )

    if ((server.DBMS_NAME[0:3] != 'IDS') and (server.DBMS_NAME[0:2] != "AS")):
      drop = 'DROP TABLE test_195'
      try:
        result = ifx_db.exec_immediate(conn, drop)
      except:
        pass
      create = 'CREATE TABLE test_195 (id INTEGER, data XML)'
      result = ifx_db.exec_immediate(conn, create)
    
      insert = "INSERT INTO test_195 values (0, '<TEST><def><xml/></def></TEST>')"
    
      ifx_db.exec_immediate(conn, insert)
    
      sql =  "SELECT data FROM test_195"
      stmt = ifx_db.prepare(conn, sql)
      ifx_db.execute(stmt)
      result = ifx_db.fetch_assoc(stmt)
      while( result ):
        print "Output:", result
        result = ifx_db.fetch_assoc(stmt)
      ifx_db.close(conn)
    else:
      print "Native XML datatype is not supported."

#__END__
#__LUW_EXPECTED__
#Output:%s<TEST><def><xml/></def></TEST>
#__ZOS_EXPECTED__
#Output:%s<TEST><def><xml/></def></TEST>
#__SYSTEMI_EXPECTED__
#Native XML datatype is not supported.
#__IDS_EXPECTED__
#Native XML datatype is not supported.
