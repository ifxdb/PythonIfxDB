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

  def test_021_CommitDelete(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_021)

  def run_test_021(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
      
    if conn:
      stmt = ifx_db.exec_immediate(conn, "SELECT count(*) FROM animals")
      res = ifx_db.fetch_tuple(stmt)
      rows = res[0]
      print rows
        
      ifx_db.autocommit(conn, 0)
      ac = ifx_db.autocommit(conn)
      if ac != 0:
        print "Cannot set ifx_db.AUTOCOMMIT_OFF\nCannot run test"
        #continue
        
      ifx_db.exec_immediate(conn, "DELETE FROM animals")
        
      stmt = ifx_db.exec_immediate(conn, "SELECT count(*) FROM animals")
      res = ifx_db.fetch_tuple(stmt)
      rows = res[0]
      print rows
        
      ifx_db.commit(conn)
      
      stmt = ifx_db.exec_immediate(conn, "SELECT count(*) FROM animals")
      res = ifx_db.fetch_tuple(stmt)
      rows = res[0]
      print rows

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
      stmt = ifx_db.prepare(conn, insert)
      if stmt:
        for animal in animals:
          result = ifx_db.execute(stmt, animal)
      ifx_db.commit(conn)
      ifx_db.close(conn)
    else:
      print "Connection failed."
      
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
