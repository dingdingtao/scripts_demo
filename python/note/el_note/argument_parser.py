'''
Author: dingdingtao
Date: 2020-12-06 13:11:52
LastEditTime: 2021-03-15 14:32:58
Description: argparse简单使用
'''
import argparse



argparse_lib = """
argparse教程
https://docs.python.org/zh-cn/3/howto/argparse.html
"""



'''
Description: 
param {*}
return {*}
'''
def parse():
    """
    创建parse对象
    parser = argparse.ArgumentParser(params)
    params:
        description - 添加功能描述
    """
    parser = argparse.ArgumentParser()

    """
    设置exclusive_group
    group = parser.add_mutually_exclusive_group()
    """
    #group = parser.add_mutually_exclusive_group()

    """
    添加参数
    parser.add_argument(params)
    params:
        arg:
            "arg_name"  必需
            "-arg_name"   简写
            "--arg_name"  可选
        help - 备注(使用提示.)
        action - 使用形式(是否需要参数等...)[store_true|count]
        type - 类型默认为string(设置传入参数的类型)[int|string|float|...]
        choices - 输入的可选值(限定取值范围)
        default - 设置默认值

    exmaples:
        parser.add_argument("-v", "--verbosity", action="count", default=0,
                        help="increase output verbosity")
    """
    parser.add_argument("-v", "--verbosity",  default=0,
                    help="increase output verbosity", choices=[0,1,2,3])
    
    """
    转换参数列表
    args = parser.parse_args()
    结果为元组 Namespace(arg_name=value)
    可以通过args.arg_name来取对应参数值
    """
    args = parser.parse_args()
    print(args.verbosity)



if __name__ == "__main__":
    parse()