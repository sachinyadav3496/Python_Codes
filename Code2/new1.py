for i in range(10):
    for j in range(10-i):
        print("*",end='')
    for j in range(2*i):
        print(" ",end='')
    for j in range(10-i):
        print("*",end='')
    print()
