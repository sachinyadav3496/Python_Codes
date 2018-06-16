def prime(num):

    flag = True

    for var in range(2,num//2):

        if num % var == 0 :

            flag = False

            break

        else :

            flag = True


    if flag :

        return True

    else :

        return False

if __name__ == "__main__" :

    s = int(input("Enter start point - "))
    e = int(input("End point - "))

    for num in range(s,e+1):

        if prime(num) :

            print(num,end='  ')



            



