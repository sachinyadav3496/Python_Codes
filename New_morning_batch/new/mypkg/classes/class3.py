
class A:

    def show(self):

        print("Hello I am A")

    def display(self):

        print("Can you see me ?")

class B(A):

    def display(self):

        print("This is called polymorphism and over riding.")

   
obj = B()

obj.show()
obj.display()

boj = A()
boj.show()
boj.display()
