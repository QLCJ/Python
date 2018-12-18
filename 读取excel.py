# !/usr/bin/env python
# -*- coding:utf-8 -*-

import xlrd

#打开文件（路径）
ex = xlrd.open_workbook('U:\\2016级信息工程成绩信息.xls')

#打开表格文件的第一张表  索引从0开始
sheet = ex.sheets()[0]

#获取第一张表格函数值赋值给nrows
nrows = sheet.nrows

#用for遍历所有行数
for i in range (nrows):
    print(sheet.row_values(i))       #打印所有遍历到的行数的内容

#打印第一张表格的第二列所有内容
#print(sheet.col_values(1))