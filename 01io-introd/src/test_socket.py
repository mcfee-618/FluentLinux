#coding:utf-8
"""
@author: mcfee
@description:
@file: test_socket.py
@time: 2020/7/22 下午7:09
"""
import socket
data = ""
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))
# 发送数据:
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n'.encode("utf-8"))
s.setblocking(0)  # 设置非阻塞
buffer = []
while True:
    # 每次最多接收1k字节:
    try:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
        print(d)
    #如果kernel中的数据还没有准备好，那么它并不会block用户进程，而是立刻返回一个error。
    except Exception as e:
        print("干其他的工作")
s.close()
