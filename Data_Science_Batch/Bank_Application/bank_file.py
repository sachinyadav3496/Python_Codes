import sys
import os
import time
from getpass import getpass
import json
data = {}
def read():
    global data
    f = open('bank.db')
    data = json.load(f)
    f.close()
def update_log(s):
    f = open('bank.log','a')
    f.write('\n'+str(s))
def details(i):
    read()
    cls()
    print("Name : {:>100}".format(data['user'][i]))
    print("Account Number : {:>100}".format(data['acc'][i]))
    print("Balance : {:>100}".format(data['bal'][i]))
    print("Redirecting you to main menu ...")
    time.sleep(4)
    choice(i)
def update():
    read()
    f = open('bank.db','w')
    json.dump(data,f)
    f.close()


def credit(i):
    read()
    cls()
    bal = float("{:.2f}".format(float(input("Enter amount to Credit : "))))
    data['bal'][i] += bal
    #commit into file
    update()
    print("{} amount is added to your account sucessfully".format(bal))
    print("You now have {} rs in your account".format(float(data['bal'][i])))
    print("Redirecting you to main menu ...")
    time.sleep(4)
    choice(i)

def debit(i):
    read()
    cls()
    bal = float("%.2f"%(float(input("Enter amount to withdraw : "))))
    if bal > data['bal'][i]:
        print("Insufficent Balance ")
        print("Redireting to debit")
        time.sleep(4)
        debit(i)
    else :
        data['bal'][i] -= bal
        update()
        print("{} is withdrawn from your account sucessfully".format(bal))
        print("Your Remaing Balance is ",data['bal'][i])
        print("Redirecting you to main menu ....")
        time.sleep(4)
        choice(i)
def choice(i):
            cls()
            print("1. Debit")
            print("2. Credit")
            print("3. Account Details")
            print("4. Logout")
            ch = int(input("Your Choice : "))
            if ch == 1 : 
                debit(i)
            elif ch == 2 : 
                credit(i)
            elif ch == 3 : 
                details(i)
            elif ch == 4 : 
                bank()
            else : 
                print("Invalid Choice Try Again ")
                choice(i)

def login():
    read()
    cls()
    acc = int(input("Your Acc Number : "))
    if acc in data['acc'] : 
        password = getpass("Password : ")
        i = data['acc'].index(acc)
        if password == data['password'][i] : 
            s = "user with acc {} logged in at {} ".format(acc,time.ctime())
            update_log(s)
            choice(i)
                
        else :
            print("Invalid Password Try Again")
            s = "user with acc {} tried a failed login at {}".format(acc,time.ctime())
            update_log(s)
            login()
    else :
        print("No such Account Exists : ")
        s = "An authroized Acess Deteced at time {}".format(time.ctime())
        update_log(s)
        print("Redirecting to main menu")
        time.sleep(3)
        bank()

def cls():
    os.system('cls')
    print("\n\n\n\n")
    print("Time = ",time.ctime())
    print("\n")
    
def password_input():
    p = getpass()
    q = getpass("Re-Type your Password : ")
    if p == q :
        return p
    else : 
        print("Password does not match\nTry again")
        return password_input()
        
def signup():
    read()
    global data
    os.system('cls')
    print("\n\n\n\n")
    print("Time = ",time.ctime())
    print("\n")
    name = input("Enter your name : ")
    password = password_input()
    bal = float("%.2f"%(float(input("Enter initial amount : "))))
    acc = data['acc'][-1] + 1
    data['user'].append(name)
    data['acc'].append(acc)
    data['password'].append(password)
    data['bal'].append(bal)
    update()
    os.system('cls')
    print("\n\n\n\n")
    print("Time = ",time.ctime())
    print("\n")
    print("Account Sucessfully Created")
    print("Please note down your account number for future use")
    print("Account Number : ",acc)
    print("Redirecting to LOGIN Page ...")
    time.sleep(3)
    login()


def bank():
    read()
    s = "Application Started at : {}".format(time.ctime())
    update_log(s)
    os.system('cls')
    print("\n\n\n\n")
    print("Time = ",time.ctime())
    print("\n")
    print("1. Login ")
    print("2. Signup ")
    print("3. Exit ")
    ch = int(input("Your Choice : "))
    if ch == 1 : 
        login()
    elif ch == 2 : 
        signup()
    elif ch == 3 : 
        os.system('cls')
        print("\n\n\n\n")
        print("Thanks for using our services ")
        print("Exiting ... ")
        time.sleep(3)
        os.system('cls')
        sys.exit(0)
    else : 
        os.system('cls')
        print("\n\n\n\n")
        print("Invalid Choice Try Again  ")
        print("Redirecting you to Home ... ")
        time.sleep(3)
        bank()

if __name__ == "__main__" : 
    bank()
