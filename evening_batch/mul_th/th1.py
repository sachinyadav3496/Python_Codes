import _thread as t
import time

def hello(name,value):
    
    for var in range(5):
        
        print("Thread1 - Name = ",name)

        time.sleep(value)

def bye(name,value):

    for var in range(3):
        
        print("Thread2 - Name = ",name)
        time.sleep(value)


t1 = t.start_new_thread(hello,('python',3))
t2 = t.start_new_thread(bye,('java',3))
t3 = t.start_new_thread(hello,('python',3))

while True:
    pass

