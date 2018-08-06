class complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
    def __add__(self,obj):
        return complex(self.r+obj.r,self.i+obj.i)
    def __str__(self):
        return '{}+{}'.format(self.r,self.i)

x = complex(3.0,-4.5)
print("Complex Number 1st = {}+{}".format(x.r,x.i))
y = complex(5.0,-6.5)
print("Complex Number 1st = {}+{}".format(y.r,y.i))
z = x+y
print("Addition of c1+c2 = {}".format(x+y))
