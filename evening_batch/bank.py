import json
import os
if os.path.exists('bank.txt'):

    with open('bank.txt') as f:
        bank = json.load(f)
else :
    with open('bank.txt','w') as f:
        b = { 'user':['ram','hari','mohan'],'acc':[1001,1002,1003],'bal':[10000,50000,134000] }
        json.dump(b,f)
    with open('bank.txt') as f:
        bank = json.load(f)


t = 0

def verify_acc(acc,i):
    if acc == bank['acc'][i]:
        return True
    else :
        return False

def login():
    "This is login fuction to ensure your login "
    global t
    t+=1
    name = input("Enter your name - ")
    if name in bank['user'] :
        i = bank['user'].index(name)
        acc = int(input("Enter your acc no. - "))
        ck = verify_acc(acc,i)
        if ck == True :
            choice(name,acc,i)

            
        else :

    
            if t < 3:
                print("User Acc Invalid\nTry Again ")
                login()
            else :
                print("Max. Try Limit Crossed. Exiting Bank application ")
                exit(0)
    else :
            if t < 3:
                print("User name Invalid\nTry Again ")
                login()
            else :
                print("Max. Try Limit Crossed. Exiting Bank application ")
                exit(0)
def choice(name,acc,i):
    ch  = int(input("Enter your choice \n 1.Debit\n2.Credit\n3.chkbal"))
    if ch == 1:
        debit(name,acc,i)



def debit(name,acc,i):
    global bank
    amount = int(input("Enter amount to withdraw - "))
    if bank['bal'][i] < amount :
        print("Insufficient Balance ")
    else:
        bank['bal'][i] -= amount
        print("You have left "+str(bank['bal'][i])+"$" )
        
def main():
    login()
    with open('bank.txt','w') as f:
        json.dump(bank,f)

if __name__ == "__main__" :
    main()
