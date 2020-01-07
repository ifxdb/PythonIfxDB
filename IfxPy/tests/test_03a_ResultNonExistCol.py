# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_03a_ResultNonExistCol(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_03a)

  def run_test_03a(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    server = IfxPy.server_info( conn )

    if conn:
      stmt = IfxPy.exec_immediate(conn, "SELECT id, breed, name, weight FROM animals WHERE id = 0")
      
      while ( IfxPy.fetch_row(stmt) ):
         breed = IfxPy.result(stmt, 1)
         print("string(%d) \"%s\"" % (len(breed), breed))
         name = IfxPy.result(stmt, "name")
         print("string(%d) \"%s\"" % (len(name), name))
         name = IfxPy.result(stmt, "passport")
         print(name)
      IfxPy.close(conn)
      
    else:
      print("Connection failed.")

#__END__
#__IDS_EXPECTED__
#string(3) "cat"
#string(16) "Pook            "
#None
