"""
    Python 多进程是通过multiprocessing实现，和多线程的threading.Thread差不多，可以利用multiprocessing.Process对象
    创建进程对象。这个进程对象有start run join等方法，其中和线程不同的是对象的守护方式，守护线程是setDeamon，守护进程是daemon属性
    完成的

    多进程实现方式一：
        代码开启了五个子进程执行函数，结果是同时打印的，实现了真正的并行操作，就是多CPU同时执行任务，
        我们知道进程是python中最小的资源分配单元，也就是进程中间的数据，内存是不共享的，每启动一个进程，
        都要独立分配资源和拷贝访问的数据，所以进程的启动和销毁的代价是比较大了，所以在实际中使用多进程，要根据服务器的配置来设定

    多进程实现方式二
        创建一个类继承Process类

    Process类其他方法
        构造方法：
            Process([group [, target [, name [, args [, kwargs]]]]])
            　　group: 线程组
            　　target: 要执行的方法
            　　name: 进程名
            　　args/kwargs: 要传入方法的参数

        实例方法：
        　　is_alive()：返回进程是否在运行,bool类型。
        　　join([timeout])：阻塞当前上下文环境的进程程，直到调用此方法的进程终止或到达指定的timeout（可选参数）。
        　　start()：进程准备就绪，等待CPU调度
        　　run()：strat()调用run方法，如果实例进程时未制定传入target，这star执行t默认run()方法。
        　　terminate()：不管任务是否完成，立即停止工作进程

        属性：
        　　daemon：和线程的setDeamon功能一样
        　　name：进程名字
        　　pid：进程号

    Python多线程通信
        进程是系统独立调度核分配系统资源（CPU、内存）的基本单位，进程之间是相互独立的，
        每启动一个新的进程相当于把数据进行了一次克隆，子进程里的数据修改无法影响到主进程中的数据，
        不同子进程之间的数据也不能共享，这是多进程在使用中与多线程最明显的区别。
        但是难道Python多进程中间难道就是孤立的吗？当然不是，python也提供了多种方法实现了多进程中间的通信和数据共享（可以修改一份数据）

        进程队列Queue
            Queue在多线程中也说到过，在生成者消费者模式中使用，是线程安全的，是生产者和消费者中间的数据管道，那在python多进程中，
            它其实就是进程之间的数据管道，实现进程通信

        管道Pipe
            管道Pipe和Queue的作用大致差不多，也是实现进程间的通信

        Manager
            Queue和Pipe只是实现了数据交互，并没实现数据共享，即一个进程去更改另一个进程的数据。那么就要用到Managers

        进程池
            进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，
            那么程序就会等待，直到进程池中有可用进程为止。就是固定有几个进程可以使用。
            进程池中有两个方法：
                apply：同步，一般不使用
                apply_async：异步
            对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

        进程池map方法
            import os
            import PIL

            from multiprocessing import Pool
            from PIL import Image

            SIZE = (75,75)
            SAVE_DIRECTORY = \'thumbs\'

            def get_image_paths(folder):
                return (os.path.join(folder, f)
                        for f in os.listdir(folder)
                        if \'jpeg\' in f)

            def create_thumbnail(filename):
                im = Image.open(filename)
                im.thumbnail(SIZE, Image.ANTIALIAS)
                base, fname = os.path.split(filename)
                save_path = os.path.join(base, SAVE_DIRECTORY, fname)
                im.save(save_path)

            if __name__ == \'__main__\':
                folder = os.path.abspath(
                    \'11_18_2013_R000_IQM_Big_Sur_Mon__e10d1958e7b766c3e840\')
                os.mkdir(os.path.join(folder, SAVE_DIRECTORY))

                images = get_image_paths(folder)

                pool = Pool()
                pool.map(creat_thumbnail, images) #关键点，images是一个可迭代对象
                pool.close()
                pool.join()
        这段代码的主要工作就是将遍历传入的文件夹中的图片文件，一一生成缩略图，并将这些缩略图保存到特定文件夹中。
        这我的机器上，用这一程序处理 6000 张图片需要花费 27.9 秒。 map 函数并不支持手动线程管理，反而使得相关的 debug 工作也变得异常简单。
        map在爬虫的领域里也可以使用，比如多个URL的内容爬取，可以把URL放入元祖里，然后传给执行函数。

"""
import random
import time
from multiprocessing import Process, Queue, Pipe, Manager, Pool


def func(name):
    print(f"测试 {name} 多进程")


def construct_process_type_one():
    """
    多进程实现方式一
    :return:
    """

    process_list = []
    for i in range(5):
        # 实例化进程对象
        p = Process(target=func, args=(f"Python{i}",))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    print("结束测试")


# 继承Process类
class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"测试{self.name}多进程")


def construct_process_type_two():
    process_list = []
    for i in range(5):
        # 实例化进程
        p = MyProcess(f"Python{i}")
        p.start()
        process_list.append(p)
    for process in process_list:
        process.join()
    print("结束测试")


def process_queue_case(q, i):
    print(f"子进程{i}, 开始put数据")
    q.put(f"我是{i}, 通过queue通信")


def call_queue_function():
    q = Queue()
    process_list = []
    for i in range(3):
        # 参数中要把q对象传给执行函数，这样子进程才能和主进程用Queue通信
        p = Process(target=process_queue_case, args=(q, i, ))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    print("主进程获取Queue数据")
    print(q.get())
    print(q.get())
    print(q.get())
    print("结束测试")
    # 通过执行可以看到我们主进程中可以通过Queue获取子进程中put数据，实现进程间他通信


def process_pipe_case(conn):
    print("子进程发送消息")
    conn.send("您好，主进程")
    print("子进程接收消息")
    print(conn.recv())
    conn.close()


def call_pipe_function():
    # pipe实例化生成一个双向管道
    conn1, conn2 = Pipe()
    # conn2传给子进程
    p = Process(target=process_pipe_case, args=(conn2,))
    p.start()
    print("主进程接收消息")
    print(conn1.recv())
    print("主进程发送消息")
    conn1.send("您好，子进程")
    p.join()
    print("结束测试")
    # 可以看到主进程和子进程可以相互发送消息


def process_manager_case(dic, lis, index):
    dic[index] = "a"
    dic["2"] = "b"
    lis.append(index)


def call_manager_function():
    with Manager() as manager:
        # 注意，字典声明方式不能直接通过{}定义
        dic = manager.dict()
        l = manager.list(range(5))
        process_list = []
        for i in range(10):
            p = Process(target=process_manager_case, args=(dic, l, i))
            p.start()
            process_list.append(p)

        for process in process_list:
            process.join()

        print(dic)
        print(l)
        # 可以看到主进程定义了一个字典和一个列表，在子进程中，可以添加和修改字典的内容，在列表中插入新的数据
        # 实现进程间的数据共享，即可以共同修改同一份数据


def process_pool_case(name):
    print(name)
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print(f"spend time: {end - start}")


def call_pool_function():
    pool = Pool(5)
    for i in range(10):
        pool.apply_async(func=process_pool_case, args=(i,))

    pool.close()
    pool.join()
    print("结束测试")


if __name__ == '__main__':
    # construct_process_type_one()
    # construct_process_type_two()
    # call_queue_function()
    # call_pipe_function()
    # call_manager_function()
    call_pool_function()