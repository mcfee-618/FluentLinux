#coding:utf-8
"""
@author: mcfee
@description:
@file: sign_client.py
@time: 2020/7/30 上午10:30
"""
import socket
import signal
import os
import fcntl


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("127.0.0.1", 9655))
server.setblocking(False)
fd= server.fileno()

def test1(*args):
    print(server.recv(100))
    print("kkk")
    exit()

signal.signal(signal.SIGIO,test1)
# 设置信号处理函数
fcntl.fcntl(fd,fcntl.F_SETOWN, os.getpid()) # 获得／设置异步I/O所有权,设置将接收SIGIO和SIGURG信号的进程id或进程组id
fcntl.fcntl(fd,fcntl.F_SETFL, os.O_ASYNC|os.O_NONBLOCK) # 当I/O可用的时候,允许SIGIO信号发送到进程组,例如:当有数据可以读的时候
# 当输入缓存中的输入数据就绪时（输入数据可读），内核向用F_SETOWN来绑定的那个进程发送SIGIO信号
# file set flag
while True:
    try:
        input()
    except Exception as e:
        pass
    print("222")


# fcntl()针对(文件)描述符提供控制.参数fd是被参数cmd操作(如下面的描述)的描述符.针对cmd的值,fcntl能够接受第三个参数（arg）
# 获得／设置异步I/O所有权(cmd=F_GETOWN或F_SETOWN).
# 获得／设置文件状态标记(cmd=F_GETFL或F_SETFL).