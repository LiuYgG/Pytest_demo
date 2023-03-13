# -*- coding:utf-8 -*-
'''
  CreateTime: 2023 年 02 月 20 日

  读取 config 目录下的 data.yaml 数据
'''
# import yaml
import os
import json

# 获取数据文件目录路径
def get_data_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"data","test_param", "test_param.json")
    return path

# 读取数据文件方法
def get_test_data():
    with open(get_data_path(), encoding='utf8') as f:
        data = json.loads(f.read())
        test = data
        return test

get_data = get_test_data()
print(get_data)
