def calc(x,y,ch):

    if ch == '+':

       return x+y

    elif ch == '-':

       return x-y
   
    elif ch == '*':

       return x*y

    elif ch == '/':

       if y == 0 :

           return "Divison By Zero Error"
       else:

            return x/y

    elif ch == '//' :

        return x//y

    elif ch == '%' :

        return x%y

    elif ch == '**' :

        return x**y

    else :

        return "Error Mind you input"


print("\n\nWelcome To Calc Program\n\n")


while True :

    var1 = int(input("\n\nEnter value of x = "))
    var2 = int(input("\nEnter value of y = "))
    var3 = input("\nEnter your Choice \n +,-,*,/,//,%,**  - ")

    result = calc(var1,var2,var3)

    print("\n\nResult = ",result)
    
    choice = input("\n\nPress y to continue - ")
    
    if choice.lower() == 'y' :

        pass
    else :
        
        print("\n\nThanks for using Calc Program\n\n")
        break
    
