def addTags(*tags):
    def decorator(oldFunc):
        def makeup(*args,**kwargs):
            code = oldFunc(*args,**kwargs)
            for tag in reversed(tags):
                code = "<{0}>{1}</{0}>".format(tag,code)
            return code
        return makeup
    return decorator
@addTags("p","i","b")
def myWeb(name):
    return "Welcome mr. "+name+" To my blog !!! "
print(myWeb(input("Enter your name - ")))

