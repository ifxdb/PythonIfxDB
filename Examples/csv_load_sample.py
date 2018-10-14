
import csv
import pandas as pd
import IfxPy


# Lists are enclosed in brackets:
# l = [1, 2, "a"]

# Tuples are enclosed in parentheses:
# Tuples are faster and consume less memory
# t = (1, 2, "a")

# Dictionaries are built with curly brackets:
# d = {"a":1, "b":2}
# Sets are made using the set() builtin function

# Creating Pandas DataFrames from Lists and Dictionaries
# http://pbpython.com/pandas-list-dict.html
# https://www.datacamp.com/community/tutorials/pandas-read-csv


def LoadCsvSample( csv_file_name, table_name, ConStr ):
    try:
        # netstat -a | findstr  9088
        conn = IfxPy.connect( ConStr, "", "")
    except Exception as e:
        print ('ERROR: Connect failed')
        print ( e )
        quit()


    try:
        sql = "drop table {};".format(table_name)
        print ( sql )
        stmt = IfxPy.exec_immediate(conn, sql)
    except:
        print ('FYI: drop table failed')


    # head -n 5 sample.csv
    # "Store","DayOfWeek","Date","Sales","Customers","Open","Promo","StateHoliday","SchoolHoliday"
    # 1,5,2015-07-31,5263,555,1,1,"0","1"
    # 2,5,2015-07-31,6064,625,1,1,"0","1"
    # 3,5,2015-07-31,8314,821,1,1,"0","1"
    # 4,5,2015-05-31,13995,1498,1,1,"0","1"

    # The colum and its type for full list is.
    # Store             int64
    # DayOfWeek         int64
    # Date             object
    # Sales             int64
    # Customers         int64
    # Open              int64
    # Promo             int64
    # StateHoliday     object
    # SchoolHoliday     int64

    sql = '''
    create table {} (
    Store int,
    DayOfWeek int,
    Date LVARCHAR,
    Sales int,
    Customers int,
    Open int,
    Promo int,
    StateHoliday char(6),
    SchoolHoliday int
    ); '''.format(table_name)

    stmt = IfxPy.exec_immediate(conn, sql)

    sql = '''
    INSERT INTO {} (
    Store,
    DayOfWeek,
    Date,
    Sales,
    Customers,
    Open,
    Promo,
    StateHoliday,
    SchoolHoliday )
     VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ? );
    '''.format(table_name)

    stmt = IfxPy.prepare(conn, sql)

    c1 = None
    c2 = None
    c3 = None
    c4 = None
    c5 = None
    c6 = None
    c7 = None
    c8 = None
    c9 = None

    IfxPy.bind_param(stmt, 1, c1, IfxPy.SQL_PARAM_INPUT, IfxPy.SQL_INTEGER)
    IfxPy.bind_param(stmt, 2, c2, IfxPy.SQL_PARAM_INPUT, IfxPy.SQL_INTEGER)
    IfxPy.bind_param(stmt, 3, c3, IfxPy.SQL_PARAM_INPUT, IfxPy.SQL_CHAR)
    IfxPy.bind_param(stmt, 4, c4, IfxPy.SQL_PARAM_INPUT, IfxPy.SQL_INTEGER)
    IfxPy.bind_param(stmt, 5, c5, IfxPy.SQL_PARAM_INPUT, IfxPy.SQL_INTEGER)
    IfxPy.bind_param(stmt, 6, c6, IfxPy.SQL_PARAM_INPUT, IfxPy.SQL_INTEGER)
    IfxPy.bind_param(stmt, 7, c7, IfxPy.SQL_PARAM_INPUT, IfxPy.SQL_INTEGER)
    IfxPy.bind_param(stmt, 8, c8, IfxPy.SQL_PARAM_INPUT, IfxPy.SQL_CHAR)
    IfxPy.bind_param(stmt, 9, c9, IfxPy.SQL_PARAM_INPUT, IfxPy.SQL_INTEGER)


    # Read the CSV file and insert into the table
    with open( csv_file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_count = 0
        for row in csv_reader:
            row_count += 1

            # Convert the List to tuple
            tup =  tuple(row)

            if row_count == 1:
                print( "Header :", tup )
            else:
                print( tup )
                IfxPy.execute(stmt, tup )
        print(f'Rows Inserted is {row_count-1} .')


    # SELECT the inserted rows
    sql = "SELECT * FROM t1"
    stmt = IfxPy.exec_immediate(conn, sql)
    dictionary = IfxPy.fetch_both(stmt)

    rc = 0
    while dictionary != False:
        rc = rc + 1
        # print ("--  Record {0} --".format(rc))
        # print ("c1 is : ",  dictionary[0])
        # print ("c2 is : ", dictionary[1])
        # print ("c3 is : ", dictionary[2])
        # print ("c4 is : ", dictionary[3])
        # print ("c5 is : ", dictionary[4])
        # print ("c6 is : ", dictionary[5])
        # print ("c7 is : ", dictionary[6])
        # print ("c8 is : ", dictionary[7])
        # print ("c9 is : ", dictionary[8])

        # print (" ")
        dictionary = IfxPy.fetch_both(stmt)

    print(f'Rows Selected is {rc} .')
    IfxPy.close(conn)
    print ("Done")


####### Run the sample function ######
if __name__ == "__main__":
    ConStr = "SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;SERVICE=9088;UID=informix;PWD=xxxx;"
    LoadCsvSample('sample.csv', 't1', ConStr)

