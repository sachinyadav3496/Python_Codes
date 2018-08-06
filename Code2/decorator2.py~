import os 
def Outer(func):
    x = "This is a decorator"
    def inner(name):
        if os.path.exists(name):
            func(name)
        else:
            print("Files does not exist")
    return inner
@Outer
def something(fName):
    with open(fName) as f:
        print(f.read())

something("decorator2.py")
something("jadu m jadu")
