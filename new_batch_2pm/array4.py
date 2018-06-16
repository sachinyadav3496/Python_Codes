print("\n\n Welcome to Array \n\n")
m = int(input("Enter no of rows - "))
n = int(input("Enter no of cols - "))
print("Enter values for Array 1 ")
array1 = [ [ int(input("A1[%s][%s] = "%(row,col))) for col in range(n) ] for row in range(m) ]
print("\nEnter values for Array 2 ")
array2= [ [ int(input("A2[%s][%s] = "%(row,col))) for col in range(n) ] for row in range(m) ]
print("Given Array 1 = ")
for row in range(m):
    for col in range(n):
        print(array1[row][col],end='     ')
    print()
print("Given Array 2 = ")
for row in range(m):
    for col in range(n):
        print(array2[row][col],end='     ')
    print()
print("printing Addition of Array ")
for row in range(m):
    for col in range(n):
        print(array1[row][col]+array2[row][col], end = '     ')
    print()
print("\n\n")
