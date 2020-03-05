# -*- coding=utf-8 -*-
"""
-------------------------------
    Project:    AI
    File Name:  main.py
    Description: Pandas入门练习
    Author:     Administrator
    Date:       2020/02/24
    Time:       08:21
-------------------------------
    Modify Activity:
                2020/02/24
-------------------------------
"""
__author__ = 'Administrator'

import requests
from lxml import etree


class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()   # 帮助我们维持一个会话，并且自动处理Cookies

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//div[@class=\'auth-form px-3\']/input[@name=\'authenticity_token\']/@value')
        print('token=', token)
        return token

    def login(self, email, password):
        # 构造一个表单，复制各个字段
        post_data = {
            'commit': 'Sign in',
            'utf-8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def dynamics(self, html):
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class, "alert")]')
        for item in dynamics:
            dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
            print(dynamic)

    def profile(self, html):
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')
        print('name=', name)
        email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
        print(name, email)

if __name__ == '__main__':
    login = Login()
    login.login(email='1315395621', password='9500asce!!')

