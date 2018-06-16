a = int(input("Enter a no . "))
b = int(input("Enter a no . "))
c = int(input("Enter a no . "))

if a >= b and a >= c :
    print("Greatest no is a - ", a)
elif b >= a and b >=c :
    print("Greatest no is b - ", b)
else :
    print("Greatest no is c - ", c)
print("Welcome to the even_odd program ")

n = input("Enter a no. - ") #taking i/p

if int(n) % 2 == 0 :
    print("Given input is an even no. ", n)
else :
    print("Given input is a odd no. ", n)
print("Bye Bye")
