#coding:utf-8
"""
@author: mcfee
@description:信号处理函数
@file: test_signal.py
@time: 2020/6/23 下午3:45
"""
import signal,os

def test(sign,frame):
    print("信号触发方法")

print(os.getpid())
signal.signal(signal.SIGALRM,test)

signal.alarm(4)
signal.pause()
# pause()悬挂调用进程直至有信号到达。仅当这个信号导致执行句柄函数并且句柄函数返回，pause()调用才返回。
print("收到信号")