from getpass import getpass
import json

with open('bank.db') as fp :
    bank = json.load(fp)

print("\n\nWelcome python Bank - \n\n")

print("Please Choose your option\n")
print("1.Login\n2.SignUp\n")

ch = int(input())

if ch == 1 :
    
    print("\n\nWelcome to python Bank Services - \n\n")

    name = input("Please Input your Name = ").strip()
    name = name.lower()

    if name in bank.keys():
        
        password = getpass("Please Input your Password - ")

        if password == bank[name][2]:

            print("\n\nWelcome to python Bank Menu - \n\n")
            print("1.Debit\n2.Credit\n3.Check Balance\n4.Delete Account\n")
            ch = int(input())

            if ch == 1 :
                
                bal = int(input("Please Input Amount to Withdraw - "))
                
                if bal <= bank[name][1] :

                    bank[name][1] = bank[name][1] - bal
                    with open('bank.db','w') as fp:
                        json.dump(bank,fp)

                    print("\nYou have left ",bank[name][1]," in your Account.")
               
                else:

                    print("\n\nInsufficent Balance\nCan't Process Your Request \n\n")



            elif ch == 2 :

                bal = int(input("Please Input Amount to be Creadit in your account - "))
                bank[name][1] += bal
                with open('bank.db','w') as fp:
                        json.dump(bank,fp)

                print("Your Updated Balance is ",bank[name][1])

            elif ch == 3 :
                
                print("\nName = ",name)
                print("\nAcc. No. = ",bank[name][0])
                print("\nBalance = ",bank[name][1])
                print("\n\nThanks for Using Python Bank Services \n\n")

            elif ch == 4 :

                del bank[name]

                print("Your Account Sucessfully Deleted ")
                print("\n\nThanks for Using Python Bank Services \n\n")

            else :

                print("\n\nInvalid Option\n\n")

            
        else :

            print("\n\nInvalid Password\n\n")
    
    else :

        print("\n\nInvalid User\n\n")

elif ch == 2 :

    print("\n\nWelcome To Signup Page \n\n")
    name = input("Please Input your name - ")
    bal = int(input("Please Input your balance - "))
    acc = int(input("Please Input account no. - "))
    password = input("Please Input your Password - ")

    bank[name] = [acc,bal,password]


    with open('bank.db','w') as fp:
        json.dump(bank,fp)
    
    print("\n\nYour Account Sucessfully Created - \n\n")

else :

    print("\nInvalid Input\nRun Program Again")

