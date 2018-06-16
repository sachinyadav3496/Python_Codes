"""This module contains a function called prime.prime function takes one argument as a int number and return True if no is prime else return false."""


def prime(num):

    """It will return True if num is prime else it will return False."""
    
    for var in range(2,num//2):

        if num % var == 0 :

            flag = False
            break

        else :

            flag = True

    if flag == True :

        return True

    else :

        return False

if __name__ == "__main__" :

    print(prime(int(input("Enter a no. - ").strip())))

    print("Hello")
    print("hi")

