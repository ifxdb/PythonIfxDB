#//////////////////////////////////////////////////////////////////////////
# Copyright 2017 OpenInformix 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http ://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Authors:
#      Sathyanesh Krishnan
#
#//////////////////////////////////////////////////////////////////////////

import os
import sys
import unittest
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import re
import glob
import config

class IfxDbTest(unittest.TestCase):
  
  slash = '/'
  
  # Currently, this function serves no purpose.
  # However, this function has to be defined if the
  #   unittest.TestCase is inherited in the given class.
  # For future reference, this function is called 
  #   everytime a test is ran in this testsuite.
  def setUp(self):
    pass

  # This function gets a list of all the test files located
  #   in the current_dir/config.test_dir directory.
  def getFileList(self):
    if (sys.platform[0:3] == 'win'):
      self.slash = '\\'
    dir = config.test_dir + self.slash
    if (os.environ.get("SINGLE_PYTHON_TEST", None)):
      testfile = dir + os.environ.get("SINGLE_PYTHON_TEST", None)
      filelist = glob.glob(testfile)
    else:
      filelist = glob.glob(dir + "test_*.py")
      
    for i in range(0, len(filelist)):
      filelist[i] = filelist[i].replace('.py', '')
      filelist[i] = filelist[i].replace(config.test_dir + self.slash, '')
    filelist.sort()
    return filelist

  # This function is called to run all the tests.
  def runTest(self):
    filelist = self.getFileList();
    suite = unittest.TestSuite()
    
    sys.path = [os.path.dirname(os.path.abspath(__file__)) + self.slash + config.test_dir] + sys.path[0:]
    
    for i in range(0, len(filelist)):
      exec("import %s" % filelist[i])
      testFuncName = filelist[i].replace(config.test_dir + self.slash, '')
      exec("suite.addTest(%s.IfxPyTestCase(testFuncName))" % filelist[i])
      
    unittest.TextTestRunner(verbosity=2).run(suite) 

obj = IfxDbTest()
suite = obj.runTest()
