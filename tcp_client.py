# -*- coding=utf-8 -*-
"""
-------------------------------
    Project:    AI
    File Name:  tcp_client.py
    Description: TCP客户端
    Author:     Administrator
    Date:       2020/02/24
    Time:       08:23
-------------------------------
    Modify Activity:
                2020/02/24
-------------------------------
"""
__author__ = 'Administrator'

import socket
import pprint

target_host = '127.0.0.1'   # 目标主机
target_port = 9999                # 目标端口

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP客户端

client.connect((target_host, target_port))      # 连接目标主机
# HTTP请求需要一个固定的格式
client.send(b'I am tcp')

response = client.recv(4096)        # 接受响应内容

pprint.pprint(response)

