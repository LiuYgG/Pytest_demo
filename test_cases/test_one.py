# -*- coding:utf-8 -*-
'''
  CreateTime: 2023 年 02 月 20 日
  普通测试用例文件夹
'''
import pytest

@pytest.mark.P0
def test_one():
    a = 1
    b = 1
    assert a == b

if __name__ == '__main__':
    pytest.main()