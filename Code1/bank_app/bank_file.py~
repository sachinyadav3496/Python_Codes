import time
import getpass
import json

with open('bank.db') as f:
    bank = json.load(f) 


def credit(i):

    amount = int(input("\n\nEnter amount to deposit = "))
    bank['bal'][i] += amount
    with open('bank.db','w') as fp:
        json.dump(bank,fp)
    time.sleep(2)
    print("\nYou have sucessfully credited bal %s rs in your account"%(amount))
    print("\n\nUpdated Balance = %s"%(bank['bal'][i]))
    choice(i)

def debit(i):

    
    amount = int(input("\n\nEnter amount to withdraw = "))
    if bank['bal'][i] > amount :

        bank['bal'][i] -= amount
        with open('bank.db','w') as fp:
            json.dump(bank,fp)

        time.sleep(2)
        print("\nYou have sucessfully debited bal %s rs in your account"%(amount))
        print("\n\nUpdated Balance = %s"%(bank['bal'][i]))
        choice(i)
    else :

        print("\n\nYou does not have suffcient balance in your account \n\nTry Again \n\n")
        time.sleep(2)
        debit(i)

def chk_bal(i):

    
        print("Name = ",bank['users'][i])
        print("Account Number = ",bank['acc_no'][i])
        print("Your Balance = %s rupees "%(bank['bal'][i]))
        choice(i)
    




def choice(i):
    
    print("\n\n1.Debit\n2.Credit\n3.Chk_balance\n4.Profile\n5.logout\nEnter your choice - ",end='')
    ch = int(input())
    if ch == 1 :

        debit(i)

    elif ch == 2 :

        credit(i)

    elif ch == 3 :

        chk_bal(i)

    elif  ch == 4 :

        profile(i)

    elif ch == 5 :

        print("\n\nThanks for using python bank \n\n")
        time.sleep(3)
        main()
    else :

        print("\n\nInvalid choice \n\nTry Again \n\n")
        time.sleep(3)
        choice(i)






def sign_up():

    name = input("Enter your name - ").strip()
    if name.lower() in bank['users'] :

        print("User name already taken \nChoose another name ")
        sign_up()
    else:

        pass1=getpass.getpass()
        pass2=getpass.getpass("Confirm Password :")

        if pass1 == pass2 :

            bal = int(input("\nEnter amount to credit - "))
            
            acc_no = bank['acc_no'][-1]+1
            
            bank['users'].append(name)
            bank['acc_no'].append(acc_no)
            bank['bal'].append(bal)
            bank['password'].append(pass1)

            with open('bank.db','w') as fp:
                json.dump(bank,fp)
            login()

        else:
            print("\n\nPassword Does not Match...Try again\n\n")
            time.sleep(3)
            sign_up()


def login():
    
    print("\n\nWelcome to Login facility \n\n")

    name = input("Enter your user name - ").strip()
    if name.lower() in bank['users'] :
        i = bank['users'].index(name.lower())
        password = getpass.getpass()

        if password == bank['password'][i]:

            choice(i)
        else :
            login()
    else :

        print("Wrong input press y to continue ")
        ch = input().strip()

        if ch.lower() == 'y':

            login()
        else :

            print("\n\nThanks for using python bank \n\n")
            time.sleep(3)
            exit(0)



def main():

    print("\n\nWelcome to python Bank \n\n")
    ch = int(input("1.login\n2.sign_up\n3.exit\nEnter your choice - "))
    if ch == 1 :

        login()
    elif ch == 2 :

        sign_up()
    elif ch == 3 :

        print("\n\nThanks for using python bank \n\n ")
        time.sleep(3)
        exit(0)
    else :
        print("Wrong Choice Try again ")
        main()


if __name__ == '__main__' :

    main()
