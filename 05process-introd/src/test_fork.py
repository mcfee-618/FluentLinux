#coding:utf-8
"""
@author: mcfee
@description:fork函数使用
@file: test_fork.py
@time: 2020/7/13 上午10:36
"""
import os

num=2
value=os.fork()
## 后面就要分叉了，分为父进程和子进程
if(value>0):
    num=33
    print(num,os.getpid())
    while True:
        pass
else:
    print(num,os.getpid())
    # 一直处于僵尸状态
    # changba-176       6542   0.0  0.0        0      0   ??  Z    10:39上午   0:00.00 (Python)
