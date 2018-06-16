import _thread

def mul(name):
    print("Result of "+ name + " is " )
for i in range(10):
    _thread.start_new_thread(mul,('Thread'+str(i),))
for j in range(10,20):
    _thread.start_new_thread(mul,('Thread'+str(i),))
for k in range(20,30):
    _thread.start_new_thread(mul,('Thread'+str(1),))
    print()
