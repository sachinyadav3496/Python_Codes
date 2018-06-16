n = int(input("Enter no. of lines - "))

for var in range(n):

    if var < n//2 :

        for x in range((n//2+1)-var) :

            print(" ",end='')

        for y in range(var):

            print("*",end='')
        for y in range(var):
            print("*",end='')
    
    elif var == n//2:

        continue

    else:

        for x in range(var-(n//2)):

            print(" ",end='')

        for y in range((n//2)-(var-(n//2))):

            print("*",end='')
        for y in range((n//2)-(var-(n//2))):
            print("*",end='')

    print()
