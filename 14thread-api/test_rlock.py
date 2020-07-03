#coding:utf-8
"""
@author: mcfee
@description:
@file: test_rlock.py
@time: 2020/7/3 上午11:04
"""
import threading

lock = threading.RLock()# 可重入锁
lock.acquire()
lock.acquire()

"""
这两种琐的主要区别是：RLock允许在同一线程中被多次acquire。而Lock却不允许这种情况。注意：如果使用RLock，那么acquire和release必须成对出现，即调用了n次acquire，必须调用n次的release才能真正释放所占用的琐。
"""