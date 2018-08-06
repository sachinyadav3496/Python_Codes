class parent(object):
     """This is parent class"""
     def __init__(self,a,b):
             self.name = a
             self.addr = b
     def set(self):
         self.name = input()
         self.addr = input()
     def disp(self):
             print("Name = ",self.name)
             print("Addr = ",self.addr)
     def get(self):
        parent.disp(self)
class child(parent):
     def __init__(self,x,y):
             parent.__init__(self,x,y)
             self.name = x
     def show(self):
             print("Child Class ")
             print("Name = ",self.name)
             print("Addr = ",self.addr)
             print("Parent Class")
             parent.disp(self)
obj1 = child(input(),input())
obj1.show()
obj1.set()
obj1.get()
obj1.show()
