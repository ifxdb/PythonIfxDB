### Copyright 2017 ifxdb and Informix

### Licensed under the Apache License, Version 2.0

## PythonIfxDB
Informix Native Driver for Python

### Project status: Internal beta
##### Coming soon
* Linux build 
* PyPI: https://pypi.python.org/pypi/ifx_db
* Tests
* Examples 
* Documentation 
 

## Build 
#### Linux Build 
Coming soon

#### Windows build 
##### Prerequisite:
* Python 2.7 or above (Python 3x support will be coming soon)
* clone the PythonIfxDB repository
* Visual Studio 2008 or above
* Informix client SDK 410xC2 or above
* Set environment variable CSDK_HOM and MY_PY_DIR

```
Example: 
SET CSDK_HOM=c:\informix
SET MY_PY_DIR=C:\Dev\Python27
```

### Get the source code
For easiness of explanation let me assume C:\Work0 is the location when we clone the PythonIfxDB repository.  
(You may clone it at any location though, if so make adjustment for the instructions as well).

```
cd C:\Work0
git clone https://github.com/ifxdb/PythonIfxDB.git
```

### Windows build 
```
Open VS2008 (or latest) command windows
cd C:\Work0\PythonIfxDB\ifx_db
edit setup.py


python setup.py build > out.txt 2>&1

FYI: 
While running setup.py for package build, Python 2.7 searches for an installed Visual Studio 2008.  
(The installation path of VS2008 is stored in the variable VS90COMNTOOLS).  
The general pattern for VS installation path is  
VS<internal version number>COMNTOOLS.  
That means if you are using higher version of VS then you may map VSxxCOMNTOOLS for that VS to VS90COMNTOOLS. For example:

If you are using Visual Studio 2010 (VS10): 
SET VS90COMNTOOLS=%VS100COMNTOOLS%

If you are using Visual Studio 2012 (VS11): 
SET VS90COMNTOOLS=%VS110COMNTOOLS%

If you are using Visual Studio 2013 (VS12): 
SET VS90COMNTOOLS=%VS120COMNTOOLS%

If you are using Visual Studio 2015 (VS14): 
SET VS90COMNTOOLS=%VS140COMNTOOLS%

and then issue the folloing command
python setup.py build
```

### Install
On successful build the Informix python package (ifx_db.pyd) should have built at 
```
C:\Work0\PythonIfxDB\ifx_db\build\lib.win-amd64-2.7
For the time being, you may manually copy Informix python package (ifx_db.pyd) to your Python module directory.

CD MyPyModuleDir
COPY C:\Work0\PythonIfxDB\ifx_db\build\lib.win-amd64-2.7\ ifx_db.pyd
```


## Example 

#### Simple  connect and disconnect
```python
ConStr = "SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;PROTOCOL=onsoctcp;SERVICE=9088;UID=TestUser1;PWD=MySimplePass1;"

# netstat -a | findstr  9088
conn = ifx_db.connect( ConStr, "", "")

# Do some work
# -- -- -- -- --
# -- -- -- -- --
ifx_db.close(conn)
```


### Preliminary diagnostic tips 
##### Cconnection problem
+ check the service port mapped to which IP etc
- for example the port you configured is 9088 then
- netstat -a | findstr  9088


#### Simple Query database
```python

import ifx_db

ConStr = "SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;PROTOCOL=onsoctcp;SERVICE=9088;UID=TestUser1;PWD=MySimplePass1;"

conn = ifx_db.connect( ConStr, "", "")


SetupSqlSet = [
    "drop table t1;", 
    "create table t1 ( c1 int, c2 char(20), c3 int, c4 int ) ;", 
    "insert into t1 values( 1, 'val 1', 101, 201 );",
    "insert into t1 values( 2, 'val 2', 102, 202 );",
    "insert into t1 values( 3, 'val 3', 103, 203 );",
    "insert into t1 values( 4, 'val 4', 104, 204 );",
    "insert into t1 values( 5, 'val 5', 105, 2005 );"
]

for sql in SetupSqlSet:
    print sql
    stmt = ifx_db.exec_immediate(conn, sql)


sql = "SELECT * FROM t1"
stmt = ifx_db.exec_immediate(conn, sql)
dictionary = ifx_db.fetch_both(stmt)

rc = 0
while dictionary != False:
    rc = rc + 1;
    print "--  Record {0} --".format(rc)
    print "c1 is : ",  dictionary[0]
    print "c2 is : ", dictionary[1]
    print "c3 is : ", dictionary["c3"]
    print "c4 is : ", dictionary[3]
    print " "
    dictionary = ifx_db.fetch_both(stmt)

ifx_db.close(conn)

print "Done"

```
