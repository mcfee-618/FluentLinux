#coding:utf-8
"""
@author: mcfee
@description:
@file: test_lock.py
@time: 2020/7/2 下午6:24
"""
import threading
import time
import random

num = 0

lock=threading.Lock()

def increment():
    global num
    time.sleep(random.random()/10)
    for i in range(300000):
        lock.acquire()
        num = num + 1
        lock.release()
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
#每次运行会得到不同的结果，多个线程可能导致竞争状态,
#其中的一个办法就是上锁，这保证同一个时间只有一个线程获得锁，只有一个线程能够进入临界区