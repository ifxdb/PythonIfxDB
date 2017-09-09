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

  def test_157a_FetchAssocWithoutScrollableCursorErr(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_157a)

  def run_test_157a(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    server = IfxPy.server_info( conn )

    print "Starting..."
    if conn:
      sql = "SELECT id, name, breed, weight FROM animals ORDER BY breed"
      result = IfxPy.exec_immediate(conn, sql)

      try:
          i = 2
          row = IfxPy.fetch_assoc(result, i)
          while ( row ):
              if (server.DBMS_NAME[0:3] == 'Inf'):
                print "%-5d %-16s %-32s %10s" % (row['id'], row['name'], row['breed'], row['weight'])
              else:
                print "%-5d %-16s %-32s %10s" % (row['ID'], row['NAME'], row['BREED'], row['WEIGHT'])
              i = i + 2
          row = IfxPy.fetch_assoc(result, i)
      except:
          print "SQLSTATE: %s" % IfxPy.stmt_error(result)
          print "Message: %s" % IfxPy.stmt_errormsg(result)
	
      print "DONE"

#__END__
#__LUW_EXPECTED__
#Starting...
#SQLSTATE: HY106
#Message: [IBM][CLI Driver] CLI0145E  Fetch type out of range. SQLSTATE=HY106 SQLCODE=-99999
#DONE
#__ZOS_EXPECTED__
#Starting...
#SQLSTATE: HY106
#Message: [IBM][CLI Driver] CLI0145E  Fetch type out of range. SQLSTATE=HY106 SQLCODE=-99999
#DONE
#__SYSTEMI_EXPECTED__
#Starting...
#SQLSTATE: HY106
#Message: [IBM][CLI Driver] CLI0145E  Fetch type out of range. SQLSTATE=HY106 SQLCODE=-99999
#DONE
#__IDS_EXPECTED__
#Starting...
#SQLSTATE: HY106
#Message: [Informix][Informix ODBC Driver]Fetch type out of range. SQLCODE=-11086
#DONE

