# -*- coding=utf-8 -*-
"""
-------------------------------
    Project:    AI
    File Name:  login.py
    Description:
    Author:     Administrator
    Date:       2020/02/29
    Time:       11:59
-------------------------------
    Modify Activity:
                2020/02/29
-------------------------------
"""
__author__ = 'Administrator'

from bs4 import BeautifulSoup as bs
import requests
import random
import pprint

user_list = (
        {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1"},
        {'user-agent': "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1"},
        {'user-agent': "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11"},
        {'user-agent': "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"},
        {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
    )

user_agent = random.choice(user_list)
response = requests.get('https://github.com', user_agent)
soup = bs(response.text, 'lxml-xml')
with open('github.txt', 'w+', encoding='utf-8') as f:
    print(soup, file=f)
    print('OK')
# pprint.pprint(soup)
# print(soup.select('div form[action=\'/session\'] input[name=\'authenticity_token\']'))



