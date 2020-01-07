#

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_048_FetchTupleBinaryData_02(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_048)

  def run_test_048(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    if (not conn):
      print("Could not make a connection.") 
      return 0
    server = IfxPy.server_info( conn )
    
    fp = open("tests/spook_out.png", "wb")
    result = IfxPy.exec_immediate(conn, "SELECT picture FROM animal_pics WHERE name = 'Spook'")
    if (not result):
      print("Could not execute SELECT statement.")
      return 0
    row = IfxPy.fetch_tuple(result)
    if row:
      fp.write(row[0])
    else:
      print(IfxPy.stmt_errormsg())
    fp.close()
    cmp = (open('tests/spook_out.png', "rb").read() == open('tests/spook.png', "rb").read())
    print("Are the files the same:", cmp)

#__END__
#__LUW_EXPECTED__
#Are the files the same: True
#__ZOS_EXPECTED__
#Are the files the same: True
#__SYSTEMI_EXPECTED__
#Are the files the same: True
#__IDS_EXPECTED__
#Are the files the same: True
