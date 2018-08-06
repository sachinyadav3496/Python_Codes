import threading
import time
f = 0
class newThread(threading.Thread):
    def __init__(self,tno,tname,counter):
        threading.Thread.__init__(self)
        self.tno = tno
        self.name = tname
        self.counter = counter
    def t(self,tname,c,d):
        while c:
            if f:
                tname.exit
            time.sleep(delay)
            print("%s : %s"%(tname,time.ctime(time.time())))
            c -= 1
    def run(self):
        print("Strarting Thread = ",self.name)
        t(self.name,self.counter,5)
        print("Exiting Thread - ",self.name)
thread1 = newThread(1,"one",1)
thread2 = newThread(2,"two",2)
thread1.start()
thread2.start()
print("Exiting Main Thread")
