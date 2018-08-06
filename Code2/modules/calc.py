def add(a,b):
    """ this an addition function which return addition of two numbers """
    print("You are in add() function ")
    s = a+b
    return s
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b


def main():
    ch = int(input("1.add\n2.sub\n3.mul\n4.div\n5.mod\ninput - "))
    x = int(input("Enter a no - "))
    y = int(input("Enter a no - "))
    if ch == 1:
        print("Result is - ",add(x,y))
    elif ch == 2:
        
        print("Result is - ",sub(x,y))
    elif ch == 3:
        print("Result is - ",mul(x,y))
    elif ch == 4:
        print("Result is - ",div(x,y))
    elif ch == 5:
        print("Result is - ",mod(x,y))
    else :
        print("Invalid Choice - Try Again ")
    ch1 = input("Do you want to continue - y/n - ")
    if ch1.lower() == 'y':
        main()
    else :
        exit(0)


if __name__ == '__main__' :
    main()

