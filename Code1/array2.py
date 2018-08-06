print("\n\n Welcome to Array \n\n")
array1 = [
        [int(input("a1[0][0] = ")),int(input("a1[0][1] = ")),int(input("a1[0][2] = "))],
        [int(input("a1[1][0] = ")),int(input("a1[1][1] = ")),int(input("a1[1][2] = "))],
        [int(input("a1[2][0] = ")),int(input("a1[2][1] = ")),int(input("a1[2][2] = "))],
        ]

array2 = [
        [int(input("a2[0][0] = ")),int(input("a2[0][1] = ")),int(input("a2[0][2] = "))],
        [int(input("a2[1][0] = ")),int(input("a2[1][1] = ")),int(input("a2[1][2] = "))],
        [int(input("a2[2][0] = ")),int(input("a2[2][1] = " )),int(input("a2[2][2] = "))],
        ]


print("Given Array 1 = ")

for row in range(3):

    for col in range(3):

        print(array1[row][col],end='     ')
    print()

print("Given Array 2 = ")

for row in range(3):

    for col in range(3):

        print(array2[row][col],end='     ')
    print()

print("printing Addition of Array ")

for row in range(3):

    for col in range(3):


        print(array1[row][col]+array2[row][col], end = '     ')

    print()



print("\n\n")
