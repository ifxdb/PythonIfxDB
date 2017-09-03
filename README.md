##### Copyright 2017 ifxdb and Informix

### Licensed under the Apache License, Version 2.0

## PythonIfxDB
Informix native Python driver is a high performing data access interface suitable for highly scalable enterprise or IoT solutions that works with Informix database. The **Advanced native extension module** is the heart piece of driver which is completely written in **C language** for better efficiency and performance. The **Python Database API Specification v2.0 API** has been created on top of this native layer with Python code by focusing on application API level compatibility.  

The driver has been well tested across all major platforms such as **ARM**, **Linux**, and **Windows**; and it has been certified to work with **Raspberry Pi** too.  

The development activities of the driver are powered by passion, dedication and independent thinking. You may send pull request, together we grow as an open community; relevant discussion and queries are answered by community through stackoverflow. [http://stackoverflow.com/questions/tagged/informix](http://stackoverflow.com/questions/tagged/informix)  

**FYI**: Soon we will be getting to **pip install**, for the time being you may download prebuilt native driver binary from prebuilt folder. These binaries may not be built with latest source code on the repository.  
* [prebuilt](https://github.com/ifxdb/PythonIfxDB/tree/master/prebuilt)

#### ifx_db (Advanced native extension module)
This set of API contains advanced features defined by Informix. This database extension module is written in C language for better efficiency and performance while maintaining cross platform support.  

#### ifx_pydb (coming soon)
This set of API implements [Python Database API Specification v2.0](http://www.python.org/dev/peps/pep-0249/).

### Project status: Beta 
Most of ifx_db driver (Advanced native extension module) functionality is fully functional; we are in the process of adding documentation, examples and pip install. We will get to RC soon.

##### Coming soon
* Examples 
* Documentation 
* PyPI: https://pypi.python.org/pypi/ifx_db
 
##### Future Roadmap
* Django
* SQLAlchemy 


## Windows build
##### Prerequisite:
* [Python 2.7 or above](https://www.python.org/downloads/)
* [Python 3.4 or above](https://www.python.org/downloads/)
* clone the PythonIfxDB repository
* Visual Studio 2008 or above (Windows Only)
* Informix client SDK 410xC2 or above
* Set environment variable **CSDK_HOME** and **MY_PY_DIR**

### Clone the source code
Let's assume **C:\work** is the location when we clone the PythonIfxDB repository.  
(You may clone it at any location though; if so make adjustment for the instructions as well).

```bat
cd C:\work
or
cd /work 

git clone https://github.com/ifxdb/PythonIfxDB.git
```

##### Build Shell Environment 
Set **CSDK_HOME** and **MY_PY_DIR** environment variables.  
The environment **CSDK_HOME** points to the **Informix Client SDK**.   
The environment **MY_PY_DIR** points to the Python source code installation.  

```bat
REM Open VS2008 (or latest) command windows
SET CSDK_HOME=c:\informix
SET MY_PY_DIR=C:\Dev\Python27
```

##### Starting the build
```bash
cd C:\work\PythonIfxDB\ifx_db
python setup.py build > out.txt 2>&1
```

FYI: 
While running setup.py for package build, Python 2.7 searches for an installed Visual Studio 2008. (The installation path of VS2008 is stored in the variable VS90COMNTOOLS). The general pattern for VS installation path is 
```bat 
VS<internal version number>COMNTOOLS.  
```
That means if you are using higher version of VS then you may map **VSxxCOMNTOOLS** for that VS to **VS90COMNTOOLS**.  

```bash
#For example:   
#If you are using Visual Studio 2010 (VS10):  
SET VS90COMNTOOLS=%VS100COMNTOOLS%  
  
#If you are using Visual Studio 2012 (VS11):   
SET VS90COMNTOOLS=%VS110COMNTOOLS%  
  
#If you are using Visual Studio 2013 (VS12):   
SET VS90COMNTOOLS=%VS120COMNTOOLS%  
  
#If you are using Visual Studio 2015 (VS14):   
SET VS90COMNTOOLS=%VS140COMNTOOLS%  
```

And then issue the folloing command  
```
python setup.py build  > out.txt 2>&1
```

### Install
On successful build the Informix python package (**ifx_db.pyd**) should have built at  
C:\work\PythonIfxDB\ifx_db\build\lib.win-amd64-2.7
For the time being, you may manually copy Informix python package (ifx_db.pyd) to your Python module directory.

```bat
COPY  C:\work\PythonIfxDB\ifx_db\build\lib.win-amd64-2.7\ifx_db.pyd
```


## Linux Build 
##### Prerequisite:
* [Python 2.7 or above](https://www.python.org/downloads)
* [Python 3.4 or above](https://www.python.org/downloads)
* Informix client SDK 410xC2 or above
* Set environment variable CSDK_HOME and MY_PY_DIR
* Operating System Unicode encoding should match with your python interpreter encoding. 

**MY_PY_DIR** points to the Python installation directory. During the driver build it need python header files, if the current Python installation doesn’t have the header file then you may need to get Python source code.

##### FYI: Unicode encoding
The python interpreter used should match with operating system default Unicode encoding. 
Some of the Linux flavors, python interpreter is available with UCS2/UTF16 and also UCS4/UTF32.
If the OS default for Unicode is UTF32 then the ifxdb driver will work if the python interpreter is also using the Unicode UCS4/UTF32.  


###### To check which Unicode encoding your python interpreter is using.
```Python
# When built with --enable-unicode=ucs4:
>>> import sys
>>> print sys.maxunicode
1114111

# When built with --enable-unicode=ucs2:
>>> import sys
>>> print sys.maxunicode
65535
```

#### Build Python from its source code
By any chance if you don’t have the right python interpreter or you don’t have the development environment for building native library then you may have to build python from its source. Python can be built from it source by using the following steps.  

Determine the Unicode encoding needed for your python interpreter. Most of the Linux platforms are by default UCS4/UTF32, the following step is to build python for UCS4/UTF32 Unicode encoded string.

##### [Download and extract python source code](https://www.python.org/downloads)
```bash
cd /work/dev
# rm ./Python
# sudo rm -rf ./Python-2.7.13
tar zxvf Python-2.7.13.tgz
ln -s  ./Python-2.7.13  ./Python

cd /work/dev/Python
sudo ./configure --enable-unicode=ucs4
```
###### Fire the Python build
```bash
$ cd /work/dev/Python
$ sudo ./configure --enable-unicode=ucs4
$ sudo make

# install is not needed for driver build thouhg 
# $ sudo altinstall
```

##### Clone the informix python driver source code
```bash
mkdir /work/ifxdb
cd /work/ifxdb

git clone https://github.com/ifxdb/PythonIfxDB.git
```

##### Set Env for driver build 
```bash
# Say you have installed Informix CSDK or IDS server at /work/informix
# You have installed or unzip Python 2.7 at /work/dev/Python

export CSDK_HOME=/work/informix
export MY_PY_DIR=/work/dev/Python
```

#### Fire the driver build
```bash
cd /work/ifxdb/PythonIfxDB/ifx_db
rm -rf build

python setup.py build > out.txt 2>&1

# if all go well, then Informix native python driver will be at
# if x86 Linux with 64bit build then
ls -l build/lib.linux-x86_64-2.7/ifx_db.so

# Similarly if ARM then 
ls -l build/lib.linux-armv7l-2.7/ifx_db.so
```

##### Copy the dirver native lib
The native lib is good enough to get advance features working. The **Python Database API Specification v2.0** features are wrapper on top of the advance features that can be obtained by copying **ifx_pydb.py**

```bash
# Copy Informix python package (ifx_db.so) to your Python module directory
# For example:
cp /work/ifxdb/PythonIfxDB/ifx_db/build/lib.linux-x86_64-2.7/ifx_db.so .

# if ARM
# cp /work/ifxdb/PythonIfxDB/ifx_db/build/lib.linux-armv7l-2.7/ifx_db.so .
```

####  Quick Try
```bash
mkdir /work/ifxdb/try/
cd /work/ifxdb/try/
cp /work/ifxdb/PythonIfxDB/Examples/test1.py .

rm ifx_db.so
cp /work/ifxdb/PythonIfxDB/ifx_db/build/lib.linux-x86_64-2.7/ifx_db.so .
# if ARM then
# cp /work/ifxdb/PythonIfxDB/ifx_db/build/lib.linux-armv7l-2.7/ifx_db.so .

# Edit test1.py to modify connection information
# You also need the following CSDK setup for driver runtime
# export LD_LIBRARY_PATH=${INFORMIXDIR}/lib:${INFORMIXDIR}/lib/esql:${INFORMIXDIR}/lib/cli:${INFORMIXDIR}/lib:/usr/lib
# export PATH=$INFORMIXDIR/bin:$PATH
```
```
python test1.py
```


## Run full tests
##### Specify connection information
```bash
cd /work/ifxdb/PythonIfxDB/ifx_db
cp   config.py.sample   config.py
# Then Modify the connection properties specified in config.py
```

##### Run all the tests
```
cp /work/ifxdb/PythonIfxDB/ifx_db/build/lib.linux-x86_64-2.7/ifx_db.so .
# if ARM then
# cp /work/ifxdb/PythonIfxDB/ifx_db/build/lib.linux-armv7l-2.7/ifx_db.so .

python tests.py
```

##### Run a single test
```bash
# Single test can be run by specifying test name in the SINGLE_PYTHON_TEST environment variable.

# For example:
SET    SINGLE_PYTHON_TEST=test_001_ConnDb.py
# or
export SINGLE_PYTHON_TEST=test_001_ConnDb.py

python tests.py
```
#### Run tests with Python 3.x
```
The source files in the 'tests' directory were written for Python 2.
To be able to run the tests suite with Python 3 you need to convert the files to Python 3 format.
You can use the '2to3' Python utility in the 'ifx_db/tests' directory, for example:
$ cd /work/ifx_db/PythonIfxDB/ifx_db/tests
$ 2to3 -w *.py
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
stmt = ifx_db.exec_immediate(conn, sql)
dictionary = ifx_db.fetch_both(stmt)

rc = 0
while dictionary != False:
    rc = rc + 1
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

