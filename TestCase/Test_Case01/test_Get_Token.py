#!/usr/bin/env python
# encoding:utf-8
import sys
sys.path.append('./venv/lib/python2.7/site-packages')
import unittest
from src import excuteCFG
from src import ApiRequest
#from src import info as log
import random
import string
    ##TODO:client_ip与content_type暂未纳入测试用例中

try:
    cfgfile = '/Users/fanglujie/Documents/Project/Api_Test/config.ini'
    username = excuteCFG.ConfigRead(cfgfile, 'GET_TOKEN', 'username').CfgRead()
    url = excuteCFG.ConfigRead(cfgfile, 'GET_TOKEN', 'url').CfgRead()
    password = excuteCFG.ConfigRead(cfgfile, 'GET_TOKEN', 'password').CfgRead()
    loginMode = excuteCFG.ConfigRead(cfgfile, 'GET_TOKEN', 'loginMode').CfgRead()
    service = excuteCFG.ConfigRead(cfgfile, 'GET_TOKEN', 'service').CfgRead()
    content_type = excuteCFG.ConfigRead(cfgfile, 'GET_TOKEN', 'content-type').CfgRead()
    client_ip = excuteCFG.ConfigRead(cfgfile, 'GET_TOKEN', 'client_ip ').CfgRead()
    header = {'Content-Type': content_type, 'client_ip': client_ip}
    data = {'username': username, 'password': password, 'loginMode': loginMode, 'service': service}
except IOError, e:
    print '读取配置文件异常'
    #log.getErrorInfo('读取配置文件异常')

class Get_Token(unittest.TestCase):

    def setUp(self):
        pass
        '''正向用例'''
    def test_get_token(self):
        response = ApiRequest.ApiTest('POST', url, data)
        self.assertIn('success',response.apicall()[1])
        '''url异常情况'''
    def test_get_token_ex_url(self):
        ex_url = url + 'exception'
        response = ApiRequest.ApiTest('POST', ex_url, data)
        self.assertIn('error',response.apicall()[1])
        '''username异常情况'''
    def test_get_token_ex_username(self):
        ex_username = username + 'exception'
        ex_data = {'username': ex_username, 'password': password, 'loginMode': loginMode, 'service': service}
        response = ApiRequest.ApiTest('POST', url, ex_data)
        self.assertIn('error', response.apicall()[1])
        '''username为空情况'''
    def test_get_token_null_username(self):
        ex_username = ''
        ex_data = {'username': ex_username, 'password': password, 'loginMode': loginMode, 'service': service}
        response = ApiRequest.ApiTest('POST', url, ex_data)
        self.assertIn('error', response.apicall()[1])
        '''password异常情况'''
    def test_get_token_ex_passwd(self):
        ex_password = password + 'exception'
        ex_data = {'username': username, 'password': ex_password, 'loginMode': loginMode, 'service': service}
        response = ApiRequest.ApiTest('POST', url, ex_data)
        self.assertIn('error', response.apicall()[1])
        '''password为空情况'''
    def test_get_token_null_passwd(self):
        ex_password = ''
        ex_data = {'username': username, 'password': ex_password, 'loginMode': loginMode, 'service': service}
        response = ApiRequest.ApiTest('POST', url, ex_data)
        self.assertIn('error', response.apicall()[1])
        '''loginMode异常情况'''
    def test_get_token_ex_loginMode(self):
        ex_loginMode = random.randint(0,100)
        ex_data = {'username': username, 'password': password, 'loginMode': ex_loginMode, 'service': service}
        response = ApiRequest.ApiTest('POST', url, ex_data)
        self.assertIn('error', response.apicall()[1])
        '''loginMode为空情况'''
    def test_get_token_null_loginMode(self):
        ex_loginMode = ''
        ex_data = {'username': username, 'password': password, 'loginMode': ex_loginMode, 'service': service}
        response = ApiRequest.ApiTest('POST', url, ex_data)
        self.assertIn('error', response.apicall()[1])
        '''service异常情况'''
    def test_get_token_ex_service(self):
        ex_service = service + 'exception'
        ex_data = {'username': username, 'password': password, 'loginMode': loginMode, 'service':ex_service}
        response = ApiRequest.ApiTest('POST', url, ex_data)
        self.assertIn('error', response.apicall()[1])
        '''service为空情况'''
    def test_get_token_null_service(self):
        ex_service = ''
        ex_data = {'username': username, 'password': password, 'loginMode': loginMode, 'service':ex_service}
        response = ApiRequest.ApiTest('POST', url, ex_data)
        self.assertIn('error', response.apicall()[1])

    def tearDown(self):
        pass


if __name__ =="__main__":
    unittest.main()