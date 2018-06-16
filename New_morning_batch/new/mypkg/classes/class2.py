__author__ = 'sachin yadav'
__author__ = 'sachin yadav'

class robot:

    """HI i am robot Class"""

    name = "HI I am robot Class's object"

    def show(self):

        print("HI Class's object name = %s"%(self.name))

    def nameSet(self):

        self.name = input("Enter Name - ")

class child(robot):

    var = "Hi i am child"

    def display(self):

        robot.show(self)
        print(self.var)

    def input(self):

        robot.nameSet(self)
        self.var = input("\nYour Input - ")


if __name__ == "__main__":

    print("\n\n")
    obj = child()

    obj.display()
    obj.input()
    obj.display()



    print("\n\n")

