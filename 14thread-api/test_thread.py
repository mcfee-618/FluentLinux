#coding:utf-8
"""
@author: mcfee
@description:
@file: test_thread.py
@time: 2020/7/2 下午5:18
"""
import threading

local1 = threading.local()
def run(a,b):
    local1.x=4 #线程本地变量，每个线程一份
    print(local1.x)
    for i in range(10):
        print(a+b)
    return "出口"

thread1 = threading.Thread(target=run,args=[2,3])
thread1.start()
print(thread1.join()) #  """Wait until the thread terminates.
print(thread1.isAlive())
print(thread1.ident)
print(thread1.isDaemon())


#线程本地数据
#线程本地数据是特定线程的数据。管理线程本地数据，只需要创建一个 local （或者一个子类型）的实例并在实例中储存属性：

# mydata = threading.local()
# mydata.x = 1
