<!--
 * @Author: dingdingtao
 * @Date: 2021-01-06 21:48:22
 * @LastEditTime: 2021-01-06 21:55:46
 * @LastEditors: dingdingtao
 * @Description: 自定义正则-敏感词匹配
-->

```
自定义敏感词和正则并匹配
```

# bin目录
```
主要功能模块
data_handle.py - 数据处理
```

# config目录
```
配置文件目录
config.json
{
    "filename": "data目录下excel文件名",
    "sheetname": "表名",
    "reg_filename": "regexp目录下excel文件名",
    "reg_sheetname": "表名",

    "host": "数据库连接地址",
    "port": 端口号,
    "user": "用户名",
    "password": "密码",
    "db": "库名",
    "charset": "编码格式"
}
```

# data目录
```
敏感词存放目录,放敏感词excel文件
```

# regexp目录
```
正则存放目录,放正则excel文件
```

# regexp_sensitive.py
```
入口文件
```