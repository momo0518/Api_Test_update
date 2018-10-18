#!/usr/bin/env python
# encoding:utf-8
    ##author:fanglujie
    ##date:2018/09/10
import sys
sys.path.append('./venv/lib/python2.7/site-packages')
import unittest
import HTMLTestRunner
import time

def creatsuite():
    testunit = unittest.TestSuite()
    test_dir = '/Users/fanglujie/Documents/Project/Api_Test/TestCase'
    #test_dir = '/Users/fanglujie/Documents/Project/UI_CPK/TestCase/test_case2'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py',top_level_dir=None)
    for test_case in discover:
        print test_case
        testunit.addTests(test_case)
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = './result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'应用商店分中心测试报告', description=u'用例执行情况:')


if __name__ == '__main__':
    alltestnames = creatsuite()
    runner.run(alltestnames)
    fp.close()
