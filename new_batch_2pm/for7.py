
print("\n\n")

rows = int(input("Enter no of rows - "))

for row_no in range(rows) :
   
    for col_no in range(rows-row_no-1):

        print(" ",end='')

    for col_no in range(row_no):

        print("*",end='')

    print()


print("\n\n")
