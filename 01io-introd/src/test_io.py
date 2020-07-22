#coding:utf-8
"""
@author: mcfee
@description:
@file: test_io.py
@time: 2020/7/22 下午4:05
"""
import time
import os
file = open("1.txt","w",buffering=20)

file.write("22")
file.write("333")
#file.flush()
print(os.getpid())
time.sleep(1000)
