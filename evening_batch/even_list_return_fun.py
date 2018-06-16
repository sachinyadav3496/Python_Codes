def even(args): #function to return even no list
    """ even(args) -> This is a function which filter even no. from a list.
    Also return a list full of even numbers.
    here args is a common list of mixed no. """

    even = []

    for item in args: 
        if item % 2 == 0 :
            even.append(item)
    return even

print("Welcome to even filtering , def of program -\n\n\n  ",even.__doc__)
print()
print()
n = int(input("Enter no of items - "))
l = []
print()
for var in range(n):
    num = int(input())
    l.append(num)

even_list = even(l)
print()
print("Here is the list of even no.  = ",even_list)
print()
