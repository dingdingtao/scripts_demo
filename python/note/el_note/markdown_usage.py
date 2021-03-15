'''
Author: dingdingtao
Date: 2020-12-06 20:41:22
LastEditTime: 2020-12-06 21:18:06
Description: markdown库
'''
import markdown



"""
markdown参考
https://www.cnblogs.com/JiangLe/p/12682912.html
https://github.com/Python-Markdown/markdown/
"""



input_path = "H:\\Demo\\Python\\Scripts_demo\\markdown.md"
output_path = "H:\\Demo\\Python\\Scripts_demo\\Scripts\\test\\markdown_usage_output.html"



'''
Description: 读.md解析转换成.html文件
param {*}
return {*} 转换后的html文本
'''
def markdown_parse():
    with open(input_path, "r", encoding="utf8") as f:
        mark = f.read()
    # mark = "# 一级标题"
    html = markdown.markdown(mark)
    with open(output_path, "w", encoding="utf8") as f:
        f.write(html)
    return html



if __name__ == "__main__":
    html = markdown_parse()
    print(html)