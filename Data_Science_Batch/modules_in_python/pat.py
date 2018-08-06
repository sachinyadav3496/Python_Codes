def mypattern(lines):
    for row in range(lines):
        print("*"*(lines-row),end='')
        print(" "*row,end='')
        print(" "*(lines-row),end='')
        print("*"*row)
if __name__ == "__main__" :

    mypattern(int(input("Enter number of lines : ")))
    print("__name__ = ",__name__)
