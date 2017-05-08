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

  def test_157_FetchAssocScrollableCursor_01(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_157)

  def run_test_157(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    server = ifx_db.server_info( conn )

    if conn:
      sql = "SELECT id, name, breed, weight FROM animals ORDER BY breed"
      if (server.DBMS_NAME[0:3] != 'IDS'):
        result = ifx_db.exec_immediate(conn, sql, {ifx_db.SQL_ATTR_CURSOR_TYPE: ifx_db.SQL_CURSOR_KEYSET_DRIVEN})
      else:
        result = ifx_db.exec_immediate(conn, sql, {ifx_db.SQL_ATTR_CURSOR_TYPE: ifx_db.SQL_CURSOR_STATIC})

      i = 2
      row = ifx_db.fetch_assoc(result, i)
      while ( row ):
        if (server.DBMS_NAME[0:3] == 'IDS'):
	           print "%-5d %-16s %-32s %10s\n" % (row['id'], row['name'], row['breed'], row['weight'])
        else:
	           print "%-5d %-16s %-32s %10s\n" % (row['ID'], row['NAME'], row['BREED'], row['WEIGHT'])
        i = i + 2
        row = ifx_db.fetch_assoc(result, i)
#
#__END__
#__LUW_EXPECTED__
#0     Pook             cat                                    3.20
#5     Rickety Ride     goat                                   9.70
#2     Smarty           horse                                350.00
#__ZOS_EXPECTED__
#0     Pook             cat                                    3.20
#5     Rickety Ride     goat                                   9.70
#2     Smarty           horse                                350.00
#__SYSTEMI_EXPECTED__
#0     Pook             cat                                    3.20
#5     Rickety Ride     goat                                   9.70
#2     Smarty           horse                                350.00
#__IDS_EXPECTED__
#0     Pook             cat                                    3.20
#5     Rickety Ride     goat                                   9.70
#2     Smarty           horse                                350.00
