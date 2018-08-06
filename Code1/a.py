import threading
import time
def print_time(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        print("%s:%s"%(threadName,time.ctime(time.time())))
        count+=1
try:
    threading.run(print_time,("Thread_1",2))
    threading.run(print_time,("Thread_2",4))
except:
    print("Error: unable to create thread")
print_time("sachin",1)

