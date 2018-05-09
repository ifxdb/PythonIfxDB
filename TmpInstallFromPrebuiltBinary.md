


### [Driver install by using prebuilt binary](https://github.com/OpenInformix/IfxPy/tree/master/prebuilt)  
FYI: This is only a temporary arrangement till we get all platforms to Python Package Index.   
  
**FYI**: Soon the driver package module will be ready with package manager; meanwhile you may download the driver binary from **IfxPy/prebuilt/...** folder. **FYI**: When you download the prebuilt, clone (or zip) the repository and then take the prebuilt binary. The usage of **wget**, **curl** etc may not get the right binary content from github.

### Python 2.7 then
The prebuilt Informix Python 2.7.x driver binaries are available as **ZIP** (tar file on Linux and zip on Windows).
```bash
git clone https://github.com/OpenInformix/IfxPy.git

IfxPy/prebuilt/27x/ARM/IfxPy.so.tar
IfxPy/prebuilt/27x/Linux64/IfxPy.so.tar
IfxPy\prebuilt\27x\Win64\IfxPy.zip
```
### Python 3.x then
The prebuilt Informix Python 3.x driver binaries are available as **ZIP/tar** as well as **Wheel Package**.
```bash
git clone https://github.com/OpenInformix/IfxPy.git

### ZIP/tar
IfxPy/prebuilt/3x/ARM/IfxPy.so.tar
IfxPy\prebuilt\3x/Win64\IfxPy.zip
# If you are using older python 3x then you may have to rename SO file to IfxPy.so
IfxPy/prebuilt/3x/Linux64/IfxPy.cpython-35m-x86_64-linux-gnu.so.tar

### Wheel Package
# The wheel package is created by using Python 3.6, 
# and it is compatible with Python Enhancement Proposals (PEPs). 
# Then PIP installation is expected to go smooth. 
# If you are still on older python then you may copy the zip/tar module.
IfxPy/prebuilt/3x/ARM/IfxPy-3.0.1-cp35-cp35m-linux_armv7l.whl
IfxPy/prebuilt/3x/Linux64/IfxPy-3.0.1-cp35-cp35m-linux_x86_64.whl
IfxPy\prebuilt\3x/Win64\IfxPy-3.0.1-cp36-cp36m-win_amd64.whl
```

#### Installing the drive from Wheel Package.
```bash
git clone https://github.com/OpenInformix/IfxPy.git

# if ARM v7
pip3 install IfxPy/prebuilt/3x/ARM/IfxPy-3.0.1-cp35-cp35m-linux_armv7l.whl
# if Linux_x86_64
pip3 install IfxPy/prebuilt/3x/Linux64/IfxPy-3.0.1-cp35-cp35m-linux_x86_64.whl
# if Win64
pip3 install IfxPy\prebuilt\3x\Win64\IfxPy-3.0.1-cp36-cp36m-win_amd64.whl
```
