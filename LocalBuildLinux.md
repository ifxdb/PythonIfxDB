## Linux Build 
--------------
##### Prerequisite:
* [Python 2.7 or above](https://www.python.org/downloads)
* [Python 3.4 or above](https://www.python.org/downloads)
* setuptools (pip/pip3 install setuptools)
* Informix client SDK 410xC2 or above
* Set environment variable CSDK_HOME and MY_PY_DIR
* Operating System Unicode encoding should match with your python interpreter encoding. 

**MY_PY_DIR** points to the Python installation directory. During the driver build it need python header files, if the current Python installation doesn’t have the header file then you may need to get Python source code.

##### FYI: Unicode encoding
The python interpreter used should match with operating system default Unicode encoding. 
Some of the Linux flavors, python interpreter is available with UCS2/UTF16 and also UCS4/UTF32.
If the OS default for Unicode is UTF32 then the OpenInformix driver will work if the python interpreter is also using the Unicode UCS4/UTF32.  


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
--------------------------------------
By any chance if you don’t have the right python interpreter or you don’t have the development environment for building native library then you may have to build python from its source. Python can be built from it source by using the following steps.  

Determine the Unicode encoding needed for your python interpreter. Most of the Linux platforms are by default UCS4/UTF32, the following step is to build python for UCS4/UTF32 Unicode encoded string.

##### [Download and extract python source code](https://www.python.org/downloads)
This instruction is for both Python 2.7 and Python 3.x build.  The commented Python 3.x build instruction is good for building it from source.
```bash
cd /work/dev

rm ./Python
sudo rm -rf ./Python-2.7.13
# sudo rm -rf ./Python-3.5.2

wget https://www.python.org/ftp/python/2.7.14/Python-2.7.13.tgz
# wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz

tar zxvf Python-2.7.13.tgz
# tar zxvf Python-3.5.2.tgz

ln -s  ./Python-2.7.13  ./Python
# ln -s  ./Python-3.5.2  ./Python

cd /work/dev/Python
sudo ./configure --enable-unicode=ucs4
```
###### Fire the Python build
```bash
$ cd /work/dev/Python
$ sudo ./configure --enable-unicode=ucs4
$ sudo make

# /work/dev/Python to be added to the path
# install is not needed for driver build thouhg
# $ sudo altinstall
```
#### Build Informix Python driver
---------------------------------

##### Clone the informix python driver source code
```bash
mkdir /work/t1
cd /work/t1

git clone https://github.com/OpenInformix/IfxPy.git
```

##### Set Env for driver build 
```bash
# sudo ln -s /home/informix/1210UC9 /work/informix
# Assuming 'CSDK' is installed at /work/informix
export CSDK_HOME=/work/informix
export MY_PY_DIR=/work/dev/Python
export PATH=/work/dev/Python:$PATH
```

#### Fire the driver build
```bash
cd /work/t1/IfxPy/IfxPy
rm -rf build

# '/work/dev/Python' has added to the path, then
# export PATH=/work/dev/Python:$PATH
# $ which python
# /work/dev/Python/python
# pip install setuptools
python setup.py build > out.txt 2>&1
#python3 setup.py build > out.txt 2>&1

# if all go well, then Informix native python driver will be at

# if Linux x86_64bit with Python 2.7 build then
ls -l ./build/lib.linux-x86_64-2.7/IfxPy.so

# if ARM v7 with Python 2.7 then 
ls -l build/lib.linux-armv7l-2.7/IfxPy.so

# if Linux x86_64bit with Python 3.x build then
# ls -l ./build/lib.linux-x86_64-3.5/IfxPy.cpython-35m-x86_64-linux-gnu.so

# on armv7 with Python 3.x
# ls -l ls ./build/lib.linux-armv7l-3.5/IfxPy.cpython-35m-arm-linux-gnueabihf.so
```
#### Other Build Options
-------------------------
* [pip](https://pip.pypa.io/en/stable/reference/)
* [Pip Wheel](https://pip.pypa.io/en/stable/reference/pip_wheel/)

```bash
# Make sure you have installed wheel before doing the build
pip install wheel
#pip3 install wheel

cd /work/t1/IfxPy/IfxPy
python setup.py bdist_wheel
#python3 setup.py bdist_wheel

# On successful build, it would have created the whl file under dist folder. 
# For example : 
# /work/t1/IfxPy/IfxPy/dist/IfxPy-3.0.1-cp27-cp27mu-linux_armv7l.whl
# /work/t1/IfxPy/IfxPy/dist/IfxPy-3.0.1-cp35-cp35m-linux_armv7l.whl

# Python 3.x wheel build to the prebuilt location for ARM v7
# cp /work/t1/IfxPy/IfxPy/dist/IfxPy-3.0.1-cp35-cp35m-linux_armv7l.whl /work/t1/IfxPy/prebuilt/3x/ARM/.
# md5sum /work/t1/IfxPy/prebuilt/3x/ARM/IfxPy-3.0.1-cp35-cp35m-linux_armv7l.whl

# YOu may use pip intall to install the driver from the whl file
# For example:
# pip3 install  /work/t1/IfxPy/prebuilt/3x/ARM/IfxPy-3.0.1-cp35-cp35m-linux_armv7l.whl
# pip3 uninstall  /work/t1/IfxPy/prebuilt/3x/ARM/IfxPy-3.0.1-cp35-cp35m-linux_armv7l.whl
```


##### Copy the dirver native lib
The native lib is good enough to get advance features working. The **Python Database API Specification v2.0** features are wrapper on top of the advance features that can be obtained by copying **IfxPyDbi.py**

```bash
# Copy Informix python package (IfxPy.so) to your Python module directory
# For example:
# Python 2.7 on linux-x86_64
cp /work/t1/IfxPy/IfxPy/build/lib.linux-x86_64-2.7/IfxPy.so .

# Python 2.7 ARMv7 
# cp /work/t1/IfxPy/IfxPy/build/lib.linux-armv7l-2.7/IfxPy.so .

# Python 3.x on ARMv7 
# cp /work/t1/IfxPy/IfxPy/build/lib.linux-armv7l-3.5/IfxPy.cpython-35m-arm-linux-gnueabihf.so  ./IfxPy.so
```

####  Quick test of the local build
-----------------------------------

#### Get a sample code
```bash
cd /work/try/
cp /work/t1/IfxPy/Examples/Sample1.py Sample.py

rm IfxPy.so
# rm *.so

# Python 2.7 on linux-x86_64
cp /work/t1/IfxPy/IfxPy/build/lib.linux-x86_64-2.7/IfxPy.so .

# Python 3.x on linux-x86_64
# cp /work/t1/IfxPy/IfxPy/build/lib.linux-x86_64-3.5/IfxPy.cpython-35m-x86_64-linux-gnu.so .

# if ARM then
# cp /work/t1/IfxPy/IfxPy/build/lib.linux-armv7l-2.7/IfxPy.so .

# Python 3.x on ARM v7
# cp /work/t1/IfxPy/IfxPy/build/lib.linux-armv7l-3.5/IfxPy.cpython-35m-arm-linux-gnueabihf.so ./IfxPy.so
```

#### Set runtime environment to pick Informix Client SDK libraries
```bash
export INFORMIXDIR=/work/informix
export LD_LIBRARY_PATH=${INFORMIXDIR}/lib:${INFORMIXDIR}/lib/esql:${INFORMIXDIR}/lib/cli
# Set the INFORMIXSQLHOSTS too, say 
# export INFORMIXSQLHOSTS=/work/dev/srv/ids0/sqlhosts
```

#### Run the sample
```bash
# '/work/dev/Python' has added to the path, then
# $ which python
# /work/dev/Python/python

vi Sample.py
# Edit Sample.py connection information, and then run
python Sample.py
```

