### Copyright 2017 ifxdb and Informix

### Licensed under the Apache License, Version 2.0

## PythonIfxDB
Informix Python Driver is a high performing data access interface for Python applications. This module has implementation of Python Database API Specification v2.0 for Informix Dynamic Server and also advanced features as extension. 

#### ifx_db
This set of API contains advanced features defined by Informix. This database extension module is written in C language for better efficiency and performance while maintaining cross platform support.

#### ifx_pydb (coming soon)
This set of API implements [Python Database API Specification v2.0](http://www.python.org/dev/peps/pep-0249/).

### Project status: Alpha
Most of ifx_db driver functionality is fully functional; we are in the process of adding documentation, tests cases and examples. There is a chance API spec might change by the time we arrive public beta.

##### Coming soon
* Linux build 
* Tests
* Examples 
* Documentation 
* PyPI: https://pypi.python.org/pypi/ifx_db
 
##### Future Roadmap
* Django
* SQLAlchemy 


## Build 
##### Prerequisite:
* Python 2.7 or above (Python 3x support will be coming soon)
* clone the PythonIfxDB repository
* Visual Studio 2008 or above (Windows Only)
* Informix client SDK 410xC2 or above
* Set environment variable CSDK_HOME and MY_PY_DIR

### Clone the source code
For easiness of explanation let's assume C:\work is the location when we clone the PythonIfxDB repository.  
(You may clone it at any location though; if so make adjustment for the instructions as well).

```
cd C:\work
or
cd /work 

git clone https://github.com/ifxdb/PythonIfxDB.git
```


## Windows build 

##### Build Shell Environment 
Set CSDK_HOME and MY_PY_DIR environment variables.  
The environment CSDK_HOME points to the Informix Client SDK installation directory.   
The environment CS MY_PY_DIR points to the Python installation directory.  
FYI: Edit setup.py manually for the time being, it has been hardcoded in it.

```
Open VS2008 (or latest) command windows

Example:
SET CSDK_HOME=c:\informix
SET MY_PY_DIR=C:\Dev\Python27
```

##### Starting the build
```
cd C:\work\PythonIfxDB\ifx_db
python setup.py build > out.txt 2>&1
```

FYI: 
While running setup.py for package build, Python 2.7 searches for an installed Visual Studio 2008. (The installation path of VS2008 is stored in the variable VS90COMNTOOLS). The general pattern for VS installation path is 
``` 
VS<internal version number>COMNTOOLS.  
```
That means if you are using higher version of VS then you may map VSxxCOMNTOOLS for that VS to VS90COMNTOOLS.  
  
For example:   
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


### Install
On successful build the Informix python package (ifx_db.pyd) should have built at  
C:\work\PythonIfxDB\ifx_db\build\lib.win-amd64-2.7
For the time being, you may manually copy Informix python package (ifx_db.pyd) to your Python module directory.

```
COPY  C:\work\PythonIfxDB\ifx_db\build\lib.win-amd64-2.7\ifx_db.pyd
```



## Linux Build 
##### Prerequisite:
* Python 2.7 or above (Python 3x support will be coming soon)
* Informix client SDK 410xC2 or above
* Set environment variable CSDK_HOME and MY_PY_DIR
* Operating System Unicode encoding should match with your python interpreter encoding. 

##### FYI: Unicode encoding
The python interpreter used should match with operating system default Unicode encoding. 
Some of the Linux flavors, python interpreter is available with UCS2/UTF16 and also UCS4/UTF32.
If the OS default for Unicode is UTF32 then the ifxdb driver will work if the python interpreter is also using the Unicode UCS4/UTF32.  

You may compile python interpreter from source by using the following flag to build UCS4/UTF32 Unicode string.
```
--enable-unicode=ucs4
Eg: 
$ cd <Your Python Src>
$ sudo ./configure --enable-unicode=ucs4
$ sudo make
$ sudo altinstall
```

###### To check which Unicode encoding your python interpreter is using.
```
When built with --enable-unicode=ucs4:
>>> import sys
>>> print sys.maxunicode
1114111

When built with --enable-unicode=ucs2:
>>> import sys
>>> print sys.maxunicode
65535
```
  
##### Clone the python driver code
```
mkdir /work/ifxdb
cd /work/ifxdb

git clone https://github.com/ifxdb/PythonIfxDB.git
```

##### Set Env for build 
```
Say you have installed Informix CSDK at /work/sqldist.c  
And you have installed Python 2.7 at /work/dev/Python


export CSDK_HOME=/work/sqldist.c
export MY_PY_DIR=/work/dev/Python
```

##### Fire the build
```
cd /work/ifxdb/PythonIfxDB/ifx_db
rm -rf build

python setup.tmp.linux.py build > out.txt 2>&1

ls -l build/lib.linux-x86_64-2.7/ifx_db.so
```

##### Copy the ifx_db python dirver  
```
cd to your python applicaiton dir
cp /work/ifxdb/PythonIfxDB/ifx_db/build/lib.linux-x86_64-2.7/ifx_db.so .
```



## Example 

#### Connecting to Informix database
```python
import ifx_db

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


#### Simple Query 

##### FYI: ifx_db fetch functions
* ifx_db.fetch_tuple()  
Returns a tuple, indexed by column position, representing a row in a result set. The columns are 0-indexed.  

* ifx_db.fetch_assoc()  
Returns a dictionary, indexed by column name, representing a row in a result set.  

* ifx_db.fetch_both()  
Returns a dictionary, indexed by both column name and position, representing a row in a result set.  

* ifx_db.fetch_row()  
Sets the result set pointer to the next row or requested row. Use this function to iterate through a result set.  


```python
import ifx_db

ConStr = "SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;PROTOCOL=onsoctcp;SERVICE=9088;UID=TestUser1;PWD=MySimplePass1;"

conn = ifx_db.connect( ConStr, "", "")


SetupSqlSet = [
    "drop table t1;", 
    "create table t1 ( c1 int, c2 char(20), c3 int, c4 int ) ;", 
    "insert into t1 values( 1, 'Sunday', 101, 201 );",
    "insert into t1 values( 2, 'Monday', 102, 202 );",
    "insert into t1 values( 3, 'Tuesday', 103, 203 );",
    "insert into t1 values( 4, 'Wednesday', 104, 204 );",
    "insert into t1 values( 5, 'Thursday', 105, 2005 );",
    "insert into t1 values( 6, 'Friday', 106, 206 );",
    "insert into t1 values( 7, 'Saturday', 107, 207 );"
]

for sql in SetupSqlSet:
    print sql
    stmt = ifx_db.exec_immediate(conn, sql)


sql = "SELECT * FROM t1"
stmt2 = ifx_db.exec_immediate(conn, sql)
dictionary = ifx_db.fetch_both(stmt2)

rc = 0
while dictionary != False:
    rc = rc + 1
    print "--  Record {0} --".format(rc)
    print "c1 is : ",  dictionary[0]
    print "c2 is : ", dictionary[1]
    print "c3 is : ", dictionary["c3"]
    print "c4 is : ", dictionary[3]
    print " "
    dictionary = ifx_db.fetch_both(stmt2)

ifx_db.close(conn)

print "Done"
```

### Python Database API Specification
[Python Database API Specification v2.0](http://www.python.org/dev/peps/pep-0249/)  
  

### Informix Advance Python Driver APIs
* ifx_db.connect:  
Connect to the database.  

* ifx_db.exec_immediate:  
Prepares and executes an SQL statement.  

* ifx_db.prepare:  
Prepares an SQL statement.    

* ifx_db.bind_param:  
Binds a Python variable to an SQL statement parameter.  

* ifx_db.execute:  
Executes an SQL statement that was prepared by * ifx_db.prepare().  

* ifx_db.fetch_tuple:  
Returns an tuple  

* ifx_db.fetch_assoc:  
Returns a dictionary  

* ifx_db.fetch_both:  
Returns a dictionary  

* ifx_db.fetch_row:  
Sets the result set pointer to the next row or requested row.  

* ifx_db.result:  
Returns a single column from a row in the result set.  

* ifx_db.active:  
Checks if the specified connection resource is active.  

* ifx_db.autocommit:  
Returns or sets the AUTOCOMMIT state for a database connection.  

* ifx_db.callproc:  
Returns a tuple containing OUT/INOUT variable value.  

* ifx_db.check_function_support:  
return true if fuction is supported otherwise return false.  

* ifx_db.close:  
Close a database connection.  

* ifx_db.conn_error:  
Returns a string containing the SQLSTATE returned by the last connection attempt.  

* ifx_db.conn_errormsg:  
Returns an error message and SQLCODE value representing the reason the last database connection attempt failed. 

* ifx_db.conn_warn:  
Returns a warning string containing the SQLSTATE returned by the last connection attempt.  

* ifx_db.client_info:  
Returns a read-only object with information about the IDS database client.  

* ifx_db.column_privileges:  
Returns a result set listing the columns and associated privileges for a table.  

* ifx_db.columns:  
Returns a result set listing the columns and associated metadata for a table.  

* ifx_db.commit:  
Commits a transaction.  

* ifx_db.cursor_type:  
Returns the cursor type used by a statement resource.  

* ifx_db.execute_many:  
Execute SQL with multiple rows.

* ifx_db.field_display_size:  
Returns the maximum number of bytes required to display a column.  

* ifx_db.field_name:  
Returns the name of the column in the result set.  

* ifx_db.field_nullable:  
Returns indicated column can contain nulls or not.  

* ifx_db.field_num:  
Returns the position of the named column in a result set.  

* ifx_db.field_precision:  
Returns the precision of the indicated column in a result set.  

* ifx_db.field_scale:  
Returns the scale of the indicated column in a result set.  

* ifx_db.field_type:  
Returns the data type of the indicated column in a result set.  

* ifx_db.field_width:  
Returns the width of the indicated column in a result set.  

* ifx_db.foreign_keys:  
Returns a result set listing the foreign keys for a table.  

* ifx_db.free_result:  
Frees resources associated with a result set.  

* ifx_db.free_stmt:  
Frees resources associated with the indicated statement resource.  

* ifx_db.get_option:  
Gets the specified option in the resource.  

* ifx_db.num_fields:  
Returns the number of fields contained in a result set.  

* ifx_db.num_rows:  
Returns the number of rows affected by an SQL statement.  

* ifx_db.get_num_result:  
Returns the number of rows in a current open non-dynamic scrollable cursor.  

* ifx_db.primary_keys:  
Returns a result set listing primary keys for a table.  

* ifx_db.procedure_columns:  
Returns a result set listing the parameters for one or more stored procedures.  

* ifx_db.procedures:  
Returns a result set listing the stored procedures registered in a database.  

* ifx_db.rollback:  Rolls back a transaction.  

* ifx_db.server_info:  
Returns an object with properties that describe the IDS database server.  

* ifx_db.get_db_info:  
Returns an object with properties that describe the IDS database server according to the option passed.  

* ifx_db.set_option:  
Sets the specified option in the resource.  

* ifx_db.special_columns:  
Returns a result set listing the unique row identifier columns for a table.  

* ifx_db.statistics:  
Returns a result set listing the index and statistics for a table.  

* ifx_db.stmt_error:  
Returns a string containing the SQLSTATE returned by an SQL statement.  

* ifx_db.stmt_warn:  
Returns a warning string containing the SQLSTATE returned by last SQL statement.  

* ifx_db.stmt_errormsg:  
Returns a string containing the last SQL statement error message.  

* ifx_db.table_privileges:  
Returns a result set listing the tables and associated privileges in a database. 

* ifx_db.tables:  
Returns a result set listing the tables and associated metadata in a database.  

* ifx_db.get_last_serial_value:  
Returns last serial value inserted for identity column.

