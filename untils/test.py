# -*- coding:utf-8 -*-
'''
  CreateTime: 2023 年 02 月 20 日
'''
import os

print(os.path.realpath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
print(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"config","data.yml"))