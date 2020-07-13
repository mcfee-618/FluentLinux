#coding:utf-8
"""
@author: mcfee
@description:
@file: test_wait.py
@time: 2020/7/13 上午11:42
"""
import os

num=2
value=os.fork()
## 后面就要分叉了，分为父进程和子进程
if(value>0):
    os.wait()
    num=33
    print(num,os.getpid())
else:
    print(num,os.getpid())