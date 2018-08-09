
### Solaris Build

This note contain information about the driver build on Solaris. It is a note that we received from Indika and team about the build.

```bash
From: Indika 

Hi Sathya,

Here are the summarized steps we have followed to build the INFORMIX ifxpy driver on SOLARIS 11.2 - SPARC. 



1. upgraded the INFORMIX PYTHON driver from "https://www.opencsw.org/packages/python27/" website  

python -V => Python 2.7.11 and it is installed in "/opt/csw/bin" 
ls -lrt /opt/csw/bin/py*

-rwxr-xr-x   1 root     bin         5196 Mar 14  2016 /opt/csw/bin/python2.7
lrwxrwxrwx   1 root     other         22 Jun 26 18:11 /opt/csw/bin/python2 -> /opt/csw/bin/python2.7
lrwxrwxrwx   1 root     other         20 Jun 26 18:11 /opt/csw/bin/python -> /opt/csw/bin/python2


2. Installed py_pip  from https://www.opencsw.org/packages/CSWpy-pip/ URL and also installed wheel (e.g pip install wheel )

3. Cloned the INFORMIX PYTHON driver source code to the SOLARIX box  from the following URL - > https://github.com/OpenInformix/IfxPy.git and extracted to the "/export/home/informix/IFxPy/ " directory. 

4. Installed INFORMIX CSDK 32k binaries to the "/informix_1/cs/csdk "  directory since we are getting errors for 64 bit CSDK driver when building the 'IFXPY' driver for SOLARIS. 

5. Upgraded the GCC version also from https://www.opencsw.org/packages/gcc5g++/ URL

6. Build the driver
export CSDK_HOME=/informix_1/cs/csdk
export MY_PY_DIR=/opt/csw/bin
export PATH=/opt/csw/bin:/informix_1/cs/csdk/bin:/usr/bin:/usr/bin:$PATH
export INFORMIXDIR=/informix_1/cs/csdk
export LD_LIBRARY_PATH=$INFORMIXDIR/lib:$INFORMIXDIR/lib/esql:$INFORMIXDIR/lib/cli
export INFORMIXSQLHOSTS=/informix_1/cs/csdk/etc/sqlhosts
INFORMIXSERVER=DEVELOPMENT_IT

a.cat /informix_1/cs/csdk/etc/sqlhosts
DEVELOPMENT_IT  onsoctcp       192.168.2.211         IDS_11_fib

Note - DBSERVER is located in remote server. 
and e.g # grep -i IDS_11_fib /etc/services
IDS_11_fib      49553/tcp
b.Go to 'IFXPY' driver copied directory - e.g -> /export/home/informix/IFxPy/IfxPy/IfxPy
run "python setup.py bdist_wheel" command 

c.After successful build, it would have created the whl file under dist folder. 
ls -lrt ./dist/*whl
-rw-r--r--   1 root     root      143782 Jul  3 22:41 ./dist/IfxPy-2.7.1-cp27-cp27mu-solaris_2_11_sun4v_32bit.whl

d.Copied  the binary to prebuild 
cp <Above file> ../prebuilt/27x/Linux64/*whl

e.To install run the following commabnd
pip install ../prebuilt/27x/Linux64/IfxPy-2.7.1-cp27-cp27mu-solaris_2_11_sun4v_32bit.whl 

f. Get a sample code to check the connectivity to INFORMIX DB

E.g -> 

import IfxPy
ConStr = "SERVER=DEVELOPMENT_IT;DATABASE=stores;HOST=192.168.2.211;SERVICE=49553;UID=dayanana;PWD=xxxxxxx;"
# netstat -a | findstr  9088
conn = IfxPy.connect( ConStr, "", "")
SetupSqlSet = [
    "create table t1 ( c1 int, c2 char(20), c3 int, c4 int ) ;",
    "insert into t1 values( 1, 'Sunday', 101, 201 );",
    "insert into t1 values( 2, 'Monday', 102, 202 );",
    "insert into t1 values( 3, 'Tuesday', 103, 203 );",
    "insert into t1 values( 4, 'Wednesday', 104, 204 );",
    "insert into t1 values( 5, 'Thursday', 105, 2005 );",
    "insert into t1 values( 6, 'Friday', 106, 206 );",
    "insert into t1 values( 7, 'Saturday', 107, 207 );"
]
try:
    sql = "drop table t1;"
    print ( sql )
    stmt = IfxPy.exec_immediate(conn, sql)
except:
    print ('FYI: drop table failed')
for sql in SetupSqlSet:
    print (sql)
    stmt = IfxPy.exec_immediate(conn, sql)
sql = "SELECT * FROM t1"
stmt = IfxPy.exec_immediate(conn, sql)
dictionary = IfxPy.fetch_both(stmt)
rc = 0
while dictionary != False:
    rc = rc + 1
    print ("--  Record {0} --".format(rc))
    print ("c1 is : ",  dictionary[0])
    print ("c2 is : ", dictionary[1])
    print ("c3 is : ", dictionary["c3"])
    print ("c4 is : ", dictionary[3])
    print (" ")
    dictionary = IfxPy.fetch_both(stmt)
IfxPy.close(conn)
print ("Done")



f. Then run - > python <Sample program name>.py

 output -->>
echo 'select * from t1' |dbaccess stores
Database selected.
         c1 c2                            c3          c4
          1 Sunday                       101         201
          2 Monday                       102         202
          3 Tuesday                      103         203
          4 Wednesday                    104         204
          5 Thursday                     105        2005
          6 Friday                       106         206
          7 Saturday                     107         207
7 row(s) retrieved.
Best Regards,
 
Indika 

```


```
________________________________________
From: Sathyanesh Krishnan

Hi Indika,

Glad to know you could successfully build the driver on Solaris.
It will be great help if you could update the documentation if you found any difference.
That can benefit others on the similar situation.

Regards,
Satyan.

```
