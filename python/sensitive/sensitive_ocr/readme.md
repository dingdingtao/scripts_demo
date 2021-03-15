<!--
 * @Author: dingdingtao
 * @Date: 2020-12-24 12:37:00
 * @LastEditTime: 2021-03-12 18:47:54
 * @LastEditors: dingdingtao
 * @Description: 目录结构及文件用途
-->

# 目录结构
## config
```
存放配置文件
```
### config.json
```
配置文件
```
### base_config.py
```
读取配置文件接口
```

## sql
```
存放sql语句
```

## handle
### data_handle.py
```
用于数据处理，查询和配置文件读取等接口
```

## step_1_data
### hive_presto.py  
```
从hive查数据
```
### cleanning_data.py
```
清洗数据
```
### get_data_mysql.py  
```
获取数据，将数据存到mysql
```

## step_2_ocr
### inflection_ocr.jar  
```
java 将文字绘制成图,放到out目录
```
### ocr_handle.py  
```
调用ocr识别接口，识别图片内容
```

## step_3_sensitive
### toent_handle.py  
```
获取敏感词查询动态参数
```
### sensitive_query.py  
```
调用敏感词查询接口，查询、存储数据
```

## step_4_export
### export_result.py  
```
导出数据到excel表
```

## out
```
图片临时存放目录
```

## result
```
导出结果、附件excel存放目录
```
