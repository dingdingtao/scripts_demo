'''
Author: dingdingtao
Date: 2020-12-07 22:15:18
LastEditTime: 2020-12-07 22:26:40
Description: re 正则表达式
'''
import re



'''
Description: 
param {*}
return {*}
'''
def reg():
    r'''

    re.match(pattern, string, flags=0)
        pattern : 匹配的正则表达式
        string  : 要匹配的字符串。
        flags   : 标志位，用于控制正则表达式的匹配方式。


    re.search(pattern, string, flags=0)
        pattern : 匹配的正则表达式
        string  : 要匹配的字符串。
        flags   : 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。


    re.sub(pattern, repl, string, count=0, flags=0)
        pattern : 正则中的模式字符串。
        repl    : 替换的字符串，也可为一个函数。
        string  : 要被查找替换的原始字符串。
        count   : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。


    re.compile(pattern[, flags])
        pattern : 一个字符串形式的正则表达式
        flags : 可选，表示匹配模式，比如忽略大小写，多行模式等。


    re.findall(string[, pos[, endpos]])
        string : 待匹配的字符串。
        pos : 可选参数，指定字符串的起始位置，默认为 0。
        endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。

        
    re.finditer(pattern, string, flags=0)
        pattern	匹配的正则表达式
        string	要匹配的字符串。
        flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

        
    re.split(pattern, string[, maxsplit=0, flags=0])
        pattern	匹配的正则表达式
        string	要匹配的字符串。
        maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
        flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。


    |re.I   |	使匹配对大小写不敏感|
    |re.L   |	做本地化识别（locale-aware）匹配|
    |re.M   |	多行匹配，影响 ^ 和 $|
    |re.S   |	使 . 匹配包括换行在内的所有字符|
    |re.U   |	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.|
    |re.X   |	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。|
    '''
    pass

