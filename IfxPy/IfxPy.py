import os
# if 'CSDK_HOME' not in os.environ['PATH']:
#     os.environ['PATH'] = os.environ['PATH'] + ";" + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'CSDK_HOME', 'bin')
def __bootstrap__():
   global __bootstrap__, __loader__, __file__
   import sys, pkg_resources, imp
   __file__ = pkg_resources.resource_filename(__name__,'IfxPy\IfxPy.pyd')
   __loader__ = None; del __bootstrap__, __loader__
   imp.load_dynamic(__name__,__file__)
__bootstrap__()