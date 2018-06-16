import threading
from threading import Thread
import time

def hello(name,t):
    for var in range(10):
        print("hello ",name)

        time.sleep(t)


t1 = Thread(target=hello, args=('python',2))
t2 = Thread(target=hello,args=('mar java',.5))
t3 = Thread(target=hello,args=('mit java',1))
t4 = Thread(target=hello,args=('lut java',.2))


print("welcome to the world of threads - ")

t1.start()
t2.start()
t3.start()
t4.start()

t4.join()
print("t4 is finished")

t1.join(5)
print("t1 is finished")
