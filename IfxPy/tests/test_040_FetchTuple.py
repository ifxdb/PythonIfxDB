# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_040_FetchTuple(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_040)
  
  def run_test_040(self): 
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)

    IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_OFF)
      
    # Drop the test table, in case it exists
    drop = 'DROP TABLE animals'
    try:
      result = IfxPy.exec_immediate(conn, drop)
    except:
      pass
      
    # Create the test table
    create = 'CREATE TABLE animals (id INTEGER, breed VARCHAR(32), name CHAR(16), weight DECIMAL(7,2))'
    result = IfxPy.exec_immediate(conn, create)
      
    insert = "INSERT INTO animals values (0, 'cat', 'Pook', 3.2)"
      
    IfxPy.exec_immediate(conn, insert)
      
    stmt = IfxPy.exec_immediate(conn, "select * from animals")
    
    onerow = IfxPy.fetch_tuple(stmt)
     
    for element in onerow:
      print element

    IfxPy.rollback(conn)

#__END__
#__LUW_EXPECTED__
#0
#cat
#Pook            
#3.20
#__ZOS_EXPECTED__
#0
#cat
#Pook            
#3.20
#__SYSTEMI_EXPECTED__
#0
#cat
#Pook            
#3.20
#__IDS_EXPECTED__
#0
#cat
#Pook            
#3.20
