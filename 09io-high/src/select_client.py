#coding:utf-8
"""
@author: mcfee
@description:
@file: select_client.py
@time: 2020/7/30 下午2:36
"""
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("127.0.0.1", 9655))
while True:
    try:
        msg = server.send(bytes("hello".encode("utf-8"))) #BlockingIOError: [WinError 10035] 无法立即完成一个非阻止性套接字操作。
        msg = server.recv(100)
    except BlockingIOError as e:
        print("做些别的")
    else:
        print(msg)
        break
