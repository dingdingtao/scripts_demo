'''
Author: dingdingtao
Date: 2020-12-21 10:26:38
LastEditTime: 2021-03-15 14:20:23
LastEditors: dingdingtao
Description: 删除文件
'''
import os


'''
description: 删除目录下所有文件
param {*} basepath 删除目录
return {*} 是否成功
'''
def del_files(basepath):
    try:
        files = basepath
        if os.path.exists(basepath):
            files = os.listdir(basepath)
        else:
            print("not exists:", str(basepath))
            return False
        for fi in files: 
            remove_filepath = os.path.join(basepath,fi)
            if os.path.exists(remove_filepath):
                if os.path.isdir(remove_filepath):
                    del_files(remove_filepath)
                    os.rmdir(remove_filepath)
                    print("remove dir: ", str(remove_filepath))
                else:
                    os.remove(remove_filepath)
                    print("remove file: ", str(remove_filepath))
            else:
                print("not exists:", str(remove_filepath))
    except Exception as e:
        print(e)
        return False
    return True


'''
description: 删除单个文件
param {*} filepath 文件路径
return {*} 是否成功
'''
def del_file(filepath):
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            print("remove: ",str(filepath))
        else:
            print("not exists")
            return False
    except Exception as e:
        print(e)
        return False
    return True


if __name__ == "__main__":
    del_base = "H:\\aaa"
    flag = False

    '''删除文件'''
    # flag = del_file(del_base)

    '''删除目录下所有文件'''
    flag = del_files(del_base)
    
    if flag:
        print("删除成功.")
    else:
        print("删除失败.")
