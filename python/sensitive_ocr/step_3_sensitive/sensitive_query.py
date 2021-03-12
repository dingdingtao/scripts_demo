'''
Author: dingdingtao
Date: 2020-12-04 16:31:17
LastEditTime: 2021-03-12 19:06:14
LastEditors: dingdingtao
Description: 敏感词查询
'''
import requests
import pandas as pd
import json
import time
import xlrd
import xlwt
import os
import sys
import pymysql
import threading
from step_3_sensitive import toent_handle
from tqdm import tqdm

'''
引入data_handle模块查询数据
'''
CURRENT_PATH = os.path.dirname(__file__)
sys.path.append(os.path.join(CURRENT_PATH,"../handle"))
import data_handle as dh


cookies = "浏览器cookies"
url = "url"


'''
description: 
param {*} text
return {*}
'''
def request_datas(c, text):
    data = {
        """请求数据"""
    }
    return data


'''
description: 
param {*} c
param {*} t
return {*}
'''
def request_header(c,t):
    header = {
        """request_header"""
    }
    return header



'''
description: 敏感词测试
param {*} text 测试的敏感词
param {*} toent
return {*} 测试结果-命中的敏感词
'''
def query(c, text, t):
    
    data = request_datas(c, text)
    header = request_header(cookies, t)
    try:
        r = requests.post(url, headers=header, data=json.dumps(data)).json()
    except json.decoder.JSONDecodeError:
        time.sleep(2)
        r = requests.post(url, headers=header, data=json.dumps(data)).json()

    return r



'''
description: 批量查询数据处理 
param {*} 查询结果
return {*} 去重之后的查询结果
'''
def query_handle(res):
    handled_res = {}
    for k,v in res.items():
        if k == 'data':
            handled_res[k] = None
            continue
        handled_res[k] = v
    try:
        if None != res['data']:
            res['data'] = res['data'][1:]
            handled_res['data'] = []
            item = {}

            for data in res['data']:
                flag = False
                for i,r in enumerate(handled_res['data']):
                    if r[0]['content'] == data['content']:
                        flag = True
                        handled_res['data'][i].append(data)
                        break
                if not flag:
                        handled_res['data'].append([data])
    except:
        if 4001001 == res['code']:
            print(res['msg'])
        else:
            print("error")
        pass
    
    return handled_res




'''
description: 敏感词查询
param {*} sensitive_word (id,测试敏感词,ocr敏感词)
param {*} t toent
param {*} thread 线程名
return {*}
'''
def sensitive_test(cf, sensitive_word, t, thread):

    connection = pymysql.connect(host=dh.HOST, port=dh.PORT, user=dh.USER,password=dh.PASS, db=dh.DB, charset=dh.CODE)
    cursor = connection.cursor()


    '''
    description: 更新数据语句
    param {*} word
    param {*} distinct
    param {*} flag
    param {*} thread
    return {*}
    '''
    def query_route(word, distinct, flag, thread):
        sql = """update {table} set word_rs={value} where word={v}""".format(table=cf['table_name'], value=word, v=distinct)
        if flag:
            sql = """update {table} set ocr_word_rs={value} where ocr_word={v}""".format(table=cf['table_name'], value=word, v=distinct)
        cursor.execute(sql)
        connection.commit()


    '''
    description: 数据查询接口
    param {*} words
    param {*} distinct
    param {*} flag
    return {*}
    '''
    def query_result_handle(words, distinct, flag):
        try:
            with tqdm(words['data'], desc="updata progress", ncols=80) as t:
                for data in t:
                    key = []
                    for d in data:
                        key.append(d['keyword']) 
                    nn = 0
                    for k in key:
                        if k == 'None' or k == None:
                            nn = nn + 1
                    if nn == len(key):
                        key=['None']
                    try:
                        keyword = connection.escape(str(key))
                    except TypeError:
                        keyword = connection.escape("None")
                    distinct_field = connection.escape(data[0]['content'])
                    if "NULL" != distinct_field:
                        query_route(keyword, distinct_field, flag, thread)
        except Exception as e:
            print(e)
            t.close()
        t.close()
    

    '''
    description: 
    param {*} words
    param {*} ids
    param {*} flag
    return {*}
    '''
    def do_test(c, words, ids, flag):
        if None != words:
            query_word = query_handle(query(c, words, t))
            if query_word['code'] == 0:
                query_result_handle(query_word, ids, flag)
            return query_word['code']
        return 0
                
                
    ids = sensitive_word[0]
    word = sensitive_word[1]
    ocr_word = sensitive_word[2]
    word_code = do_test(cf, word, ids, False)
    ocr_word_code = do_test(cf, ocr_word, ids, True)

    cursor.close()
    connection.close()
    return (word_code,ocr_word_code)


'''
Description: 
param {*} thread 线程名
return {*}
'''
def sensitive(config, thread):
    datas = dh.fetchall_data_sensitive(config)
    toent = toent_handle.request_toent()
    code = 200
    '''
    description: 
    param {*} datas
    return {*}
    '''
    def pack_datas(datas):
        tid, tword, tocr_word = [], [], []
        for x in datas:
            tid.append(x[0])
            if None == x[1] or "" == x[1]:
                tword.append("None")
            else:
                tword.append(x[1])
            if None == x[2] or "" == x[2]:
                tocr_word.append("None")
            else:
                tocr_word.append(x[2])
        return (tid,tword,tocr_word)
    
    if 0 != len(datas):
        try:
            with tqdm([list(datas)[i:i + 500] for i in range(0, len(list(datas)), 500)], desc="sensitive progress", ncols=80) as t:
                for n_list in t:
                    word = pack_datas(n_list)
                    code = sensitive_test(config, word, toent, thread)
                    if 401 == code[0] or 401 == code[1]:
                        toent = toent_handle.request_toent()
                        code = sensitive_test(word, toent, thread)
        except Exception as e:
            t.close()
            print(e)
            return False
        t.close()
    else:
        print("无结果.")
        return False
    return True



def run(c):
    has_sen = False
    try:
        print("敏感词查询.")
        has_sen = sensitive(c, "Thread")
        # for i in range(3):
        #     threading.Thread(target=sensitive,args=("Thread-" + str(i + 1),)).start()
        #     time.sleep(2)
        print("查询完成.")
        return has_sen
    except Exception as e:
        print(e)
        return has_sen


if __name__ == "__main__":
    run()