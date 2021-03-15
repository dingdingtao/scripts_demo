'''
Author: dingdingtao
Date: 2020-12-06 13:21:11
LastEditTime: 2020-12-06 21:17:39
Description: git教程-简单git指令
'''


git_lib = """
Git教程
https://www.liaoxuefeng.com/wiki/896043488029600
"""


step1 = """
创建SSH Key
cmd命令行:
    ssh-keygen -t rsa -C "youremail@example.com"
生成id_rsa和id_rsa.pub这两个文件(私钥和公钥)
"""


step2 = """
GitHub添加ssh
Account settings -> Add SSH Key -> 用id_rsa.pub内容创建 GitHub SSH Key
"""


step3 = """
添加远程库
git remote add origin git@github.com:michaelliao/learngit.git
"""


step4 = """
push到远程库
git push origin master
"""


step5 = """
clone到本地
git clone git@github.com:michaelliao/gitskills.git
"""


git_vscode = """
安装git
配置git:
    config --global user.name "username"
    config --global user.email "email@xxx.com"
vscode安装git blame插件:
    git init
    git clone 远程库
"""



'''
Description: 
param {*}
return {*}
'''
def git():
    pass



if __name__ == "__main__":
    pass