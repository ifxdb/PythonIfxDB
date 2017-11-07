import os
import sys
import struct
from setuptools import setup
from distutils.core import Extension


PACKAGE = 'IfxPy'
VERSION = '3.0.1'
LICENSE = 'Apache License 2.0'

machine_bits =  8 * struct.calcsize("P")
is64Bit = True
csdk_home = os.environ['CSDK_HOME']
py_home = os.environ['MY_PY_DIR']

if machine_bits == 64:
    is64Bit = True
    sys.stdout.write("Detected 64-bit Python\n")
else:
    is64Bit = False
    sys.stdout.write("Detected 32-bit Python\n")

if('win32' in sys.platform):
    ext_module_IfxPyn = Extension('IfxPy',
        include_dirs = [py_home + '\\include', csdk_home + '\\incl\\cli'],
        libraries = ['iclit09b'],
        library_dirs = [ py_home + '\libs', csdk_home + '\lib'],
        sources = ['ifxpyc.c'])
else:
    ext_module_IfxPyn = Extension('IfxPy',
        include_dirs = [ py_home,  py_home + '/Include', csdk_home +'/incl/cli'],
        libraries = ['ifdmr', 'thcli'],
        library_dirs = [ csdk_home + '/lib/cli', py_home + '/Lib'],
        sources = ['ifxpyc.c'])

long_description='Informix native Python driver is a high performing data access interface suitable for highly scalable enterprise and IoT solutions to works with Informix database.'

setup (name    = PACKAGE, 
       version = VERSION,
       license = LICENSE,
       description      = 'Python DB driver for Informix',
       long_description = long_description,
       
       # The project's main homepage.
       #url='https://github.com/OpenInformix/IfxPy',

       author           = 'Informix Application Development Team',
       #author_email='xyz@hcl.com',

       # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
       classifiers=[
           # How mature is this project? Common values are
           #   3 - Alpha
           #   4 - Beta
           #   5 - Production/Stable
           'Development Status :: 4 - Beta',

           # Indicate who your project is intended for
           'Intended Audience :: Informix Python Applicatin Developers',
           'Topic :: Software Development',

           # Pick your license as you wish (should match "license" above)
           'License :: Apache Version 2.0 License',

           # Specify the Python versions you support here. In particular, ensure
           # that you indicate whether you support Python 2, Python 3 or both.
           'Programming Language :: Python :: 2.7',
           'Programming Language :: Python :: 3.4',
           'Programming Language :: Python :: 3.5',
           'Programming Language :: Python :: 3.6',
       ],
       long_description_content_type='text/markdown',

       # What does your project relate to?
       keywords='Informix Python Enterprise TimeSeries IoT',


       ext_modules = [ext_module_IfxPyn]
      )

