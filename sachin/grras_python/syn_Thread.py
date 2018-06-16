#!/bin/usr/python3
import threading
import time

class myThread( threading.Thread ):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting "+self.name)
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        threadLock.release()
    def print_time(threadName,delay,counter):
        while counter:
            time.sleep(delay)
            print("%s:%s"%(threadName,time.ctime(time.time)))
            count -= 1
threadLock=threading.Lock()
print(threadLock)
threads = []
thread1 = myThread(1,"Thread_1",1)
thread2 = myThread(2,"Thread_2",2)
thread1.start()
thread2.start()
threads.append(thread1)
threads.append(thread2)
print(threads)
for t in threads:
    t.join()
print("Exist main Thread")
