def decorate(old_func):
    def work(arg):
        print("Hello World!! HOw are you !!!")
        print("welcome mr. ",arg)
    return work
@decorate
def hello(name):
    print("Hello mr .")

x = input("Enter your name - ")
hello(x)
