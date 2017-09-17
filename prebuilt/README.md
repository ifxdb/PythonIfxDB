

### Information about the prebuilt driver binaries

We will be getting to **pip install** soon, for the time being you may download prebuilt native driver binary from prebuilt folder. These binaries may not be built with latest source code on the repository. 


#### Python 2.7x 
| **Platform** | **Py Version** |     **Location**          | **MD5 hash**
|:-------------|:---------------|:--------------------------|:--------------------------------
| `ARM`        |   2.7.13       |  27x/ARM/IfxPy.so.tar    | 74e2e45e9b9052ad373d0b9ea4a6410a
| `Win64`      |                |      Coming soon          |
| `Linux64`    |                |      Coming soon          |


#### Python 3.x 
| **Platform** | **Py Version** |     **Location**          | **MD5 hash**
|:-------------|:---------------|:--------------------------|:--------------------------------
| `Arm`        |                |     Coming soon           | 
| `Win64`      |                |     Coming soon           |
| `Linux64`    |                |     Coming soon           |



###  Linux Checking Hash
```bash
cd node-IfxPy
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

