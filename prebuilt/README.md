

### Information about the prebuilt driver binaries

We will be getting to **pip install** soon, for the time being you may download prebuilt native driver binary from prebuilt folder. These binaries may not be built with latest source code on the repository. 


#### Python 2.7x 
| **Platform** | **Py Version** |     **Location**          | **MD5 hash**
|:-------------|:---------------|:--------------------------|:--------------------------------
| `ARM`        |   2.7.13       |  27x/ARM/IfxPy.so.tar     | 74e2e45e9b9052ad373d0b9ea4a6410a
| `Win64`      |                |      Coming soon          |
| `Linux64`    |                | 27x/Linux64/IfxPy.so.tar  | 1f2885bf2f86fd1677e0a0286d8ef4c6


#### Python 3.x 
| **Platform** | **Py Version** |     **Location**          | **MD5 hash**
|:-------------|:---------------|:--------------------------|:--------------------------------
| `Arm`        |                |     Coming soon           | 
| `Win64`      |                |     Coming soon           |
| `Linux64`    |                |     Coming soon           |



###  Linux Checking Hash
```bash
cd /work/t1/IfxPy/IfxPy/build/lib.linux-x86_64-2.7/
# cd /work/t1/IfxPy/IfxPy/build/lib.linux-armv7l-2.7/
tar -cvf IfxPy.so.tar ./IfxPy.so

md5sum ./IfxPy.so.tar
tar -xvf IfxPy.so.tar
```


### Windows Built in tools for checking Hash value
* [PowerShell.Utility](https://docs.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Utility/Get-FileHash?view=powershell-5.1)

* [certutil](https://technet.microsoft.com/library/cc732443.aspx)
```bash
certutil -hashfile IfxPy.dll.7z  MD5
# use 7zip to unzip it 
```

