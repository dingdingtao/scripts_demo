'''
Author: dingdingtao
Date: 2021-01-21 10:48:45
LastEditTime: 2021-01-21 10:50:32
LastEditors: dingdingtao
Description: 
'''
import hive_presto

sql = """
    SELECT cast(id AS varchar)id,
        cast(parent_id AS varchar)parent_id,
        cn_name,
        en_name,
        ru_name
    FROM mysql_tb.bigo_t_cps_manage_label
"""

def run():
    datas = hive_presto.hive_presto_sg_sql(sql)

    print(datas)


if __name__ == "__main__":
    run()