## Windows build
----------------
##### Prerequisite:
* [Python 2.7 or above](https://www.python.org/downloads/) or [Python 3.4 or above](https://www.python.org/downloads/)
* Informix client SDK 410xC2 or above
* Set environment variable **CSDK_HOME** and **MY_PY_DIR**
* If Python 2.7 then Visual Studio 2008 or above
* If Python 3.x then Visual Studio 2015 or above

### Clone the source code
-------------------------
Let's assume **C:\work** is the location when we clone the IfxPy repository.  
(You may clone it at any location though; if so make adjustment for the instructions as well).

```bat
cd C:\work

git clone https://github.com/OpenInformix/IfxPy.git
```

### Build Shell Environment
---------------------------
Set **CSDK_HOME** and **MY_PY_DIR** environment variables.  
The environment **CSDK_HOME** points to the **Informix Client SDK**.   
The environment **MY_PY_DIR** points to the Python source code installation.  

#### Python 2.7 build shell environment 
```bat
# Open VS2008 (or latest) command windows
# set VS90COMNTOOLS if you are using latest vs, for eg, vs2015 then
SET VS90COMNTOOLS=%VS140COMNTOOLS%

SET CSDK_HOME=c:\informix
SET MY_PY_DIR=C:\Dev\Python27
```


FYI: 
While running setup.py for package build, **Python 2.7** searches for an installed Visual Studio 2008. (The installation path of VS2008 is stored in the variable VS90COMNTOOLS). The general pattern for VS installation path is 
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
  
#If you are using Visual Studio 2017 (VS15):   
SET VS90COMNTOOLS=%VS150COMNTOOLS%
```

#### Python 3.x build shell environment 
The **Python 3.x** build uses Visual Studio 2015 or above then, if you are building with python 3.x then make your you have VS2015 or above available on your system.
```bat
# Open VS2015 (or latest) command windows

SET CSDK_HOME=c:\informix
SET MY_PY_DIR=C:\Dev\Anaconda3

```


### Starting the build 
```bash
cd C:\work\IfxPy\IfxPy
python setup.py build > out.txt 2>&1
```
On successful build the Informix native driver module (**IfxPy.pyd**) should have built at  
C:\work\IfxPy\IfxPy\build\lib.win-amd64-2.7  (if Python 2.7 on Win64 then)   
C:\work\IfxPy\IfxPy\build\lib.win-amd64-3.6  (if Python 3.6 on Win64 then)   


#### Other Build Options
-------------------------
* [pip](https://pip.pypa.io/en/stable/reference/)
* [Pip Wheel](https://pip.pypa.io/en/stable/reference/pip_wheel/)

```bash
# Make sure you have installed wheel before doing the build
pip install wheel

cd C:\work\IfxPy\IfxPy
python setup.py bdist_wheel

# On successful build, it would have created the whl file under dist folder. 
# For example : 
# C:\work\IfxPy\IfxPy\dist\IfxPy-3.0.1-cp36-cp36m-win_amd64.whl

# YOu may use pip intall to install the driver from the whl file
#  it will get distributed to your <Python Install Directory>\Lib\site-packages\
# pip install  dist\IfxPy-<driver version>-cp36-cp36m-win_amd64.whl
# For example:
pip install  dist\IfxPy-3.0.1-cp36-cp36m-win_amd64.whl
```


### Install
-----------
The python documentation has various python package install options, you may choose any of the option.
* [Installing Packages](https://packaging.python.org/tutorials/installing-packages/)
* [Installing Python 2.x Modules](https://docs.python.org/2/install/index.html)
* [Installing Python 3.x Modules](https://docs.python.org/3/install/index.html)  

If you are looking for a simple build test verification only situation, then you may manually copy Informix python modules (IfxPy.pyd and IfxPyDbi.py) to your Python application module directory. 
```bash
# if Python 2.7 on Win64 then
COPY  C:\work\IfxPy\IfxPy\build\lib.win-amd64-2.7\IfxPy.pyd

# if Python 3.6 on Win64 then
COPY  C:\work\IfxPy\IfxPy\build\lib.win-amd64-3.6\IfxPy.cp36-win_amd64.pyd
```

Try a sample
```bash
cd C:\work\IfxPy\try
copy  C:\work\IfxPy\IfxPy\build\lib.win-amd64-2.7\IfxPy.pyd
copy Sample1.py Sample.py
set PATH=C:\Informix\bin;%PATH%

# Edit Sample.py connection information, and then run
python Sample.py
```

