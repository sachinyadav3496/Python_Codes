import time
import os
from getpass import getpass
bank = {
     'user' : [ 'ram','shyam','hari',],
     'password' : [ 'python','java','redhat' ],
     'bal' : [ 2000.0,345634.0,34354.0 ],
     'acc' : [ 1001, 1002, 1003 ],
  }

def signup():
    os.system('cls')
    print("\n\n\n\n")
    print("Current Time : ",time.ctime())
    print("\n")
    name = input("Enter name : ")
    bal = float(input("Balance : "))
    password = getpass()
    a_no = bank['acc'][-1] + 1
    bank['user'].append(name)
    bank['password'].append(password)
    bank['bal'].append(bal)
    bank['acc'].append(a_no)
    print("Your account sucessfully created")
    print("Write down your acc no. carefully : ",a_no)
    print("redirecting you to login page")
    time.sleep(3)
    login()

def login():
    os.system('cls')
    print("\n\n\n\n")
    print("Current Time : ",time.ctime())
    print("\n")
    acc = int(input("Enter your account number : "))
    if acc in bank['acc'] : 
        p = getpass("Enter your Password : ")
        i = bank['acc'].index(acc)
        if p == bank['password'][i] : 
            print("Logged in sucess fully")
            main_menu(i)
        else : 
            print("Invaid Password \nTry Again")
            login()
    else : 
        print("No such account exist")
        main()
    
def main():
    os.system('cls')
    print("\n\n\n\n")
    print("Current Time : ",time.ctime())
    print("\n")
    print("Choices are : ")
    s  = """
    1. login
    2. signup
    3. exit 
    """
    print(s)
    ch = int(input("Enter your choice : "))
    if ch == 1 : 
        login()
    elif ch == 2 : 
        signup()
    elif ch == 3 : 
        os.system('cls')
        print("\n\n\n\n")
        exit(0)
    else : 
        print("Invalid Choice ")
        main()

def main_menu(i):
    os.system('cls')
    print("\n\n\n\n")
    print("Current Time : ",time.ctime())
    print("\n")
    print("1. Debit")
    print("2. Credit")
    print("3. Chk Balance")
    print("4. Logout")
    ch = int(input("Enter your choice : "))
    if ch == 1 : 
        debit(i)
    elif ch == 2 : 
        credit(i)
    elif ch == 3 : 
        chkbal(i)
    elif ch == 4 : 
        main()
    else :
        print("Invalid Choice \n Try again")
        main_menu()

def debit(i):
    os.system('cls')
    print("\n\n\n\n")
    print("Current Time : ",time.ctime())
    print("\n")
    global bank
    bal = float(input("Enter amont to withdraw : "))
    if bal > bank['bal'][i] : 
        print("Insufficent Balance")
        print("Your current Balance is : ",bank['bal'][i])
        print("Try again")
        debit(i)
    else : 
        bank['bal'][i] -= bal
        print("{} amount is sucessfully debited from your account".format(bal))
        print("Your current Balance is : ",bank['bal'][i])
        print("Thanks for using our service ")
        print("Redirecting to main menu")
        time.sleep(2)
        main_menu(i)

def credit(i):
    os.system('cls')
    print("\n\n\n\n")
    print("Current Time : ",time.ctime())
    print("\n")
    bal = float(input("Enter amount to credit : "))
    bank['bal'][i] += bal
    print("Your current Balance is : ",bank['bal'][i])
    print("Redirecting you to main menu")
    time.sleep(3)
    main_menu(i)

def chkbal(i):
    os.system('cls')
    print("\n\n\n\n")
    print("Current Time : ",time.ctime())
    print("\n")
    for key in bank:
            print("{} = {}".format(key,bank[key][i]))
    
    print("Redirecting you to main menu")
    time.sleep(3)
    main_menu(i)
if __name__ == "__main__" : 
    main()
