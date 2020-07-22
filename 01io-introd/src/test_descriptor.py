#coding:utf-8
"""
@author: mcfee
@description:
@file: test_descriptor.py
@time: 2020/7/22 下午4:55
"""
import os
import sys

os.close(sys.stdin.fileno())
file1=os.open("1.txt",os.O_CREAT)
print(file1)
#os.close(file1)
file1=os.open("2.txt",os.O_CREAT)
print(file1)

#open调用成功返回一个新的文件描述字，返回的一定是当前最小的未使用的描述字【每个进程有自己的文件描述字】