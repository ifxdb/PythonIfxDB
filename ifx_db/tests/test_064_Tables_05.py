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

  def test_064_Tables_05(self):
    obj = IfxDbTestFunctions()
    obj.assert_expectf(self.run_test_064)

  def run_test_064(self):
    conn = ifx_db.connect(config.database, config.user, config.password)
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
    
    if (server.DBMS_NAME[0:3] == 'IDS'):
        result = ifx_db.tables(conn, None, 't')
    else:
        result = ifx_db.tables(conn, None, 'T')
    
    for i in range(0, ifx_db.num_fields(result)):
      print "%s, " % ifx_db.field_name(result, i)
    print
    print
  
    i = 0
    row = ifx_db.fetch_tuple(result)
    while ( row ):
      ifx_db.num_fields(result)
      if (i < 4):
        print ", " + row[1] + ", " + row[2] + ", " + row[3] + ", , \n"
      i = i + 1
      row = ifx_db.fetch_tuple(result)

    ifx_db.free_result(result)

    ifx_db.exec_immediate(conn, 'DROP TABLE t.t1')
    ifx_db.exec_immediate(conn, 'DROP TABLE t.t2')
    ifx_db.exec_immediate(conn, 'DROP TABLE t.t3')
    ifx_db.exec_immediate(conn, 'DROP TABLE t.t4')

#__END__
#__LUW_EXPECTED__
#TABLE_CAT, TABLE_SCHEM, TABLE_NAME, TABLE_TYPE, REMARKS, 
#
#, T, T1, TABLE, , 
#, T, T2, TABLE, , 
#, T, T3, TABLE, , 
#, T, T4, TABLE, , 
#__ZOS_EXPECTED__
#TABLE_CAT, TABLE_SCHEM, TABLE_NAME, TABLE_TYPE, REMARKS, 
#
#, T, T1, TABLE, , 
#, T, T2, TABLE, , 
#, T, T3, TABLE, , 
#, T, T4, TABLE, , 
#__SYSTEMI_EXPECTED__
#TABLE_CAT, TABLE_SCHEM, TABLE_NAME, TABLE_TYPE, REMARKS, 
#
#, T, T1, TABLE, , 
#, T, T2, TABLE, , 
#, T, T3, TABLE, , 
#, T, T4, TABLE, , 
#__IDS_EXPECTED__
#table_cat, table_schem, table_name, table_type, remarks, 
#
#, t, t1, TABLE%s, , 
#, t, t2, TABLE%s, , 
#, t, t3, TABLE%s, , 
#, t, t4, TABLE%s, ,
