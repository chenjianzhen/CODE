# -*- coding=utf-8 -*-
"""
-------------------------------
    Project:    AI
    File Name:  netcat.py
    Description:取代netcat
    Author:     Administrator
    Date:       2020/02/25
    Time:       09:56
-------------------------------
    Modify Activity:
                2020/02/25
-------------------------------
"""
__author__ = 'Administrator'

import sys
import socket
import getopt
import threading
import subprocess

listen                     = False
command                    = False
upload                     = False
execute                    = ""
target                     = ""
upload_destination         = ""
port                       = 0

def usage():
    """
    命令行参数用法
    :return:
    """
    print('BHP Net Tool')
    print('Usage: netcat.py -t target_host -p port')
    print('-l listen        -listen on [host]:[port] for incoming connections')
    print('-e -excute=file_to_run       -execute the given file upon receiving a connection')
    print('-c --command             -initialize a command shell')
    print('-u --upload=destination      -upon receiving connection upload a file and write to [destination]')
    print('Examples:')
    print('netcat.py -t 192.168.0.1 -p 5555 -l -c')
    print('netcat.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe')
    print('netcat.py -t 192.168.0.1 -p 5555 -l  -e=\"cat /etc/passwd\"')
    sys.exit(0)

def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((target, port))

        if len(buffer): # 是否接收到数据
            client.send(buffer)

        while True:     # 接收回传数据
            recv_len = 1
            response = ''

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data
                if recv_len < 4096:
                    break

            print(response)

            buffer = input("")
            buffer += '\n'
            client.send(buffer)

    except:
        print('[*]Exception! Exiting!')
        client.close()

def run_command(command):

    command = command.rstrip()

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = "Failed to execute command.\r\n"
    return output

def client_handler(client_socket):
    global upload
    global execute
    global command

    if len(upload_destination):

        file_buffer = ""

        while True:
            data = client_socket.recv(1024)

            if not data:
                break
                # #########################################

def server_loop():
    global target

    if not len(target):
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))

    server,listen(5)

    while True:
        client_socket, addr = server.accept()

        client_thread = threading.Thread(target=client_handler, args=(client_socket,))

        client_thread.start()

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    # 读取命令行选项
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu",\
                                   ["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o,a in opts:
        if o in ('--h', '--help'):
            usage()
        elif o in ('-l', '--listen'):
            listen = True
        elif o in ('-e', '--execute'):
            execute = a
        elif o in ('-c', '--commandshell'):
            command = True
        elif o in ('-u', '--upload'):
            upload_destination = a
        elif o in ('-t', '--target'):
            target = a
        elif o in ('-p', '--port'):
            port = int(a)
        else:
            assert False, "Unhandled Option"

        if not listen and len(target) and port > 0:

            buffer = sys.stdin.read()

            client_sender(buffer)

        if listen:
            server_loop()

if __name__ == 'main':
    main()