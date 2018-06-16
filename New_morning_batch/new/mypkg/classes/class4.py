import time
class robot:
    "Hi i am robot class."

    def __init__(self,name='robot',work=None,price=0):

        self.name = name
        self.work = work
        self.price = price

    def show(self):

        print("Name = ",self.name)
        time.sleep(1)
        print("Type = ",self.work)
        time.sleep(1)
        print("Price = ",self.price)
        time.sleep(1)
    
    def __del__(self):
        
        print("\n\nDeleting name ",self.name)
        del self.name
        time.sleep(1)
        print("\n\nDeleting work ",self.work)
        del self.work
        time.sleep(1)
        print("\n\nDeleting price ",self.price)
        del self.price
        time.sleep(1)

obj1 = robot()
obj2 = robot('sachin')
obj3 = robot('arpit','comedian')
obj4 = robot('aditi','student',50000)

print("\n\n")
obj1.show()
print("\n\n")
obj2.show()
print("\n\n")
obj3.show()
print("\n\n")
obj4.show()

print("\n\n")



