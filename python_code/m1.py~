import _thread as t
import time
def count(name,count,f):
    print("Thread Name = ",name)
    while count > 0 :
        print(name, " - ", time.ctime())
        time.sleep(f)
        count -=1
def date(name,n):
    print("Thread = ", name)
    while n>0:
        print(n)
        time.sleep(2)

t1 = t.start_new_thread(count,('one',5,2))
t2 = t.start_new_thread(count,('two',4,3))
t2 = t.start_new_thread(date,('three',3))
while True:
    pass


