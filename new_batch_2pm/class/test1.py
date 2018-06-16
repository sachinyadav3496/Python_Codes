class fraction(object):
    def __init__(self,n,d):
        self.numerator,self.denominator = fraction.reduce(n,d)
    @staticmethod
    def gcd(a,b):
        while b != 0 :
            a,b = b,a%b
        return a
    @classmethod
    def reduce(cls,n1,n2):
        g = cls.gcd(n1,n2)
        return (n1 // g, n2 // g)
    def __str__(self):
        return str(self.numerator)+'/'+str(self.denominator)

x = fraction(int(input("Enter numerator = ")),int(input("Enter denominator = ")))
print(x)

