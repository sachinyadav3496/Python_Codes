import _thread as th
import time
x = 1

def hello(name):
    global x 
    print("Hello Thread ",name,"Calling for x = ",x)
    x = x + 1
    time.sleep(2)
def bye(name):
    global x 
    print("Bye Thread ",name,"Calling fo x = ",x)
    x = x - 1
    time.sleep(2)

th.start_new_thread(hello,('sachin',))
th.start_new_thread(bye,('sachin',))
th.start_new_thread(hello,('upendra',))
th.start_new_thread(bye,('updendra',))
th.start_new_thread(hello,('shivani',))
th.start_new_thread(bye,('shivani',))
th.start_new_thread(hello,('parul',))
th.start_new_thread(bye,('parul',))
while True :
    pass
