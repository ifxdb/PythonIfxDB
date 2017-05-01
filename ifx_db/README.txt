Sample Readme

CSDK_HOM=c:\informix
MY_PY_DIR=C:\Dev\Python27

INCLUDE
$(MY_PY_DIR)\include;$(CSDK_HOM)\incl\cli


LIB
$(MY_PY_DIR)\libs;$(CSDK_HOM)\lib

iclit09b.lib 

drop table t1;
create table t1 ( c1 int, c2 char(20), c3 int, c4 int ) ;
insert into t1 values( 1, 'val-1', 101, 201 );
insert into t1 values( 2, 'val-2', 102, 202 );
insert into t1 values( 3, 'val-3', 103, 203 );
insert into t1 values( 4, 'val-4', 104, 204 );
insert into t1 values( 5, 'val-5', 105, 205 );

SELECT * FROM t1;

c1 c2                            c3          c4
 1 val-1                        101         201
 2 val-2                        102         202
 3 val-3                        103         203
 4 val-4                        104         204
 5 val-5                        105         205

