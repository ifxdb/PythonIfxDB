# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_157_FetchAssocScrollableCursor_01(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_157)

  def run_test_157(self):
    conn = IfxPy.connect(config.ConnStr + 'ENABLESCROLLABLECURSORS=1', config.user, config.password)
    server = IfxPy.server_info( conn )

    if conn:
      sql = "SELECT id, name, breed, weight FROM animals ORDER BY breed"
      if (server.DBMS_NAME[0:3] != 'Inf'):
        result = IfxPy.exec_immediate(conn, sql, {IfxPy.SQL_ATTR_CURSOR_TYPE: IfxPy.SQL_CURSOR_KEYSET_DRIVEN})
      else:
        result = IfxPy.exec_immediate(conn, sql, {IfxPy.SQL_ATTR_CURSOR_TYPE: IfxPy.SQL_CURSOR_STATIC})

      i = 2
      row = IfxPy.fetch_assoc(result, i)
      while ( row ):
        if (server.DBMS_NAME[0:3] == 'Inf'):
	           print "%-5d %-16s %-32s %10s\n" % (row['id'], row['name'], row['breed'], row['weight'])
        else:
	           print "%-5d %-16s %-32s %10s\n" % (row['ID'], row['NAME'], row['BREED'], row['WEIGHT'])
        i = i + 2
        row = IfxPy.fetch_assoc(result, i)
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
