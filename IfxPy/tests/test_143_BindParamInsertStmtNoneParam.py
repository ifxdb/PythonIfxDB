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

  def test_143_BindParamInsertStmtNoneParam(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_143)

  def run_test_143(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    
    ifx_db.autocommit(conn, ifx_db.SQL_AUTOCOMMIT_OFF)

    insert1 = "INSERT INTO animals (id, breed, name, weight) VALUES (NULL, 'ghost', NULL, ?)"
    select = 'SELECT id, breed, name, weight FROM animals WHERE weight IS NULL'
    
    if conn:
      stmt = ifx_db.prepare(conn, insert1)
    
      animal = None
      ifx_db.bind_param(stmt, 1, animal)
    
      if ifx_db.execute(stmt):
        stmt = ifx_db.exec_immediate(conn, select)
        row = ifx_db.fetch_tuple(stmt)
        while ( row ):
          #row.each { |child| print child }
          for i in row:
            print i
          row = ifx_db.fetch_tuple(stmt)

      ifx_db.rollback(conn)
    else:
      print "Connection failed."

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
