import threading
import time

class myPersonalThread(threading.Thread):

    def __init__(self,name,th_id,counter):

        threading.Thread.__init__(self)
        self.name = name
        self.th_id = th_id
        self.count = counter
    def run(self):
        print("Running Thread ")
        time.sleep(2)
        print("Hi this is obj1 ",self.name)
        print("Id of the obj is ",self.th_id)
        myThread(self.name)  
        print("Exiting Thread")
        time.sleep(self.count)


def myThread(name):
    print("Hi i am a Thread called ",name)
class new_Thread(threading.Thread):
    def __init__(self,name,flag):
        threading.Thread.__init__(self)
        self.name = name
        self.flag = flag
    def run(self):
        print("HEy this is new thread",self.name)
        bye(self.name,self.flag)
        print("Hey bye bye from new thread",self.name)
def bye(name,flag):
    print("You are in Bye thread ",name)
    time.sleep(flag)
    print("Bye bye from Bye Thread",name)

ob1 = myPersonalThread('Thread1',1,3)
ob2 = myPersonalThread('Thread2',2,1)
ob3 = myPersonalThread('Thread3',3,.5)
ob4 = myPersonalThread('Thread4',4,2)
ob5 = myPersonalThread('Thread5',5,1)
a = new_Thread('sachin',2)
b = new_Thread('aakasha',3)
c = new_Thread('shivani',1)


ob1.start()
ob2.start()
ob3.start()
ob4.start()
ob5.start()
a.start()
b.start()
c.start()

while True:
    a.join()
    b.join()
    c.join()
    ob1.join()
    ob2.join()
    ob3.join()
    ob4.join()
    ob5.join()
    break


