# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_021_CommitDelete(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_021)

  def run_test_021(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
      
    if conn:
      stmt = IfxPy.exec_immediate(conn, "SELECT count(*) FROM animals")
      res = IfxPy.fetch_tuple(stmt)
      rows = res[0]
      print(rows)
        
      IfxPy.autocommit(conn, 0)
      ac = IfxPy.autocommit(conn)
      if ac != 0:
        print("Cannot set IfxPy.AUTOCOMMIT_OFF\nCannot run test")
        #continue
        
      IfxPy.exec_immediate(conn, "DELETE FROM animals")
        
      stmt = IfxPy.exec_immediate(conn, "SELECT count(*) FROM animals")
      res = IfxPy.fetch_tuple(stmt)
      rows = res[0]
      print(rows)
        
      IfxPy.commit(conn)
      
      stmt = IfxPy.exec_immediate(conn, "SELECT count(*) FROM animals")
      res = IfxPy.fetch_tuple(stmt)
      rows = res[0]
      print(rows)

      # Populate the animal table
      animals = (
        (0, 'cat',        'Pook',         3.2),
        (1, 'dog',        'Peaches',      12.3),
        (2, 'horse',      'Smarty',       350.0),
        (3, 'gold fish',  'Bubbles',      0.1),
        (4, 'budgerigar', 'Gizmo',        0.2),
        (5, 'goat',       'Rickety Ride', 9.7),
        (6, 'llama',      'Sweater',      150)
      )
      insert = 'INSERT INTO animals (id, breed, name, weight) VALUES (?, ?, ?, ?)'
      stmt = IfxPy.prepare(conn, insert)
      if stmt:
        for animal in animals:
          result = IfxPy.execute(stmt, animal)
      IfxPy.commit(conn)
      IfxPy.close(conn)
    else:
      print("Connection failed.")
      
#__END__
#__LUW_EXPECTED__
#7
#0
#0
#__ZOS_EXPECTED__
#7
#0
#0
#__SYSTEMI_EXPECTED__
#7
#0
#0
#__IDS_EXPECTED__
#7
#0
#0
