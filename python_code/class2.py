class parent:
    'This is parent class.'
    obj = 0
    def __init__(self,name,val):
        self.name = name
        self.val = val
        parent.obj += 1
    def display(self):
        print("Name = ", self.name)
        print("Val = ", self.val)
        print("Total Obj = ", parent.obj)
    def show(self,arg,arg1):
        print("Welcome to show function")
        print("Name = ", self.name)
        print("Val = ", self.val)
        print("Total obj. = ", parent.obj)
        print("Arg1 = ", arg)
        print("Arg2 = ", arg1)
a = parent('sachin','don')
a.display()
a.show('hey','ho')
class child(parent):
    def __init__(self):
        self.name='child'
        self.val='no'
    def display(self):
        print("Name = ",self.name)
        print("Val = ",self.val)
        print(parent.obj)
    b = parent("Sachin","yadav")
    b.show("Thiss iss ","cool")
b = child()
b.display()
b.show('hey','ho')


