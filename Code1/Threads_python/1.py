import time
import _thread
def print_time(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count+=1
        print("%s:%s"%(threadName,time.ctime(time.time())))
try:
    _thread.start_new_thread( print_time, ("Thread_1",2) )
    _thread.start_new_thread(print_time,("Thread_2",4) )
except:
    print("Error:unable to create new thread")
while 1:
    pass

