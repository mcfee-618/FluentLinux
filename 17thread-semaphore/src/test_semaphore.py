#coding:utf-8
"""
@author: mcfee
@description:
@file: test_semaphore.py
@time: 2020/7/10 下午10:52
"""
import time
import threading,random

s1=threading.Semaphore(1)	#添加一个计数器

num=0
def increment():
    global num
    time.sleep(random.random()/10)
    for i in range(300000):
        s1.acquire()
        num = num + 1
        s1.release()
        #print("thread {0} value is {1}".format(threading.currentThread(),num))

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)
thread3 = threading.Thread(target=increment)
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print(num)