'''
Author: dingdingtao
Date: 2020-12-29 10:13:47
LastEditTime: 2021-03-12 18:47:31
LastEditors: dingdingtao
Description: 发送邮件
'''
import io
import sys
import os
import smtplib
import time
from datetime import datetime
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import pymysql


CURRENT_PATH = os.path.dirname(__file__)
sys.path.append(os.path.join(CURRENT_PATH,"../handle"))
import data_handle as dh


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
    mail_user = "mail_user"
    mail_pass = "mail_pass"
    recivers = to_reciver + cc_reciver
    message = MIMEMultipart()
    message['Subject'] = Header(mail_title, 'utf-8')
    message['From'] = '附加信息' + '<' + mail_user + '>'
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
        smtpobj = smtplib.SMTP_SSL('邮件服务器', 000)
        smtpobj.login(mail_user, mail_pass)
        smtpobj.sendmail(mail_user, recivers, message.as_string())
    except smtplib.SMTPException:
        pass
    finally:
        smtpobj.quit()


'''
description: 查询cid对应所有收件人
param {*} c 配置信息
return {*} 收件人列表
'''
def fetch_recivers(c):
    sql = """
        select {fields} from {table} where cid={configid} and ext='1'
    """.format(fields=",".join(dh.SENDMAIL_TABLE['tabledtype'].keys()), table=dh.SENDMAIL_TABLE['tablename'], configid=c['cid'])
    connection = pymysql.connect(host=dh.HOST, port=dh.PORT, user=dh.USER,password=dh.PASS, db=dh.DB, charset=dh.CODE)
    cursor = connection.cursor()
    cursor.execute(sql)
    recivers = cursor.fetchall()
    cursor.close()
    connection.close()
    return recivers


'''
description: 封装数据
param {*} datas 待封装数据
return {*} 封装后的数据
'''
def pack_datas(datas):
    config = {}
    for i,k in enumerate(dh.SENDMAIL_TABLE['tabledtype'].keys()):
        config[k] = datas[i]
    return config


'''
description: 发送邮件
param {*} c 配置信息
param {*} p 附件路径
param {*} t 实际开始时间
return {*} 是否成功
'''
def run(c, p, t):
    print("发送邮件.")
    try:
        fetch_reciver = fetch_recivers(c)
        to_reciver = []
        cc_reciver = []
        mail_title = "mail_title " + c['table_name'] + " (" + str(t) +")"
        content = c['comment']
        filepath = [p]
        fname = c['table_name'] + ".xlsx"
        for fr in fetch_reciver:
            pack = pack_datas(fr)
            to_reciver.append(pack['email'])

        if 0 != len(to_reciver):
            send_email(to_reciver=to_reciver, cc_reciver=cc_reciver, mail_title=mail_title, content=content, path=filepath, fname=fname)
            print("发送成功.")
        else:
            print("发送失败.")
            return False
        return True
    except Exception as e:
        traceback.print_exc()
        print("发送失败.")
        return False


if __name__ == "__main__":
    pass