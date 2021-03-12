'''
Author: dingdingtao
Date: 2020-12-07 10:02:52
LastEditTime: 2021-03-12 18:42:31
LastEditors: dingdingtao
Description: 调用ocr接口
'''
import sys
import os
import json
import requests
import base64
import pymysql
import re
import jpype
from tqdm import tqdm

'''
引入data_handle模块查询数据
'''
CURRENT_PATH = os.path.dirname(__file__)
sys.path.append(os.path.join(CURRENT_PATH,"../handle"))
import data_handle as dh



'''
description: ocr接口
param {*} fpath 图片路径
return {*}
'''
def ocr_video_caption(fpath):
    try:
        url = "ocr接口"
        req = {}
        if fpath.startswith('http'):
            req['image_url'] = fpath         # url key:  video url or image url
        else:
            fpath = fpath.replace("\\","/")
            with open(fpath, 'rb') as fp:
                raw_data = base64.b64encode(fp.read()).decode("ascii")
                req['image_base64'] = [raw_data]   # image key: raw_video or raw_image
        #req["caption"] = 1   # 0: close video caption  1: open video caption filter function
        req["bboxes"] = 0   # 0: return texts only;  1: return texts, boxes and scores
        req = json.dumps(req)
        
        res = requests.post(url=url, data=req, timeout=300)

        status = res.status_code
        if status == 200:
            return res.json() 
        else:
            # print('request not succeed', res.json())
            return res.json() 
    except Exception as e:
        print(e)



'''
description: 根据传入的路径调用ocr接口
param {*} url_or_path ocr接口识别的目录
return {*} 元组(原词 id,ocr接口识别结果 word_ocr)
'''
def detect_reco(c):
    url_or_path=dh.OCR_PATH
    sql = """
        select id from {table} where ocr_word=''
    """.format(table=c['table_name'])

    connection = pymysql.connect(host=dh.HOST, port=dh.PORT, user=dh.USER,password=dh.PASS, db=dh.DB, charset=dh.CODE)
    cursor = connection.cursor()
    cursor.execute(sql)
    ids = cursor.fetchall()
    cursor.close()
    connection.close()

    '''
    根据查询内容排除已处理的数据
    '''
    result = []
    if os.path.isdir(url_or_path):
        for word_id in ids:
            fi = os.path.join(url_or_path,str(word_id[0]) + ".png")
            if os.path.exists(fi) and os.path.isfile(fi):
                result.append((word_id[0],fi))
    else:
        res = ocr_video_caption(url_or_path)
        print(res)

    return result



'''
description: 保存ocr识别结果到数据库
param {*}
return {*}
'''
def detect_ocr_word(c, word):
    
    connection = pymysql.connect(host=dh.HOST, port=dh.PORT, user=dh.USER,password=dh.PASS, db=dh.DB, charset=dh.CODE)
    cursor = connection.cursor()

    distinct_id = word[0]
    res = ocr_video_caption(word[1])
    
    if res['status'] == 500:
        result = connection.escape("None")
    else:
        result = connection.escape(res['result'][0]['text'])
    sql = """update {table} set ocr_word={values} where id={distinct_value}""".format(table=c['table_name'],values=result,distinct_value=distinct_id)

    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()
    
    '''
    将识别完的图片删除
    '''
    os.remove(word[1])



'''
description: ocr识别
param {*} 配置信息
return {*} ocr识别是否成功
'''
def detect_ocr_handle(c):
    ocr_words = detect_reco(c)
    print("ocr识别.")
    if 0 == len(ocr_words):
        return False
    try:
        with tqdm(ocr_words, desc="ocr progress", ncols=80) as t:
            for word in t:
                detect_ocr_word(c, word)
    except Exception as e:
        t.close()
        print(e)
        return False
    t.close()
    print("识别完成.")
    return True


'''
description: 调用Java 文字转图片jar包
param {*} c 配置信息
return {*}
'''
def ocr_java_image(c):
    demo = dh.fetch_jclass()
    demo.main([c['table_name']])


'''
description: ocr识别
param {*} c 配置信息
return {*} ocr是否完成
'''
def run(c):
    try:
        ocr_java_image(c)
        has_ocr = detect_ocr_handle(c)
        return has_ocr
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    run()