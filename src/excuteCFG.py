#!/usr/bin/env python
# encoding:utf-8
import ConfigParser
#from src import info as log
class ConfigRead(object):
    def __init__(self,file,item,section):
        self.file = file
        self.item = item
        self.section = section

    def CfgRead(self):
        try:
            config = ConfigParser.ConfigParser()
            config.read(self.file)
            #log.getInfo('读取配置文件：'+str(self.file))
            #log.getInfo('读取配置信息：'+'SECTION：'+str(self.item)+' '+'ITEM：'+str(self.section))
            return config.get(self.item,self.section)
        except Exception,e:
            pass

class ConfigWrite(object):
    def __init__(self,ile,item,section,value):
        self.file = file
        self.item = item
        self.section = section
        self.value = value

    def CfgWrite(self):
        try:
            config = ConfigParser.ConfigParser()
            config.read(self.cfgfile)
            config.set(self.section, self.item, self.value)
            #log.getInfo('写入配置文件：' + str(self.file))
            #log.getInfo('写入配置信息：' + 'SECTION：' + str(self.item) + ' ' + 'ITEM：' + str(self.section)+' '+'VALUE：'+str(self.value))
            config.write(open(self.cfgfile, 'w'))
        except Exception, e:
            pass

