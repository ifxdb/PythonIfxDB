### Information about the prebuilt driver binaries
We will be getting to **pip install** soon, for the time being you may download prebuilt native driver binary from prebuilt folder. These binaries may not be built with latest source code on the repository. 

FYI: When you download the prebuilt, clone or zip the repository and then take the prebuilt binary. The usage of wget, curl etc may not get right binary content from github.


#### Python 2.7x 
| **Platform** | **Py Version** |     **Location**          | **MD5 hash**
|:-------------|:---------------|:--------------------------|:--------------------------------
| `ARM`        |   2.7.13       |  27x/ARM/IfxPy.so.tar     | 74e2e45e9b9052ad373d0b9ea4a6410a
| `Linux64`    |                | 27x/Linux64/IfxPy.so.tar  | 1f2885bf2f86fd1677e0a0286d8ef4c6
| `Win64`      |                |  27x/Win64/IfxPy.zip      | 29fd9fdb62986a48a6d1e8416aab7c2d


#### Python 3.x 
| **Platform** | **Py Version** |     **Location**                                        | **MD5 hash**
|:-------------|:---------------|:--------------------------------------------------------|:---------------------
| `Arm`        |  3.6.2         |  3x/ARM/IfxPy.so.tar                                    | a3d0fe5ff019b3de46ba0355272e29e7
| `Arm`        |  3.6.2         |  3x/ARM/IfxPy-3.0.1-cp35-cp35m-linux_armv7l.whl         | 07415084844664562c84a23b5538e874
| `Linux64`    |  3.5.2         |  3x/Linux64/IfxPy.cpython-35m-x86_64-linux-gnu.so.tar   | a3df1448f43b7576dadd89336f407e82
| `Win64`      | 3.6.4 Anaconda |  3x/Win64/IfxPy.zip                                     | e606f3d4bba22483d2291e2401406330
| `Win64`      | 3.6.4 Anaconda |  3x/Win64/IfxPy-3.0.1-cp36-cp36m-win_amd64.whl          | f85ee178fffbe8bf16ebb9f88040a895



###  Checking Hash on Linux
#### Python 2.7x: 
```bash
# Linux x86_64
cd /work/t1/IfxPy/IfxPy/build/lib.linux-x86_64-2.7/

# ARM
cd /work/t1/IfxPy/IfxPy/build/lib.linux-armv7l-2.7/

tar -cvf IfxPy.so.tar ./IfxPy.so
md5sum ./IfxPy.so.tar
# tar -xvf IfxPy.so.tar
```

#### Python 3x
```bash
###### Linux x86_64 
cd /work/t1/IfxPy/IfxPy/build/lib.linux-x86_64-3.5/

tar -cvf IfxPy.cpython-35m-x86_64-linux-gnu.so.tar ./IfxPy.cpython-35m-x86_64-linux-gnu.so
md5sum ./IfxPy.cpython-35m-x86_64-linux-gnu.so.tar

# copy the tar to IfxPy/prebuilt/35x/Linux64
# To extract download the tar and then
# tar -xvf IfxPy.cpython-35m-x86_64-linux-gnu.so.tar

###### ARM v7
cd /work/t1/IfxPy/IfxPy/build/lib.linux-armv7l-3.5/
cp IfxPy.cpython-35m-arm-linux-gnueabihf.so IfxPy.so
tar -cvf IfxPy.so.tar ./IfxPy.so

md5sum ./IfxPy.so
#a3d0fe5ff019b3de46ba0355272e29e7  ./IfxPy.so.tar
# cp IfxPy.so.tar /work/t1/IfxPy/prebuilt/35x/ARM
```

#### Wheel Build
-------------------------

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

### Windows Built in tools for checking Hash value
* [PowerShell.Utility](https://docs.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Utility/Get-FileHash?view=powershell-5.1)

* [certutil](https://technet.microsoft.com/library/cc732443.aspx)
```bash
certutil -hashfile IfxPy.zip  MD5
# use 7zip to unzip it 
```

