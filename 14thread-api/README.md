

##LOCK【互斥变量】

* 互斥变量主要用于多个线程竞争访问某个共享资源。多线程程序中，共享数据的读写必须是原子的。也就是说，一个线程在读或写某个共享数据期间，不希望受到其他线程的干扰，否则将发生不可预知的结果。每次只有一个线程执行，也就是互斥执行。
* 互斥变量只有两种状态：已锁或未锁，故也称互斥变量为互斥锁。对于“锁”这个概念我们应当很熟悉，互斥变量表示的逻辑概念就是锁。线程对一个互斥变量加锁，只有在该变量处于未锁状态时才能成功返回，否则将受阻直至互斥变量被释放。试图获得同一个互斥变量的其他线程将被阻塞。
* 已锁住的互斥变量必须由获得它的线程释放才能恢复为未锁状态。当它被释放后，等待获得该互斥变量的线程之一将获得成功。


```
# 一旦一个线程获得一个锁，会阻塞随后尝试获得锁的线程，直到它被释放；
pthread_mutex_t lock;
pthread_mutex_lock(&lock);
x = x + 1; # 临界区
pthread_mutex_unlock(&lock);
```

* 处理上锁失败的情况：线程对互斥变量上锁不成功时，系统可以有三种方法来使线程阻塞：a）立即阻塞，即释放线程占用的CPU资源，使其从运行状态进入等待状态；b）让线程在一个循环中轮询查看是否能获得互斥变量，如果一段时间后仍未成功，则进入阻塞；c）在一个循环中不断地轮询，直到获得互斥变量。
    * 单处理机系统通常采用第一种方法，因为系统只有一个处理机，轮询既浪费CPU时间，也妨碍占有互斥变量的线程释放该互斥变量。
    * 多处理机或多核系统可以使用三种方法之一，一般多采用立即阻塞或者轮询一段时间后阻塞。    

![avatar](static/1.jpg)

* spin锁:

##Condition Variables

Condition variables are useful when some kind of signaling must take place between threads, if one thread is waiting for another to do something before it can continue. 

```
int pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex);
int pthread_cond_signal(pthread_cond_t *cond);
```

条件变量总是与某种类型的锁对象相关联，当调用上述任何一个例程时，这把锁应该锁住。

##相关链接

https://www.zhihu.com/question/332113890/answer/1052024052