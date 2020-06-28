#coding:utf-8
"""
@author: mcfee
@description:
@file: test_setitimer.py
@time: 2020/6/28 下午4:16
"""
import os,signal,time


def signal_test(sign,frame):
    print("signal end  {0}".format(time.time()))

print("siganl start {0}".format(time.time()))
signal.signal(signal.SIGALRM,signal_test)
signal.setitimer(signal.ITIMER_REAL,1)
#signal.setitimer(signal.ITIMER_VIRTUAL,1)
signal.signal(signal.SIGALRM,signal_test)
time.sleep(5)