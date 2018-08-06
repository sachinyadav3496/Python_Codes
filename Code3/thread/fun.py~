import threading 
import time

def intro(name,id,dob):
    print("Name = ",name)
    print("ID = ",id)
    print("DOB = ",dob)

class fun(threading.Thread):
    def __init__(self,a,b,c):
        threading.Thread.__init__(self)
        self.t_name=a
        self.t_id=b
        self.t_dob=c
    def run(self):
        print("It is a Thread")
        intro(self.t_name,self.t_id,self.t_dob)
        lock.acquire()
        for i in range(10):
            print("Thread ",self.name)
            print(self.name, "X = ", fun.x)
            time.sleep(2)
            print(self.name,"Y = ",fun.y)
            fun.x +=1
            fun.y+=2
        lock.release()
        print("Exiting Thread ", self.t_name)

fun.x = 0
fun.y = 0
lock = threading.Lock()
t1= fun("one",1,"3-4-96")
t2 = fun("two",2,"4-6-1991")
t3 = fun("three",3,"5-5-97")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("We have done Multithreading")

