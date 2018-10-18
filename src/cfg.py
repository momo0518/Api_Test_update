#!/usr/bin/env python
# encoding:utf-8
import ConfigParser
from src import info as log
class ConfigRead():
    def CfgRead(self,cfgfile,item,section):
        try:
            self.cfgfile = cfgfile
            self.item = item
            self.section = section
            config = ConfigParser.ConfigParser()
            config.read(cfgfile)
            return config.get(item,section)
        except Exception,e:
            log.getErrorInfo("类型问题 %s", e)

    def CfgWrite(self,cfgfile,section,item,value):
        try:
            self.cfgfile = cfgfilea
            self.item = item
            self.section = section
            self.value = value 
            config = ConfigParser.ConfigParser()
            config.read(cfgfile)
            config.set(section,item,value)
            config.write(open(cfgfile,'w'))
        except Exception, e:
            log.getErrorInfo("类型问题 %s", e)



