import os
import sys
import struct
from setuptools import setup
from distutils.core import Extension

# Writing the Setup Script
# https://docs.python.org/3.4/distutils/setupscript.html#distutils-installing-scripts


PACKAGE   = 'IfxPy'
VERSION   = '3.0.1'
VERSION2X = '2.7.1'
LICENSE   = 'Apache License 2.0'
IfxPyLongDescription='Informix native Python driver is a high performing data access interface suitable for highly scalable enterprise and IoT solutions to works with Informix database.'

# Specifying the files to distribute
# https://docs.python.org/3.4/distutils/sourcedist.html#manifest
# IfxPy_modules = ['config', 'IfxPyDbi', 'testfunctions', 'tests']
IfxPy_modules = ['IfxPyDbi']


#package_data = { 'IfxPyPkg': [ 'data/IfxPyPackageData1.txt', 'data/IfxPyPackageData2.txt']}
# package_data = { 'IfxPyPkgData': [ 'data/*.txt'] }

# Installing Additional Files
# https://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
# data_files = [ ('IfxPySample', ['./README.rst']),
#                ('IfxPySample', ['../Examples/Sample1.py']),
#                ('IfxPySample', ['../Examples/DbAPI_Sample1.py']),
#                ('IfxPySample', ['../Examples/DbAPI_Sample_executemany.py']),
#                ('IfxPySample', ['../Examples/DbAPI_Sample_Params.py']),
#                ('IfxPySample', ['./LICENSE.txt']) ]

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
    IfxPyNative_ext_modules = Extension('IfxPy',
        include_dirs = [py_home + '\\include', csdk_home + '\\incl\\cli'],
        libraries = ['iclit09b'],
        library_dirs = [ py_home + '\libs', csdk_home + '\lib'],
        sources = ['ifxpyc.c'])
else:
    IfxPyNative_ext_modules = Extension('IfxPy',
        include_dirs = [ py_home,  py_home + '/Include', csdk_home +'/incl/cli'],
        libraries = ['ifdmr', 'thcli'],
        library_dirs = [ csdk_home + '/lib/cli', py_home + '/Lib'],
        sources = ['ifxpyc.c'])


# Supporting both Python 2 and Python 3 with Setuptools
# http://setuptools.readthedocs.io/en/latest/python3.html
extra = {}
if sys.version_info >= (3, ):
    extra['use_2to3'] = True
else:
    VERSION = VERSION2X

setup (name    = PACKAGE, 
       version = VERSION,
       license = LICENSE,
       description      = 'Informix native Python driver',
       long_description = IfxPyLongDescription,
       
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
           'Intended Audience :: Developers',
           'Topic :: Software Development',

           # Pick your license as you wish (should match "license" above)
           'License :: OSI Approved :: Apache Software License',

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

       ext_modules = [IfxPyNative_ext_modules],
       py_modules   = IfxPy_modules,
    #    package_data = package_data,
    #    data_files   = data_files,
    #    include_package_data = True,
       **extra
      )
