'''
Author: dingdingtao
Date: 2020-12-06 14:19:17
LastEditTime: 2020-12-08 22:20:52
Description: xlrd模块使用方式
'''
import xlrd

def xlrd_usage():
    
    '''
    例子:
    fname = "sample.xls"
    bk = xlrd.open_workbook(fname)
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("Sheet1")
    except:
        print "no sheet in %s named Sheet1" % fname
        return None
    nrows = sh.nrows
    ncols = sh.ncols
    print "nrows %d, ncols %d" % (nrows,ncols)
    
    cell_value = sh.cell_value(1,1)
    print cell_value
    
    row_list = []
    for i in range(1,nrows):
        row_data = sh.row_values(i)
        row_list.append(row_data)
    '''
    xlrd.open_workbook()