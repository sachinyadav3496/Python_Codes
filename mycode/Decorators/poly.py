#p(x) = a.x2+bx+c

def polynomial_creator(a,b,c):
    def polynomial(x):
        return a*x**2+b*x+c
    return polynomial
p1 = polynomial_creator(2,3,-1)
p2 = polynomial_creator(-1,2,1)

for x in range(-2,2,1):
    print(x,p1(x),p2(x))

