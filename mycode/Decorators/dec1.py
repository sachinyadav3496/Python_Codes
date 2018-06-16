def our_decorator(func):
    def function_wrapper(x):
        print("Before Calling "+func.__name__)
        func(x)
        print("After Calling "+func.__name__)
        return "Thanks for using Decorators"
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi,foo has been called with "+str(x))

print(foo("Hello World"))
