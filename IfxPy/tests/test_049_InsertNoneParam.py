# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_049_InsertNoneParam(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_049)
	  
  def run_test_049(self):      
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)

    IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_OFF)
      
    insert = "INSERT INTO animals (id, breed, name, weight) VALUES (?, ?, ?, ?)"
    select = 'SELECT id, breed, name, weight FROM animals WHERE weight IS NULL'
      
    if conn:
      stmt = IfxPy.prepare(conn, insert)
      
      if IfxPy.execute(stmt, (None, 'ghost', None, None)):
        stmt = IfxPy.exec_immediate(conn, select)
        row = IfxPy.fetch_tuple(stmt)
        while ( row ): 
          #row.each { |child| puts child }
          for child in row:
            print(child)
          row = IfxPy.fetch_tuple(stmt)
      IfxPy.rollback(conn)
    else:
      print("Connection failed.")

#__END__
#__LUW_EXPECTED__
#None
#ghost
#None
#None
#__ZOS_EXPECTED__
#None
#ghost
#None
#None
#__SYSTEMI_EXPECTED__
#None
#ghost
#None
#None
#__IDS_EXPECTED__
#None
#ghost
#None
#None
