def even(num):
    if num % 2 : 
        return False
    else : 
        return True 

def odd(num):
    if num % 2 : 
        return True 
    else :
        return False

if __name__ == "__main__" : 
    print("Choice : 1.even 2.odd")
    ch = int(input("Your Choice : "))
    if ch == 1 : 
        print(" Even : ",even(int(input("Enter a number : "))))
    else : 
        print("Odd : ",odd(int(input("Enter a number : "))))
