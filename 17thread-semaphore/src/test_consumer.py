#coding:utf-8
"""
@author: mcfee
@description:
@file: test_consumer.py
@time: 2020/7/10 下午10:55
"""
import time
import threading,random

full1=threading.Semaphore(0)	#添加一个计数器
empty1=threading.Semaphore(10)

def produce():
    empty1.acquire()
    full1.release()


def full():
    full1.acquire()
    empty1.release()

thread1 = threading.Thread(target=full)
thread2 = threading.Thread(target=produce)
thread3 = threading.Thread(target=full)
thread4 = threading.Thread(target=produce)
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()