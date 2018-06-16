def thisFun(*args):

    """This is fun function which just print out any number of arguments you passed into it."""
    c = 1
    for var in args:

        print("Argument %i is %s "%(c,var))
        c += 1 

print(thisFun.__doc__)

def newFun(**kwargs):

    for key in kwargs:


        print(key,"=",kwargs[key])

