"""
进程 线程 协程（学习资料）
    https://www.jianshu.com/p/3dcad9926073 基本概念文章
    https://www.jianshu.com/p/ba7fa25d3590 C10K问题
    https://zhuanlan.zhihu.com/p/64702600  多进程
    https://www.cnblogs.com/luyuze95/p/11289143.html 多线程
    https://mp.weixin.qq.com/s/Hgp-x-T3ss4IiVk2_4VUrA   多线程和GIL
    https://mp.weixin.qq.com/s/RZSBe2MG9tsbUVZLHxK9NA   多线程同步锁、死锁和递归锁
    https://mp.weixin.qq.com/s/vKsNbDZnvg6LHWVA-AOIMA   多线程之间同步条件、信号量和队列
    https://juejin.cn/post/6971037591952949256#heading-21 协程简单使用
    https://blog.csdn.net/sui_yi123/article/details/81876207  多协程

进程、线程、线程的对比

    进程是资源分配的单位
    线程是操作系统调度的单位
    进程切换需要的资源最大，效率很低
    线程切换需要的资源一般，效率一般（当然了在不考虑GIL的情况下）
    协程切换任务资源很小，效率高
    多进程、多线程根据cpu核数不一样可能是并行的，但是协程是在一个线程中 所以是并发

总结
    进程、线程、协程都是可以完成多任务的，可以根据自己实际开发的需要选择使用
    由于线程、协程需要的资源很少，所以使用线程和协程的几率最大
    开辟协程需要的资源最少
"""