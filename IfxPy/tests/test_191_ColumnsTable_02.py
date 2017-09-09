# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#
# NOTE: IDS requires that you pass the schema name (cannot pass None)

import unittest, sys
import ifx_db
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_191_ColumnsTable_02(self):
    obj = IfxDbTestFunctions()
    obj.assert_expectf(self.run_test_191)

  def run_test_191(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    server = ifx_db.server_info( conn )

    if conn:
      result = ifx_db.columns(conn,None,config.user,"emp_photo");    

      i = 0
      row = ifx_db.fetch_both(result)
      while ( row ):
        if ( (row['COLUMN_NAME'] != 'emp_rowid') and (i < 3) ):
          print "%s,%s,%s,%s\n" % (row['TABLE_SCHEM'], 
          row['TABLE_NAME'], row['COLUMN_NAME'], row['IS_NULLABLE'])
        i = i + 1
        row = ifx_db.fetch_both(result)
      print "done!"
    else:
      print "no connection: ", ifx_db.conn_errormsg()    

#__END__
#__IDS_EXPECTED__
#%s,emp_photo,empno,NO
#%s,emp_photo,photo_format,NO
#%s,emp_photo,picture,YES
#done!
