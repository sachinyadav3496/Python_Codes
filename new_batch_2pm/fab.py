
def fab(num):
    
    p = 0
    n = 1 
    num -= 2
    print(p,end=' ')
    print(n,end=' ')

    while num :
        
        temp = p

        p = n

        n = temp+n
        
        print(n,end =' ')

        num -= 1

if __name__ == "__main__" :
    num = int(input("Enter range of fab - "))
    
    fab(num)


