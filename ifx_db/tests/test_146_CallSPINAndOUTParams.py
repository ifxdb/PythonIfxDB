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

  def test_146_CallSPINAndOUTParams(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_146)

  def run_test_146(self):      
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    server = ifx_db.server_info( conn )
    
    if conn:
      name = "Peaches"
      second_name = "Rickety Ride"
      weight = 0
    
      print "Values of bound parameters _before_ CALL:"
      print "  1: %s 2: %s 3: %d\n" % (name, second_name, weight)
     	
      stmt, name, second_name, weight = ifx_db.callproc(conn, 'match_animal', (name, second_name, weight))
    
      if stmt is not None:
        print "Values of bound parameters _after_ CALL:"
        print "  1: %s 2: %s 3: %d\n" % (name, second_name, weight)

#__END__
#__IDS_EXPECTED__
#Values of bound parameters _before_ CALL:
#  1: Peaches 2: Rickety Ride 3: 0
#
#Values of bound parameters _after_ CALL:
#  1: Peaches 2: TRUE 3: 12
#
