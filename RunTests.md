
## Run tests
------------

#### Set Informix Client SDK Runtime Environment 
**FYI**: Make sure to set Informix Client SDK Runtime Environment before running applications

##### Linux
```bash
export LD_LIBRARY_PATH=${INFORMIXDIR}/lib:${INFORMIXDIR}/lib/esql:${INFORMIXDIR}/lib/cli
export PATH=$INFORMIXDIR/bin:$PATH
```

##### Windows
```bat
# say you have installed CSDK at C:\informix then
SET PATH=C:\informix\bin;%PATH%
```

### Preliminary diagnostic tips 
##### Cconnection problem
+ check the service port mapped to which IP etc
- for example the port you configured is 9088 then
- netstat -a | findstr  9088


##### Specify connection information
```bash
# cd C:\work\IfxPy\IfxPy
cd /work/t1/IfxPy/IfxPy
cp   config.py.sample   config.py
```
Then Modify the connection properties specified in config.py

##### Run all tests
```bash
# copy C:\work\IfxPy\IfxPy\build\lib.win-amd64-2.7\IfxPy.pyd
cp /work/t1/IfxPy/IfxPy/build/lib.linux-x86_64-2.7/IfxPy.so .
# if ARM then
# cp /work/t1/IfxPy/IfxPy/build/lib.linux-armv7l-2.7/IfxPy.so .

python tests.py
```

##### Run a single test
A single test can be run by specifying test name in the **SINGLE_PYTHON_TEST** environment variable.
```bash
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
You can use the '2to3' Python utility in the 'IfxPy/tests' directory, for example:
$ cd /work/IfxPy/IfxPy/IfxPy/tests
$ 2to3 -w *.py
```


