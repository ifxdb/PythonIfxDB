#

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_264_InsertRetrieveBIGINTTypeColumn(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_264)

  def run_test_264(self):
    # Make a connection
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)

    if conn:
       server = IfxPy.server_info( conn )
       if (server.DBMS_NAME[0:3] == 'Inf'):
          op = {IfxPy.ATTR_CASE: IfxPy.CASE_UPPER}
          IfxPy.set_option(conn, op, 1)

       # Drop the tab_bigint table, in case it exists
       drop = 'DROP TABLE tab_bigint'
       result = ''
       try:
         result = IfxPy.exec_immediate(conn, drop)
       except:
         pass
       # Create the tab_bigint table
       if (server.DBMS_NAME[0:3] == 'Inf'):
          create = "CREATE TABLE tab_bigint (col1 INT8, col2 INT8, col3 INT8, col4 INT8)"
       else:
          create = "CREATE TABLE tab_bigint (col1 BIGINT, col2 BIGINT, col3 BIGINT, col4 BIGINT)"
       result = IfxPy.exec_immediate(conn, create)

       insert = "INSERT INTO tab_bigint values (-9223372036854775807, 9223372036854775807, 0, NULL)"
       res = IfxPy.exec_immediate(conn, insert)
       print "Number of inserted rows:", IfxPy.num_rows(res)

       stmt = IfxPy.prepare(conn, "SELECT * FROM tab_bigint")
       IfxPy.execute(stmt)
       data = IfxPy.fetch_both(stmt)
       while ( data ):
         print data[0]
         print data[1]
         print data[2]
         print data[3]
         print type(data[0]) is long
         print type(data[1]) is long 
         print type(data[2]) is long
         data = IfxPy.fetch_both(stmt)

       # test IfxPy.result for fetch of bigint
       stmt1 = IfxPy.prepare(conn, "SELECT col2 FROM tab_bigint")
       IfxPy.execute(stmt1)
       IfxPy.fetch_row(stmt1, 0)
       if (server.DBMS_NAME[0:3] != 'Inf'):
         row1 = IfxPy.result(stmt1, 'COL2')
       else:
         row1 = IfxPy.result(stmt1, 'col2')
       print row1
       
       IfxPy.close(conn)

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
