'''
Author: dingdingtao
Date: 2020-12-06 13:11:52
LastEditTime: 2021-03-15 14:19:41
Description: 整理目录文件
'''
import os
import re
import shutil
import argparse



'''
Description: 查询path目录以及子目录下的所有文件 clean_ 开头的文件夹除外
param {*} path 基目录
return {*} 基目录,所有查到的文件路径
'''
def find_all_subfiles(path):
    files = os.listdir(path)
    result = []
    for f in files:
        sub_file = os.path.join(path,f)
        if os.path.isdir(sub_file):
            if re.match(r'clean_', f, re.I):
                continue
            r = find_all_subfiles(sub_file)[1]
            result = result + r
        else:
            result.append(sub_file)
    return path,result



'''
Description: 移动文件到指定文件夹
param {*} path 基目录
param {*} filepath 文件路径
param {*} out 输出目录
return {*}
'''
def move(path,filepath,out):
    new_path = os.path.join(path,"clean_" + out)
    if not os.path.exists(new_path) :
        os.mkdir(new_path)
    shutil.move(filepath,new_path)



'''
Description: 清理逻辑
param {*} path 基目录
param {*} files 所有要移动的文件的路径
return {*}
'''
def clean_files(path,files):
    for f in files:
        if os.path.exists(f):
            fix = os.path.splitext(f)[-1]
            if re.match( r'\.xlsx|\.xls', fix, re.M|re.I):
                move(path,f,"表格")
            elif re.match( r'\.png|\.jpg|\.gif', fix, re.M|re.I):
                move(path,f,"图片")
            elif re.match( r'\.exe', fix, re.M|re.I):
                move(path,f,"应用程序")
            elif re.match( r'\.7z|\.zip|\.rar', fix, re.M|re.I):
                move(path,f,"压缩包")
            elif re.match( r'\.pdf|\.ppt|\.pptx|\.doc|\.docx', fix, re.M|re.I):
                move(path,f,"ppt_word文档")
            elif re.match( r'\.htm|\.html', fix, re.M|re.I):
                move(path,f,"页面")
            elif re.match( r'\.txt|\.json', fix, re.M|re.I):
                move(path,f,"文本")
            elif re.match( r'\.py|\.java|\.pyw|\.class|\.c|\.cpp', fix, re.M|re.I):
                move(path,f,"脚本")
            elif re.match( r'\.mp4|\.mov|\.wmv|\.avi', fix, re.M|re.I):
                move(path,f,"视频")
            else:
                move(path,f,"其他")



if __name__ == "__main__":
    basepath = 'C:\\Users\\Administrator\\Downloads'
    
    path,r = find_all_subfiles(basepath)
    clean_files(path,r)
