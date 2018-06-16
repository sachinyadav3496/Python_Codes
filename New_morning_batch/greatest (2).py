__author__ = 'sachin yadav'

"""This is a module to print greatest no among three numbers"""

x = int(input("Enter value of x - "))
y = int(input("Enter value of y - "))
z = int(input("Enter value of z - "))

if x >= y and x >= z :

    print("X is greatest ",x)

elif y >= x and y >= z :

    print("Y is greatest ",y)

else :

    print("Z is greatest ",z)

