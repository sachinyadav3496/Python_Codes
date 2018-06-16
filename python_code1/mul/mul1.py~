import time
import threading
def squre(n):
    print("Calcultaing the squre of numbers - ")
    for k in n:
        time.sleep(.2)
        print("Squre of "+str(k)+" = "+str(k*k))

def cube(n):
    print("Calcultaing the cube of numbers - ")
    for i in n:
        time.sleep(.2)
        print("cube of "+str(i)+" = "+str(i*i*i))
arr=(1,2,3,4,5,6)
t=time.time()
t1=threading.Thread(target=squre,args=(arr,))
t2=threading.Thread(target=cube,args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Done Processing in "+str(time.time()-t)+" seconds")
print("I am done with threading")


