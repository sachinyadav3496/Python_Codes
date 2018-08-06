def hello(a,b):
    c = a/b
    f = open("adfh")
a = int(input("input - "))
b = int(input("input - "))
try:
    hello(a,b)
except ZeroDivisionError as e:
    print("Error!!! ",e)
    hello(b,a)
except IOError as e:
    print("Error!!!",e)
    for i in range(10):
        print("hello")
    
