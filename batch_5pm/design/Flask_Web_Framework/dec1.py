def decorate(old_func):
    def lets_decorate(name):
        print("*"*100)
        print("*"*100)
        old_func(name)
        print("*"*100)
        print("*"*100)
    return lets_decorate

@decorate
def hello(name):
    print(f"Hello mr. {name} to the original hello function")

@decorate
def squre(num):
    print(f"squre of {num} is {num**2}")

#hello = decorate(hello)
#squre = decorate(squre)


if __name__ == "__main__" : 

    #hello('sachin yadav')
    hello('sachin yadav')
    squre(1234)
