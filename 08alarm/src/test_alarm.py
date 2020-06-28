#coding:utf-8
"""
@author: mcfee
@description:
@file: test_alarm.py
@time: 2020/6/24 下午6:28
"""
import signal
import time

def signal_test(sign,frame):
    print("signal {0}".format(time.time()))

def raise_signal():
    print("signal {0}".format(time.time()))


signal.signal(signal.SIGALRM,signal_test)
signal.alarm(5)
print(time.time())
time.sleep(20) #信号可以中断睡眠，但是执行信号句柄后，如果时间不满足条件还会继续睡眠
print(time.time())