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

  def test_065_FilterTableName(self):
    obj = IfxDbTestFunctions()
    obj.assert_expectf(self.run_test_065)

  def run_test_065(self):
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
    
    if (server.DBMS_NAME[0:3] == 'IDS'):
      result = ifx_db.tables(conn, None, '%', "t3")
    else:
      result = ifx_db.tables(conn, None, '%', "T3")
    
    columns = ifx_db.num_fields(result)
    
    for i in range(0, columns):
      print "%s, " % ifx_db.field_name(result, i)
    print "\n\n"
   
    row = ifx_db.fetch_tuple(result) 
    while ( row ):
      final = ", " + row[1] + ", " + row[2] + ", " + row[3] + ", , ";
      row = ifx_db.fetch_tuple(result)

    print final
    
    ifx_db.free_result(result)

    ifx_db.exec_immediate(conn, 'DROP TABLE t.t1')
    ifx_db.exec_immediate(conn, 'DROP TABLE t.t2')
    ifx_db.exec_immediate(conn, 'DROP TABLE t.t3')
    ifx_db.exec_immediate(conn, 'DROP TABLE t.t4')

#__END__
#__LUW_EXPECTED__
#TABLE_CAT, TABLE_SCHEM, TABLE_NAME, TABLE_TYPE, REMARKS, 
#
#, T, T3, TABLE, , 
#__ZOS_EXPECTED__
#TABLE_CAT, TABLE_SCHEM, TABLE_NAME, TABLE_TYPE, REMARKS, 
#
#, %sT, T3, TABLE, , 
#__SYSTEMI_EXPECTED__
#TABLE_CAT, TABLE_SCHEM, TABLE_NAME, TABLE_TYPE, REMARKS, 
#
#, T, T3, TABLE, , 
#__IDS_EXPECTED__
#table_cat, table_schem, table_name, table_type, remarks, 
#
#, t, t3, TABLE, ,
