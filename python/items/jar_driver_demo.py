'''
Author: dingdingtao
Date: 2021-03-23 12:11:30
LastEditTime: 2021-03-23 12:15:14
LastEditors: dingdingtao
Description: python 驱动jar包
'''
import jpype
import os


'''
description: 开启jvm
param {*}
return {*}
'''
def start_jvm():
    jar_path = os.path.join(CURRENT_PATH, "inflection_ocr.jar")
    jvmPath = jpype.getDefaultJVMPath() 
    jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=%s" % jar_path)# 启动虚拟机
    

'''
description: 加载图片转换接口
param {*}
return {*} 类
'''
def fetch_jclass():
    demo = jpype.JClass('run/OcrDemo')
    return demo


'''
description: 关闭jvm虚拟机
param {*}
return {*}
'''
def shutdown_jvm():
    jpype.shutdownJVM()


def run():
    start_jvm()
    demo = fetch_jclass()
    demo.main(["arg1","arg2"])
    shutdown_jvm()


if __name__ == "__main__":
    run()
