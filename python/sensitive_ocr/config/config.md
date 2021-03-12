<!--
 * @Author: dingdingtao
 * @Date: 2020-12-08 17:51:14
 * @LastEditTime: 2021-01-05 17:45:37
 * @LastEditors: dingdingtao
 * @Description: 
-->


# config配置文件

```
{
    数据库配置
    ------------------------------------
    "host": "数据库连接地址",
    "port": 端口,
    "user": "用户名",
    "pass": "密码",
    "db": "数据库",
    "charset": "编码"
    ------------------------------------
}
```

# _config配置文件

```
{
    结果表
    ------------------------------------

    "outTable": {
        "tablename": "",
        "tabledtype": {
            "id": "BIGINT",
            "cid": "BIGINT",
            "word": "TEXT",
            "ocr_word": "TEXT",
            "word_rs": "TEXT",
            "ocr_word_rs": "TEXT"
        },
        "sql": "",
        "business": "",
        "app": "",
        "countrys": "",
        "comment": ""
    },

    
    配置表
    ------------------------------------
    "configTable": {
        "tablename": "ocr_sensitive_config_tb_dt",
        "tabledtype": {
            "cid": "BIGINT",
            "appid": "BIGINT",
            "businessid": "BIGINT",
            "countrys": "TEXT",
            "sql_path": "TEXT",
            "sql_filename": "TEXT",
            "table_name": "TEXT",
            "comment": "TEXT",
            "ext1": "TEXT",
            "ext2": "TEXT",
            "ext3": "TEXT"}
    },
    

    记录表
    ------------------------------------

    "recordTable": {
        "tablename": "ocr_sensitive_record_tb_dt",
        "tabledtype": {
            "rid":"BIGINT",
            "cid": "BIGINT",
            "runtime": "TEXT",
            "realtime": "TEXT",
            "finishtime": "TEXT",
            "step": "TEXT",
            "success": "TEXT",
            "ext1": "TEXT",
            "ext2": "TEXT",
            "ext3": "TEXT"
        }
    },

    
    收件表
    ------------------------------------

    "sendmailTable": {
        "tablename": "ocr_sensitive_sendmail_tb_dt",
        "tabledtype": {
            "sid":"BIGINT",
            "cid": "BIGINT",
            "email": "TEXT",
            "ename": "TEXT",
            "comment": "TEXT",
            "ext": "TEXT"
        }
    }
    ------------------------------------
}
```