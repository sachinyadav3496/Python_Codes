import _thread as th
import time

def somefunction(name,f):
  for i in range(5):
    print("This is %s on %s "%(name,time.ctime()))
    time.sleep(f)

t1 = th.start_new_thread(somefunction,("thread1",2,))
t2 = th.start_new_thread(somefunction,("thread2",3,))
t3 = th.start_new_thread(somefunction,("thread3",4,))
while True:
    t1.join()
    t2.join()
    t3.join()
