'''
Author: dingdingtao
Date: 2021-03-18 15:04:19
LastEditTime: 2021-03-18 18:11:37
LastEditors: dingdingtao
Description: 大麦网
'''
import json
import time
import urllib
import smtplib
import requests
from lxml import etree
from datetime import datetime
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


'''请求基本信息'''
url = "https://search.damai.cn"
url_path = "/searchajax.html?keyword={keyword}&cty=&ctl=&sctl=&tsg=0&st=&et=&order=0&pageSize={pageSize}&currPage={currPage}&tn="
cookies = "cna=gdxVGBlMVSYCATr44gbcp25B; t=ffec32f37e17bd60597cb4a2e2683e6a; damai.cn_nickName=%E8%9C%97%E7%89%9B%E5%95%8A%E4%BD%A0%E5%9C%A8%E6%83%B3%E4%BB%80%E4%B9%88; UM_distinctid=177f091b9899f6-0b5eab54059e73-c791039-1fa400-177f091b98ad83; cn_7415364c9dab5n09ff68_dplus=%7B%22distinct_id%22%3A%20%22177f091b9899f6-0b5eab54059e73-c791039-1fa400-177f091b98ad83%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201614648825%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201614648825%2C%22initial_view_time%22%3A%20%221614643927%22%2C%22initial_referrer%22%3A%20%22https%3A%2F%2Fsearch.damai.cn%2F%22%2C%22initial_referrer_domain%22%3A%20%22search.damai.cn%22%7D; xlly_s=1; cookie2=1dce0cdfcaa3fd2dd34835afbf1fb5e7; _tb_token_=7983e1e6377be; XSRF-TOKEN=74c46895-f139-40d8-b7e8-24fa86b17ec0; isg=BGtrP4kkj-AXh9NbQu1b1BBz-o9VgH8C8QFN4N3oFKoBfIreZFLBUhad1rwS3Nf6; l=eBgPIrWqjIYpuMwKBOfZourza779YIRfguPzaNbMiOCPOmCp5SoFW6wVvB89CnGVHsZ2J3zWDma_BqT95yCSnxv9-cBdqMr-3dC..; tfstk=cRZGBb4JdPu_9cu3PGi_CukZ7H7dZeKqZorQYo4nrzbT1JqFisTez5vdKfVgDE1.."

'''发件信息'''
# 发件邮箱
mail_user = "mail_user"
# 邮箱密码
mail_pass = "mail_pass"
# 邮箱smtp服务器
smpt_host = 'smtp.qq.com'
# 服务器端口
smpt_port = 465
# 发件人姓名
send_name = "dingdingtao"
# 邮件主题
mail_zt = "大麦网查询结果"

'''收件信息'''
# 收件人邮箱
rcv_mail = ["rcv_mail"]
# 抄送人邮箱
rcc_mail = []

'''查询关键字'''
search_keyword = "tfboys"

'''
description: 请求参数
param {*} 
return {*} 请求参数
'''
def request_datas(kw, ps, cp):
    data = {
        "keyword": kw,
        "pageSize": ps,
        "currPage": cp
    }
    return "".join([url, url_path]).format(keyword=kw, pageSize=ps, currPage=cp),data


'''
description: 请求头
param {*} c cookie
return {*} 请求头
'''
def request_header(c, url, url_path):
    header = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
        "cookie": c,
        "referer": "".join([url,url_path]),
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        "x-xsrf-token": "74c46895-f139-40d8-b7e8-24fa86b17ec0"
    }
    return header


'''
description: 发送邮件
param {*} to_reciver 收件人
param {*} cc_reciver 抄送人
param {*} mail_title 邮件标题
param {*} content 邮件内容
param {*} path 附件路径
param {*} fname 附件文件名
return {*}
'''
def send_email(to_reciver, cc_reciver, mail_title, content, path, fname):
    recivers = to_reciver + cc_reciver
    message = MIMEMultipart()
    message['Subject'] = Header(mail_title, 'utf-8')
    message['From'] = send_name + '<' + mail_user + '>'
    message.attach( MIMEText(content, 'html', 'utf-8') )

    if len(to_reciver)>0:
        message['To'] = ','.join(to_reciver)

    if len(cc_reciver):
        message['Cc'] = ','.join(cc_reciver)

    for p in path:
        part = MIMEApplication( open(p, 'rb').read() )
        part.add_header('Content-Disposition', 'attachment', filename=fname)
        message.attach(part)
        
    try:
        smtpobj = smtplib.SMTP_SSL(smpt_host, smpt_port)
        smtpobj.login(mail_user, mail_pass)
        smtpobj.sendmail(mail_user, recivers, message.as_string())
    except smtplib.SMTPException as e:
        print(e)
        pass
    finally:
        smtpobj.quit()


def run(keyword):
    pageCounter = 1
    result_datas = []
    error_type = ""
    is_error = False
    send_flag = False

    while pageCounter:
        try:
            '''拼接请求参数'''
            url, data = request_datas(urllib.parse.quote(keyword), "60", str(pageCounter))
            '''拼接请求头部信息'''
            header = request_header(cookies, url, url_path) 
            '''发起请求'''
            r = requests.post(url, headers=header, data=json.dumps(data)).json()
            '''请求结束的条件'''
            if len(r['pageData']['resultData']) == 0:
                break
            '''保存需要的信息'''
            for result in r['pageData']['resultData']:
                result_datas.append([result['id'], result['nameNoHtml'], result['showstatus'], result['showtime'], result['venue'], result['venuecity'], result['price_str']])
            pageCounter += 1
            send_flag = True
        except Exception as e:
            '''记录是否出差以及错误类型'''
            is_error = True
            if isinstance(e, KeyError):
                error_type = 'KeyError'
            else:
                error_type = 'Unknown'
            print(e)
            break
    
    '''根据是否出错，错误类型判断是否发送邮件提示'''
    if is_error:
        print("error type:", error_type)
        send_flag = False
        if len(result_datas) != 0:
            send_flag = True
    
    '''如果标记为True发送查询结果,否则根据情况给出提示或发送邮件告警'''
    if send_flag:
        # print(result_datas)
        print("data count:",len(result_datas))
        content = ""
        for r in result_datas:
            content = content + "<br>"  + ",".join(r)
        content = u'{}'.format(content)
        send_email(rcv_mail, rcc_mail, mail_zt, content, "", "")
    else:
        if error_type == 'KeyError':
            print("no result.")
        elif error_type == "Unknown":
            send_email(rcv_mail, rcc_mail, mail_zt, "script error.", "", "")
        else:
            pass

if __name__ == "__main__":
    while True:
        '''持续监听'''
        if datetime.now().strftime("%M:%S") == '20:00':
            run(search_keyword)
            time.sleep(1)
            # if datetime.now().weekday() == 4:
            #     run(search_keyword)
            #     time.sleep(1)
        else:
            time.sleep(1)

    '''单次测试'''
    # run(search_keyword)