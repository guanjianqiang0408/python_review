"""
https://www.cnblogs.com/luyuze95/p/11289143.html 多线程
https://mp.weixin.qq.com/s/Hgp-x-T3ss4IiVk2_4VUrA   多线程和GIL
https://mp.weixin.qq.com/s/RZSBe2MG9tsbUVZLHxK9NA   多线程同步锁、死锁和递归锁
https://mp.weixin.qq.com/s/vKsNbDZnvg6LHWVA-AOIMA   多线程之间同步条件、信号量和队列

Python线程
    定义：
        线程也叫轻量级进程，操作系统能够进行运算调度的最小单位，被包含在进程中，是进程中实际运作单位。可与同属一个进程的其他线程
    共享进程所拥有的全部资源。一个线程可以创建和撤销另一个线程，同一进程中的多个线程之间可以并发执行

    作用：
        线程在程序中是独立、并发的执行流。进程中线程之间的隔离程度要小，它们共享内存、文件句柄和其他进程应有的状态
        线程的划分尺度小于进程，使得多线程程序的并发性高。进程在执行过程中有独立的内存单元，而多线程共享内存，从而极大提高了程序的运行效率
        线程比进程有更高的性能，线程共享环境包括进程代码段、进程的公有数据等，利用这些共享的数据，线程之间容易实现通信
        操作熊创建进程，必须为该进程分配独立内存空间，并分配大量资源。但创建线程更简单，所以使用多线程实现并发比使用多进程性能要高很多。

    优点：
        进程之间不能共享内存，线程可以
        操作系统创建进程，需要为该进程分配系统资源，但创建线程代码小很多。因此，使用多线程实现多任务并发比使用多进程效率高
        Python内置了多线程功能支持，而不是单纯作为底层操作系统的调度方式，从而简化了Python的多线程编程

    实现
        普通创建线程
            使用threading.Thread()方式创建线程函数
        自定义线程类
            继承 threading.Thread()方式创建线程类
        守护线程
            使用setDaemon(True)把所有的子线程都变成了主线程的守护线程，因此当主进程结束后，子线程也随之结束。所以当主线程结束后，整个程序结束
"""
import threading
import time


# 普通创建线程
def thread_function_case(n):
    print(f"task: {n}")
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print(0)
    time.sleep(1)


def call_thread_function():
    """
    普通创建线程方式，threading.Thread()
    """
    t1 = threading.Thread(target=thread_function_case, args=("t1",))
    t2 = threading.Thread(target=thread_function_case, args=("t2",))
    t1.start()
    t2.start()


#自定义线程类
class CustomThread(threading.Thread):
    def __init__(self, n):
        # 重构run函数必须写
        super(CustomThread, self).__init__()
        self.n = n

    def run(self):
        print(f"task: {self.n}")
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print(0)


def call_custome_thread():
    t1 = CustomThread("t1")
    t2 = CustomThread("t2")
    t1.start()
    t2.start()


if __name__ == '__main__':
    # call_thread_function()
    call_custome_thread()
