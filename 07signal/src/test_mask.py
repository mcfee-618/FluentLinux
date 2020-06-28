#coding:utf-8
"""
@author: mcfee
@description:阻塞信号
@file: test_signal.py
@time: 2020/6/23 下午3:45
"""
import signal
import time

def test(sign,frame):
    print("触发方法")

signal.signal(signal.SIGALRM,test)
signal.pthread_sigmask(signal.SIG_BLOCK,[signal.SIGALRM])   # 设置信号屏蔽
signal.alarm(1)
time.sleep(2)
print(signal.sigpending())
signal.pthread_sigmask(signal.SIG_UNBLOCK,[signal.SIGALRM]) # 解除信号屏蔽
###解除信号屏蔽后，信号就交付了



