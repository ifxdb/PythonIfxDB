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

  def test_008_ColumnInfo(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_008)

  def run_test_008(self):
    op = {IfxPy.ATTR_CASE: IfxPy.CASE_NATURAL}
    conn = IfxPy.connect(config.ConnStr, config.user, config.password, op)
    server = IfxPy.server_info( conn )
    result = IfxPy.columns(conn,None,None,"employee")
    row = IfxPy.fetch_both(result)
    value1 = None
    value2 = None
    value3 = None
    value4 = None
    if (row.has_key('TABLE_NAME')):
      value1 = row['TABLE_NAME']
    if (row.has_key('COLUMN_NAME')):
      value2 = row['COLUMN_NAME']
    if (row.has_key('table_name')):
      value3 = row['table_name']
    if (row.has_key('column_name')):
      value4 = row['column_name']
    print value1
    print value2
    print value3
    print value4

    op = {IfxPy.ATTR_CASE: IfxPy.CASE_UPPER}
    IfxPy.set_option(conn, op, 1)
    result = IfxPy.columns(conn,None,None,"employee")
    row = IfxPy.fetch_both(result)
    value1 = None
    value2 = None
    value3 = None
    value4 = None
    if (row.has_key('TABLE_NAME')):
      value1 = row['TABLE_NAME']
    if (row.has_key('COLUMN_NAME')):
      value2 = row['COLUMN_NAME']
    if (row.has_key('table_name')):
      value3 = row['table_name']
    if (row.has_key('column_name')):
      value4 = row['column_name']
    print value1
    print value2
    print value3
    print value4
    
    op = {IfxPy.ATTR_CASE: IfxPy.CASE_LOWER}
    IfxPy.set_option(conn, op, 1)
    result = IfxPy.columns(conn,None,None,"employee")
    row = IfxPy.fetch_both(result)
    value1 = None
    value2 = None
    value3 = None
    value4 = None
    if (row.has_key('TABLE_NAME')):
      value1 = row['TABLE_NAME']
    if (row.has_key('COLUMN_NAME')):
      value2 = row['COLUMN_NAME']
    if (row.has_key('table_name')):
      value3 = row['table_name']
    if (row.has_key('column_name')):
      value4 = row['column_name']
    print value1
    print value2
    print value3
    print value4

#__END__
#__IDS_EXPECTED__
#employee
#empno
#None
#None
#employee
#empno
#None
#None
#None
#None
#employee
#empno
