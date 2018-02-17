### Information about the prebuilt driver binaries
We will be getting to **pip install** soon, for the time being you may download prebuilt native driver binary from prebuilt folder. These binaries may not be built with latest source code on the repository. 

FYI: When you download the prebuilt, clone or zip the repository and then take the prebuilt binary. The usage of wget, curl etc may not get right binary content from github.


#### Python 2.7x 
| **Platform** | **Py Version** |     **Location**          | **MD5 hash**
|:-------------|:---------------|:--------------------------|:--------------------------------
| `ARM`        |   2.7.13       |  27x/ARM/IfxPy.so.tar     | 74e2e45e9b9052ad373d0b9ea4a6410a
| `Win64`      |                |  27x/Win64/IfxPy.zip      | 29fd9fdb62986a48a6d1e8416aab7c2d
| `Linux64`    |                | 27x/Linux64/IfxPy.so.tar  | 1f2885bf2f86fd1677e0a0286d8ef4c6


#### Python 3.x 
| **Platform** | **Py Version** |     **Location**          | **MD5 hash**
|:-------------|:---------------|:--------------------------|:--------------------------------
| `Arm`        |  3.6.2         |  35x/ARM/IfxPy.so.tar     | a3d0fe5ff019b3de46ba0355272e29e7
| `Win64`      |                |  Coming soon              |
| `Linux64`    |  3.5.2         |  35x/Linux64/IfxPy.cpython-35m-x86_64-linux-gnu.so.tar          | a3df1448f43b7576dadd89336f407e82



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


### Windows Built in tools for checking Hash value
* [PowerShell.Utility](https://docs.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Utility/Get-FileHash?view=powershell-5.1)

* [certutil](https://technet.microsoft.com/library/cc732443.aspx)
```bash
certutil -hashfile IfxPy.zip  MD5
# use 7zip to unzip it 
```

