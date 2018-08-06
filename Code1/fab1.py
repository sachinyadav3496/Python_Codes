
def fab(num):
    
    p = 0
    n = 1 
    num -= 2
    l = [0,1]
    while num :
        
        temp = p

        p = n

        n = temp+n
        l.append(n)

        num -= 1
    return l

if __name__ == "__main__" :
    num = int(input("Enter range of fab - "))
    
    fab_list = fab(num)
    print(fab_list)
    
    s = 0
    for num in fab_list:

        s += num

    print("summation of  list = %s "%s)


