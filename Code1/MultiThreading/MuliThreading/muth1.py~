import threading
import time
exitflag = 0
class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting Thread - ",self.name)
        print_time(self.name,self.counter,5)
        print("Exiting Thread - ",self.name)
def print_time(threadName,counter,delay):
    print("thread active count = ",threading.activeCount())
    print("current thread = ",threading.currentThread())
    print("enumerate thread = ",threading.enumerate())
    while counter:
        if exitflag:
            threadName.exit
        time.sleep(delay)
        print("Share data is x = %d , y = %d " %(myThread.x,myThread.y))
        myThread.x+=1
        myThread.y+=1
        print("%s : %s "%(threadName,time.ctime(time.time())))
        counter -= 1
myThread.x = 1
myThread.y = 2
print("thread active count = ",threading.activeCount())
print("current thread = ",threading.currentThread())
print("enumerate thread = ",threading.enumerate())
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting Main Thread")
