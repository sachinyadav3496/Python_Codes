def prime(num):

    flag = True

    for var in range(2,num//2):

        if num % var == 0 :

            flag = False

            break

        else :

            flag = True


    if flag :

        print("Given no. %i is prime"%num)

    else :

        print("Given no. %i is not prime"%num)

n = int(input("Enter a no to check whether it is prime or not - "))

prime(n)




