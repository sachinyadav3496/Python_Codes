def calc(x,y,ch):
    if ch == "+":
        return x+y
    
    elif ch == "-":
        return x-y

    elif ch == "*":
        return x*y

    elif ch == "/":
        if y == 0 :
            return "divison by zero error"

        else: 
            return x/y

    elif ch == "//":
        return x//y

    elif ch == "%":
        return x%y

    elif ch == "**":
        return x**y
     
    else:
        return "error"


print("\n\nwelcome\n\n")

while True: 

    var1 = int(input("\n\nenter value of x = "))
    var2 = int(input("\n\nenter value of y = "))
    var3 = input("\n\nenter your choice\n +,-,*,/,//,%,**\n")
    
    result = calc(var1,var2,var3)

    print("\n\nresult = ",result)

    ch = input("\n\nDo you want to continue - y/n ").strip()
    
    if ch.lower() == 'y' :

        continue

    else :

        break
