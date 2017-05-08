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

  def test_062_Tables_03(self):
    obj = IfxDbTestFunctions()
    obj.assert_expectf(self.run_test_062)

  def run_test_062(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    server = ifx_db.server_info( conn )

    create = 'CREATE SCHEMA AUTHORIZATION t'
    try:
      result = ifx_db.exec_immediate(conn, create) 
    except:
      pass
    
    create = 'CREATE TABLE t.t1( c1 integer, c2 varchar(40))'
    try:
      result = ifx_db.exec_immediate(conn, create) 
    except:
      pass
    
    create = 'CREATE TABLE t.t2( c1 integer, c2 varchar(40))'
    try:
      result = ifx_db.exec_immediate(conn, create) 
    except:
      pass
    
    create = 'CREATE TABLE t.t3( c1 integer, c2 varchar(40))'
    try:
      result = ifx_db.exec_immediate(conn, create) 
    except:
      pass
    
    create = 'CREATE TABLE t.t4( c1 integer, c2 varchar(40))'
    try:
      result = ifx_db.exec_immediate(conn, create) 
    except:
      pass
    
    if conn:
      if (server.DBMS_NAME[0:3] == 'IDS'):
        schema = 't'
      else:
        schema = 'T'
      result = ifx_db.tables(conn,None,schema);    
      i = 0
      row = ifx_db.fetch_both(result)
      while ( row ):
        str = row[1] + "/" + row[2] + "/" + row[3]
        if (i < 4):
          print str
        i = i + 1
        row = ifx_db.fetch_both(result)

      ifx_db.exec_immediate(conn, 'DROP TABLE t.t1')
      ifx_db.exec_immediate(conn, 'DROP TABLE t.t2')
      ifx_db.exec_immediate(conn, 'DROP TABLE t.t3')
      ifx_db.exec_immediate(conn, 'DROP TABLE t.t4')

      print "done!"
    else:
      print "no connection: #{ifx_db.conn_errormsg}";    

#__END__
#__LUW_EXPECTED__
#T/T1/TABLE
#T/T2/TABLE
#T/T3/TABLE
#T/T4/TABLE
#done!
#__ZOS_EXPECTED__
#T/T1/TABLE
#T/T2/TABLE
#T/T3/TABLE
#T/T4/TABLE
#done!
#__SYSTEMI_EXPECTED__
#T/T1/TABLE
#T/T2/TABLE
#T/T3/TABLE
#T/T4/TABLE
#done!
#__IDS_EXPECTED__
#t/t1/TABLE%s
#t/t2/TABLE%s
#t/t3/TABLE%s
#t/t4/TABLE%s
#done!
