# import threading
# import time
#
# def helloworld():
#     time.sleep(2)
#     print("hello world")
# t=threading.Thread(target=helloworld)
# t.start()
# print("main thread")


# 同种任务并行

# import threading
# import time
#
# def helloworld(id):
#     time.sleep(2)
#     print("thread %d helloworld" % id )
#
# for i in range(5):
#     t=threading.Thread(target=helloworld,args=(i,))
#     t.start()
# print("main thread")


# 多线程访问网页

# import threading
# from urllib import request
# def get():
#     url="https://www.jd.com/"
#     r=request.urlopen(url)
#     print(r.code)
#
# for i in range(100):
#     t=threading.Thread(target=get)
#     t.start()


# 线程间同步
# import threading,time
# count=0
#
# def adder():
#     global count
#     count+=1
#     time.sleep(0.5)
#     count+=1
#
# threads=[]
# for i in range(1000):
#     thread=threading.Thread(target=adder)
#     threads.append(thread)
#
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
# print(count)
#
#加锁
# import threading, time
#
# count = 0
#
# def adder(addlock):
#     global count
#     addlock.acquire()
#     count = count + 1
#     time.sleep(0.1)
#     count = count + 1
#     addlock.release()
#
# addlock = threading.Lock()
# threads = []
# for i in range(100):
#     thread = threading.Thread(target=adder,args=(addlock,))
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()
#
# print(count)


# 使用with加锁
#
# import threading,time
# count=0
# def adder(addlock):
#     global count
#     with addlock:
#         count +=1
#         time.sleep(0.1)
#         count +=1
#
# addlock=threading.Lock()
# threads=[]
# for i in range(100):
#     thread=threading.Thread(target=adder,args=(addlock,))
#     thread.start()
#     threads.append(thread)
# for thread in threads:
#     thread.join()
#
# print(count)


# queue模块
# import threading,queue
# import time
#
# numconsumers=20
# numproducers=20
# nummessages=4
#
# lock=threading.Lock()
# dataqueue=queue.Queue()
#
# def producer(idnum):
#     for msgum in range(nummessages):
#         dataqueue.put("producer id =%d,count=%d"%(idnum,msgum))
#
# def consumer(idnum):
#     while True:
#         try:
#             data=dataqueue.get(block=False)
#         except queue.Empty:
#             break
#         with lock:
#             print("consumer",idnum,"got=>",data)
#         time.sleep(0.1)
#         dataqueue.task_done()
#
# if __name__ == '__main__':
#     consumerThreads=[]
#     producerTheads=[]
#     for i in range(numproducers):
#         t=threading.Thread(target=producer,args=(i,))
#         producerTheads.append(t)
#         t.start()
#     for i in range(numconsumers):
#         t=threading.Thread(target=consumer,args=(i,))
#         consumerThreads.append(t)
#         t.start()
#     dataqueue.join()


# 多进程--multiprocessing

# import os
# from multiprocessing import Process,Lock
#
# def whoami(label,lock):
#     msg = '%s: name:%s, pid:%s'
#     with lock:
#         print(msg % (label, __name__,os.getpid()))
#
# if __name__ == '__main__':
#     lock=Lock()
#
#     for i in range(5):
#         p=Process(target=whoami,args=("child",lock))
#         p.start()
#


# 队列
# from multiprocessing import Process,Queue,Lock
# import queue
# import time
#
# numconsumers = 20
# numproducers = 20
# nummessages = 4
#
# def producer(idnum,dataQueue):
#     for  msgnum in range(nummessages):
#         dataQueue.put("producer id=%d, count=%d" % (idnum, msgnum))
#
# def consumer(idnum,dataqueue,lock):
#     while True:
#         try:
#             data=dataqueue.get(block=False)
#         except queue.Empty:
#             break
#         with lock:
#             print("consumer", idnum, "got => ", data)
#         time.sleep(0.1)
#
# if __name__ == '__main__':
#     lock=Lock()
#     dataQueue=Queue()
#     consumers=[]
#     producers = []
#
#     for i in range(numproducers):
#         p=Process(target=producer,args=(i,dataQueue))
#         producers.append(p)
#         p.daemon=True
#         p.start()
#     for i in range(numconsumers):
#         p=Process(target=consumer,args=(i,dataQueue,lock))
#         consumers.append(p)
#         p.daemon=True
#         p.start()
#     for p in consumers:
#         p.join()
#     for p in producers:
#         p.join()

# 进程池

# from multiprocessing import Pool
# import time
#
# def func(num):
#     print("hello world %d" % num)
#     time.sleep(3)
# if __name__ == '__main__':
#     pool=Pool(processes=5)#设置进程运行的次数--processes
#     for i in range(100):
#         pool.apply_async(func,(i,))# apply顺序# apply_async并发
#     pool.close()
#     pool.join()

# pool.map
# from multiprocessing import Pool
# import time
# def f(x):
#     time.sleep(0.5)
#     return x*x
# if __name__ == '__main__':
#     with Pool(5)as p:
#         print(p.map(f,range(10)))


