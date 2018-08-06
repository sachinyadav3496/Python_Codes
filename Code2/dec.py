def Tags(*tags):
    def deco(oldfunc):
        def ch(st):
            code = st
            for tag in reversed(tags):
                code += "<{0}>{1}</{0}>".format(tag,code)
            return code
        return ch
    return deco

@Tags(tuple(input() for var in range(3)))
def myfunc(string):
    return string

print("Your web page msg is - \n",myfunc((input("Enter your messege - "))))

