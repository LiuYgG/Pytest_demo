# -*- coding:utf-8 -*-
'''
  CreateTime: 2023 年 02 月 20 日
'''
import allure
import pytest
import requests
import json
from untils.get_data import get_data

url = "https://api.apiopen.top/api/login/"
param = [
    ({"Content-Type": "application/json"}, {"account": "123456@qq.com", "password": "123456"}),
    ({"Content-Type": "application/json"}, {"account": "123456@qq.com", "password": "123456"}),
    ({"Content-Type": "application/json"}, {"account": "123456@qq.com", "password": "123456"})
]

class Test_model(object):

    def setup_class(self):
        print("===============用例开始执行=================")

    def teardown_class(self):
        print("===============用例结束执行=================")


    @allure.description('一个登录验证的测试')
    @pytest.mark.parametrize("headers, paydata", param)
    def test_parametrize_login_status_success(self, headers, paydata):
        r = requests.post(url=url,
                          data=paydata,
                          headers=headers)
        assert r.status_code != 200
        # print(r.json())
        # result = r.json()
        # assert result['code'] == 403

    @allure.description('验证登录错误的测试')
    @pytest.mark.parametrize("headers, paydata", param)
    def test_paramterize_login_code_error(self, headers, paydata):
        r = requests.post(url=url,data=paydata, headers=headers)
        result = r.json()
        assert result['code'] == 400