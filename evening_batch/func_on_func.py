def hello(n):
    print("Hello ! ", n)

def wide(x):
    
    def call():
        return x("Python")
    return call()

print(wide(hello))
