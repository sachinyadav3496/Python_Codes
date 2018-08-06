

def pat():
    n = int(input("Enter no. of rows - "))
    for i in range(n):
        for j in range(i+1):
            print("*",end='')
        print()
def pat1():
    n = int(input("Enter no. of rows - "))
    for i in range(n):
        for j in range(n-i):
            print("*",end='')
        print()

if __name__ == '__main__':
    pat()
    print()
    print()
    pat1()
