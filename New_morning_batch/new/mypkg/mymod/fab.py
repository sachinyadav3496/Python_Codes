__author__ = 'sachin yadav'

def fab(num):

    print("\n\n")
    print("0",end='  ')
    print("1",end='  ')
    prev = 0
    next = 1

    for term in range(num-2):

        temp = prev
        prev = next
        next = temp + next

        print(next,end='  ')

    print("\n\n")

def fab_sum(num):
    
    s = 1
    p = 0
    n = 1
    for var in range(num-2):
        
        t = p
        p = n
        n = t + n 

        s = s + n 

    return s



if __name__ == "__main__" :

    n = int(input("Enter no of terms - "))

    fab(n)

    n = int(input("Enter no of terms to get sum - "))

    print("Sum of digit = ",fab_sum(n))
