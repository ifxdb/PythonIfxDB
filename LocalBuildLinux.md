## Linux Build 
--------------
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
```

#### Fire the driver build
```bash
cd /work/t1/IfxPy/IfxPy
rm -rf build

python setup.py build > out.txt 2>&1

# if all go well, then Informix native python driver will be at
# if x86 Linux with 64bit build then
ls -l build/lib.linux-x86_64-2.7/IfxPy.so

# Similarly if ARM then 
ls -l build/lib.linux-armv7l-2.7/IfxPy.so
```

##### Copy the dirver native lib
The native lib is good enough to get advance features working. The **Python Database API Specification v2.0** features are wrapper on top of the advance features that can be obtained by copying **IfxPyi.py**

```bash
# Copy Informix python package (IfxPy.so) to your Python module directory
# For example:
cp /work/t1/IfxPy/IfxPy/build/lib.linux-x86_64-2.7/IfxPy.so .

# if ARM
# cp /work/t1/IfxPy/IfxPy/build/lib.linux-armv7l-2.7/IfxPy.so .
```

####  Quick test of the local build
-----------------------------------

#### Get a sample code
```bash
cd /work/try/
cp /work/t1/IfxPy/Examples/Sample1.py Sample.py

rm IfxPy.so
cp /work/t1/IfxPy/IfxPy/build/lib.linux-x86_64-2.7/IfxPy.so .
# if ARM then
# cp /work/t1/IfxPy/IfxPy/build/lib.linux-armv7l-2.7/IfxPy.so .
```

#### Set runtime environment to pick Informix Client SDK libraries
```bash
export INFORMIXDIR=/work/informix
export LD_LIBRARY_PATH=${INFORMIXDIR}/lib:${INFORMIXDIR}/lib/esql:${INFORMIXDIR}/lib/cli
export PATH=$INFORMIXDIR/bin:$PATH
```

#### Run the sample
```bash
vi Sample.py
# Edit Sample.py connection information, and then run
python Sample.py
```

