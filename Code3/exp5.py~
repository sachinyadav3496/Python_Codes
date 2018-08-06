def Networkerror(RuntimeError):
    def __init__(self,arg):
        self.arg=arg
try:
    raise Networkerror("bad arg")
except Networkerror as e:
    print(e.args)
