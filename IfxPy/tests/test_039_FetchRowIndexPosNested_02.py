# 

#

#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_039_FetchRowIndexPosNested_02(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_039)

  def run_test_039(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)
    serverinfo = IfxPy.server_info( conn )

    if (serverinfo.DBMS_NAME[0:3] != 'Inf'):
      result = IfxPy.prepare(conn, "SELECT * FROM animals", {IfxPy.SQL_ATTR_CURSOR_TYPE: IfxPy.SQL_CURSOR_KEYSET_DRIVEN})
    else:
      result = IfxPy.prepare(conn, "SELECT * FROM animals")
    IfxPy.execute(result)
    row = IfxPy.fetch_row(result)
    while ( row ):
      if (serverinfo.DBMS_NAME[0:3] != 'Inf'):
        result2 = IfxPy.prepare(conn, "SELECT * FROM animals", {IfxPy.SQL_ATTR_CURSOR_TYPE: IfxPy.SQL_CURSOR_KEYSET_DRIVEN})
      else:
        result2 = IfxPy.prepare(conn, "SELECT * FROM animals")
      IfxPy.execute(result2)
      while (IfxPy.fetch_row(result2)):
        print("%s : %s : %s : %s" % (IfxPy.result(result2, 0), \
                                     IfxPy.result(result2, 1), \
                                     IfxPy.result(result2, 2), \
                                     IfxPy.result(result2, 3)))
      row = IfxPy.fetch_row(result)

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
