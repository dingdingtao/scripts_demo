'''
Author: dingdingtao
Date: 2020-12-06 15:18:01
LastEditTime: 2021-01-06 15:27:56
Description: pandas
'''
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy

'''
pandas中文教程w3cschool
https://www.w3cschool.cn/hyspo/hyspo-io8d372c.html
'''


def excel():
    datas = []

    '''
    DataFrame.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', 
        float_format=None, columns=None, header=True, index=True, 
        index_label=None, startrow=0, startcol=0, engine=None, 
        merge_cells=True, encoding=None, inf_rep='inf', verbose=True, 
        freeze_panes=None)

    excel_writer：文件路径或现有的ExcelWriter。
    sheet_name：它是指包含DataFrame的工作表的名称。
    na_repr：缺少数据表示形式。
    float_format：这是一个可选参数, 用于格式化浮点数字符串。
    列：指要写入的列。
    header：写出列名。如果给出了字符串列表, 则假定它是列名的别名。
    index：写入索引。
    index_label：引用索引列的列标签。如果未指定, 并且标头和索引为True, 则使用索引名称。如果DataFrame使用MultiIndex, 则应给出一个序列。
    startrow：默认值0。它指向转储DataFrame的左上单元格行。
    startcol：默认值0。它指向转储DataFrame的左上方单元格列。
    engine：这是一个可选参数, 用于写入要使用的引擎, openpyxl或xlsxwriter。
    merge_cells：返回布尔值, 其默认值为True。它将MultiIndex和Hierarchical行写为合并的单元格。
    encoding：这是一个可选参数, 可对生成的excel文件进​​行编码。仅对于xlwt是必需的。
    inf_rep：它也是一个可选参数, 默认值为inf。它通常表示无穷大。
    详细：返回一个布尔值。它的默认值为True。
    它用于在错误日志中显示更多信息。
    Frozen_panes：它也是一个可选参数, 用于指定要冻结的最底部一行和最右边一列。
    '''
    df = pd.DataFrame(datas)
    df.to_excel("test.xlsx")
    pass



def sql():
    '''
    pandas to_sql()定义
    DataFrame.to_sql(name, con, schema=None, 
        if_exists='fail', index=True, index_label=None, 
        chunksize=None, dtype=None, method=None)


    if_exists 参数用于当目标表已经存在时的处理方式，默认是 fail，即目标表存在就失败，另外两个选项是 replace 表示替代原表，即删除再创建，append 选项仅添加数据。

    '''

    '''
    表结构
    dtype={'EMP_ID': sqlalchemy.types.BigInteger(),
       'GENDER': sqlalchemy.types.String(length=20),
       'AGE': sqlalchemy.types.BigInteger(),
       'EMAIL':  sqlalchemy.types.String(length=50),
       'PHONE_NR':  sqlalchemy.types.String(length=50),
       'EDUCATION':  sqlalchemy.types.String(length=50),
       'MARITAL_STAT':  sqlalchemy.types.String(length=50),
       'NR_OF_CHILDREN': sqlalchemy.types.BigInteger()
       }
    '''

    engine = create_engine('mysql+pymysql://user:password@localhost/stonetest?charset=utf8')
    
    '''
    读数据
    '''
    df = pd.read_sql('emp_master', engine)
    

    '''
    写数据
    '''
    df.to_sql('emp_backup', engine)
    
    pass



def cvs():
    pass

