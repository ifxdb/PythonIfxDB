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

  def test_049_InsertNoneParam(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_049)
	  
  def run_test_049(self):      
    conn = ifx_db.connect(config.database, config.user, config.password)

    ifx_db.autocommit(conn, ifx_db.SQL_AUTOCOMMIT_OFF)
      
    insert = "INSERT INTO animals (id, breed, name, weight) VALUES (?, ?, ?, ?)"
    select = 'SELECT id, breed, name, weight FROM animals WHERE weight IS NULL'
      
    if conn:
      stmt = ifx_db.prepare(conn, insert)
      
      if ifx_db.execute(stmt, (None, 'ghost', None, None)):
        stmt = ifx_db.exec_immediate(conn, select)
        row = ifx_db.fetch_tuple(stmt)
        while ( row ): 
          #row.each { |child| puts child }
          for child in row:
            print child
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
