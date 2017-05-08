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

  def test_060_Tables_01(self):
    obj = IfxDbTestFunctions()
    obj.assert_expectf(self.run_test_060)

  def run_test_060(self):
    conn = ifx_db.connect(config.database, config.user, config.password)
    server = ifx_db.server_info( conn )
    
    create = 'CREATE SCHEMA AUTHORIZATION t'
    try:
      result = ifx_db.exec_immediate(conn, create)
    except:
      pass
    
    create = 'CREATE TABLE t.t1( c1 INTEGER, c2 VARCHAR(40))'
    try:
      result = ifx_db.exec_immediate(conn, create)
    except:
      pass
    
    create = 'CREATE TABLE t.t2( c1 INTEGER, c2 VARCHAR(40))'
    try:
      result = ifx_db.exec_immediate(conn, create) 
    except:
      pass
    
    create = 'CREATE TABLE t.t3( c1 INTEGER, c2 VARCHAR(40))'
    try:
      result = ifx_db.exec_immediate(conn, create) 
    except:
      pass
    
    create = 'CREATE TABLE t.t4( c1 INTEGER, c2 VARCHAR(40))'
    try:
      result = ifx_db.exec_immediate(conn, create) 
    except:
      pass
    
    if conn:
      if (server.DBMS_NAME[0:3] == 'IDS'):
        result = ifx_db.tables(conn, None, 't')
      else:
        result = ifx_db.tables(conn, None, 'T')
      i = 0
      row = ifx_db.fetch_both(result)
      while ( row ):
        if (i < 4):
          print "/%s/%s" % (row[1], row[2])
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
#/T/T1
#/T/T2
#/T/T3
#/T/T4
#done!
#__ZOS_EXPECTED__
#/T/T1
#/T/T2
#/T/T3
#/T/T4
#done!
#__SYSTEMI_EXPECTED__
#/T/T1
#/T/T2
#/T/T3
#/T/T4
#done!
#__IDS_EXPECTED__
#/t/t1
#/t/t2
#/t/t3
#/t/t4
#done!
