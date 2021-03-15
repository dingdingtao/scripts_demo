<!--
 * @Author: dingdingtao
 * @Date: 2021-01-01 19:50:46
 * @LastEditTime: 2021-03-15 12:39:55
 * @Description: 
-->

# hive_to_mysql
```
从hive导出数据到mysql
```
1. 修改sql目录下test.sql文件为你要执行的语句或把语句文件放到这个目录下(记得要把`'${day}'`替换成具体日期)
2. 修改config目录下config.json文件  
    `mysql_table`：要导入的mysql数据库表名  
    `mysql_tablehead`：要导入的数据表表头（按照工作流建表语句的顺序写就可以了）
3. 执行hive_to_mysql.py文件
4. 等待查询&导数据导入（查询成功之后会输出查询结果，导入数据到mysql）


# hive_to_excel
```
从hive导出数据到excel
```
1. 修改sql目录下test.sql文件为你要执行的语句或把语句文件放到这个目录下(记得要把`'${day}'`替换成具体日期)
2. 修改config目录下config.json文件  
    `excel_name`：要导入的excel文件名  
    `excel_sheet`：要导入的excel表名
    `excel_columns`：表头（按照工作流建表语句的顺序写就可以了）
3. 执行hive_to_excel.py文件
4. 等待查询&导数据导入（查询成功之后会输出查询结果，导入数据到excel）

# hive_fetch
```
hive查询
```
