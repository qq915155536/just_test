#  ===========================
# -*- coding:utf-8 -*-
# Time :2022/11/1 14:56
# Author :小灬天
# QQ:915155536
# File :test_login.py
#  ===========================
import unittest
import requests


# 测试登陆类
class UnitCase(unittest.TestCase):
    # 登录函数
    def test_login(self):
        url = 'http://11.168.3.220:8081/api/login1'
        data = {
            "account": "cs001",
            "password": "123456",
            "threeCode": "PVG",
            "verifyCode": "456"
        }
        base_headers = {'threeCode': 'PVG'}
        res = requests.post(url=url, json=data, headers=base_headers)
        # 断言
        act_res = res.json()['code']
        expect_res = 200
        self.assertEqual(expect_res,act_res,msg='断言失败，登录测试用例，执行失败')

if __name__ == '__main__':
    unittest.main()