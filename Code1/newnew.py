import thread
import time
def print_thread(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count+=1
        print(threadName,":",time.ctime(time.time()))

#try block 
try:
    print("Hello!")
except:
    print("Exception")

