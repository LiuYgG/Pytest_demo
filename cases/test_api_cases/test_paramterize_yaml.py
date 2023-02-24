# -*- coding:utf-8 -*-
'''
  CreateTime: 2023 年 02 月 20 日
'''
import pytest
from untils.read_data import get_data

# 单参数
# @pytest.mark.parametrize("name", get_data['hero_name'])
# def test_parametrize_01(name):
#     print(name)

# 多参数
# @pytest.mark.parametrize("name,word", get_data['heros_name_word'])
# def test_parametrize_01(name, word):
#     print(f'{name}的台词是：{word}')