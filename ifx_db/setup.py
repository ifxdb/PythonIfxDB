import os
import sys


from distutils.core import setup, Extension


module1 = Extension('ifx_db',
                    sources = ['ifx_db.c'])

setup (name = 'PackageName',
       version = '1.0',
       description = 'This is a ifx_db package',
       ext_modules = [module1])
