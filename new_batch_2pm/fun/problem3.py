from math import sqrt 
def prime(n):

    for var in range(2,int(sqrt(n)+1)):

        if n % var == 0 :

            flag = False
            break
        else :
            flag = True

    return flag

l = list(map(int,input().split()))
print(*list(filter(prime,l)))








#res = list(map(prime,l))
#print(*res)

