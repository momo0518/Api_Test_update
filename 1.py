#!/usr/bin/env python
# encoding:utf-8
from src import ApiRequest
from src import excuteCFG
import time
cfgfile = '/Users/fanglujie/Documents/Project/Api_Test/config.ini'
username = excuteCFG.ConfigRead(cfgfile, 'GET_TOKEN', 'username').CfgRead()
url = excuteCFG.ConfigRead(cfgfile, 'GET_ACCESS_TOKEN', 'url').CfgRead()
password = excuteCFG.ConfigRead(cfgfile, 'GET_TOKEN', 'password').CfgRead()
loginMode = excuteCFG.ConfigRead(cfgfile, 'GET_TOKEN', 'loginMode').CfgRead()
service = excuteCFG.ConfigRead(cfgfile, 'GET_TOKEN', 'service').CfgRead()
content_type = excuteCFG.ConfigRead(cfgfile, 'GET_TOKEN', 'content-type').CfgRead()
client_ip = excuteCFG.ConfigRead(cfgfile, 'GET_TOKEN', 'client_ip ').CfgRead()

client_id = excuteCFG.ConfigRead(cfgfile, 'GET_ACCESS_TOKEN', 'client_id').CfgRead()
client_secret = excuteCFG.ConfigRead(cfgfile, 'GET_ACCESS_TOKEN', 'client_secret').CfgRead()
grant_type = excuteCFG.ConfigRead(cfgfile, 'GET_ACCESS_TOKEN', 'grant_type').CfgRead()
data = {'client_id': client_id, 'client_secret': client_secret, 'grant_type': grant_type}


print client_id
print client_secret
print grant_type
print url

response = ApiRequest.ApiTest('POST', url, data)
print response.apicall()[1]

