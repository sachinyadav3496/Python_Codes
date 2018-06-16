import math

""" This module contain two functions.
prime(num)->will check given argument if it is prime then return True else False
prime_range(start,end)->will print all prime no in range give start to end
main()->it is to check a no is prime or not 
"""

def prime(num):

    """prime(num)->Will return True if given argument is a prime no else return false"""

    if  num <= 1:

        return False

    elif num <= 3 :

        return True

    else :

        for var in range(2,int(math.sqrt(num)+1)): #math.squrt will give square root of num


            if num % var :

                f = True

            else :
                
                f = False
                break

        if f :

            return True

        else :
            
            False

def prime_range(end,start=2):

    """prime_range(start,end)->This function will take two argument as start and end
    and will print all the prime no which exists in range start-end."""

    print()
    for num in range(start,end+1) :

        if prime(num):

            print(num,end="     ")
    print()


def main():
    
    """main()->It will use to check a no is prime or not """

    n = int(input("Enter a no. to check it is prime or not - "))

    if prime(n) :

        print("Given no. %s is a prime no. "%(n))
    
    else :

        print("Given no. %s is not a prime no. "%(n))

    num1 = int(input("Enter starting point"))
    num2 = int(input("Enter end point"))

    prime_range(start=num1,end=num2)

if __name__ == "__main__":

    main()    
                



