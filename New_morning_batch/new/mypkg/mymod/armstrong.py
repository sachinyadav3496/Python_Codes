import time

def arm(num):

    temp = num
    s =  0
    
    p = 0

    while temp :

        temp //= 10
        p += 1

    temp = num

    while temp :

        r = temp % 10 
        temp = temp // 10
        s = s + r**p

    if s == num :

        return True

    else :
        
        return False

def arm_range(start,end):
    l = []

    for num in range(start,end+1):

        if arm(num) :
            
            l.append(num)
    return l

if __name__ == "__main__":

    num = int(input("Enter a no - "))
    
    time.sleep(1)
    
    print("\nChecking given no %s is armstrong or not \n"%(num))

    time.sleep(3)

    if arm(num) :

        print("Given no %s is a armstrong no. "%(num))
    
    else:

        print("Given no %s is not a armstrong no. \n\n"%(num))

    
    print("\nWelcome to range armstrong")

    start = int(input("\nEnter starting Range - "))
    end = int(input("\nEnter endin Range - \n"))

    for var in arm_range(start,end) :

        print(var,end = '    ')

    print("\n\n")

