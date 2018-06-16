def calc(x,y,ch):
    if ch == '+' : 
        return x+y
    elif ch == '-' : 
        return x-y
    elif ch == '*' :
        return x*y
    elif ch == '/' :
        if y == 0 :
            return 'y can not be Zero for division'
        else :
            return x/y
    else :
        return 'Invalid Choice '

k = int(input("Enter X : "))
l = int(input("Enter y: "))
ch = input("Enter choice +,-,*,/ : ").strip()
result = calc(k,l,ch)
print("Result is = ",result)
