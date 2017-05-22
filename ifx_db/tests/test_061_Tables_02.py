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

  def test_061_Tables_02(self):
    obj = IfxDbTestFunctions()
    obj.assert_expectf(self.run_test_061)

  def run_test_061(self):
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
      server = ifx_db.server_info( conn )
      op = {ifx_db.ATTR_CASE: ifx_db.CASE_UPPER}
      ifx_db.set_option(conn, op, 1)

      result = ifx_db.tables(conn, None, 't');
      i = 0
      row = ifx_db.fetch_both(result)
      while ( row ):
        str = row['TABLE_SCHEM'] + row['TABLE_NAME'] + row['TABLE_TYPE']
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
      print "no connection: %s" % ifx_db.conn_errormsg()

#__END__
#__IDS_EXPECTED__
#tt1TABLE%s
#tt2TABLE%s
#tt3TABLE%s
#tt4TABLE%s
#done!
