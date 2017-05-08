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
    def test_createDropDB(self):
        obj = IfxDbTestFunctions()
        if ((obj.server.DBMS_NAME == "DB2") or (obj.server.DBMS_NAME[0:3] != "DB2")):
            raise unittest.SkipTest("createdb, dropdb not Supported")
        obj.assert_expect(self.run_test_createDropDB)

    def run_test_createDropDB(self):
        database = 'test001'
        conn_str = "DATABASE=%s;HOSTNAME=%s;PORT=%d;PROTOCOL=TCPIP;UID=%s;PWD=%s;" % (database, config.hostname, config.port, config.user, config.password)
        conn_str_attach = "attach=true;HOSTNAME=%s;PORT=%d;PROTOCOL=TCPIP;UID=%s;PWD=%s;" % (config.hostname, config.port, config.user, config.password) #for create db or drop db API it is nessesory that connection only attach to the DB server not to any existing database of DB server
        conn_attach = ifx_db.connect(conn_str_attach, '', '')

        if conn_attach:
            conn = False
            try:
                conn = ifx_db.connect(conn_str, '', '')
            except:
                pass

            if conn:
                ifx_db.close(conn)
                conn = False
                try:
                    ifx_db.dropdb(conn_attach, database)
                except:
                    print 'Errors occurred during drop database'
            try:        
                #create databse   
                rc = ifx_db.createdb(conn_attach, database)
                if rc:
                    conn = ifx_db.connect(conn_str, '', '')
                    if conn:
                        print 'database created sucessfully'
                        ifx_db.close(conn)
                        conn = False
                    else:
                        print 'database is not created'
                else:
                    print 'Errors occurred during create database'

                #drop databse
                rc = ifx_db.dropdb(conn_attach, database)
                if rc:
                    try:
                        conn = ifx_db.connect(conn_str, '', '')
                    except:
                        print 'datbase droped sucessfully'
                    if conn:
                        print 'Errors occurred during drop database'
                        ifx_db.close(conn)
                        conn = False
                else:
                    print 'Errors occurred during delete database'
                    
                #create database with codeset option
                rc = ifx_db.createdb(conn_attach, database, 'iso88591')
                if rc:
                    conn = ifx_db.connect(conn_str, '', '')
                    server_info = ifx_db.server_info( conn )
                    if conn and (server_info.DB_CODEPAGE == 819):
                        print 'database with codeset created sucessfully'
                        ifx_db.close(conn)
                        conn = False
                    else:
                        print 'database is not created'
                else:
                    print 'Errors occurred during create database'

                #drop database
                rc = ifx_db.dropdb(conn_attach, database)
                if rc:
                    try:
                        conn = ifx_db.connect(conn_str, '', '')
                    except:
                        print 'datbase droped sucessfully'
                    if conn:
                        print 'Errors occurred during drop database'
                        ifx_db.close(conn)
                        conn = False
                else:
                    print 'Errors occurred during drop database'
            except:
                print ifx_db.conn_errormsg()
                pass
            ifx_db.close(conn_attach)
        else:
            print ifx_db.conn_errormsg()

#__END__
#__LUW_EXPECTED__
#database created sucessfully
#datbase droped sucessfully
#database with codeset created sucessfully
#datbase droped sucessfully
