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

  def test_190_ColumnsTable_01(self):
    obj = IfxDbTestFunctions()
    obj.assert_expectf(self.run_test_190)

  def run_test_190(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    server = ifx_db.server_info( conn )

    if conn:
      if (server.DBMS_NAME[0:3] == 'Inf'):
        result = ifx_db.columns(conn,None,config.user,"employee")
      else:
        result = ifx_db.columns(conn,None,None,"EMPLOYEE")

      row = ifx_db.fetch_tuple(result)
      while ( row ):
        str = row[1] + "/" + row[3]
        print str
        row = ifx_db.fetch_tuple(result)
      print "done!"
    else:
      print "no connection:", ifx_db.conn_errormsg()

#__END__
#__LUW_EXPECTED__
#%s/EMPNO
#%s/FIRSTNME
#%s/MIDINIT
#%s/LASTNAME
#%s/WORKDEPT
#%s/PHONENO
#%s/HIREDATE
#%s/JOB
#%s/EDLEVEL
#%s/SEX
#%s/BIRTHDATE
#%s/SALARY
#%s/BONUS
#%s/COMM
#done!
#__ZOS_EXPECTED__
#%s/EMPNO
#%s/FIRSTNME
#%s/MIDINIT
#%s/LASTNAME
#%s/WORKDEPT
#%s/PHONENO
#%s/HIREDATE
#%s/JOB
#%s/EDLEVEL
#%s/SEX
#%s/BIRTHDATE
#%s/SALARY
#%s/BONUS
#%s/COMM
#done!
#__SYSTEMI_EXPECTED__
#%s/EMPNO
#%s/FIRSTNME
#%s/MIDINIT
#%s/LASTNAME
#%s/WORKDEPT
#%s/PHONENO
#%s/HIREDATE
#%s/JOB
#%s/EDLEVEL
#%s/SEX
#%s/BIRTHDATE
#%s/SALARY
#%s/BONUS
#%s/COMM
#done!
#__IDS_EXPECTED__
#%s/empno
#%s/firstnme
#%s/midinit
#%s/lastname
#%s/workdept
#%s/phoneno
#%s/hiredate
#%s/job
#%s/edlevel
#%s/sex
#%s/birthdate
#%s/salary
#%s/bonus
#%s/comm
#done!
