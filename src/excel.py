# !/usr/bin/python
 # -*- coding: UTF-8 -*-
from src import info as log
import xlrd
import xlwt
from xlutils.copy import copy
from xlwt import Style
#获取行数
def get_rows(path,index):
    try:
        workbook = xlrd.open_workbook(path, on_demand=True)
        return workbook.sheet_by_index(index).nrows
    except Exception,e:
        log.getErrorInfo(e)
#获取列数
def get_cols(path,index):
    try:
        workbook = xlrd.open_workbook(path, on_demand=True)
        return workbook.sheet_by_index(index).ncols
    except Exception,e:
        log.getErrorInfo(e)
#获取行内容
def get_row_content(path,index,x):
    try:
        workbook = xlrd.open_workbook(path, on_demand=True)
        return workbook.sheet_by_index(index).row_values(x)
    except Exception,e:
        log.getErrorInfo(e)
#获取列内容
def get_col_content(path,index,y):
    try:
        workbook = xlrd.open_workbook(path, on_demand=True)
        return workbook.sheet_by_index(index).col_values(y)
    except Exception,e:
        log.getErrorInfo(e)
#获取制定内容
def get_content(path,index,x,y):
    try:
        workbook = xlrd.open_workbook(path, on_demand=True)
        return workbook.sheet_by_index(index).cell(x,y)
    except Exception,e:
        log.getErrorInfo(e)
#写入指定内容

def input_content(path,index,x, y, str, styl=Style.default_style):
    try:
        workbook = xlrd.open_workbook(path, on_demand=True)
        workbook_new = copy(workbook)
        ws = workbook_new.get_sheet(index)
        ws.write(x, y, str, styl)
        workbook_new.save(path)
    except Exception,e:
        log.getErrorInfo(e)



