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
        主线程等待子线程结束
            为了让守护线程执行结束后，主线程在结束，可以使用join方法，让主线程等待子线程执行
        多线程共享全局变量
            线程是进程的执行单元，进程是系统分配资源的最小单元，所以在同一个进程中的多线程是共享资源的
        互斥锁
            避免多个线程同时修改同一条数据时可能出现脏数据，所以出现了线程锁。即同一时刻允许一个线程执行操作。线程锁用于锁定资源。
            由于线程间是进行随机调度，如果有多个线程同时操作一个对象，如果没有保护好被调用对象，会造成程序结果不可预期，即“线程不安全”，为了避免这种情况
        就出现了互斥锁

        同步锁
            todo

        队列
            todo

        递归锁
            RLock和Lock用法一摸一样，但它支持嵌套，在多个锁没有释放的时候一般使用RLock

        信号量
            互斥锁同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据

        事件
            python线程的事件用于主线程控制其他线程的执行，事件是一个简单的线程同步对象，主要提供一下几个方法
                clear 将flag设置为False
                set 将flag设置为True
                is_set 判断是否设置了flag
                wait 会一直监听flag，如果没有检测到flag就一直处于阻塞状态
            事件处理机制：全局定义一个flag，当flag为False，event.wait()就会阻塞，当flag为True，event.wait()便不在阻塞

    GIL(Global Interpreter Lock) 全局解释器锁
        非python环境中，单核情况下，同时只能有一个任务执行。多核时可以支持多个线程同时执行。但是在python中，无论多少核，同时
    只能执行一个线程，原因就是GIL的存在导致的
        GIL来源时设计之初的考虑，为了数据安全所作的决定，某个线程想要执行，必须先拿GIL，且只有一个，没有拿到的，就不允许进行CPU执行。
        Python多线程工作过程：
            获取公共数据
            申请GIL
            python解释器调用os原生线程
            os操作cpu执行运算
            当该线程执行时间到后，无论运算是否已经执行完，GIL都被要求释放
            由其他进程重复上述步骤
            等其他进程执行完，又切换到之前的进程，整个过程时每个线程执行自己的原酸，当执行时间到就进行切换
        Python针对不同类型的代码执行效率也不同
            CPU密集型代码，计算工作多，ticks技术很快达到阈值，然后触发GIL释放与再竞争（多线程来回切换当然需要资源），所以python下
        多线程对CPU密集型代码并不友好
            IO密集代码（文件处理，网络爬虫），多线程能够有效提升效率（单线程下IO操作会进行IO等待，造成不必要的时间浪费，而开启多线程能在线程A等待
        的时候，自动切换到线程B，可以不浪费CPU资源，从而能提升程序执行效率），所以Python的多线程对IO密集型代码比较友好
    多线程使用建议
        Python下想要充分利用多核CPU，就用多进程。因为每个进程有独立的GIL，互不干扰，这样就可以真正意义上的并行执行，在python中，多进程
    的执行效率优于多线程（仅针对多核CPU而言）
"""
import threading
import time
from threading import Thread, Lock


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


# 守护线程
def call_setDaemon():
    """
    设置守护线程后，主线程结束，子线程结束
    :return:
    """
    t = threading.Thread(target=thread_function_case, args=("t1",))
    # 把子进程设置为守护线程，必须在start之前设置
    t.setDaemon(True)
    t.start()
    print("end")


# 主线程等待子线程结束 join
def master_thread_wait_slave_thread():
    t = threading.Thread(target=thread_function_case,args=("t1",))
    t.setDaemon(True)
    t.start()
    # 设置主线程等待子线程结束
    t.join()
    print("end")


num = 100


# 多线程共享全局变量
def mutil_thread_func1():
    global num
    for i in range(3):
        num += 1
    print(f"in func1 num is: {num}")


def mutil_thread_func2():
    global num
    print(f"in func2 num is: {num}")


def mutil_thread_public_source():
    """
    多线程共享全局变量
    :return:
    """
    t1 = threading.Thread(target=mutil_thread_func1)
    t1.start()
    time.sleep(1)
    t2 = threading.Thread(target=mutil_thread_func2)
    t2.start()

# 互斥锁
n=100
lock = Lock()
l = []


def lock_func():
    global n
    lock.acquire()
    temp = n
    time.sleep(0.1)
    n = temp - 1
    print(n)
    lock.release()


def call_lock():
    for i in range(100):
        p = Thread(target=lock_func)
        l.append(p)
        p.start()

    for p in l:
        p.join()


# 递归锁
gl_num = 0
rlock = threading.RLock()


def rlock_func(lock):
    global gl_num
    rlock.acquire()
    gl_num += 1
    time.sleep(1)
    print(gl_num)
    rlock.release()


def call_rlock():
    for i in range(100):
        t = threading.Thread(target=rlock_func, args=(rlock,))
        t.start()


# 信号量
def simple_variable(n, semaphore):
    semaphore.acquire()
    time.sleep(1)
    print(f"run the thread： {n}")
    semaphore.release()


def call_simple_variable():
    new_num = 0
    # 声明允许最多n个线程同时运行
    semaphore = threading.BoundedSemaphore(5)
    for i in range(22):
        t = threading.Thread(target=simple_variable, args=(i, semaphore,))
        t.start()
    while threading.active_count() != 1:
        pass
    else:
        print("all thread ends")


# event 模拟红绿灯
event = threading.Event()


def lighter():
    count = 0
    event.set() # 初始值为绿灯
    while True:
        if 5 < count < 10:
            event.clear() # 红灯，清楚标志位
            print("light is red")
        elif count > 10:
            event.set() # 绿灯，设置标志位
        else:
            print("light is green")
        time.sleep(1)
        count += 1


def cars(name):
    while True:
        # 判断是否设置了标志位
        if event.is_set():
            print(f"[{name}]cars running")
            time.sleep(1)
        else:
            print(f"[{name}]see ligth is red, cars stoping")
            event.wait()
            print(f"[{name}]see light is green, cars running")


def didi_func():
    light = threading.Thread(target=lighter)
    light.start()

    car = threading.Thread(target=cars, args=("Tycor",))
    car.start()


if __name__ == '__main__':
    # call_thread_function()
    # call_custome_thread()
    # call_setDaemon()
    # master_thread_wait_slave_thread()
    # mutil_thread_public_source()
    # call_lock()
    # call_rlock()
    # call_simple_variable()
    didi_func()