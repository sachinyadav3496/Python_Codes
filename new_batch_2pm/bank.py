
bank = { 
        'users' : [ 'ram', 'shyam', 'hari' ],
        'acc_no' : [ 1001, 1002, 1003 ],
        'bal' : [ 10000, 20000, 35000 ],
        'password' : [ 'redhat', 'python', 'Asimov' ],

        }
c1 = 0

while True :

    name = input("Enter your User Name - ").strip()
    c1 += 1

    if name.lower() in bank['users'] :

        c1 = 0
        while True :

            password = input("Enter your password - ").strip()
            c1 += 1

            i = bank['users'].index(name)

            if password == bank['password'][i] :

                print("\n\nWelcome Sbka Apna Bank\n\n")

                while True :

                    ch = int(input("Choose Your Service - \n1.Debit\n2.Credit\n3.Check Balance\n4.Exit\nYour Choice - "))
                    
                    if ch == 1 :

                        print("\n\nWelcome to Debit Service \n\n")
                        amount = int(input("Enter amount to be debited - "))

                        if amount > bank['bal'][i] :

                            print("Insufficent Balance can not withdraw %s"%(amount))
                            print("You have only %s rupees in your account"%(bank['bal'][i]))
                            print("Try Again")

                        else :

                            print("%s sucessfully debited to your account"%(amount))
                            bank['bal'][i] = bank['bal'][i] - amount
                            print("You have left with %s rupees in your account"%(bank['bal'][i]))


                    elif ch == 2:

                        amount = int(input("Enter amount credit - "))

                        bank['bal'][i] += amount

                        print("Successfully Credited %s rupees in your account"%(amount))
                        print("Your new balance is %s rupees "%(bank['bal'][i]))
                    
                    elif ch == 3 :

                        print("Name = ",bank['users'][i])
                        print("Account Number = ",bank['acc_no'][i])
                        print("Your Balance = %s rupees "%(bank['bal'][i]))

                    
                    elif ch == 4 :

                        print("\n\nThanks for Using Sbka Apna Bank \n\n")
                        exit(0)

                    else :

                        print("\n\nInvalid Choice \n\n")
            

            else :

                print("\nInvalid Password \nTry Again")
                

            if c1 > 3 :

                print("\nYou have tried max time\nNow go to hell \n")
                exit(0)

    else :

        print("\nInvalid User Name\nTry Again\n")

    if c1 > 3 :
        
        print("You have Tried Maximum time\nBye Bye Now")
        break
