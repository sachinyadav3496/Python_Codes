def params(oldfunc):
    def inside(*args,**kwargs):
        print("Param : ",args,kwargs)
        return oldfunc(*args,**kwargs)
    return inside
@params
def mul(x,y=10):
    print("Result = ",x*y)
mul(4,4)
mul(3)
mul(y=10,x=20)
