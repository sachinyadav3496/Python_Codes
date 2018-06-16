__author__ = 'sachin yadav'

class robot:

    """HI i am robot Class"""

    name = "HI I am robot Class's object"

    def show(self):

        print("HI Class's object name = %s"%(self.name))

    def nameSet(self):

        self.name = input()


obj1 = robot()
obj2 = robot()
obj3 = robot()
l = [ obj1,obj2,obj3 ]
print("\n\n")
print("Calling Object1's Show Function ")
obj1.show()
c = 0
print()
for var in range(3):

    c += 1
    print("Enet name of object %s - "%(c),end='')
    l[var].nameSet()
    print()

print("\n\n")
for var in range(3):

    print("Printng Name of Object ",var)
    l[var].show()
    print()


print("\n\n")

