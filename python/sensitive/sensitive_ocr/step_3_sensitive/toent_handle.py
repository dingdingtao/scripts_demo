'''
Author: dingdingtao
Date: 2020-12-10 19:31:37
LastEditTime: 2021-03-12 19:06:50
LastEditors: dingdingtao
Description: 动态参数请求
'''
import json
import requests
import time


cookies = "浏览器cookies"
url = "动态参数接口"



'''
description: 请求参数
param {*} 
return {*} 请求参数
'''
def request_datas():
    data = {
        """请求参数"""
    }
    return data


'''
description: 请求头
param {*} c cookie
return {*} 请求头
'''
def request_header(c):
    header = {
        """request_header"""
    }
    return header



'''
description: 请求动态参数
param {*}
return {*} 参数值
'''
def request_toent():
    '''参数'''
    data = request_datas()
    '''请求头'''
    header = request_header(cookies)
    try:
        r = requests.post(url, headers=header, data=json.dumps(data)).json()
    except json.decoder.JSONDecodeError:
        time.sleep(3)
        r = requests.post(url, headers=header, data=json.dumps(data)).json()
        
    if r['code'] != 0:
        return ""
    
    return r['data']['token']



if __name__ == "__main__":
    r = request_toent()
    print(r)
