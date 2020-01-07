# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_143_BindParamInsertStmtNoneParam(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_143)

  def run_test_143(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_OFF)

    insert1 = "INSERT INTO animals (id, breed, name, weight) VALUES (NULL, 'ghost', NULL, ?)"
    select = 'SELECT id, breed, name, weight FROM animals WHERE weight IS NULL'
    
    if conn:
      stmt = IfxPy.prepare(conn, insert1)
    
      animal = None
      IfxPy.bind_param(stmt, 1, animal)
    
      if IfxPy.execute(stmt):
        stmt = IfxPy.exec_immediate(conn, select)
        row = IfxPy.fetch_tuple(stmt)
        while ( row ):
          #row.each { |child| print child }
          for i in row:
            print(i)
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
