'''
Author: dingdingtao
Date: 2020-12-28 09:42:52
LastEditTime: 2021-03-12 18:48:09
LastEditors: dingdingtao
Description: 入口程序
'''
import pymysql
import datetime
import os

from handle import data_handle as dh
from step_0_init import init as step0
from step_1_data import get_data_mysql as step1
from step_2_ocr import ocr_handle as step2
from step_3_sensitive import sensitive_query as step3
from step_4_export import export_result as step4
from step_5_sendmail import sendmail as step5

'''
description: 查询所有配置信息
param {*}
return {*} 元组配置信息
'''
def get_all_configs():
    sql = """
        select {fields} from {table} where ext1='1' ORDER BY RAND()
    """.format(fields=",".join(dh.CONFIG_TABLE['tabledtype'].keys()), table=dh.CONFIG_TABLE['tablename'])
    connection = pymysql.connect(host=dh.HOST, port=dh.PORT, user=dh.USER,password=dh.PASS, db=dh.DB, charset=dh.CODE)
    cursor = connection.cursor()
    cursor.execute(sql)
    configs = cursor.fetchall()
    cursor.close()
    connection.close()
    return configs


'''
description: 配置信息封装成对象
param {*} datas 查询配置表结果
return {*} 封装结果
'''
def pack_datas(datas):
    config = {}
    for i,k in enumerate(dh.CONFIG_TABLE['tabledtype'].keys()):
        config[k] = datas[i]
    return config


'''
description: 输出分隔符
param {*} 配置信息
return {*} 
'''
def sep_line(c):
    sep = """

    
    {name}
    ---------------------------------
    """.format(name=c['sql_filename'])
    print(sep)
    
    
'''
description: 分步执行
param {*}
return {*}
'''
def run():
    runtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    configs = get_all_configs()
    dh.start_jvm()
    for config in configs:
        issucess = 'False'
        try:
            realtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            pack_config = pack_datas(config)
            sep_line(pack_config)
            table = dh.OUT_TABLE
            
            '''初始化'''
            step = "step0"
            step_realtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            fs0 = step0.run(table, pack_config)
            step_finishtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            dh.record(pack_config, runtime, step_realtime, step_finishtime, step, fs0)
            if not fs0:
                continue
            
            '''查询数据、存储数据'''
            step = "step1"
            step_realtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            fs1 = step1.run(table, pack_config)
            step_finishtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            dh.record(pack_config, runtime, step_realtime, step_finishtime, step, fs1)
            if not fs1:
                continue
            
            '''ocr转换、ocr识别'''
            step = "step2"
            step_realtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            fs2 = step2.run(pack_config)
            step_finishtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            dh.record(pack_config, runtime, step_realtime, step_finishtime, step, fs2)
            if not fs2:
                continue
            
            '''敏感词查询'''
            step = "step3"
            step_realtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            fs3 = step3.run(pack_config)
            step_finishtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            dh.record(pack_config, runtime, step_realtime, step_finishtime, step, fs3)
            if not fs3:
                continue

            '''导出数据'''
            step = "step4"
            step_realtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            fs4, export_path = step4.run(pack_config)
            step_finishtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            dh.record(pack_config, runtime, step_realtime, step_finishtime, step, fs4)
            if not fs4:
                continue

            '''发送邮件'''
            step = "step5"
            step_realtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            fs5 = step5.run(pack_config, export_path, realtime)
            step_finishtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            dh.record(pack_config, runtime, step_realtime, step_finishtime, step, fs5)
            if not fs5:
                continue

            finishtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            issucess = 'True'
        except:
            finishtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        step = "step_all"
        try:
            dh.record(pack_config, runtime, realtime, finishtime, step, issucess)
        except Exception as e:
            print(e)
    dh.shutdown_jvm()
    pass



if __name__ == "__main__":
    run()
    # while True:
    #     if datetime.datetime.now().strftime("%H:%M:%S") == '00:00:00': # 整点
    #         if datetime.datetime.now().day() == 7: # 每月七号
    #             try:
    #                 run()
    #             except Exception as e:
    #                 pass
    #         time.sleep(1)
    #     else:
    #         time.sleep(1)