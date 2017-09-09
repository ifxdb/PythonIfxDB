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

  def test_261_FetchObjectAccess(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_261)

  def run_test_261(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    
    server = IfxPy.server_info( conn )
    if (server.DBMS_NAME[0:3] == 'Inf'):
      op = {IfxPy.ATTR_CASE: IfxPy.CASE_UPPER}
      IfxPy.set_option(conn, op, 1)

    if (server.DBMS_NAME[0:3] == 'Inf'):
      sql = "SELECT breed, TRIM(TRAILING FROM name) AS name FROM animals WHERE id = ?"
    else:
      sql = "SELECT breed, RTRIM(name) AS name FROM animals WHERE id = ?"

    if conn:
      stmt = IfxPy.prepare(conn, sql)
      IfxPy.execute(stmt, (0,))

#      NOTE: This is a workaround
#      function fetch_object() to be implemented...
#      pet = IfxPy.fetch_object(stmt)
#      while (pet):
#          print "Come here, %s, my little %s!" % (pet.NAME, pet.BREED)
#          pet = IfxPy.fetch_object(stmt)
      
      class Pet:
          pass
      
      data = IfxPy.fetch_assoc(stmt)
      while ( data ):
         pet = Pet()
         pet.NAME = data['NAME']
         pet.BREED = data['BREED']
         print "Come here, %s, my little %s!" % (pet.NAME, pet.BREED)
         data = IfxPy.fetch_assoc(stmt)
         
      IfxPy.close(conn)
      
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#Come here, Pook, my little cat!
#__ZOS_EXPECTED__
#Come here, Pook, my little cat!
#__SYSTEMI_EXPECTED__
#Come here, Pook, my little cat!
#__IDS_EXPECTED__
#Come here, Pook, my little cat!
