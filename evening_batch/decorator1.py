def old_func(a,b):
    return a+b
def decorate(old):
    def use(x,y):
        return "x = "+str(x)+" \ny = "+str(y)+"\nx + y = "+str(x+y)
    return use
def main():

    new = decorate(old_func)
    p = int(input("Enter value of x = "))
    q = int(input("Enter value of y = "))
    res = new(p,q)
    print("Result is as below - ")
    print(res)

if __name__ == '__main__':
    main()

