import sys


data = { 'name'     : ['ram','shyam','hari'] , 
         'acc'      : [1001,1002,1003], 
         'bal'      : [10000,50000,20000],          
         'password' : ['redhat','python','hariom']  
         }


def menu(i):

    global data

    print("Welcome to my bank services \nChoose which service you want to use ")

    print("1.Debit into account")
    print("2.Credit into account")
    print("3.Check Balance")
    print("4.Exit")

    ch = int(input("\nEnter your choice\t:  "))

    if ch == 1 :
        
        amount = int(input("Enter Withdrawal Amount -  : "))
        
        if amount >= data['bal'][i] :

            print("You Don't have sufficient Balance to withdraw")
            print("Your Balance is = ",data['bal'][i])
            print("Plese Try again")

            menu(i)

        else:

            data['bal'][i] -=  amount 

            print("Your account sucessfully debited to ",amount)
            print("Your remaining balance is - ",data['bal'][i])

            menu(i)

    elif ch == 2 :

        amount = int(input("Enter amount to credit- "))

        data['bal'][i] += amount

        print("Your account sucessfully credited with ",amount)
        print("Your Account Balance is - ",data['bal'][i])

        menu(i)

    elif ch == 3 :

        print("Name = ",data['name'][i])
        print("Acc no. = ",data['acc'][i])
        print("Balance = ",data['bal'][i])

        menu(i)

    else :
        
        sys.exit(1)










def bank():

    global data

    print("Welcome to mybank services - ")

    user_name = input("Enter your username - ")

    if user_name in data['name'] :
        
        i = data['name'].index(user_name)
        
        user_password = input("Enter your Password - ")

        if user_password == data['password'][i] :
            
           user_account = int(input("Enter your account NO. - ")) 

           if user_account == data['acc'][i] :
               
               menu(i)
           
           else :
               
               print("Error!! Invalid or Wrong Account No. \nPlease Try Again ")
                
               bank()


        else:
            
            print("Error!! Passwod incorrect \n Please try again ")
            
            bank()


    else :
        
        print("Error!!! User Does not Exists \nTry again")
        
        bank()



if __name__ == "__main__" :
    bank()

