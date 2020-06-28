"""
@author: mcfee
@description:信号处理函数
@file: test_signal.py
@time: 2020/6/23 下午3:45
"""

import signal
import os
import time


def handler(signum, frame):
    print('Signal handler called with signal', signum)


signal.signal(signal.SIGALRM, handler)       # 信号句柄
# signal.signal(signal.SIGALRM,signal.SIG_DFL) # 默认操作：interrupted by signal 14: SIGALRM
# signal.signal(signal.SIGALRM,signal.SIG_IGN) # 忽略信号
signal.alarm(1)
time.sleep(2)
