#!/usr/bin/env python
# encoding:utf-8
import requests
#from src import info as log
class ApiTest(object):
    def __init__(self,method,url,data):
        self.method = method
        self.url = url
        self.data = data
    def apicall(self):
        result = ''
        if self.method == 'GET':
            if self.data != '':
                try:
                    result = requests.get(self.url, self.data,timeout=5)
                    return result.status_code, result.content
                except requests.HTTPError:
                    pass
                    #log.getErrorInfo('GET方法请求异常，请重试')
                except requests.ConnectionError:
                    pass
                    #log.getErrorInfo('连接异常，请检查测试用例或网络连接状态')
                except SyntaxError,e:
                    pass
                    #log.getErrorInfo(e)
            else:
                try:
                    result = requests.get(self.url,timeout=5)
                    return result.status_code,result.content
                except requests.HTTPError:
                    pass
                    #log.getErrorInfo('GET方法请求异常，请重试')
                except requests.ConnectionError:
                    pass
                    #log.getErrorInfo('连接异常，请检查测试用例或网络连接状态')
                except SyntaxError,e:
                    pass
                    #log.getErrorInfo(e)

        if self.method == 'POST':
            if self.data != '':

                '''解决连接keepalive'''
                '''
                seesion = resquest.session()
                session.post(url,data)
                '''
                try:
                    result = requests.post(self.url, self.data,timeout=5)
                    return result.status_code, result.content
                except requests.HTTPError:
                    pass
                    #log.getErrorInfo('GET方法请求异常，请重试')
                except requests.ConnectionError:
                    pass
                    #log.getErrorInfo('连接异常，请检查测试用例或网络连接状态')
                except SyntaxError,e:
                    pass
                    #log.getErrorInfo(e)
            else:
                try:
                    result = requests.post(self.url,timeout=5)
                    return result.status_code, result.content
                except requests.HTTPError:
                    pass
                    #log.getErrorInfo('GET方法请求异常，请重试')
                except requests.ConnectionError:
                    pass
                    #log.getErrorInfo('连接异常，请检查测试用例或网络连接状态')
                except SyntaxError,e:
                    pass
                    #log.getErrorInfo(e)

        #未做json转换
        return result
