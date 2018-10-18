#!/usr/bin/env python
# encoding:utf-8
import requests
import src.info as log
class APITest():
    def apicall(self, method, url, data):
        result = ''
        if method == 'GET':
            if data != '':
                try:
                    result = requests.get(url, data,timeout=10)
                    log.getDebug(result.status_code)
                    log.getDebug(result.content)
                    log.getInfo(result.status_code)
                    log.getInfo(result.content)
                    return result.status_code, result.content
                except requests.ConnectTimeout,e:
                    log.getErrorInfo("错误信息：" + str(e))
                except requests.RequestException,e:
                    log.getErrorInfo("错误信息：" + str(e))
            else:
                try:
                    result = requests.get(url,timeout=10)
                    log.getDebug(result.status_code)
                    log.getDebug(result.content)
                    log.getInfo(result.status_code)
                    log.getInfo(result.content)
                    return result.status_code, result.content
                except requests.ConnectTimeout,e:
                    log.getErrorInfo("错误信息：" + str(e))
                except requests.RequestException,e:
                    log.getErrorInfo("错误信息：" + str(e))
        if method == 'POST':
            if data != '':
                try:
                    result = requests.post(url, data,timeout=10)
                    log.getDebug(result.status_code)
                    log.getDebug(result.content)
                    log.getInfo(result.status_code)
                    log.getInfo(result.content)
                    return result.status_code,result.content
                except requests.ConnectTimeout,e:
                    return e
                    log.getErrorInfo("错误信息：" + str(e))
                except requests.RequestException,e:
                    log.getErrorInfo("错误信息：" + str(e))

            else:
                try:
                    result = requests.post(url,timeout=10)
                    log.getDebug(result.status_code)
                    log.getDebug(result.content)
                    log.getInfo(result.status_code)
                    log.getInfo(result.content)
                    return result.status_code, result.content
                except requests.ConnectTimeout,e:
                    log.getErrorInfo("错误信息：" + str(e))
                except requests.RequestException,e:
                    log.getErrorInfo("错误信息：" + str(e))
        #未做json转换
        return result
