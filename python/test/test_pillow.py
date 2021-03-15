'''
Author: dingdingtao
Date: 2020-12-21 10:41:59
LastEditTime: 2021-03-15 14:28:50
LastEditors: dingdingtao
Description: 
'''
#先导入所需的包
import pygame
import os
import pandas as pd
pygame.init()  #  初始化

B = """𝐖𝐞𝐥𝐜𝐨𝐦𝐞;𝐭𝐨;𝐦𝐲𝐩𝐫𝐨𝐟𝐢🤴🤴"""       #  变量B需要转图片的文字
text = u"{0}".format(B)           #  引号内引用变量使用字符串格式化
# text=str(pd.read_csv(r'D:\output.csv',encoding='gbk'))
print(text)
#设置字体大小及路径
font = pygame.font.Font(os.path.join("F:\\test\\fonts", "syht.ttf"), 26)
# font = pygame.font.Font(os.path.join("/Users/akun/Library/Fonts", "msyh.ttf"), 26)
#设置位置及颜色
rtext = font.render(text, True, (0, 0, 0), (255 ,255 ,255))

#保存图片及路径
pygame.image.save(rtext, "D:\output.png")