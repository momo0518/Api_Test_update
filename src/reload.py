#!/usr/bin/env python
# encoding:utf-8
    ##author：fanglujie
    ##date：2018/09/02
import sys
sys.path.append('./venv/lib/python2.7/site-packages')
from src import excuteCFG
import os
import shutil
import time
import ConfigParser
from src import info as log
    #cfg配置文件
    #file_path工程目录
    #result_file是data目录下的测试结果
    #先将example.xls复制一份做为副本

cfgfile = './config.ini'
file_path = os.path.abspath('.')
result_file = os.listdir('./data')
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

shutil.copyfile('./data/'+result_file[0],'./data/'+now+'.xls')
#shutil.copyfile('./data/'+result_file[0],'./data/example.xls')
try:
    config = ConfigParser.ConfigParser()
    config.read(cfgfile)
    config.set('setting','xls_back',now+'.xls')

    config.write(open(cfgfile, 'w'))
except IOError:
    log.getErrorInfo('写入配置文件异常')
try:
    xls_back = excuteCFG.ConfigRead(cfgfile, 'setting', 'xls_back').CfgRead()
except IOError:
    log.getErrorInfo('读取配置文件异常')
'''
try:
    if os.listdir('./data'):
        shutil.move('./data/'+xls_back, file_path+'/TestResult/'+xls_back)
except BaseException:
    log.getErrorInfo('测试结果拷贝异常')
'''
try:
    config = ConfigParser.ConfigParser()
    config.read(cfgfile)
    config.set('setting','xls','./data/'+now+'.xls')
    config.write(open(cfgfile, 'w'))
except IOError:
    log.getErrorInfo('写入配置文件异常')




