API description of IfxPy driver is given below. If you want to access the same for IfxPyi wrapper, please visit [Python Database API Specification v2.0](http://www.python.org/dev/peps/pep-0249/)

# API Description for the IfxPy driver #

Table of Contents
-----------------
* [IfxPy.active](#IfxPyactive)
* [IfxPy.autocommit](#IfxPyautocommit)
* [IfxPy.bind_param](#IfxPybind_param)
* [IfxPy.callproc](#IfxPycallproc)
* [IfxPy.client_info](#IfxPyclient_info)
* [IfxPy.close](#IfxPyclose)
* [IfxPy.column_privileges](#IfxPycolumn_privileges)
* [IfxPy.columns](#IfxPycolumns)
* [IfxPy.commit](#IfxPycommit)
* [IfxPy.conn_error](#IfxPyconn_error)
* [IfxPy.conn_errormsg](#IfxPyconn_errormsg)
* [IfxPy.connect](#IfxPyconnect)
* [IfxPy.cursor_type](#IfxPycursor_type)
* [IfxPy.dropdb](#IfxPydropdb)
* [IfxPy.exec_immediate](#IfxPyexec_immediate)
* [IfxPy.execute](#IfxPyexecute)
* [IfxPy.execute_many](#IfxPyexecute_many)
* [IfxPy.fetch_tuple](#IfxPyfetch_tuple)
* [IfxPy.fetch_assoc](#IfxPyfetch_assoc)
* [IfxPy.fetch_both](#IfxPyfetch_both)
* [IfxPy.fetch_row](#IfxPyfetch_row)
* [IfxPy.field_display_size](#IfxPyfield_display_size)
* [IfxPy.field_name](#IfxPyfield_name)
* [IfxPy.field_num](#IfxPyfield_num)
* [IfxPy.field_precision](#IfxPyfield_precision)
* [IfxPy.field_scale](#IfxPyfield_scale)
* [IfxPy.field_type](#IfxPyfield_type)
* [IfxPy.field_width](#IfxPyfield_width)
* [IfxPy.foreign_keys](#IfxPyforeign_keys)
* [IfxPy.free_result](#IfxPyfree_result)
* [IfxPy.free_stmt](#IfxPyfree_stmt)
* [IfxPy.get_option](#IfxPyget_option)
* [IfxPy.next_result](#IfxPynext_result)
* [IfxPy.num_fields](#IfxPynum_fields)
* [IfxPy.num_rows](#IfxPynum_rows)
* [IfxPy.prepare](#IfxPyprepare)
* [IfxPy.primary_keys](#IfxPyprimary_keys)
* [IfxPy.procedure_columns](#IfxPyprocedure_columns)
* [IfxPy.procedures](#IfxPyprocedures)
* [IfxPy.result](#IfxPyresult)
* [IfxPy.rollback](#IfxPyrollback)
* [IfxPy.server_info](#IfxPyserver_info)
* [IfxPy.set_option](#IfxPyset_option)
* [IfxPy.special_columns](#IfxPyspecial_columns)
* [IfxPy.statistics](#IfxPystatistics)
* [IfxPy.stmt_error](#IfxPystmt_error)
* [IfxPy.stmt_errormsg](#IfxPystmt_errormsg)
* [IfxPy.table_privileges](#IfxPytable_privileges)
* [IfxPy.tables](#IfxPytables)

### IfxPy.active ###
`bool IfxPy.active(IFXConnection connection)`

**Description**

Checks if the specified IFXConnection is active.

**Parameters**
* connection - A valid IFXConnection

**Return Values**
* `True` - the resource is active
* `False` - the resource is not active


### IfxPy.autocommit ###
`mixed IfxPy.autocommit ( IFXConnection connection [, bool value] )`

**Description**

Returns and sets the AUTOCOMMIT behavior of the specified IFXConnection.

**Parameters**
* connection - A valid IFXConnection
* value - One of the following constants:
    * `SQL_AUTOCOMMIT_OFF`
    * `SQL_AUTOCOMMIT_ON`

**Return Values**
* When `value` is not passed:
    * `0` - AUTOCOMMIT is off
    * `1` - AUTOCOMMIT is on
* When `value` is passed:
    * `True` - AUTOCOMMIT was set to `value` successfully
    * `False` - AUTOCOMMIT was not set to `value` successfully


### IfxPy.bind_param ###
`bool IfxPy.bind_param (IFXStatement stmt, int parameter-number, string variable [, int parameter-type [, int data-type [, int precision [, int scale [, int size]]]]] )`

**Description**

Binds a Python variable to an SQL statement parameter in an IFXStatement returned by IfxPy.prepare().
This function gives you more control over the parameter type, data type,
precision, and scale for the parameter than simply passing the variable as
part of the optional input tuple to IfxPy.execute().

**Parameters**
* stmt - A prepared statement returned from IfxPy.prepare()
* parameter-number - The 1-indexed position of the parameter in the prepared statement
* variable - A Python variable to bind to the parameter specified by parameter-number
* parameter-type - A constant specifying the parameter input/output type:
    * `SQL_PARAM_INPUT` - an input-only parameter
    * `SQL_PARAM_OUTPUT` - an output-only parameter
    * `SQL_PARAM_INPUT_OUTPUT` - the parameter is used for both input and output
    * `PARAM_FILE` - The data is stored in the file name specified in `variable` instead of in `variable` itself. This can be used to avoid storing lots of LOB data in memory.
* data-type - A constant specifying the SQL data type that the Python variable should be bound as:
    * `SQL_BINARY`
    * `CHAR`
    * `DOUBLE`
    * `LONG`
* precision - The precision of the variable
* scale - The scale of the variable

**Return Values**
* `True` - the bind succeeded
* `None` - the bind failed

### IfxPy.callproc ###
`( IFXStatement [, ...] ) IfxPy.callproc( IFXConnection connection, string procname [, parameters] )`

**Description**

Calls a stored procedure with the given name. The parameters tuple must contain one entry for each argument (IN/OUT/INOUT) that the procedure expects. Returns an IFXStatement containing result sets and modified copy of the input parameters. IN parameters are left untouched whereas INOUT/OUT parameters are possibly replaced by new values.

A call to a stored procedure may return zero or more result sets. You can retrieve a row as a tuple/dict from the IFXStatement using IfxPy.fetch_assoc(), IfxPy.fetch_both(), or IfxPy.fetch_tuple(). Alternatively, you can use IfxPy.fetch_row() to move the result set pointer to next row and fetch a column at a time with IfxPy.result().

Samples for the API usage can be referred from test_146_CallSPINAndOUTParams.py, test_148_CallSPDiffBindPattern_01.py or test_52949_TestSPIntVarcharXml.py.

**Parameters**
* connection - A valid IFXConnection
* procname - A valid strored procedure name
* parameters - A tuple containing as many parameters as required by the stored procedure.


**Return Values**
* On success, a tuple containing an IFXStatement object followed by the parameters passed to the procedure, if any. 
* On failure, the value `None`


### IfxPy.client_info ###
`object IfxPy.client_info ( IFXConnection connection )`

**Description**

Returns a read-only object with information about the database client.

**Parameters**
* connection - A valid IFXConnection returned from IfxPy.connect() 

**Return Values**
* On success, an object with the following fields:
    * APPL_CODEPAGE - The application code page
    * CONN_CODEPAGE - The code page for the current connection
    * DATA_SOURCE_NAME - The data source name (DSN) used to create the current connection to the database
    * DRIVER_NAME - The name of the library that implements the Call Level Interface (CLI) specification
    * DRIVER_ODBC_VER - The version of ODBC driver. This returns a string "MM.mm" where MM is the major version and mm is the minor version. 
    * DRIVER_VER - The version of the client, in the form of a string "MM.mm.uuuu" where MM is the major version, mm is the minor version, and uuuu is the update. For example, "08.02.0001" represents major version 8, minor version 2, update 1.
    * ODBC_SQL_CONFORMANCE - There are three levels of ODBC SQL grammar supported by the client:
        * MINIMAL - Supports the minimum ODBC SQL grammar
        * CORE - Supports the core ODBC SQL grammar
        * EXTENDED - Supports extended ODBC SQL grammar
    * ODBC_VER - The version of ODBC that the ODBC driver manager supports. This returns a string "MM.mm.rrrr" where MM is the major version, mm is the minor version, and rrrr is the release. The client always returns "03.01.0000"
* On failure, `False`


### IfxPy.close ###
`bool IfxPy.close ( IFXConnection connection )`

**Description**

Closes the connection.


**Parameters**
* connection - A valid IFXConnection

**Return Values**

Returns `True` on success or `False` on failure.


### IfxPy.column_privileges ###
`IFXStatement IfxPy.column_privileges ( IFXConnection connection [, string qualifier [, string schema [, string table-name [, string column-name]]]] )`

**Description**

Returns a result set listing the columns and associated privileges for a table.

**Parameters**
* connection - A valid IFXConnection
* schema - The schema which contains the tables. To match all schemas, pass `None` or an empty string.
* table-name - The name of the table or view. To match all tables in the database, pass `None` or an empty string.
* column-name - The name of the column. To match all columns in the table, pass `None` or an empty string.

**Return Values**

An IFXStatement with a result set containing rows with the following columns:
* TABLE_CAT - Name of the catalog. The value is `None` if the database does not have catalogs.
* TABLE_SCHEM - Name of the schema.
* TABLE_NAME - Name of the table or view.
* COLUMN_NAME - Name of the column.
* GRANTOR - Authorization ID of the user who granted the privilege.
* GRANTEE - Authorization ID of the user to whom the privilege was granted.
* PRIVILEGE - The privilege for the column.
* IS_GRANTABLE - Whether the GRANTEE is permitted to grant this privilege to other users.


### IfxPy.columns ###
`IFXStatement IfxPy.columns ( IFXConnection connection [, string qualifier [, string schema [, string table-name [, string column-name]]]] )`

**Description**

Returns a result set listing the columns and associated metadata for a table.

**Parameters**

* connection - A valid IFXConnection
* schema - The schema which contains the tables. To match all schemas, pass '%'.
* table-name - The name of the table or view. To match all tables in the database, pass `None` or an empty string.
* column-name - The name of the column. To match all columns in the table, pass `None` or an empty string.

**Return Values**

An IFXStatement with a result set containing rows containing the following columns:
* TABLE_CAT - Name of the catalog. The value is `None` if this table does not have catalogs.
* TABLE_SCHEM - Name of the schema.
* TABLE_NAME - Name of the table or view.
* COLUMN_NAME - Name of the column.
* DATA_TYPE - The SQL data type for the column represented as an integer value.
* TYPE_NAME - A string representing the data type for the column.
* COLUMN_SIZE - An integer value representing the size of the column.
* BUFFER_LENGTH - Maximum number of bytes necessary to store data from this column.
* DECIMAL_DIGITS - The scale of the column, or `None` where scale is not applicable.
* NUM_PREC_RADIX - An integer value of either 10 (representing an exact numeric data type), 2 (representing an approximate numeric data type), or `None` (representing a data type for which radix is not applicable).
* NULLABLE - An integer value representing whether the column is nullable or not.
* REMARKS - Description of the column.
* COLUMN_DEF - Default value for the column.
* SQL_DATA_TYPE - The SQL data type of the column.
* SQL_DATETIME_SUB - An integer value representing a datetime subtype code, or `None` for SQL data types to which this does not apply.
* CHAR_OCTET_LENGTH -   Maximum length in octets for a character data type column, which matches COLUMN_SIZE for single-byte character set data, or `None` for non-character data types.
* ORDINAL_POSITION - The 1-indexed position of the column in the table.
* IS_NULLABLE - A string value where 'YES' means that the column is nullable and 'NO' means that the column is not nullable.


### IfxPy.commit ###
`bool IfxPy.commit ( IFXConnection connection )`

**Description**

Commits an in-progress transaction on the specified IFXConnection and begins a new transaction.

Python applications normally default to AUTOCOMMIT mode, so IfxPy.commit() is not necessary unless AUTOCOMMIT has been turned off for the IFXConnection.

Note: If the specified IFXConnection is a persistent connection, all transactions in progress for all applications using that persistent
connection will be committed. For this reason, persistent connections are not recommended for use in applications that require transactions.

**Parameters**
* connection - A valid IFXConnection

**Return Values**

Returns `True` on success or `False` on failure.


### IfxPy.conn_error ###
`string IfxPy.conn_error ( [IFXConnection connection] )`

**Description**

When not passed any parameters, returns the SQLSTATE representing the reason the last database connection attempt failed.

When passed a valid IFXConnection returned by IfxPy.connect(), returns the SQLSTATE representing the reason the
last operation using a IFXConnection failed.

**Parameters**
* connection - A valid IFXConnection

**Return Values**

Returns a string containing the SQLSTATE value or an empty string if there was no error.


### IfxPy.conn_errormsg ###
`string IfxPy.conn_errormsg ( [IFXConnection connection] )`

**Description**

When not passed any parameters, returns a string containing the SQLCODE and error message representing the reason the last database connection attempt failed.

When passed a valid IFXConnection returned by IfxPy.connect(), returns  a string containing the SQLCODE and error message representing the reason the
last operation using a IFXConnection failed.

**Parameters**
* connection - A valid IFXConnection

**Return Values**

Returns a string containing the SQLCODE and error message or an empty string if there was no error.


### IfxPy.connect ###
`IFXConnection IfxPy.connect(string ConnectionString, string user, string password [, dict options [, constant replace_quoted_literal])`

**Description**

Creates a new connection to an Informix Database.

**Parameters**
* ConnectionString
Connection string in the following format:
"SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;SERVICE=9088;PROTOCOL=onsoctcp;UID=informix;PWD=xxxx;"
where the parameters represent the following values:
    * hostname - The hostname or IP address of the database server.
    * port - The TCP/IP port on which the database is listening for requests.
    * username - The username with which you are connecting to the database.
    * password - The password with which you are connecting to the database.
* user - The username with which you are connecting to the database.
* password - The password with which you are connecting to the database.


**Return Values**
* On success, an IFXConnection connection object
* On failure, `None`


### IfxPy.cursor_type ###
`int IfxPy.cursor_type ( IFXStatement stmt )`

**Description**

Returns the cursor type used by an IFXStatement. Use this to determine
if you are working with a forward-only cursor or scrollable cursor.

**Parameters**

* stmt - A valid IFXStatement.

**Return Values**

One of the following values: `SQL_CURSOR_FORWARD_ONLY` 


### IfxPy.dropdb ###
`bool IfxPy.dropdb ( IFXConnection connection, string dbName )`

**Description**

Drops the specified database

**Parameters**

* connection - A valid IFXConnection as returned from IfxPy.connect() by specifying the ATTACH keyword
* dbName - Name of the database that is to be dropped.

**Return Value**

Returns `True` if specified database dropped successfully else `None`.


### IfxPy.exec_immediate ###
`stmt_handle IfxPy.exec_immediate( IFXConnection connection, string statement [, dict options] )`

**Description**

Prepares and executes an SQL statement.

If you plan to repeatedly issue the same SQL statement with different
parameters, consider calling IfxPy.prepare() and IfxPy.execute() to
enable the database server to reuse its access plan and increase the
efficiency of your database access.

If you plan to interpolate Python variables into the SQL statement,
understand that this is one of the more common security exposures.
Consider calling IfxPy.prepare() to prepare an SQL statement with
parameter markers for input values. Then you can call IfxPy.execute()
to pass in the input values and avoid SQL injection attacks.

**Parameters**

* connection - A valid IFXConnection
* statement - An SQL statement. The statement cannot contain any parameter markers.
* options - A dict containing statement options.
    * `SQL_ATTR_CURSOR_TYPE` - Set the cursor type to one of the following (not supported on all databases):
        * `SQL_CURSOR_FORWARD_ONLY`
        * `SQL_CURSOR_KEYSET_DRIVEN`
        * `SQL_CURSOR_DYNAMIC`
        * `SQL_CURSOR_STATIC`

**Return Values**

Returns a stmt_handle resource if the SQL statement was issued
successfully, or `False` if the database failed to execute the SQL statement.


### IfxPy.execute ###
`bool IfxPy.execute ( IFXStatement stmt [, tuple parameters] )`

**Description**

IfxPy.execute() executes an SQL statement that was prepared by IfxPy.prepare(). If the SQL statement returns a result set, for example, a SELECT statement that returns one or more result sets, you can retrieve a row as an tuple/dict from the stmt resource using IfxPy.fetch_assoc(), IfxPy.fetch_both(), or IfxPy.fetch_tuple(). Alternatively, you can use IfxPy.fetch_row() to move the result set pointer to the next row and fetch a column at a time from that row with IfxPy.result(). Refer to IfxPy.prepare() for a brief discussion of the advantages of using IfxPy.prepare() and IfxPy.execute() rather than IfxPy.exec_immediate(). To execute stored procedure refer IfxPy.callproc()

**Parameters**
* stmt - A prepared statement returned from IfxPy.prepare().
* parameters - An tuple of input parameters matching any parameter markers contained in the prepared statement.

**Return Values**

Returns `True` on success or `False` on failure.

### IfxPy.execute_many ###
`mixed IfxPy.execute_many( IFXStatement stmt, tuple seq_of_parameters )`

**Description**

Executes an SQL statement prepared by IfxPy.prepare() against all parameter sequences or mappings found in the sequence seq_of_parameters.

**Parameters**
* stmt - A prepared statement returned from IfxPy.prepare().
* seq_of_parameters - A tuple of tuples, with each tuple containing input parameters matching parameter markers contained in the prepared statement.

**Return Values**
* On success, returns the number of inserted/updated/deleted rows
* On failure, returns `None`. Use IfxPy.num_rows() to find out the inserted/updated/deleted row count.


### IfxPy.fetch_tuple ###
`tuple IfxPy.fetch_tuple ( IFXStatement stmt [, int row_number] )`

**Description**

Returns a tuple, indexed by column position, representing a row in a result set.

**Parameters**
* stmt - A valid stmt resource containing a result set.
* row_number - Requests a specific 1-indexed row from the result set. Passing this parameter results in a warning if the result set uses a forward-only cursor.

**Return Values**
* Returns a tuple containing all the column values in the result set for the selected row or the next row if row_number was not specified
* Returns `False` if there are no rows left in the result set, or if the row requested by row_number does not exist in the result set.


### IfxPy.fetch_assoc ###
`dict IfxPy.fetch_assoc ( IFXStatement stmt [, int row_number] )`

**Description**

Returns a dict, indexed by column name, representing a row in a result set.

**Parameters**
* stmt - A valid stmt resource containing a result set.
* row_number - Requests a specific 1-indexed row from the result set. Passing this parameter results in a warning if the result set uses a forward-only cursor.

**Return Values**
* Returns a dict containing all the column values indexed by column name for the selected row or the next row if row number was not specified.
* Returns `False` if there are no rows left in the result set, or if the row requested by row_number does not exist in the result set.


### IfxPy.fetch_both ###
`dict IfxPy.fetch_both ( IFXStatement stmt [, int row_number] )`

**Description**

Returns a dict, indexed by column name and position, representing a row in a result set.

**Parameters**
* stmt - A valid stmt resource containing a result set.
* row_number - Requests a specific 1-indexed row from the result set. Passing this parameter results in a warning if the result set uses a forward-only cursor.

**Return Values**
* Returns a dict containing all the column values indexed by column name and by 0-indexed column number for the selected row or the next row if row number was not specified.
* Returns `False` if there are no rows left in the result set, or if the row requested by row_number does not exist in the result set.


### IfxPy.fetch_row ###
`bool IfxPy.fetch_row ( IFXStatement stmt [, int row_number] )`

**Description**

Sets the result set pointer to the next row or requested row.

Use IfxPy.fetch_row() to iterate through a result set, or to point to a
specific row in a result set if you requested a scrollable cursor.

To retrieve individual fields from the result set, call the IfxPy.result()
function. Rather than calling IfxPy.fetch_row() and IfxPy.result(), most
applications will call one of IfxPy.fetch_assoc(), IfxPy.fetch_both(), or
IfxPy.fetch_tuple() to advance the result set pointer and return a complete
row.

**Parameters**
* stmt - A valid stmt resource.
* row_number - Requests a specific 1-indexed row from the result set. Passing this parameter results in a warning if the result set uses a forward-only cursor.

**Return Values**

Returns `True` if the requested row exists in the result set. Returns `False` if
the requested row does not exist in the result set.


### IfxPy.field_display_size ###
`int IfxPy.field_display_size ( IFXStatement stmt, mixed column )`

**Description**

Returns the maximum number of bytes required to display a column in a result set.

**Parameters**
* stmt - Specifies an IFXStatement containing a result set.
* column - Specifies the column in the result set. This can either be an integer representing the 0-indexed position of the column or a string containing the name of the column.

**Return Values**

Returns an integer value with the maximum number of bytes required to display
the specified column or `False` if the column does not exist.


### IfxPy.field_name ###
`string IfxPy.field_name ( IFXStatement stmt, mixed column )`

**Description**

Returns the name of the specified column in the result set.

**Parameters**
* stmt - Specifies an IFXStatement containing a result set.
* column - Specifies the column in the result set. This can either be an integer representing the 0-indexed position of the column or a string containing the name of the column.

**Return Values**

Returns a string containing the name of the specified column or `False` if the column does not exist.


### IfxPy.field_num ###
`int IfxPy.field_num ( IFXStatement stmt, mixed column )`

**Description**

Returns the position of the named column in a result set.

**Parameters**
* stmt - Specifies an IFXStatement containing a result set.
* column - Specifies the column in the result set. This can either be an integer representing the 0-indexed position of the column or a string containing the name of the column.

**Return Values**

Returns an integer containing the 0-indexed position of the specified column or `False` if the column does not exist.


### IfxPy.field_precision ###
`int IfxPy.field_precision ( IFXStatement stmt, mixed column )`

**Description**

Returns the precision of the indicated column in a result set.

**Parameters**
* stmt - Specifies an IFXStatement containing a result set.
* column - Specifies the column in the result set. This can either be an integer representing the 0-indexed position of the column or a string containing the name of the column.

**Return Values**

Returns an integer containing the precision of the specified column or `False` if the column does not exist.


### IfxPy.field_scale ###
`int IfxPy.field_scale ( IFXStatement stmt, mixed column )`

**Description**

Returns the scale of the indicated column in a result set.

**Parameters**
* stmt - Specifies an IFXStatement containing a result set.
* column - Specifies the column in the result set. This can either be an integer representing the 0-indexed position of the column or a string containing the name of the column.

**Return Values**

Returns an integer containing the scale of the specified column or `False` if the column does not exist.


### IfxPy.field_type ###
`string IfxPy.field_type ( IFXStatement stmt, mixed column )`

**Description**

Returns the data type of the indicated column in a result set.

**Parameters**
* stmt - Specifies an IFXStatement containing a result set.
* column - Specifies the column in the result set. This can either be an integer representing the 0-indexed position of the column or a string containing the name of the column.

**Return Values**

Returns a string containing the defined data type of the specified column or `False` if the column does not exist.


### IfxPy.field_width ###
`int IfxPy.field_width ( IFXStatement stmt, mixed column )`

**Description**

Returns the width of the current value of the indicated column in a result
set. This is the maximum width of the column for a fixed-length data type, or
the actual width of the column for a variable-length data type.

**Parameters**
* stmt - Specifies an IFXStatement containing a result set.
* column - Specifies the column in the result set. This can either be an integer representing the 0-indexed position of the column or a string containing the name of the column.

**Return Values**

Returns an integer containing the width of the specified character or binary column; or `False` if the column does not exist.


### IfxPy.foreign_keys ###
`IFXStatement IfxPy.foreign_keys ( IFXConnection connection, string qualifier, string schema, string table-name )`

**Description**

Returns a result set listing the foreign keys for a table.

**Parameters**

* connection - A valid IFXConnection
* schema - The schema which contains the tables. If schema is `None`, the current schema for the connection is used instead.
* table-name - The name of the table.

**Return Values**

Returns an IFXStatement with a result set containing the following columns:
* PKTABLE_CAT - Name of the catalog for the table containing the primary key. The value is `None` if this table does not have catalogs.
* PKTABLE_SCHEM - Name of the schema for the table containing the primary key.
* PKTABLE_NAME - Name of the table containing the primary key.
* PKCOLUMN_NAME - Name of the column containing the primary key.
* FKTABLE_CAT - Name of the catalog for the table containing the foreign key. The value is `None` if this table does not have catalogs.
* FKTABLE_SCHEM - Name of the schema for the table containing the foreign key.
* FKTABLE_NAME - Name of the table containing the foreign key.
* FKCOLUMN_NAME - Name of the column containing the foreign key.
* KEY_SEQ - 1-indexed position of the column in the key.
* UPDATE_RULE - Integer value representing the action applied to the foreign key when the SQL operation is UPDATE.
* DELETE_RULE - Integer value representing the action applied to the foreign key when the SQL operation is DELETE.
* FK_NAME - The name of the foreign key.
* PK_NAME - The name of the primary key.
* DEFERRABILITY - An integer value representing whether the foreign key deferrability is SQL_INITIALLY_DEFERRED, SQL_INITIALLY_IMMEDIATE, or SQL_NOT_DEFERRABLE.


### IfxPy.free_result ###
`bool IfxPy.free_result ( IFXStatement stmt )`

**Description**

Frees the system and IFXConnections that are associated with a result
set. These resources are freed implicitly when a script finishes, but you
can call IfxPy.free_result() to explicitly free the result set resources
before the end of the script.

**Parameters**
* stmt - A valid IFXStatement.

**Return Values**

Returns `True` on success or `False` on failure.


### IfxPy.free_stmt ###
`bool IfxPy.free_stmt ( IFXStatement stmt )` **(DEPRECATED)**

**Description**

Frees the system and IFXConnections that are associated with a statement
resource. These resources are freed implicitly when a script finishes, but
you can call IfxPy.free_stmt() to explicitly free the statement resources
before the end of the script.

This API is deprecated. Applications should use IfxPy.free_result instead.

**Parameters**
* stmt - A valid IFXStatement.

**Return Values**

Returns `True` on success or `False` on failure.



### IfxPy.get_option ###
`mixed IfxPy.get_option ( mixed resc, int options, int type )`

**Description**

Returns a value that is the current setting of a connection or statement
attribute.

**Parameters**
* resc - A valid IFXConnection or IFXStatement containing a result set.
* options - The options to be retrieved
* type - The type of resc
    * `0` - IFXStatement
    * `1` - IFXConnection

**Return Values**

Returns the current setting of the resource attribute provided.


### IfxPy.next_result ###
`IFXStatement IfxPy.next_result ( IFXStatement stmt )`

**Description**

Requests the next result set from a stored procedure.
A stored procedure can return zero or more result sets. While you handle the
first result set in exactly the same way you would handle the results
returned by a simple SELECT statement, to fetch the second and subsequent
result sets from a stored procedure you must call the IfxPy.next_result()
function and return the result to a uniquely named Python variable.

**Parameters**
* stmt - A prepared statement returned from IfxPy.exec_immediate() or IfxPy.execute().

**Return Values**

Returns a new IFXStatement containing the next result set if the stored
procedure returned another result set. Returns `False` if the stored procedure
did not return another result set.


### IfxPy.num_fields ###
`int IfxPy.num_fields ( IFXStatement stmt )`

**Description**

Returns the number of fields contained in a result set. This is most useful
for handling the result sets returned by dynamically generated queries, or
for result sets returned by stored procedures, where your application cannot
otherwise know how to retrieve and use the results.

**Parameters**
* stmt - A valid IFXStatement containing a result set.

**Return Values**

Returns an integer value representing the number of fields in the result set
associated with the specified IFXStatement. Returns `False` if stmt is not
a valid IFXStatement object.


### IfxPy.num_rows ###
`int IfxPy.num_rows ( IFXStatement stmt )`

**Description**

Returns the number of rows deleted, inserted, or updated by an SQL statement.

To determine the number of rows that will be returned by a SELECT statement,
issue `SELECT COUNT(*)` with the same predicates as your intended SELECT
statement and retrieve the value. If your application logic checks the number
of rows returned by a SELECT statement and branches if the number of rows is
0, consider modifying your application to attempt to return the first row
with one of IfxPy.fetch_assoc(), IfxPy.fetch_both(), IfxPy.fetch_tuple(),
or IfxPy.fetch_row(), and branch if the fetch function returns `False`.
Note: If you issue a SELECT statement using a scrollable cursor,
IfxPy.num_rows() returns the number of rows returned by the SELECT
statement. However, the overhead associated with scrollable cursors
significantly degrades the performance of your application, so if this is the
only reason you are considering using scrollable cursors, you should use a
forward-only cursor and either call `SELECT COUNT(*)` or rely on the boolean
return value of the fetch functions to achieve the equivalent functionality
with much better performance.

**Parameters**
* stmt - A valid stmt resource containing a result set.

**Return Values**

Returns the number of rows affected by the last SQL statement issued by the
specified statement handle.


### IfxPy.prepare ###
`IFXStatement IfxPy.prepare ( IFXConnection connection, string statement [, dict options] )`

**Description**

Creates a prepared SQL statement which can include 0 or more parameter markers
(? characters) representing parameters for input,output, or input/output.
You can pass parameters to the prepared statement using IfxPy.bind_param(),
or for input values only, as a tuple passed to IfxPy.execute().

There are two main advantages to using prepared statements in your application:
* Performance: when you prepare a statement, the database server
    creates an optimized access plan for retrieving data with that
    statement. Subsequently issuing the prepared statement with
    IfxPy.execute() enables the statements to reuse that access plan
    and avoids the overhead of dynamically creating a new access plan
    for every statement you issue.
* Security: when you prepare a statement, you can include parameter
    markers for input values. When you execute a prepared statement
    with input values for placeholders, the database server checks each
    input value to ensure that the type matches the column definition or
    parameter definition.

**Parameters**
* connection - A valid IFXConnection
* statement - An SQL statement, optionally containing one or more parameter markers.
* options - A dict containing statement options.
    * `SQL_ATTR_CURSOR_TYPE` - Set the cursor type to one of the following (not supported on all databases):
        * `SQL_CURSOR_FORWARD_ONLY`
        * `SQL_CURSOR_KEYSET_DRIVEN`
        * `SQL_CURSOR_DYNAMIC`
        * `SQL_CURSOR_STATIC`

**Return Values**

Returns a IFXStatement object if the SQL statement was successfully
parsed and prepared by the database server or `False` if the database
server returned an error.


### IfxPy.primary_keys ###
`IFXStatement IfxPy.primary_keys ( IFXConnection connection, string qualifier, string schema, string table-name )`

**Description**

Returns a result set listing the primary keys for a table.

**Parameters**

* connection - A valid IFXConnection
* schema - The schema which contains the tables. If schema is `None`, the current schema for the connection is used instead.
* table-name - The name of the table.

**Return Values**

Returns an IFXStatement with a result set containing the following columns:
* TABLE_CAT - Name of the catalog for the table containing the primary key. The value is `None` if this table does not have catalogs.
* TABLE_SCHEM - Name of the schema for the table containing the primary key.
* TABLE_NAME - Name of the table containing the primary key.
* COLUMN_NAME - Name of the column containing the primary key.
* KEY_SEQ - 1-indexed position of the column in the key.
* PK_NAME - The name of the primary key.


### IfxPy.procedure_columns ###
`IFXStatement IfxPy.procedure_columns ( IFXConnection connection, string qualifier, string schema, string procedure, string parameter )`

**Description**

Returns a result set listing the parameters for one or more stored procedures

**Parameters**

* connection - A valid IFXConnection
* schema - The schema which contains the procedures. This parameter accepts a search pattern containing _and % as wildcards.
* procedure - The name of the procedure. This parameter accepts a search pattern containing_ and % as wildcards.
* parameter - The name of the parameter. This parameter accepts a search pattern containing _and % as wildcards. If this parameter is `None`, all parameters for the specified stored procedures are returned.

**Return Values**

Returns an IFXStatement with a result set containing the following columns:
* PROCEDURE_CAT - The catalog that contains the procedure. The value is `None` if this table does not have catalogs.
* PROCEDURE_SCHEM - Name of the schema that contains the stored procedure.
* PROCEDURE_NAME - Name of the procedure.
* COLUMN_NAME - Name of the parameter.
* COLUMN_TYPE - An integer value representing the type of the parameter:
    * 1 (`SQL_PARAM_INPUT`) - Input (IN) parameter.
    * 2 (`SQL_PARAM_INPUT`_OUTPUT) - Input/output (INOUT) parameter.
    * 3 (`SQL_PARAM_OUTPUT`) - Output (OUT) parameter.
* DATA_TYPE - The SQL data type for the parameter represented as an integer value.
* TYPE_NAME - A string representing the data type for the parameter.
* COLUMN_SIZE - An integer value representing the size of the parameter.
* BUFFER_LENGTH - Maximum number of bytes necessary to store data for this parameter.
* DECIMAL_DIGITS - The scale of the parameter, or `None` where scale is not applicable.
* NUM_PREC_RADIX - An integer value of either 10 (representing an exact numeric data type), 2 (representing anapproximate numeric data type), or `None` (representing a data type for which radix is not applicable).
* NULLABLE - An integer value representing whether the parameter is nullable or not.
* REMARKS - Description of the parameter.
* COLUMN_DEF - Default value for the parameter.
* SQL_DATA_TYPE - An integer value representing the size of the parameter.
* SQL_DATETIME_SUB - Returns an integer value representing a datetime subtype code, or `None` for SQL data types to which this does not apply.
* CHAR_OCTET_LENGTH - Maximum length in octets for a character data type parameter, which matches COLUMN_SIZE for single-byte character set data, or `None` for non-character data types.
* ORDINAL_POSITION - The 1-indexed position of the parameter in the CALL statement.
* IS_NULLABLE - A string value where 'YES' means that the parameter accepts or returns `None` values and 'NO' means that the parameter does not accept or return `None` values.


### IfxPy.procedures ###

**Description**

resource IfxPy.procedures ( IFXConnection connection, string qualifier,
string schema, string procedure )
Returns a result set listing the stored procedures registered in a database.

**Parameters**

* connection - A valid IFXConnection
* schema - The schema which contains the procedures. This parameter accepts a search pattern containing _and % as wildcards.
* procedure - The name of the procedure. This parameter accepts a search pattern containing_ and % as wildcards.

**Return Values**

Returns an IFXStatement with a result set containing the following columns:
* PROCEDURE_CAT - The catalog that contains the procedure. The value is `None` if this table does not have catalogs.
* PROCEDURE_SCHEM - Name of the schema that contains the stored procedure.
* PROCEDURE_NAME - Name of the procedure.
* NUM_INPUT_PARAMS - Number of input (IN) parameters for the stored procedure.
* NUM_OUTPUT_PARAMS - Number of output (OUT) parameters for the stored procedure.
* NUM_RESULT_SETS - Number of result sets returned by the stored procedure.
* REMARKS - Any comments about the stored procedure.
* PROCEDURE_TYPE - Always returns 1, indicating that the stored procedure does not return a return value.


### IfxPy.result ###
`mixed IfxPy.result ( IFXStatement stmt, mixed column )`

**Description**

Returns a single column from a row in the result set
Use IfxPy.result() to return the value of a specified column in the current  **row of a result set. You must call IfxPy.fetch_row() before calling
IfxPy.result() to set the location of the result set pointer.

**Parameters**

* stmt - A valid stmt resource.
* column - Either an integer mapping to the 0-indexed field in the result set, or a string matching the name of the column.

**Return Values**

Returns the value of the requested field if the field exists in the result
set. Returns `None` if the field does not exist, and issues a warning.


### IfxPy.rollback ###

**Description**

bool IfxPy.rollback ( IFXConnection connection )
Rolls back an in-progress transaction on the specified IFXConnection
and begins a new transaction. Python applications normally default to
AUTOCOMMIT mode, so IfxPy.rollback() normally has no effect unless
AUTOCOMMIT has been turned off for the IFXConnection.
Note: If the specified IFXConnection is a persistent connection, all
transactions in progress for all applications using that persistent
connection will be rolled back. For this reason, persistent connections are
not recommended for use in applications that require transactions.

**Parameters**

* connection - A valid IFXConnection

**Return Values**

Returns `True` on success or `False` on failure.


### IfxPy.server_info ###
`IFXServerInfo IfxPy.server_info ( IFXConnection connection )`

**Description**

Returns a read-only object with information about the Informix server.

**Parameters**
* connection - A valid IFXConnection

**Return Values**
* On success, an object with the following fields:
    * DBMS_NAME - The name of the database server to which you are connected. 
    * DBMS_VER - The version of the database server, in the form of a string "MM.mm.uuuu" where MM is the major version, mm is the minor version, and uuuu is the update. For example, "08.02.0001" represents major version 8, minor version 2, update 1. (string)
    * DB_CODEPAGE - The code page of the database to which you are connected. (int)
    * DB_NAME - The name of the database to which you are connected. (string)
    * DFT_ISOLATION - The default transaction isolation level supported by the server: (string)
        * UR - Uncommitted read: changes are immediately visible by all concurrent transactions.
        * CS - Cursor stability: a row read by one transaction can be altered and committed by a second concurrent transaction.
        * RS - Read stability: a transaction can add or remove rows matching a search condition or a pending transaction.
        * RR - Repeatable read: data affected by pending transaction is not available to other transactions.
        * NC - No commit: any changes are visible at the end of a successful operation. Explicit commits and rollbacks are not allowed.
    * IDENTIFIER_QUOTE_CHAR - The character used to delimit an identifier. (string)
    * INST_NAME - The instance on the database server that contains the database. (string)
    * ISOLATION_OPTION - A tuple of the isolation options supported by the database server. The isolation options are described in the DFT_ISOLATION property. (tuple)
    * KEYWORDS - A tuple of the keywords reserved by the database server. (tuple)
    * LIKE_ESCAPE_CLAUSE - `True` if the database server supports the use of % and _wildcard characters. `False` if the database server does not support these wildcard characters. (bool)
    * MAX_COL_NAME_LEN - Maximum length of a column name supported by the database server, expressed in bytes. (int)
    * MAX_IDENTIFIER_LEN - Maximum length of an SQL identifier supported by the database server, expressed in characters. (int)
    * MAX_INDEX_SIZE - Maximum size of columns combined in an index supported by the database server, expressed in bytes. (int)
    * MAX_PROC_NAME_LEN - Maximum length of a procedure name supported by the database server, expressed in bytes. (int)
    * MAX_ROW_SIZE - Maximum length of a row in a base table supported by the database server, expressed in bytes. (int)
    * MAX_SCHEMA_NAME_LEN - Maximum length of a schema name supported by the database server, expressed in bytes. (int)
    * MAX_STATEMENT_LEN - Maximum length of an SQL statement supported by the database server, expressed in bytes. (int)
    * MAX_TABLE_NAME_LEN - Maximum length of a table name supported by the database server, expressed in bytes. (bool)
    * NON_NULLABLE_COLUMNS - `True` if the database server supports columns that can be defined as NOT NULL, `False` if the database server does not support columns defined as NOT NULL. (bool)
    * PROCEDURES - `True` if the database server supports the use of the CALL statement to call stored procedures, `False` if the database server does not support the CALL statement. (bool)
    * SPECIAL_CHARS - A string containing all of the characters other than A-Z, 0-9, and underscore that can be used in an identifier name. (string)
    * SQL_CONFORMANCE - The level of conformance to the ANSI/ISO SQL-92 specification offered by the database server: (string)
        * ENTRY - Entry-level SQL-92 compliance.
        * FIPS127 - FIPS-127-2 transitional compliance.
        * FULL - Full level SQL-92 compliance.
        * INTERMEDIATE - Intermediate level SQL-92 compliance.
* On failure, `False`


### IfxPy.set_option ###
`bool IfxPy.set_option ( mixed resc, dict options, int type )`

**Description**

Sets options for a IFXConnection or IFXStatement. You cannot set options for result set resources.

**Parameters**
* resc - A valid IFXConnection or IFXStatement.
* options - The options to be set
* type - A field that specifies the type of resc
    * 0 - IFXStatement
    * 1 - IFXConnection

**Return Values**

Returns `True` on success or `False` on failure


### IfxPy.special_columns ###
`IFXStatement IfxPy.special_columns ( IFXConnection connection, string qualifier, string schema, string table_name, int scope )`

**Description**

Returns a result set listing the unique row identifier columns for a table.

**Parameters**
* connection - A valid IFXConnection
* schema - The schema which contains the tables.
* table_name - The name of the table.
* scope - Integer value representing the minimum duration for which the unique row identifier is valid. This can be one of the following values:
    * 0 - Row identifier is valid only while the cursor is positioned on the row. (SQL_SCOPE_CURROW)
    * 1 - Row identifier is valid for the duration of the transaction. (SQL_SCOPE_TRANSACTION)
    * 2 - Row identifier is valid for the duration of the connection. (SQL_SCOPE_SESSION)

**Return Values**

Returns an IFXStatement with a result set containing the following columns:
* SCOPE - Integer value representing the minimum duration for which the unique row identifier is valid.
    * 0 (SQL_SCOPE_CURROW) - Row identifier is valid only while the cursor is positioned on the row.
    * 1 (SQL_SCOPE_TRANSACTION) - Row identifier is valid for the duration of the transaction.
    * 2 (SQL_SCOPE_SESSION) - Row identifier is valid for the duration of the connection.
* COLUMN_NAME - Name of the unique column.
* DATA_TYPE - SQL data type for the column.
* TYPE_NAME - Character string representation of the SQL data type for thecolumn.
* COLUMN_SIZE - An integer value representing the size of the column.
* BUFFER_LENGTH - Maximum number of bytes necessary to store data from thiscolumn.
* DECIMAL_DIGITS - The scale of the column, or `None` where scale is notapplicable.
* NUM_PREC_RADIX - An integer value of either 10 (representing an exact numeric data type), 2 (representing an approximate numeric data type), or `None` (representing a data type for which radix is not applicable).
* PSEUDO_COLUMN - Always returns 1.


### IfxPy.statistics ###
`IFXStatement IfxPy.statistics ( IFXConnection connection, string qualifier, string schema, string table-name, bool unique )`

**Description**

Returns a result set listing the index and statistics for a table.

**Parameters**
* connection - A valid IFXConnection
* schema - The schema that contains the table. If this parameter is `None`, the statistics and indexes are returned for the schema of the current user.
* table_name The name of the table.
* unique A boolean value representing the type of index information to return.
    * `False` -  Return only the information for unique indexes on the table.
    * `True` - Return the information for all indexes on the table.

**Return Values**

Returns an IFXStatement with a result set containing the following columns:
* TABLE_CAT - The catalog that contains the table. The value is `None` if this table does not have catalogs.
* TABLE_SCHEM - Name of the schema that contains the table.
* TABLE_NAME - Name of the table.
* NON_UNIQUE - An integer value representing whether the index prohibits unique values, or whether the row represents statistics on the table itself:
    * 0 (SQL_FALSE) - The index allows duplicate values.
    * 1 (SQL_TRUE) - The index values must be unique.
    * None - This row is statistics information for the table itself.
* INDEX_QUALIFIER - A string value representing the qualifier that would have to be prepended to INDEX_NAME to fully qualify the index.
* INDEX_NAME - A string representing the name of the index.
* TYPE - An integer value representing the type of information contained in this row of the result set:
    * 0 (SQL_TABLE_STAT) - The row contains statistics about the table itself.
    * 1 (SQL_INDEX_CLUSTERED) - The row contains information about a clustered index.
    * 2 (SQL_INDEX_HASH) - The row contains information about a hashed index.
    * 3 (SQL_INDEX_OTHER) - The row contains information about a type of index that is neither clustered nor hashed.
* ORDINAL_POSITION - The 1-indexed position of the column in the index. `None` if the row contains statistics information about the table itself.
* COLUMN_NAME - The name of the column in the index. `None` if the row contains statistics information about the table itself.
* ASC_OR_DESC - A if the column is sorted in ascending order, D if the column is sorted in descending order, `None` if the row contains statistics information about the table itself.
* CARDINALITY - If the row contains information about an index, this column contains an integer value representing the number of unique values in the index. If the row contains information about the table itself, this column contains an integer value representing the number of rows in the table.
* PAGES - If the row contains information about an index, this column contains an integer value representing the number of pages used to store the index. If the row contains information about the table itself, this column contains an integer value representing the number of pages used to store the table.
* FILTER_CONDITION - Always returns `None`.


### IfxPy.stmt_error ###
`string IfxPy.stmt_error ( [IFXStatement stmt] )`

**Description**

When not passed any parameters, returns the SQLSTATE representing the reason
the last attempt to return an IFXStatement via IfxPy.prepare(),
IfxPy.exec_immediate(), or IfxPy.callproc() failed.

When passed a valid IFXStatement, returns the SQLSTATE representing the
reason the last operation using the resource failed.

**Parameters**
* stmt - A valid IFXStatement.

**Return Values**

Returns a string containing the SQLSTATE value or an empty string if there was no error.


### IfxPy.stmt_errormsg ###
`string IfxPy.stmt_errormsg ( [IFXStatement stmt] )`

**Description**


When not passed any parameters, returns a string containing
the SQLCODE and error message representing the reason
the last attempt to return an IFXStatement via IfxPy.prepare(),
IfxPy.exec_immediate(), or IfxPy.callproc() failed.

When passed a valid IFXStatement, returns a string containing
the SQLCODE and error message representing the reason the last
operation using the resource failed.

**Parameters**
* stmt - A valid IFXStatement.

**Return Values**

Returns a string containing the SQLCODE and error message or an empty string if there was no error.


### IfxPy.table_privileges ###
`IFXStatement IfxPy.table_privileges ( IFXConnection connection [, string qualifier [, string schema [, string table_name]]] )`

**Description**

Returns a result set listing the tables and associated privileges in a database.

**Parameters**
* connection - A valid IFXConnection
* schema - The schema which contains the tables. This parameter accepts a search pattern containing _and % as wildcards.
* table_name - The name of the table. This parameter accepts a search pattern containing_ and % as wildcards.

**Return Values**

Returns an IFXStatement with a result set containing following columns:
* TABLE_CAT - The catalog that contains the table. The value is `None` if this table does not have catalogs.
* TABLE_SCHEM - Name of the schema that contains the table.
* TABLE_NAME - Name of the table.
* GRANTOR - Authorization ID of the user who granted the privilege.
* GRANTEE - Authorization ID of the user to whom the privilege was granted.
* PRIVILEGE - The privilege that has been granted. This can be one of ALTER, CONTROL, DELETE, INDEX, INSERT, REFERENCES, SELECT, or UPDATE.
* IS_GRANTABLE - A string value of "YES" or "NO" indicating whether the grantee can grant the privilege to other users.


### IfxPy.tables ###
`IFXStatement IfxPy.tables ( IFXConnection connection [, string qualifier [, string schema [, string table-name [, string table-type]]]] )`

**Description**

Returns a result set listing the tables and associated metadata in a database

**Parameters**

* connection - A valid IFXConnection
* schema - The schema which contains the tables. This parameter accepts a search pattern containing _and % as wildcards.
* table-name - The name of the table. This parameter accepts a search pattern containing_ and % as wildcards.
* table-type - A list of comma-delimited table type identifiers. To match all table types, pass `None` or an empty string.
    * ALIAS
    * HIERARCHY TABLE
    * INOPERATIVE VIEW
    * NICKNAME
    * MATERIALIZED QUERY TABLE
    * SYSTEM TABLE
    * TABLE
    * TYPED TABLE
    * TYPED VIEW
    * VIEW

**Return Values**

Returns an IFXStatement with a result set containing the following columns:
* TABLE_CAT - The catalog that contains the table. The value is `None` if this table does not have catalogs.
* TABLE_SCHEMA - Name of the schema that contains the table.
* TABLE_NAME - Name of the table.
* TABLE_TYPE - Table type identifier for the table.
* REMARKS - Description of the table.
