# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#
# NOTE: IDS requires that you pass the schema name (cannot pass nil)
#
# NOTE: IDS will not return any rows from column_privileges unless
#       there have been privileges granted to another user other
#       then the user that is running the script.  This test assumes
#       that no other user has been granted permission and therefore
#       will return no rows.

import unittest, sys
import ifx_db
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):
  
  def test_023_ColumnPrivileges(self):
    obj = IfxDbTestFunctions()
    obj.assert_expectf(self.run_test_023)

  def run_test_023(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    server = ifx_db.server_info( conn )

    if (conn != 0):
      if (server.DBMS_NAME[0:3] == 'IDS'):
        stmt = ifx_db.column_privileges(conn, None, config.user, 'animals')
      else:
        stmt = ifx_db.column_privileges(conn, None, None, 'ANIMALS')
      row = ifx_db.fetch_tuple(stmt)
      if row:
        print row[0]
        print row[1]
        print row[2]
        print row[3]
        print row[4]
        print row[5]
        print row[6]
        print row[7]
      ifx_db.close(conn)
    else:
      print ifx_db.conn_errormsg()
      print "Connection failed\n\n"

#__END__
#__LUW_EXPECTED__
#%s
#%s
#ANIMALS
#BREED
#SYSIBM
#%s
#%s
#YES
#__ZOS_EXPECTED__
#%s
#%s
#ANIMALS
#BREED
#%s
#%s
#%s
#YES
#__SYSTEMI_EXPECTED__
#%s
#%s
#ANIMALS
#BREED
#None
#%s
#%s
#YES
#__IDS_EXPECTED__
