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

  def test_264_InsertRetrieveBIGINTTypeColumn(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_264)

  def run_test_264(self):
    # Make a connection
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)

    if conn:
       server = ifx_db.server_info( conn )
       if (server.DBMS_NAME[0:3] == 'IDS'):
          op = {ifx_db.ATTR_CASE: ifx_db.CASE_UPPER}
          ifx_db.set_option(conn, op, 1)

       # Drop the tab_bigint table, in case it exists
       drop = 'DROP TABLE tab_bigint'
       result = ''
       try:
         result = ifx_db.exec_immediate(conn, drop)
       except:
         pass
       # Create the tab_bigint table
       if (server.DBMS_NAME[0:3] == 'IDS'):
          create = "CREATE TABLE tab_bigint (col1 INT8, col2 INT8, col3 INT8, col4 INT8)"
       else:
          create = "CREATE TABLE tab_bigint (col1 BIGINT, col2 BIGINT, col3 BIGINT, col4 BIGINT)"
       result = ifx_db.exec_immediate(conn, create)

       insert = "INSERT INTO tab_bigint values (-9223372036854775807, 9223372036854775807, 0, NULL)"
       res = ifx_db.exec_immediate(conn, insert)
       print "Number of inserted rows:", ifx_db.num_rows(res)

       stmt = ifx_db.prepare(conn, "SELECT * FROM tab_bigint")
       ifx_db.execute(stmt)
       data = ifx_db.fetch_both(stmt)
       while ( data ):
         print data[0]
         print data[1]
         print data[2]
         print data[3]
         print type(data[0]) is long
         print type(data[1]) is long 
         print type(data[2]) is long
         data = ifx_db.fetch_both(stmt)

       # test ifx_db.result for fetch of bigint
       stmt1 = ifx_db.prepare(conn, "SELECT col2 FROM tab_bigint")
       ifx_db.execute(stmt1)
       ifx_db.fetch_row(stmt1, 0)
       if (server.DBMS_NAME[0:3] != 'IDS'):
         row1 = ifx_db.result(stmt1, 'COL2')
       else:
         row1 = ifx_db.result(stmt1, 'col2')
       print row1
       
       ifx_db.close(conn)

#__END__
#__LUW_EXPECTED__
#Number of inserted rows: 1
#-9223372036854775807
#9223372036854775807
#0
#None
#True
#True
#True
#9223372036854775807
#__ZOS_EXPECTED__
#Number of inserted rows: 1
#-9223372036854775807
#9223372036854775807
#0
#None
#True
#True
#True
#9223372036854775807
#__SYSTEMI_EXPECTED__
#Number of inserted rows: 1
#-9223372036854775807
#9223372036854775807
#0
#None
#True
#True
#True
#9223372036854775807
#__IDS_EXPECTED__
#Number of inserted rows: 1
#-9223372036854775807
#9223372036854775807
#0
#None
#True
#True
#True
#9223372036854775807
