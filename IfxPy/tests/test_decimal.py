# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

from decimal import Decimal
import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxDbTestCase(unittest.TestCase):
	def test_decimal(self):
		obj = IfxPyTestFunctions()
		obj.assert_expect(self.run_test_decimal)
	
	def run_test_decimal(self):
		conn = IfxPy.connect(config.ConnStr, config.user, config.password)
		
		if conn:
			serverinfo = IfxPy.server_info( conn )
			
			drop = "DROP TABLE STOCKSHARE"
			try:
				result = IfxPy.exec_immediate(conn,drop)
			except:
				pass
			
			# Create the table stockprice
			create = "CREATE TABLE STOCKSHARE (id SMALLINT NOT NULL, company VARCHAR(30), stockshare DECIMAL(7, 2))"
			result = IfxPy.exec_immediate(conn, create)
			
			# Insert Directly
			insert = "INSERT INTO STOCKSHARE (id, company, stockshare) VALUES (10, 'Megadeth', 100.002)"
			result = IfxPy.exec_immediate(conn, insert)
			
			# Prepare and Insert in the stockprice table
			stockprice = (\
					(20, "Zaral", 102.205),\
					(30, "Megabyte", "98.65"),\
					(40, "Visarsoft", Decimal("123.34")),\
					(50, "Mailersoft", Decimal("134.222")),\
					(60, "Kaerci", Decimal("100.976"))\
					)
			insert = 'INSERT INTO STOCKSHARE (id, company, stockshare) VALUES (?,?,?)'
			stmt = IfxPy.prepare(conn,insert)
			if stmt:
				for company in stockprice:
					result = IfxPy.execute(stmt,company)
			
			id = 70
			company = 'Nirvana'
			stockshare = Decimal("100.1234")
			try:
				IfxPy.bind_param(stmt, 1, id)
				IfxPy.bind_param(stmt, 2, company)
				IfxPy.bind_param(stmt, 3, stockshare)
				error = IfxPy.execute(stmt);
			except:
				excp = sys.exc_info()
				# slot 1 contains error message
				print excp[1]
			
			# Select the result from the table and
			query = 'SELECT * FROM STOCKSHARE ORDER BY id'
			if (serverinfo.DBMS_NAME[0:3] != 'Inf'):
				stmt = IfxPy.prepare(conn, query, {IfxPy.SQL_ATTR_CURSOR_TYPE: IfxPy.SQL_CURSOR_KEYSET_DRIVEN})
			else:
				stmt = IfxPy.prepare(conn, query)
			IfxPy.execute(stmt)
			data = IfxPy.fetch_both( stmt )
			while ( data ):
				print "%s : %s : %s\n" % (data[0], data[1], data[2])
				data = IfxPy.fetch_both( stmt )
			try:
				stmt = IfxPy.prepare(conn, query, {IfxPy.SQL_ATTR_CURSOR_TYPE:  IfxPy.SQL_CURSOR_KEYSET_DRIVEN})
				IfxPy.execute(stmt)
				rc = IfxPy.fetch_row(stmt, -1)
				print "Fetch Row -1:%s " %str(rc)
			except:
				print "Requested row number must be a positive value"
			IfxPy.close(conn)
		else:
			print "Connection failed."

#__END__
#__LUW_EXPECTED__
#10 : Megadeth : 100.00
#20 : Zaral : 102.20
#30 : Megabyte : 98.65
#40 : Visarsoft : 123.34
#50 : Mailersoft : 134.22
#60 : Kaerci : 100.97
#70 : Nirvana : 100.12
#Requested row number must be a positive value
#__ZOS_EXPECTED__
#10 : Megadeth : 100.00
#20 : Zaral : 102.20
#30 : Megabyte : 98.65
#40 : Visarsoft : 123.34
#50 : Mailersoft : 134.22
#60 : Kaerci : 100.97
#70 : Nirvana : 100.12
#Requested row number must be a positive value
#__IDS_EXPECTED__
#10 : Megadeth : 100.00
#20 : Zaral : 102.21
#30 : Megabyte : 98.65
#40 : Visarsoft : 123.34
#50 : Mailersoft : 134.22
#60 : Kaerci : 100.98
#70 : Nirvana : 100.12
#Requested row number must be a positive value