def polynomial_creator(*coefficients):
    """cofficients are in the form a_0,a_1,a...._n"""
    def polynomial(x):
        res = 0
        for index,coeff in enumerate(coefficients):
            res += coeff * x**index
        return res
    return polynomial

p1 = polynomial_creator(4)
p2 = polynomial_creator(2,4)
p3 = polynomial_creator(2,3,-1,8,1)
p4 = polynomial_creator(-1,2,1)

for x in range(-2,2,1) :
    print(x,p1(x),p2(x),p3(x),p4(x))

