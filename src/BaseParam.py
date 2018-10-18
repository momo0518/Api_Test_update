#!/usr/bin/env python
# encoding:utf-8
import excuteCFG
import os
import json
import ApiRequest
import string
import random
from src import info as log

cfgfile = os.path.abspath('.')+'/config.ini'#配置文件位置
try:
    client_id = excuteCFG.ConfigRead(cfgfile, 'access_token', 'CLIENT_ID').CfgRead()
    client_secret = excuteCFG.ConfigRead(cfgfile, 'access_token', 'CLIENT_SECRET').CfgRead()
    url_access_token = excuteCFG.ConfigRead(cfgfile, 'access_token', 'URL').CfgRead()
    grant_type = excuteCFG.ConfigRead(cfgfile, 'access_token', 'GRANT_TYPE').CfgRead()
    sublevel = excuteCFG.ConfigRead(cfgfile, 'departmentid', 'SUBLEVEL').CfgRead()
    url_departmentid = excuteCFG.ConfigRead(cfgfile, 'departmentid', 'URL').CfgRead()
    '''获取用户token'''
    url_token = excuteCFG.ConfigRead(cfgfile, 'token', 'URL').CfgRead()
    username = excuteCFG.ConfigRead(cfgfile, 'token', 'USERNAME').CfgRead()
    password = excuteCFG.ConfigRead(cfgfile, 'token', 'PASSWORD').CfgRead()
    loginmode = excuteCFG.ConfigRead(cfgfile, 'token', 'LOGINMODE').CfgRead()
    service = excuteCFG.ConfigRead(cfgfile, 'token', 'SERVICE').CfgRead()
    client_ip = excuteCFG.ConfigRead(cfgfile, 'token', 'CLIENT_IP').CfgRead()
    content_type = excuteCFG.ConfigRead(cfgfile, 'token', 'CONTENT_TYPE').CfgRead()

except IOError,e:
    log.getErrorInfo('无法获取配置文件信息')

class AscToken(object):
    def __init__(self):
        pass

    def get_acstoken(self):
        data = {'client_id': client_id, 'client_secret': client_secret, 'grant_type': grant_type}
        log.getInfo('获取微服务token参数：'+str(data))
        try:
            response = ApiRequest.ApiTest('POST',url_access_token,data)
        except BaseException,e:
            log.getErrorInfo('无法获取微服务token')
        '''利用json形式获取access_token'''
        log.getInfo('获取正确微服务token：'+str(json.loads(response.apicall()[1])['access_token']))
        return json.loads(response.apicall()[1])['access_token']

    def get_noacstoken(self):
        '''随机伪造access_token'''
        try:
            log.getInfo('获取伪造微服务token')
            return ''.join(random.sample(string.ascii_letters+string.digits,8))+'-'+''.join(random.sample(string.ascii_letters+string.digits,4))\
                        +'-'+''.join(random.sample(string.digits,4))+'-'+''.join(random.sample(string.ascii_letters+string.digits,4))+'-'+''.join(random.sample(string.ascii_letters+string.digits,12))
        except BaseException,e:
            log.getErrorInfo('无法获取伪造微服务token')




'''department类'''
class DepartmentID(object):
    def __init__(self):
        pass
    def get_departmentid(self):
        array_departmentid = []
        access_token = AscToken().get_acstoken()
        data = {'sublevel': sublevel, 'access_token': access_token}
        try:
            response = ApiRequest.ApiTest('GET',url_departmentid,data)
        except BaseException,e:
            log.getErrorInfo('无法获取DepartmentID')
        '''返回请求结果：response.apicall()[1]，共有len(json.loads(response.apicall()[1]))-1个departmentid'''
        for i in range(0,len(json.loads(response.apicall()[1]))-1):
            array_departmentid.append(str(json.loads(response.apicall()[1])[i]['organId']))
            '''随机获取一个正确的departmentid'''
        log.getInfo('获取正确部门ID:'+str(array_departmentid[0]))
        #return array_departmentid[random.randint(0,len(json.loads(response.apicall()[1]))-1)]
        return array_departmentid[0]

    def get_nodepartmentid(self):
        try:
            log.getInfo('获取伪造DepartmentID')
            return ''.join(random.sample(string.ascii_letters + string.digits, 8)) + '-' + ''.join(
                random.sample(string.ascii_letters + string.digits, 4)) \
                   + '-' + ''.join(random.sample(string.digits, 4)) + '-' + ''.join(
                random.sample(string.ascii_letters + string.digits, 4)) + '-' + ''.join(
                random.sample(string.ascii_letters + string.digits, 13))
        except BaseException,e:
            log.getErrorInfo('无法获取伪造DepartmentID')

'''userid类'''
class UserID(object):
    def __init__(self):
        pass

    def get_usrid(self):
        array_usrid = []
        try:
            access_token = AscToken().get_acstoken()
            url_usrid = excuteCFG.ConfigRead(cfgfile, 'userid', 'URL').CfgRead()+ 'root/userinfos?access_token=' + access_token
        except BaseException,e:
            log.getErrorInfo('无法利用微服务token获取用户ID')
        except IOError,e:
            log.getErrorInfo('无法获取配置文件信息')
        data = {}
        try:
            response = ApiRequest.ApiTest('GET', url_usrid, data)
        except BaseException,e:
            log.getErrorInfo('无法获取用户ID')
        for i in range(0,len(json.loads(response.apicall()[1]))-1):
            array_usrid.append(str(json.loads(response.apicall()[1])[i]['userid']))
        '''随机获取一个正确的userid'''
        try:
            return array_usrid[random.randint(0, len(json.loads(response.apicall()[1])) - 1)]
        except BaseException,e:
            log.getErrorInfo('返回用户ID异常')


    def get_nousrid(self):
        try:
            log.getInfo('获取伪造用户ID')
            return ''.join(random.sample(string.ascii_letters + string.digits, 8)) + '-' + ''.join(
                random.sample(string.ascii_letters + string.digits, 4)) \
                   + '-' + ''.join(random.sample(string.digits, 4)) + '-' + ''.join(
                random.sample(string.ascii_letters + string.digits, 4)) + '-' + ''.join(
                random.sample(string.ascii_letters + string.digits, 13))
        except BaseException,e:
            log.getErrorInfo('无法获取伪造用户ID')

'''用户token类'''
class User_Token(object):
    def __init__(self):
        pass
    def get_token(self):
        data = {'username': username, 'password': password, 'loginMode': loginmode, 'service': service}
        header = {'Content-Type': content_type,'client_ip':client_ip}
        try:
            response = ApiRequest.ApiTest('POST',url_token,data)
        except BaseException,e:
            log.getErrorInfo('无法获取用户token')
        return str(json.loads(response.apicall()[1])['access_token'])
        '''判断无法获取token的情况'''
        '''
        if 'error' in str(response.apicall()):
            return None
        else:
            try:
                log.getInfo('用户token：'+str(json.loads(response.apicall()[1])['access_token']))
                return str(json.loads(response.apicall()[1])['access_token'])
            except BaseException,e:
                log.getErrorInfo('返回用户token异常')
        '''

    def get_notoken(self):
        '''伪造用户token'''
        try:
            log.getInfo('获取伪造用户token')
            return 'TGT'+'-'+str(random.randint(1,10000))+'-'+''.join(random.sample(string.ascii_letters + string.digits, 50))+'-'+'cas'
        except BaseException,e:
            log.getErrorInfo('无法获取伪造用户token')