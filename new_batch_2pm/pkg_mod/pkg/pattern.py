def triangle(n):
    for var in range(n):
        for _ in range(var):
            print("*",end='')
        print()

def rev_tri(n):
    for var in range(n):
        for _ in range(n-var):
            print("*",end='')
        print()

if __name__ == "__main__" :

    triangle(int(input("Enter a no to print Triangle - ")))
    rev_tri(int(input("Enter a no to print Reverse Traingle - ")))
