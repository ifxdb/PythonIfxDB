
from __future__ import print_function
import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class Wrapper(str):
  def __del__(self):
    print("Wrapper(" + self + ") being deleted")

class IfxPyTestCase(unittest.TestCase):

  def test_312_CacheBoundParameters(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_312)
  
  def run_test_312(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)

    IfxPy.autocommit(conn, IfxPy.SQL_AUTOCOMMIT_OFF)
    
    query = "INSERT INTO department (deptno, deptname, mgrno, admrdept, location) VALUES (?, ?, ?, ?, ?)"
    
    if conn:
      stmt = IfxPy.prepare(conn, query)
      params = ['STG', 'Systems & Technology', '123456', 'RSF', 'Fiji']

      print("Binding parameters")
      for i,p in enumerate(params, 1):
        IfxPy.bind_param(stmt, i, Wrapper(p))
      
      if IfxPy.execute(stmt):
        print("Executing statement")
        IfxPy.execute(stmt)

        # force the cache to be unbound
        for i,p in enumerate(params, 1):
          IfxPy.bind_param(stmt, i, p)
        
        IfxPy.rollback(conn)
      else:
        print("Connection failed.")

#__END__
#__LUW_EXPECTED__
#Binding parameters
#Executing statement
#Wrapper(STG) being deleted
#Wrapper(Systems & Technology) being deleted
#Wrapper(123456) being deleted
#Wrapper(RSF) being deleted
#Wrapper(Fiji) being deleted
#__ZOS_EXPECTED__
#Binding parameters
#Executing statement
#Wrapper(STG) being deleted
#Wrapper(Systems & Technology) being deleted
#Wrapper(123456) being deleted
#Wrapper(RSF) being deleted
#Wrapper(Fiji) being deleted
#__SYSTEMI_EXPECTED__
#Binding parameters
#Executing statement
#Wrapper(STG) being deleted
#Wrapper(Systems & Technology) being deleted
#Wrapper(123456) being deleted
#Wrapper(RSF) being deleted
#Wrapper(Fiji) being deleted
#__IDS_EXPECTED__
#Binding parameters
#Executing statement
#Wrapper(STG) being deleted
#Wrapper(Systems & Technology) being deleted
#Wrapper(123456) being deleted
#Wrapper(RSF) being deleted
#Wrapper(Fiji) being deleted
