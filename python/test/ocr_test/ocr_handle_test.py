'''
Author: dingdingtao
Date: 2021-01-19 10:38:07
LastEditTime: 2021-03-15 14:25:50
LastEditors: dingdingtao
Description: 
'''
import os
import base64
import json
import requests

'''
description: ocr接口
param {*} fpath 图片路径
return {*}
'''
def ocr_video_caption(fpath):
    try:
        url = "url"
        req = {}
        if fpath.startswith('http'):
            req['image_url'] = fpath         # url key:  video url or image url
        else:
            fpath = fpath.replace("\\","/")
            with open(fpath, 'rb') as fp:
                raw_data = base64.b64encode(fp.read()).decode("ascii")
                req['image_base64'] = [raw_data]   # image key: raw_video or raw_image
        #req["caption"] = 1   # 0: close video caption  1: open video caption filter function
        req["bboxes"] = 1   # 0: return texts only;  1: return texts, boxes and scores
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



def run():
    current_path = os.path.dirname(__file__)
    test_filepath = os.path.join(current_path, "test2.png")
    print(test_filepath)

    r = ocr_video_caption(test_filepath)

    print(r)
    pass



if __name__ == "__main__":
    run()

