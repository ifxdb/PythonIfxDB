
import pandas as pd

# Lists are enclosed in brackets:
# l = [1, 2, "a"]

# Tuples are enclosed in parentheses:
# Tuples are faster and consume less memory
# t = (1, 2, "a")

# Dictionaries are built with curly brackets:
# d = {"a":1, "b":2}
# Sets are made using the set() builtin function

# Python List vs. Tuples (Key points to remember)
# The literal syntax of tuples is shown by parentheses ()
# whereas the literal syntax of lists is shown by square brackets []
# Lists has variable length, tuple has fixed length.
# List has mutable nature, tuple has immutable nature.
# List has more functionality than the tuple.


# Basics of creating Pandas DataFrames from Lists and Dictionaries
# http://pbpython.com/pandas-list-dict.html
# https://www.datacamp.com/community/tutorials/pandas-read-csv


def csv_2sql( csv_file_name, table_name ):
    data = pd.read_csv( csv_file_name )

    # Get the first 5 rows
    # print( data.head() )

    rows, c_count = data.shape
    print( "# Number of rows={} and columns={}".format(rows, c_count ) )
    p = '    '


    print( "sql = '''")
    print( "CREATE TABLE {} ( ".format(table_name) )
    i = 0
    for col in data.columns:
        i  = i+1
        t = data[col].dtype

        if t == 'int64':
            t = "INTEGER"
        else:
            t = "LVARCHAR"

        if i == c_count:
            print( p, col, t, " ); " )
        else :
            print( p, col, t, "," )
    print( "'''")


    print( )
    print( "sql = '''")
    print( "INSERT INTO {} ( ".format(table_name) )
    i = 0
    for col in data.columns:
        i  = i+1
        if i == c_count:
            print( p, col, " ) " )
        else :
            print( p, col, "," )

    # Python 3 specific ( end = ''), to print on same line
    print( p, "VALUES ( ", end = '' )
    i = 0
    while i < c_count:
        i  = i+1
        if i == c_count:
            print( " ? ); " )
        else :
            # Python 3 specific
            print( "?, ", end = '' )
    print( "'''")


    print( "stmt = IfxPy.prepare(conn, sql)" )
    i = 0
    for col in data.columns:
        i  = i+1
        t = data[col].dtype

        if t == 'int64':
            t = "INTEGER"
        else:
            t = "LVARCHAR"

        print()
        print( "c{} = None".format(i) )
        print( "IfxPy.bind_param(stmt, {}, c{}, IfxPy.SQL_PARAM_INPUT, IfxPy.{})".format(i, i, t ) )


####### Run the sample function ######
if __name__ == "__main__":
    csv_2sql('sample.csv', 'tab1')



