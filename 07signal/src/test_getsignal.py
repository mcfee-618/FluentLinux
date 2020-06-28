# coding:utf-8
import signal

for name in dir(signal):
    if name[:3] == "SIG" and name[3] != "_":
        signum = getattr(signal, name)
        # 查看信号的操作
        gsig = signal.getsignal(signum)
        print(name, gsig)
