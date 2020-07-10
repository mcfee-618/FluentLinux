## 条件变量

当某些程序状态不符合要求时，允许线程进入休眠状态，休眠直到另一个线程唤醒。

## 条件变量实现方案

1. 自旋等待 2.休眠直到另一个线程唤醒

## 需要注意的点

1. 调用条件变量的API必须持有锁
2. while循环判断条件是否满足而不是if
3. 单个条件或者多个条件，一个条件一个队列，唤醒指定的线程需要建立多个条件变量


## 条件变量【等待队列+互斥锁+下面这个特别的锁】
```
PyThread_type_lock
PyThread_allocate_lock(void)
{
    /* 申请内存 */
    lock = (sem_t *)malloc(sizeof(sem_t));

    if (lock) {
        /*
        初始化
        value 为1，表明这个锁是 unlocked，被该进程的所有线程共享
        */
        status = sem_init(lock,0,1);
        CHECK_STATUS("sem_init");     
    }
}

#include <semaphore.h>
int sem_init(sem_t *sem, int pshared, unsigned int value);

pshared决定了这个信号量是在进程中共享还是在线程中共享。

pshared 为 非零值，那么不同进程中都可以共享
pshared 为 零值，那么在当前进程的线程中共享。
```