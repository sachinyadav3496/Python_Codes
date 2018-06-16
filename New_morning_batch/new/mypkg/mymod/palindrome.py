import time

def pal(num):

    temp = num
    s = 0

    while temp :

        r = temp % 10 
        temp = temp // 10
        s = s*10 + r

    if s == num :

        return True

    else :
        
        return False

def rev(num):

    temp = num
    s = 0
    while temp:

        r = temp % 10
        temp = temp // 10
        s = s*10 + r

    return s


if __name__ == "__main__":

    num = int(input("Enter a no - "))
    
    time.sleep(1)
    
    print("\nReverse of %s is %s \n Checking no is palindrome or not "%(num,rev(num)))

    time.sleep(3)

    if pal(num) :

        print("Given no %s is a palindrome no. "%(num))
    
    else:

        print("Given no %s is not a palindrome no. "%(num))



