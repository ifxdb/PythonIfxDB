

### Information about the prebuilt driver binaries

We will be getting to **pip install** soon, for the time being you may download prebuilt native driver binary from prebuilt folder. These binaries may not be built with latest source code on the repository. 


#### Python 2.7x 
| **Platform** | **Py Version** |     **Location**          | **MD5 hash**
|:-------------|:---------------|:--------------------------|:--------------------------------
| `Arm`        |   2.7.13       |  27x/ARM/ifx_db.so.tar    | de66bb3c74412d45156a61854b600c5f
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
cd node-ifx_db
md5sum ./ifx_db.so.tar

tar -xvf ifx_db.so.tar
```


### Windows Built in tools for checking Hash value
* [PowerShell.Utility](https://docs.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Utility/Get-FileHash?view=powershell-5.1)

* [certutil](https://technet.microsoft.com/library/cc732443.aspx)
```bash
certutil -hashfile ifx_db.dll.7z  MD5
# use 7zip to unzip it 
```

