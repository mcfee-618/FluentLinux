#coding:utf-8
"""
@author: mcfee
@description:
@file: test_condition.py
@time: 2020/7/3 下午3:33
"""
import threading

condtion = threading.Condition()
num=0
def consumer():
    global num
    for i in range(100000):
        condtion.acquire() # 条件变量的使用总是和一个互斥锁结合在一起
        # NOTE:唤醒成功未必满足条件
        while(num==0):
            condtion.wait()
        num-=1
        print("消费者",num)
        condtion.notify_all()
        condtion.release()

def producer():
    global num
    for i in range(100000):
        condtion.acquire() # 条件变量的使用总是和一个互斥锁结合在一起
        # NOTE:唤醒成功未必满足条件
        while (num== 10):
            condtion.wait()
        num+=1
        print("生产者",num)
        condtion.notify_all()
        # 必须持有锁的时候调用raise RuntimeError("cannot notify on un-acquired lock")
        # TODO WHY 移除的过程并非是线程安全的
        condtion.release()


thread1 = threading.Thread(target=producer)
thread2 = threading.Thread(target=consumer)
thread3 = threading.Thread(target=consumer)
thread4 = threading.Thread(target=producer)
thread1.start()
thread2.start()
thread3.start()
thread4.start()
print(num)