# -*- coding=utf-8 -*-
"""
-------------------------------
    Project:    AI
    File Name:  getpwd.py
    Description:
    Author:     Administrator
    Date:       2020/02/28
    Time:       20:43
-------------------------------
    Modify Activity:
                2020/02/28
-------------------------------
"""
__author__ = 'Administrator'

import getpass

user = getpass.getuser()
password = getpass.win_getpass()

print(user)
print(password)