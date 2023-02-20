# -*- coding:utf-8 -*-
'''
  CreateTime: 2023 年 02 月 20 日

  读取 config 目录下的 data.yaml 数据
'''
import yaml
import os

# 获取数据文件目录路径
path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"config","data.yaml")

# 读取数据文件方法
def read_data():
    f = open(path, encoding='utf8')
    data = yaml.safe_load(f)
    return data

get_data = read_data()
# print(get_data['hero']['name'])

