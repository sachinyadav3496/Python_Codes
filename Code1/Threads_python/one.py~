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

ob1 = myPersonalThread('Thread1',1,3)
ob2 = myPersonalThread('Thread2',2,1)
ob3 = myPersonalThread('Thread3',3,.5)
ob4 = myPersonalThread('Thread4',4,2)
ob5 = myPersonalThread('Thread5',5,1)

ob1.start()
ob2.start()
ob3.start()
ob4.start()
ob5.start()

while True:
    ob1.join()
    ob2.join()
    ob3.join()
    ob4.join()
    ob5.join()
    break


