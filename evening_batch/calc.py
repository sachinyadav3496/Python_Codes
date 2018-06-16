
import sys


def add(a,b):

    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def main():
    print("Welcome to calculator application ")
    ch = int(input("Enter your choice - \n1.add\n2.sub\n3.mul\n4.div\nChoice - "))
   
    x = int(input("Enter value of a = "))
    y = int(input("Enter value of b = "))
    print()
    if ch == 1 :
        print("Result = ", add(x,y))
    elif ch == 2 :

        print("Result = ", sub(x,y))
    elif ch == 3 :
        print("Result = ", mul(x,y))
    elif ch == 4 :

        print("Result = ", div(x,y))
    else :
        print("Wrong choice !!!")
    print()
    print()

if __name__ == "__main__" :
    print('calc'.__name__)
    main()
