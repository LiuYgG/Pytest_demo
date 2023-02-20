# -*- coding:utf-8 -*-
'''
  CreateTime: 2023 年 02 月 20 日
'''
import pytest

@pytest.mark.parametrize("name", ["values"])
def test_parametrize_01(name):
    assert name == "values"