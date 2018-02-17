
##### Licensed under the Apache License, Version 2.0

## [IfxPy](https://openinformix.github.io/IfxPy/)
-------------------------------------------------
Informix native Python driver is a high performing data access interface suitable for highly scalable enterprise and IoT solutions to works with Informix database. The **Advanced native extension module** is the heart piece of driver which is completely written in **C language** for better efficiency and performance. The **Python Database API Specification v2.0 API** has been created on top of this native layer with Python code by focusing on application API level compatibility.  

The driver has been well tested across all major platforms such as **ARM**, **Linux**, and **Windows**; and it has been certified to work with **Raspberry Pi** too.  

The development activities of the driver are powered by passion, dedication and independent thinking. You may send pull request, together we grow as an open community; relevant discussion and queries are answered by community through stackoverflow. [http://stackoverflow.com/questions/tagged/informix](http://stackoverflow.com/questions/tagged/informix)  

**FYI**: Soon we will be getting to **pip install**, for the time being you may download prebuilt native driver binary from prebuilt folder. You may build the drive from its source code on your environment to pick latest changes.  
* [prebuilt](https://github.com/OpenInformix/IfxPy/tree/master/prebuilt)  
FYI: When you download the prebuilt, clone or zip the repository and then take the prebuilt binary. The usage of wget, curl etc may not get right binary content from github.

#### [IfxPy: (Advanced Native Extension Module)](https://github.com/OpenInformix/IfxPy/wiki)
The Advanced Native Extension Module is the heart of the driver which is completely written in C language for better efficiency and performance while maintaining cross platform support.  
Please see the **[IfxPy Wiki](https://github.com/OpenInformix/IfxPy/wiki)** for the documentation. 

#### [IfxPyDbi: Python Database API Specification v2.0 support](http://www.python.org/dev/peps/pep-0249/)
Support for the Python DB API have been created on top of the native layer by focusing on application layer compatibility; then the application source code is generally more portable across databases.


### Project status: Beta 
The driver runtime is mostly functional; we are in the process of adding documentation, examples and pip install. We will get to RC soon.  

**Known Problems**: Large Object Support, Stored Procedures.

##### Coming soon
* PyPI (pit install)
 
##### Future Roadmap
* Django
* SQLAlchemy


## Build the driver from its source code
------------------
The driver source code is platform neutral; you may build the driver on any platforms. If you face any difficulty feel free to reach out to us, we are happy to help you. The following URL has instruction to build it on Windows and Linux. 

* [Windows Build](./LocalBuildWindows.md)
* [Linux Build](./LocalBuildLinux.md)
* [Run tests after the build](RunTests.md)

## Runtime Environment
----------------------
The Informix Python driver has dependency on **Informix Client SDK version 4.10 xC2 or above**. Make sure to set Informix Client SDK runtime environment before running the applications.  

Say **INFORMIXDIR** is the location where you have installed Informix Client SDK.
##### Linux
```bash
export LD_LIBRARY_PATH=${INFORMIXDIR}/lib:${INFORMIXDIR}/lib/esql:${INFORMIXDIR}/lib/cli
```

##### Windows
```bat
# c:\informix
SET PATH=%INFORMIXDIR%\bin;%PATH%
```


## Examples
-----------

#### Connection to the database
The basic connectivity to Informix database.

```python
import IfxPy

ConStr = "SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;SERVICE=9088;UID=informix;PWD=xxxx;"

# netstat -a | findstr  9088
conn = IfxPy.connect( ConStr, "", "")

# Do some work
# -- -- -- -- --
# -- -- -- -- --
IfxPy.close(conn)
```


#### Simple Query 
The driver APIs used in this example are from the set of **Advanced native extension module APIs**  

##### FYI: IfxPy fetch functions
* IfxPy.fetch_tuple()  
Returns a tuple, indexed by column position, representing a row in a result set. The columns are 0-indexed.  

* IfxPy.fetch_assoc()  
Returns a dictionary, indexed by column name, representing a row in a result set.  

* IfxPy.fetch_both()  
Returns a dictionary, indexed by both column name and position, representing a row in a result set.  

* IfxPy.fetch_row()  
Sets the result set pointer to the next row or requested row. Use this function to iterate through a result set.  


```python

import IfxPy

ConStr = "SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;SERVICE=9088;UID=informix;PWD=xxxxx;"

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

```

### [Python Database API Specification v2.0](http://www.python.org/dev/peps/pep-0249/)
-------------------------------------
The Advanced Native Extension Module is the heart of the driver which is completely written in C language for better efficiency and performance. The Python Database API Specification v2.0 APIs have been created on top of this native layer by focusing on application layer compatibility. Then the application source code is generally more portable across databases.


#### Example by using Python DB API
The driver APIs used in this example are from the set of **Python Database API Specification v2.0 APIs**

```python

import IfxPyDbi as dbapi2

ConStr = "SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;SERVICE=9088;UID=informix;PWD=xxxx;"

conn = dbapi2.connect( ConStr, "", "")
cur = conn.cursor()

try:
    stmt = cur.execute('drop table t1;')
except:
    print ('FYI: drop table failed')

cur.execute('create table t1 ( c1 int, c2 char(20), c3 int, c4 int ) ')

cur.execute("insert into t1 values( 1, 'Sunday', 101, 201 )")
cur.execute("insert into t1 values( 2, 'Monday', 102, 202 )")
cur.execute("insert into t1 values( 3, 'Tuesday', 103, 203 )")
cur.execute("insert into t1 values( 4, 'Wednesday', 104, 204 )")
cur.execute("insert into t1 values( 5, 'Thursday', 105, 2005 )")
cur.execute("insert into t1 values( 6, 'Friday', 106, 206 )")
cur.execute("insert into t1 values( 7, 'Saturday', 107, 207 )")

conn.commit ()

cur.execute ("SELECT * FROM t1")
rows = cur.fetchall()
for i, row in enumerate(rows):
    print ("Row", i, "value = ", row)

cur.close()

conn.close()
print ("Done")

```

#### DB API Example: inserts many records at a time
See the working sample of this module **DbAPI_Sample_executemany.py** in the Examples folder.  

```python
#-- -- -- -- --
#-- -- -- -- --
cur.execute('create table t1 ( c1 int, c2 char(20), c3 int, c4 int ) ')
days = [ (1, 'Sunday',  101, 201),
         (2, 'Monday',  102, 202),
         (3, 'Tuesday', 103, 203),
         (4, 'Wednesday', 104, 204),
         (5, 'Thursday', 105, 205),
         (6, 'Friday', 106, 206),
         (7, 'Saturday', 1027, 207),
       ]
cur.executemany('INSERT INTO t1 VALUES (?,?,?,?)', days)
conn.commit ()
#-- -- -- -- --
#-- -- -- -- --
```

#### DB API Example: params
See the working sample of this module **DbAPI_Sample_Params.py** in the Examples folder.  
```python
#-- -- -- -- --
#-- -- -- -- --
c1_val = 4
cur.execute("UPDATE t1 SET c2 = 'Wednesday!' WHERE c1 = (?)", (c1_val,))
conn.commit()

c3_val = 1004
cur.execute("UPDATE t1 SET c3 = (?) WHERE c1 = 4", (c3_val,))
conn.commit()

cur.execute("select * FROM t1 WHERE c1 = ?", (c1_val,))
row = cur.fetchone()
print ( "value = ", row)
#-- -- -- -- --
#-- -- -- -- --
```


### [Advanced native extension module APIs](https://github.com/OpenInformix/IfxPy/wiki)
-------------------------------------------
* IfxPy.connect:  
Connect to the database.  

* IfxPy.exec_immediate:  
Prepares and executes an SQL statement.  

* IfxPy.prepare:  
Prepares an SQL statement.    

* IfxPy.bind_param:  
Binds a Python variable to an SQL statement parameter.  

* IfxPy.execute:  
Executes an SQL statement that was prepared by * IfxPy.prepare().  

* IfxPy.fetch_tuple:  
Returns an tuple  

* IfxPy.fetch_assoc:  
Returns a dictionary  

* IfxPy.fetch_both:  
Returns a dictionary  

* IfxPy.fetch_row:  
Sets the result set pointer to the next row or requested row.  

* IfxPy.result:  
Returns a single column from a row in the result set.  

* IfxPy.active:  
Checks if the specified connection resource is active.  

* IfxPy.autocommit:  
Returns or sets the AUTOCOMMIT state for a database connection.  

* IfxPy.callproc:  
Returns a tuple containing OUT/INOUT variable value.  

* IfxPy.check_function_support:  
return true if fuction is supported otherwise return false.  

* IfxPy.close:  
Close a database connection.  

* IfxPy.conn_error:  
Returns a string containing the SQLSTATE returned by the last connection attempt.  

* IfxPy.conn_errormsg:  
Returns an error message and SQLCODE value representing the reason the last database connection attempt failed. 

* IfxPy.conn_warn:  
Returns a warning string containing the SQLSTATE returned by the last connection attempt.  

* IfxPy.client_info:  
Returns a read-only object with information about the IDS database client.  

* IfxPy.column_privileges:  
Returns a result set listing the columns and associated privileges for a table.  

* IfxPy.columns:  
Returns a result set listing the columns and associated metadata for a table.  

* IfxPy.commit:  
Commits a transaction.  

* IfxPy.cursor_type:  
Returns the cursor type used by a statement resource.  

* IfxPy.execute_many:  
Execute SQL with multiple rows.

* IfxPy.field_display_size:  
Returns the maximum number of bytes required to display a column.  

* IfxPy.field_name:  
Returns the name of the column in the result set.  

* IfxPy.field_nullable:  
Returns indicated column can contain nulls or not.  

* IfxPy.field_num:  
Returns the position of the named column in a result set.  

* IfxPy.field_precision:  
Returns the precision of the indicated column in a result set.  

* IfxPy.field_scale:  
Returns the scale of the indicated column in a result set.  

* IfxPy.field_type:  
Returns the data type of the indicated column in a result set.  

* IfxPy.field_width:  
Returns the width of the indicated column in a result set.  

* IfxPy.foreign_keys:  
Returns a result set listing the foreign keys for a table.  

* IfxPy.free_result:  
Frees resources associated with a result set.  

* IfxPy.free_stmt:  
Frees resources associated with the indicated statement resource.  

* IfxPy.get_option:  
Gets the specified option in the resource.  

* IfxPy.num_fields:  
Returns the number of fields contained in a result set.  

* IfxPy.num_rows:  
Returns the number of rows affected by an SQL statement.  

* IfxPy.get_num_result:  
Returns the number of rows in a current open non-dynamic scrollable cursor.  

* IfxPy.primary_keys:  
Returns a result set listing primary keys for a table.  

* IfxPy.procedure_columns:  
Returns a result set listing the parameters for one or more stored procedures.  

* IfxPy.procedures:  
Returns a result set listing the stored procedures registered in a database.  

* IfxPy.rollback:  Rolls back a transaction.  

* IfxPy.server_info:  
Returns an object with properties that describe the IDS database server.  

* IfxPy.get_db_info:  
Returns an object with properties that describe the IDS database server according to the option passed.  

* IfxPy.set_option:  
Sets the specified option in the resource.  

* IfxPy.special_columns:  
Returns a result set listing the unique row identifier columns for a table.  

* IfxPy.statistics:  
Returns a result set listing the index and statistics for a table.  

* IfxPy.stmt_error:  
Returns a string containing the SQLSTATE returned by an SQL statement.  

* IfxPy.stmt_warn:  
Returns a warning string containing the SQLSTATE returned by last SQL statement.  

* IfxPy.stmt_errormsg:  
Returns a string containing the last SQL statement error message.  

* IfxPy.table_privileges:  
Returns a result set listing the tables and associated privileges in a database. 

* IfxPy.tables:  
Returns a result set listing the tables and associated metadata in a database.  

* IfxPy.get_last_serial_value:  
Returns last serial value inserted for identity column.

