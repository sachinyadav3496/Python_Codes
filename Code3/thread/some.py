import _thread as t
import time
f=0
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
    global f
    f = 1
s = time.time()
t.start_new_thread(sum_squre,("Squre ",))
t.start_new_thread(sum_cube,("Cube ",))

while True:
    if f == 1:
        break
print(time.time()-s)

