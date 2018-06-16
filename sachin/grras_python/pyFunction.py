def count(a,b,c):
    print("The initial value of a: %d " %a)
    print("The initial value of b: %d " %b)
    print("The initial value of c: %d " %c)
print("Here is the Calling of function inside argument as count(10,20,30)")
count(10,20,30)
print("Now we call function with system arguments ")
a = 100
b = 200
c = 300
count(a,b,c)
print("We can do math in Function also as count(10+20,30+50,80*3)")
count(10+20,30+50,80*3)
print("We can do math with local variables also ")
count(a/10,b*3,c%13)
