# -*- coding=utf-8 -*-
"""
-------------------------------
    Project:    AI
    File Name:  udp_client.py
    Description: UDP客户端
    Author:     Administrator
    Date:       2020/02/24
    Time:       23:04
-------------------------------
    Modify Activity:
                2020/02/24
-------------------------------
"""
__author__ = 'Administrator'

import socket
import pprint

target_host =  '127.0.0.1'
target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b'fuck you', (target_host, target_port))

response = client.recvfrom(4096)

pprint.pprint(response)