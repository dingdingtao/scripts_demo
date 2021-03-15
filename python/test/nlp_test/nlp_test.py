#coding:utf-8
'''
Author: dingdingtao
Date: 2021-01-06 21:28:33
LastEditTime: 2021-01-19 10:54:49
LastEditors: dingdingtao
Description: nlp测试
'''
import json
import os
import six

import paddlehub as hub

    
'''
Description: 
param {*}
return {*}
'''
def run():
    # Load Senta-BiLSTM module
    senta = hub.Module(name="senta_bilstm")

    test_text = ["我爱你", "我恨你"]

    input_dict = {"text": test_text}

    results = senta.sentiment_classify(data=input_dict)

    for index, text in enumerate(test_text):
        results[index]["text"] = text
    for index, result in enumerate(results):
        if six.PY2:
            print(
                json.dumps(results[index], encoding="utf8", ensure_ascii=False))
        else:
            print(results[index])


if __name__ == "__main__":
    run()