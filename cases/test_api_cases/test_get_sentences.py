# -*- coding:utf-8 -*-
'''
  CreateTime: 2023 年 02 月 24 日
  获取名言接口
  url: https://api.apiopen.top/api/sentences
  code:
        {
          "code": 200,
          "message": "成功!",
          "result": {
            "name": "与余问答既有以，感时抚事增惋伤。",
            "from": "杜甫《观公孙大娘弟子舞剑器行》"
          }
        }
        ----------------------------------------------

'''
import allure
import pytest
import requests

class Test_sentences(object):


    @allure.description('一个获取一言名句的测试')
    @pytest.mark.name('获取测试')
    def test_get_sentences(self):
        url = 'https://api.apiopen.top/api/sentences'

        headers = {
            'Content-Type': 'application/json'
        }

        r = requests.request("GET", url=url, headers=headers)
        result = r.json()
        assert result['code'] == 200
        assert result['message'] == '成功!'
        print(result['result']['name'])
