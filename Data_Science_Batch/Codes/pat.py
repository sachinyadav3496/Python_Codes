for var in range(10):
    for _ in range(10-var):
        print(" ",end='')
    for _ in range(var):
        print("*",end='')
    print()
