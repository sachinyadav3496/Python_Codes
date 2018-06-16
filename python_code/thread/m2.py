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
        sum_squre(self.name)

class cube(t.Thread):
    def __init__(self,name = "thread"):
        t.Thread.__init__(self)
        self.name = name
    def run(self):
        sum_cube(self.name)

t1 = squre("Sum of Squre")
t2 = cube("Sum of Cubes")

t = time.time()
t1.start()
t2.start()


t1.join()
t2.join()
s = time.time()
print("Our Program Take time = ",s-t," secs")


