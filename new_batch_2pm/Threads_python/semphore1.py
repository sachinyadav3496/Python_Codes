import threading as th
import time
import random
x = 0

def change():
    global x 
    x += 1
    time.sleep(random.randint(1,3))
"""change()
print(x)
change()
print(x)

"""
def new():
    for var in range(1000):
        change()

one = th.Thread(target=new)
two = th.Thread(target=new)
one.start()
two.start()

one.join()
two.join()

print("Value of x = ",x) 
