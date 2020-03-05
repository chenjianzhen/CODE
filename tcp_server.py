# -*- coding=utf-8 -*-
"""
-------------------------------
    Project:    AI
    File Name:  tcp_server.py
    Description:TCP服务器
    Author:     Administrator
    Date:       2020/02/24
    Time:       23:11
-------------------------------
    Modify Activity:
                2020/02/24
-------------------------------
"""
__author__ = 'Administrator'

import socket
import threading

# 服务器需要监听的IP地址和端口
bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

# 最大连接数设置为5
server.listen(5)

print("[*] listening on %s:%d" % (bind_ip, bind_port))

def handle_client(client_socket):

    request = client_socket.recv(1024)

    print("[*] received: %s" % request)

    client_socket.send(b"ACK!")

    client_socket.close()

# 等待连接
while True:

    client, addr = server.accept()

    print("[*] accepted connection from: %s:%d" % (addr[0], addr[1]))

    client_handler = threading.Thread(target=handle_client, args=(client,))

    client_handler.start()

