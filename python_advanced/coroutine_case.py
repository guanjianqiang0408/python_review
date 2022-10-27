"""
协程
    定义：
        微线程，也称用户级线程，在不开辟线程的基础上完成多任务，也就是单线程基础下完成多任务，多任务按照一定顺序交替执行，通俗理解只要函数中
    有关键字yield就是协程

    作用：
        协程只有在非常有限制的情况下，才有用处，在单进程单线程任务中的交互中才会使用到协程

    使用场景
        需求：大量用户发送请求，后台异步处理请求，客户端反复通过接口查询自己所发的请求是否达到预期阶段
        实现逻辑：
            - 同步方式（多线程）
            - 异步方式（协程，一般不同此方法，仅做了异步等待协程切换时使用）
                创建多个协程对象，每个协程函数： 同步请求- 异步等待- 同步查询- 异步等待- 同步查询（循环）

    实现
        关键字yield函数
            协程之间执行任务按照一定顺序交替执行

        greenlet
            为了更好使用协程来完成多任务，Python中greenlet模块进行了封装，从而使得切换任务变得更简单

        gevent
            内部封装了greenlet，原理是当一个greenlet遇到IO操作时，例如访问网络，就自动切换到其他greenlet，等到IO操作完成，再在适当时候切换回来继续执行
        由于IO操作非常耗时。经常导致程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO

        给程序打补丁
            gevent . monkey 让gevent框架识别耗时操作

        注意：
            当前程序是一个死循环并且还有耗时操作，就不需要加上join方法，因为程序需要一直运行不会退出

        gevent.joinall()
            如果使用协程过多，想启动它们就要逐个使用join方法去阻塞主线程，这样代码会过于冗余，可以使用gevent.joinall()方法启动需要使用的协程

"""
# 关键字yield
import time


def work1():
    while True:
        print("work1")
        yield
        time.sleep(1)


def work2():
    while True:
        print("work2")
        yield
        time.sleep(1)


def call_yield_func():
    while True:
        next(work1())
        next(work2())


# 使用greenlet
import greenlet


def work3():
    for i in range(5):
        print("work3")
        time.sleep(1)
        # 切换到协程2执行任务
        g2.switch()


def work4():
    for i in range(5):
        print("work4")
        time.sleep(1)
        # 切换到协程1执行任务
        g1.switch()


# gevent
import gevent


def work5(n):
    for i in range(n):
        # 获取当前协程
        print(gevent.getcurrent(), i)


def call_gevent_func():
    g1 = gevent.spawn(work5, 5)
    g2 = gevent.spawn(work5, 5)
    g3 = gevent.spawn(work5, 5)
    g1.join()
    g2.join()
    g3.join()

    """
         通过运行结果上看，3个greenlet是依次运行，而不是交替运行
    """


def work6(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # 用来模拟一个耗时操作，注意不是time模块中的sleep
        gevent.sleep(1)


def call_gevent_shift_func():
    g1 = gevent.spawn(work6, 5)
    g2 = gevent.spawn(work6, 5)
    g3 = gevent.spawn(work6, 5)
    gevent.joinall([g1, g2, g3])
    """
        通过运行结果来看，当其中一个greenlet等待的时候，就会切换到其他greenlet。
    """


# # 给程序打补丁，让gevent框架识别耗时操作
# from gevent import monkey
# monkey.patch_all()


if __name__ == '__main__':
    # 关键字yield
    # call_yield_func()

    # greenlet
    # 创建协程指定对应的任务
    # g1 = greenlet.greenlet(work3)
    # g2 = greenlet.greenlet(work4)
    #
    # # 切换到第一个协程执行对应任务
    # g1.switch()

    # gevent
    # call_gevent_func()
    call_gevent_shift_func()

