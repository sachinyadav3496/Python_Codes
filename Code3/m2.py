import _thread as t
import time
def a(name):
    print("Name:",name)
    l = 0
    for i in range(10):
        l = l+(i*i)
        time.sleep(2)
    print("sum = ", l)
def b(name):
    print("Name:",name)
    k = 0
    for i in range(10):
        k = k+(i*i*i)
        time.sleep(2)
    print("sum = ", k)

s = time.time()
t.start_new_thread(a,("hello",))
t.start_new_thread(b,("bye",))
print(time.time()-s)

