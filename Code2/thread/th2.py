import threading
import time
import datetime

class myThread(threading.Thread):

    def __init__(self,name,counter):

        threading.Thread.__init__(self)

        self.threadID = counter
        self.name = name

        self.counter = counter

    def run(self):

        print("Starting " + self.name)
        time.sleep(self.counter)
        print_date(self.name,self.counter)
        
        print("Exiting "+self.name)

def print_date(threadName,counter):

        datefields = []
        today = datetime.date.today()
        datefields.append(today)

        print("%s[%d]: %s"%(threadName, counter, datefields[0]))

print("\n\n")
thread1 =  myThread("Thread1",1)
print("\n\n")
thread2 = myThread("Thread2",2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Exiting the Program!!!")

