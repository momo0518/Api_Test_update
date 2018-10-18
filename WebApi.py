#!/usr/bin/env python
# encoding:utf-8
import sys
sys.path.append('./venv/lib/python2.7/site-packages')
import unittest
import os
from src import info as log
from src import excel as excel
import xlwt
from src import ApiRequest
from src import excuteCFG
from src import BaseParam
import time
import shutil
from src import reload

    #TODO:增加新增测试用例功能
    #TODO：利用unittest重新编写

#读取配置文件信息
cfgfile = os.path.abspath('.')+'/config.ini'#配置文件位置
try:
    XLS = excuteCFG.ConfigRead(cfgfile, 'setting', 'XLS').CfgRead()
    url = int(excuteCFG.ConfigRead(cfgfile, 'setting', 'URL').CfgRead())
    method = int(excuteCFG.ConfigRead(cfgfile, 'setting', 'METHOD').CfgRead())
    data = int(excuteCFG.ConfigRead(cfgfile, 'setting', 'DATA').CfgRead())
    index = int(excuteCFG.ConfigRead(cfgfile, 'setting', 'INDEX').CfgRead())
    status_code = int(excuteCFG.ConfigRead(cfgfile, 'setting', 'STATUS_CODE').CfgRead())
    result = int(excuteCFG.ConfigRead(cfgfile, 'setting', 'RESULT').CfgRead())
    tag = int(excuteCFG.ConfigRead(cfgfile, 'setting', 'TAG').CfgRead())
    row = excel.get_rows(XLS,0)#表行数
except IOError,e:
    log.getErrorInfo(e)


class APIGetAdList(unittest.TestCase):
    def setUp(self):
        log.getInfo('初始化测试数据')

    def test_circle(self):
        log.getInfo('开始执行测试')
        for i in range(1, row):
            try:
                URL = str(excel.get_content(XLS, index, i, url))[6:].replace("'", "")
                METHOD = str(str(excel.get_content(XLS, index, i, method))[6:].replace("'", ""))
                DATA = str(excel.get_content(XLS, index, i, data))[7:-1]
                '''加入标签，便于定位传参'''
                TAG = str(excel.get_content(XLS,index,i,tag))
            except IOError,e:
                log.getErrorInfo('NO SUCH DIRECTORY'+e)
            except BaseException,e:
                log.getErrorInfo(e)

                '''获取组织结构列表get_orglist'''
            if 'get_orglist' in TAG:
                URL_RE = URL.replace('{access_token}', BaseParam.AscToken().get_acstoken())
                try:
                    response = ApiRequest.ApiTest(METHOD, URL_RE, eval(DATA))
                except BaseException, e:
                    log.getErrorInfo(e)
                try:
                    style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center')
                    '''写入状态返回码'''
                    excel.input_content(XLS, index, i, status_code, response.apicall()[0], style)
                    '''补充增加实际返回结果,解决字符编码问题'''
                    excel.input_content(XLS, index, i, result, response.apicall()[1].decode('utf-8'), style)
                except IOError, e:
                    log.getErrorInfo('NO SUCH DIRECTORY')
                except BaseException, e:
                    log.getErrorInfo(e)


                '''获取组织结构列表异常情况get_orglist_exception'''
            elif 'get_orglist_exception' in TAG:
                pass


                '''刷新用户token:ssotoken_refresh'''
            elif 'ssotoken_refresh' in TAG:
                URL_RE = URL.replace('{token}', BaseParam.User_Token().get_token())
                try:
                    response = ApiRequest.ApiTest(METHOD, URL_RE, eval(DATA))
                except BaseException, e:
                    log.getErrorInfo(e)
                try:
                    style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center')
                    '''写入状态返回码'''
                    excel.input_content(XLS, index, i, status_code, response.apicall()[0], style)
                    '''补充增加实际返回结果,解决字符编码问题'''
                    excel.input_content(XLS, index, i, result, response.apicall()[1].decode('utf-8'), style)
                except IOError, e:
                    log.getErrorInfo('NO SUCH DIRECTORY')
                except BaseException, e:
                    log.getErrorInfo(e)


                '''获取用户信息：get_userinfo'''
            elif 'get_userinfo' in TAG:
                DATA_RE = DATA.replace('{token}', BaseParam.User_Token().get_token())
                try:
                    response = ApiRequest.ApiTest(METHOD, URL, eval(DATA_RE))
                except BaseException, e:
                    log.getErrorInfo(e)
                try:
                    style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center')
                    '''写入状态返回码'''
                    excel.input_content(XLS, index, i, status_code, response.apicall()[0], style)
                    '''补充增加实际返回结果,解决字符编码问题'''
                    excel.input_content(XLS, index, i, result, response.apicall()[1].decode('utf-8'), style)
                except IOError, e:
                    log.getErrorInfo('NO SUCH DIRECTORY')
                except BaseException, e:
                    log.getErrorInfo(e)

                '''获取部门列表:get_departmentlist'''
            elif 'get_departmentlist' in TAG:
                URL_RE = (URL.replace('{access_token}', BaseParam.AscToken().get_acstoken())).replace('{departmentid}',BaseParam.DepartmentID().get_departmentid())
                try:
                    response = ApiRequest.ApiTest(METHOD, URL_RE, eval(DATA))
                except BaseException, e:
                    log.getErrorInfo(e)
                try:
                    style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center')
                    '''写入状态返回码'''
                    excel.input_content(XLS, index, i, status_code, response.apicall()[0], style)
                    '''补充增加实际返回结果,解决字符编码问题'''
                    excel.input_content(XLS, index, i, result, response.apicall()[1].decode('utf-8'), style)
                except IOError, e:
                    log.getErrorInfo('NO SUCH DIRECTORY')
                except BaseException, e:
                    log.getErrorInfo(e)


                '''获取部门详情：get_departmentdetail'''
            elif 'get_departmentdetail' in TAG:
                URL_RE = (URL.replace('{access_token}', BaseParam.AscToken().get_acstoken())).replace('{departmentid}',BaseParam.DepartmentID().get_departmentid())
                try:
                    response = ApiRequest.ApiTest(METHOD, URL_RE, eval(DATA))
                except BaseException, e:
                    log.getErrorInfo(e)
                try:
                    style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center')
                    '''写入状态返回码'''
                    excel.input_content(XLS, index, i, status_code, response.apicall()[0], style)
                    '''补充增加实际返回结果,解决字符编码问题'''
                    excel.input_content(XLS, index, i, result, response.apicall()[1].decode('utf-8'), style)
                except IOError, e:
                    log.getErrorInfo('NO SUCH DIRECTORY')
                except BaseException, e:
                    log.getErrorInfo(e)


                '''获取人员列表:get_uesrlist'''
            elif 'get_userlist' in TAG:
                URL_RE = (URL.replace('{access_token}', BaseParam.AscToken().get_acstoken())).replace('{departmentid}',BaseParam.DepartmentID().get_departmentid())
                try:
                    response = ApiRequest.ApiTest(METHOD, URL_RE, eval(DATA))
                except BaseException, e:
                    log.getErrorInfo(e)
                try:
                    style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center')
                    '''写入状态返回码'''
                    excel.input_content(XLS, index, i, status_code, response.apicall()[0], style)
                    '''补充增加实际返回结果,解决字符编码问题'''
                    excel.input_content(XLS, index, i, result, response.apicall()[1].decode('utf-8'), style)
                except IOError, e:
                    log.getErrorInfo('NO SUCH DIRECTORY')
                except BaseException, e:
                    log.getErrorInfo(e)


                '''获取人员详情:get_userdetail'''
            elif 'get_userdetail' in TAG:
                URL_RE = (URL.replace('{access_token}', BaseParam.AscToken().get_acstoken())).replace('{userid}',BaseParam.UserID().get_usrid())
                try:
                    response = ApiRequest.ApiTest(METHOD, URL_RE, eval(DATA))
                except BaseException, e:
                    log.getErrorInfo(e)
                try:
                    style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center')
                    '''写入状态返回码'''
                    excel.input_content(XLS, index, i, status_code, response.apicall()[0], style)
                    '''补充增加实际返回结果,解决字符编码问题'''
                    excel.input_content(XLS, index, i, result, response.apicall()[1].decode('utf-8'), style)
                except IOError, e:
                    log.getErrorInfo('NO SUCH DIRECTORY')
                except BaseException, e:
                    log.getErrorInfo(e)

                '''增量同步'''
            elif 'sync' in TAG:
                timestamp = str(int(time.time()))
                URL_RE = ((URL.replace('{access_token}',BaseParam.AscToken().get_acstoken())).replace('{departmentid}',BaseParam.DepartmentID().get_departmentid())).replace('{timestamp}',timestamp)
                try:
                    response = ApiRequest.ApiTest(METHOD, URL_RE, eval(DATA))
                except BaseException, e:
                    log.getErrorInfo(e)
                try:
                    style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center')
                    '''写入状态返回码'''
                    excel.input_content(XLS, index, i, status_code, response.apicall()[0], style)
                    '''补充增加实际返回结果,解决字符编码问题'''
                    excel.input_content(XLS, index, i, result, response.apicall()[1].decode('utf-8'), style)
                except IOError, e:
                    log.getErrorInfo('NO SUCH DIRECTORY')
                except BaseException, e:
                    log.getErrorInfo(e)



                '''发送消息至个人'''
            elif 'msg2sig' in TAG:
                URL_RE = URL + BaseParam.UserID().get_usrid()
                MSG = DATA.decode("unicode_escape").encode("utf8")
                DATA_RE = {'content':MSG,'access_token':BaseParam.AscToken().get_acstoken()}
                try:
                    response = ApiRequest.ApiTest(METHOD,URL_RE,DATA_RE)
                except BaseException, e:
                    log.getErrorInfo(e)

                try:
                    style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center')
                    '''写入状态返回码'''
                    excel.input_content(XLS, index, i, status_code, response.apicall()[0], style)
                    '''补充增加实际返回结果,解决字符编码问题'''
                    excel.input_content(XLS, index, i, result, response.apicall()[1].decode('utf-8'), style)
                except IOError, e:
                    log.getErrorInfo('NO SUCH DIRECTORY')
                except BaseException, e:
                    log.getErrorInfo(e)


                '''发送消息至多人'''
            elif 'msg2multi' in TAG:
                URL_RE = URL + BaseParam.UserID().get_usrid()+','+BaseParam.UserID().get_usrid()
                MSG = DATA.decode("unicode_escape").encode("utf8")
                DATA_RE = {'content':MSG,'access_token':BaseParam.AscToken().get_acstoken()}
                try:
                    response = ApiRequest.ApiTest(METHOD,URL_RE,DATA_RE)
                except BaseException, e:
                    log.getErrorInfo(e)
                try:
                    style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center')
                    '''写入状态返回码'''
                    excel.input_content(XLS, index, i, status_code, response.apicall()[0], style)
                    '''补充增加实际返回结果,解决字符编码问题'''
                    excel.input_content(XLS, index, i, result, response.apicall()[1].decode('utf-8'), style)
                except IOError, e:
                    log.getErrorInfo('NO SUCH DIRECTORY')
                except BaseException, e:
                    log.getErrorInfo(e)

                '''发送消息至部门'''
            elif 'msg2department' in TAG:
                URL_RE = URL + BaseParam.DepartmentID().get_departmentid()
                MSG = DATA.decode("unicode_escape").encode("utf8")
                DATA_RE = {'content':MSG,'access_token':BaseParam.AscToken().get_acstoken()}
                try:
                    response = ApiRequest.ApiTest(METHOD,URL_RE,DATA_RE)
                except BaseException, e:
                    log.getErrorInfo(e)
                try:
                    style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center')
                    '''写入状态返回码'''
                    excel.input_content(XLS, index, i, status_code, response.apicall()[0], style)
                    '''补充增加实际返回结果,解决字符编码问题'''
                    excel.input_content(XLS, index, i, result, response.apicall()[1].decode('utf-8'), style)
                except IOError, e:
                    log.getErrorInfo('NO SUCH DIRECTORY')
                except BaseException, e:
                    log.getErrorInfo(e)



                '''发送消息至多部门'''
            elif 'msg2mutidepartment' in TAG:
                URL_RE = URL + BaseParam.DepartmentID().get_departmentid()+','+BaseParam.DepartmentID().get_departmentid()
                MSG = DATA.decode("unicode_escape").encode("utf8")
                DATA_RE = {'content': MSG, 'access_token': BaseParam.AscToken().get_acstoken()}
                try:
                    response = ApiRequest.ApiTest(METHOD, URL_RE, DATA_RE)
                except BaseException, e:
                    log.getErrorInfo(e)
                try:
                    style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center')
                    '''写入状态返回码'''
                    excel.input_content(XLS, index, i, status_code, response.apicall()[0], style)
                    '''补充增加实际返回结果,解决字符编码问题'''
                    excel.input_content(XLS, index, i, result, response.apicall()[1].decode('utf-8'), style)
                except IOError, e:
                    log.getErrorInfo('NO SUCH DIRECTORY')
                except BaseException, e:
                    log.getErrorInfo(e)




            else:

                response = ApiRequest.ApiTest(METHOD,URL,eval(DATA))

                '''返回status_code与content'''
                '''当网络连接出现问题时，测试无法继续执行'''
                try:
                    style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center')
                    '''写入状态返回码'''
                    excel.input_content(XLS, index, i, status_code,response.apicall()[0], style)
                    '''补充增加实际返回结果,解决字符编码问题'''
                    excel.input_content(XLS, index, i, result,response.apicall()[1].decode('utf-8'), style)
                except IOError,e:
                    log.getErrorInfo('NO SUCH DIRECTORY')
                except BaseException,e:
                    log.getErrorInfo(e)




    def tearDown(self):
        xls_back = excuteCFG.ConfigRead(cfgfile, 'setting', 'xls_back').CfgRead()
        shutil.move(XLS, './TestResult/'+xls_back)
        log.getInfo('测试结束')





if __name__ == "__main__":
    unittest.main()



