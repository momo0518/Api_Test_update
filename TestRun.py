# !/usr/bin/python
 # -*- coding: UTF-8 -*-
import sys
sys.path.append('./venv/lib/python2.7/site-packages')
from HTMLTestRunner import HTMLTestRunner
import unittest
import os
import time
from src import info as log
try:
    test_dir = os.path.abspath('.')
    reportfile = os.path.abspath('.')+'/report'+'/%s_result.html'%time.strftime('%Y-%m-%d-%H-%M-%S')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='WebApi.py')
except IOError,e:
    log.getErrorInfo("错误信息："+str(e))
if __name__ == "__main__":
    filename = reportfile
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp)
    runner.run(discover)
    fp.close()
