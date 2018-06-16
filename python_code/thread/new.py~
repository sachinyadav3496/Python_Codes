import threading as t
import time

def sum_squre(name):
    print("Name:",name)
    l = 0
    for i in range(10):
        l = l+(i*i)
        time.sleep(.2)
    print("sum of squre = ", l)
def sum_cube(name):
    print("Name:",name)
    k = 0
    for i in range(10):
        k = k+(i*i*i)
        time.sleep(.2)
    print("sum of cube = ", k)
class squre(t.Thread):
    def __init__(self,name = "thread"):
        t.Thread.__init__(self)
        self.name = name
    def run(self):
        lock.acquire()
        sum_squre(self.name)
        lock.release()

class cube(t.Thread):
    def __init__(self,name = "thread"):
        t.Thread.__init__(self)
        self.name = name
    def run(self):
        lock.acquire()
        sum_cube(self.name)
        lock.release()
lock = t.Lock()
t1 = squre("Sum of Squre1")
t2 = squre("Sum of Squre2")
t3 = cube("Sum of Cubes1")
t4 = cube("Sum of Cubes2")

t = time.time()
t1.start()
t2.start()
t3.start()
t4.start()


t1.join()
t2.join()
t3.join()
t4.join()
s = time.time()
print("Our Program Take time = ",s-t," secs")


