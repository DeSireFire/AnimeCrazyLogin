#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : RaXianch
# CreatDATE : 2022/3/20
# CreatTIME : 21:30 
# Blog      : https://blog.raxianch.moe/
# Github    : https://github.com/DeSireFire
__author__ = 'RaXianch'

import sys
import base64
import requests
from lxml import etree
from requests_toolbelt import MultipartEncoder


class user_sign(object):
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.user_token = ""
        self.headers = {
            'authority': 'user.gamer.com.tw',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'referer': 'https://www.gamer.com.tw/',
        }
        self.requession = requests.Session()
        self.proxies = {}
        self.urls = {
            "get_token": '=AHaw5ibpd2bs9yd05SbvNmLyVWbhdmLyV2c19yL6MHc0RHa',
            "sign_up": '==AcoBnLul2Zvx2XvR2L4Fmah9yd05SbvNmLyVWbhdmLyV2c19yL6MHc0RHa',
            "login_out": 'whGcuQXdvd2bs9yd05SbvNmLyVWbhdmLyV2c19yL6MHc0RHa',
            "check_cookies": '==wL3RnLt92YuIXZtF2Zukmbh9yL6MHc0RHa',
        }
        self.cookies = {}

    def get_token(self):
        url = self.deco(sys._getframe().f_code.co_name)
        response = self.requession.get(url, headers=self.headers, proxies=self.proxies)
        html = etree.HTML(response.text)
        temp = html.xpath("//input[@name='alternativeCaptcha']/@value")
        temp = "".join(temp) if temp and isinstance(temp, list) and len(temp) == 1 else None
        assert temp, "登录验证密钥获取失败！"
        self.user_token = temp

    def sign_up(self):
        url = self.deco(sys._getframe().f_code.co_name)
        file_payload = {
            "userid": self.user_name,
            "password": self.password,
            "autoLogin": "T",
            "alternativeCaptcha": f"{self.user_token}",
            "twoStepAuth": "",
        }
        m = MultipartEncoder(file_payload)
        self.headers['Content-Type'] = m.content_type
        response = self.requession.post(url, headers=self.headers, data=m, proxies=self.proxies)
        assert response.status_code == 200, f"登陆失败！{response.text}"

    def login_out(self):
        url = self.deco(sys._getframe().f_code.co_name)
        data = {'token': f'{self.user_token}'}
        response = self.requession.post(url, headers=self.headers, data=data, proxies=self.proxies)
        if response.status_code == 200:
            print(f"退出成功！")
            self.requession = requests.session()
        else:
            print(f"推出失败！")

    @property
    def get_cookies(self):
        cookie = self.requession.cookies
        self.cookies = cookie.get_dict()
        return self.cookies

    @property
    def get_cookies_str(self):
        cookie = self.requession.cookies
        cookie_str = "; ".join([f"{k}={v}" for k, v in cookie.items()])
        return cookie_str

    def flush_cookies(self):
        if self.cookies:
            self.login_out()

        # 登录
        self.get_token()
        self.sign_up()

    def deco(self, temp_str):
        temp = self.urls.get(temp_str, "")
        return str(base64.b64decode(temp[::-1]), 'utf-8')


if __name__ == '__main__':
    user_name = "账号"  # 填写你自己动漫疯账号
    password = "密码"  # 填写你自己动漫疯密码

    # 登录实例化
    obj = user_sign(user_name=user_name, password=password)

    # 添加代理
    obj.proxies = {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"}

    # 不使用代理则用{}
    # obj.proxies = {}

    # 刷新ck
    obj.flush_cookies()
    # 获取ck 字典
    ck = obj.get_cookies
    print(f"字典形式的cookies: {ck}")
    # 获取ck 字符串
    ck2 = obj.get_cookies_str
    print(f"字符串形式的cookies: {ck2}")
    # 退出账号登录状态
    obj.login_out()