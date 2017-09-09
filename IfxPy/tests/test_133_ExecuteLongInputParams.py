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

  def test_133_ExecuteLongInputParams(self):
    obj = IfxDbTestFunctions()
    obj.assert_expectf(self.run_test_133)

  def run_test_133(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)

    if (not conn):
      print "Connection failed."
      return 0

    ifx_db.autocommit(conn, ifx_db.SQL_AUTOCOMMIT_OFF)

    print "Starting test ..."
    res = ''
    sql =  "INSERT INTO animals (id, breed, name, weight) VALUES (?, ?, ?, ?)"
    try:
      stmt = ifx_db.prepare(conn, sql)
      res = ifx_db.execute(stmt,(128, 'hacker of human and technological nature', 'Wez the ruler of all things PECL', 88.3))
      
      stmt = ifx_db.prepare(conn, "SELECT breed, name FROM animals WHERE id = ?")
      res = ifx_db.execute(stmt, (128,))
      row = ifx_db.fetch_assoc(stmt)
      
      for i in row:
	         print i

      ifx_db.rollback(conn)
      print "Done"
    except:
      print "SQLSTATE: %s" % ifx_db.stmt_error(stmt)
      print "Message: %s" % ifx_db.stmt_errormsg(stmt)

    try:
        stmt = ifx_db.prepare(conn, "SELECT breed, name FROM animals WHERE id = ?")
        res = ifx_db.execute(stmt, (128,))
        row = ifx_db.fetch_assoc(stmt)
        if (row):
            for i in row:
                print i
        print res
        print "SQLSTATE: %s" % ifx_db.stmt_error(stmt)
        print "Message: %s" % ifx_db.stmt_errormsg(stmt)
    except:
        print "An Exception is not expected"
        print "SQLSTATE: %s" % ifx_db.stmt_error(stmt)
        print "Message: %s" % ifx_db.stmt_errormsg(stmt)

    ifx_db.rollback(conn)
    print "Done"

#__END__
#__IDS_EXPECTED__
#Starting test ...
#
#SQLSTATE: 22001
#Message: [Informix][Informix ODBC Driver]String data right truncation. SQLCODE=-11023
#True
#SQLSTATE: 
#Message: 
#Done
