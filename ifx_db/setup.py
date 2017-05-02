import os
import sys
import struct

from distutils.core import setup, Extension

PACKAGE = 'ifx_db'
VERSION = '2.0.7'
LICENSE = 'Apache License 2.0'

machine_bits =  8 * struct.calcsize("P")
is64Bit = True
#csdk_home = os.environ['CSDK_HOME']
#py_home = os.environ['MY_PY_DIR']

if machine_bits == 64:
    is64Bit = True
    sys.stdout.write("Detected 64-bit Python\n")
else:
    is64Bit = False
    sys.stdout.write("Detected 32-bit Python\n")


ext_modules = Extension('ifx_db',
                   include_dirs = ['C:\\Dev\Python27\\include', 'C:\\Informix\\incl\\cli'],
                    libraries = ['iclit09b'],
                    library_dirs = [ 'C:\Informix\lib', 'C:\\Dev\\Python27\\libs'],
                    sources = ['ifx_db.c'])

setup (name    = PACKAGE, 
       version = VERSION,
       license = LICENSE,
       description      = 'Python DB driver for Informix',
       author           = 'Informix Application Development Team',
       ext_modules = [ext_modules])

