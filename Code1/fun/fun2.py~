import math
import time
def prime(num):
        """prime(num)-> Return True if given num is prime else return false"""
        for var in range(2,int(math.sqrt(num)+1)):
            if num % var == 0 :
                flag = False
                break
            else :
                flag = True        
        if flag :
            return True
        else :
            return False
print("\n\n",prime.__doc__)
s = int(input("\n\nEnter start point - "))
time.sleep(2)
e = int(input("Enter end point - "))
time.sleep(2)
nums = list(range(s,e+1))
print("Given no. are - ",nums)
print("\n\nProcessing Prime No. - \n\n")
for var in nums:
    if prime(var):
        print(var,end='   ')
print("\n\n")






