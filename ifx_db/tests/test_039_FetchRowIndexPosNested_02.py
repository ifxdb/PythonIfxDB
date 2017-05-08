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

  def test_039_FetchRowIndexPosNested_02(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_039)

  def run_test_039(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    serverinfo = ifx_db.server_info( conn )

    if (serverinfo.DBMS_NAME[0:3] != 'IDS'):
      result = ifx_db.prepare(conn, "SELECT * FROM animals", {ifx_db.SQL_ATTR_CURSOR_TYPE: ifx_db.SQL_CURSOR_KEYSET_DRIVEN})
    else:
      result = ifx_db.prepare(conn, "SELECT * FROM animals")
    ifx_db.execute(result)
    row = ifx_db.fetch_row(result)
    while ( row ):
      if (serverinfo.DBMS_NAME[0:3] != 'IDS'):
        result2 = ifx_db.prepare(conn, "SELECT * FROM animals", {ifx_db.SQL_ATTR_CURSOR_TYPE: ifx_db.SQL_CURSOR_KEYSET_DRIVEN})
      else:
        result2 = ifx_db.prepare(conn, "SELECT * FROM animals")
      ifx_db.execute(result2)
      while (ifx_db.fetch_row(result2)):
        print "%s : %s : %s : %s" % (ifx_db.result(result2, 0), \
                                     ifx_db.result(result2, 1), \
                                     ifx_db.result(result2, 2), \
                                     ifx_db.result(result2, 3))
      row = ifx_db.fetch_row(result)

#__END__
#__LUW_EXPECTED__
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#__ZOS_EXPECTED__
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#__SYSTEMI_EXPECTED__
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#__IDS_EXPECTED__
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
#0 : cat : Pook             : 3.20
#1 : dog : Peaches          : 12.30
#2 : horse : Smarty           : 350.00
#3 : gold fish : Bubbles          : 0.10
#4 : budgerigar : Gizmo            : 0.20
#5 : goat : Rickety Ride     : 9.70
#6 : llama : Sweater          : 150.00
