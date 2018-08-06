import os
# coding: utf-8

# Data Structure

# In[1]:


bank = {
    
    'user' : [ 'kanika','anuj','senthil','arvind' ],
    'bal' : [ 10000, 25000, 320000, 1929212],
    'acc' : [ 1001, 1002, 1003, 1004],
    'passwd' : ['abc','xyz','python','redhat'],
}


# In[2]:


def profile(i):
    print("Welcome {} ".format(bank['user'][i]).center(100,'*'))
    print("\n1.Update Name ")
    print("2.Update Password")
    print("3.Delete Account")
    print("4.Logout")
    ch = int(input("Enter your Choice : "))
    if ch == 1 : 
        name = input("Ener new name : ")
        bank['user'][i] = name
        choice(i)
    elif ch == 2 : 
        cp = input("Enter current Passsword : ")
        if cp == bank['passwd'][i] :
            from getpass import getpass
            np = getpass("Ener New Password : ")
            vp = getpass("Confirm Password : ")
            if np == vp :
                bank['passwd'][i] = np
                print("Password Sucessfully Updated")
                main()
            else :
                print("Password didn't Match ")
                print("Try Again")
                profile(i)
        else :
            print("Password Incorrect ")
            main()
    elif ch == 3 : 
        bank['user'].pop(i)
        bank['acc'].pop(i)
        bank['bal'].pop(i)
        bank['passwd'].pop(i)
        print("Bye Bye ")
        print("Your account Sucessfully Deleted")
        main()


# In[10]:


def chk_bal(i):
    print("Name = ",bank['user'][i])
    print("Acc Number = ",bank['acc'][i])
    print("Balance = ",bank['bal'][i])
    choice(i)


# In[4]:


def credit(i):
    global bank
    print("\n\nWelcome to Credit Services  ".center(1000,'*'))
    amount = int(input("Enter amount to deposite : "))
    bank['bal'][i] += amount
    print("Now you have {} rs in your account\n{} credited sucessfully in your account".format(bank['bal'][i],amount))
    choice(i)


# In[5]:


def debit(i):
    global bank
    print("\n\nWelcome Debit Services ".center(1000,'*'))
    amount = int(input("Enter amount to be withdraw : "))
    if amount > bank['bal'][i] :
        
        print("Insufficient Balance\nyou have only {} rs in your account".format(bank['bal'][i]))
        print("\nTry Again ")
        debit(i)
    else :
        bank['bal'][i] -= amount 
        print("You have withdrawn {} rs and you have left {} in your account.".format(amount,bank['bal'][i]))
        choice(i)


# In[6]:


def choice(i):
    print("Welcome back {}".format(bank['user'][i]).center(1000,'*'))
    print("\n\nMenu\n")
    print("1.Debit\n2.Credit\n3.Statement\n4.Profile Update\n5.Logout")
    ch = int(input("Enter your Choice : "))
    if ch == 1 :
        debit(i)
    elif ch == 2 :
        credit(i)
    elif ch == 3 :
        chk_bal(i)
    elif ch == 4 :
        profile(i)
    elif ch == 5 :
        main()
    else :
        print("Error: Invalid Choice\nTry Again")
        choice(i)
    


# In[7]:


def login():
    from getpass import getpass 
    print("Welcome to Login Facility".center(1000,"*"))
    print("\n\n")
    acc_no = int(input("Login ID : "))
    password = getpass("Password :")
    if acc_no in bank['acc'] : 
        i = bank['acc'].index(acc_no)
        if password == bank['passwd'][i] : 
            choice(i)
        else :
            print("\n\nError Wrong Password Try Again : ")
            login()
    else :
        print("\n\nNo such Account Exist\nYou Should Signup\n\n")
        main()


# In[8]:


def main():
    os.system('reset')
    print("Welcome to Bank Program".center(1000,'*'))
    print("Menu")
    print("1.Login\n2.SignUp\n3.Exit")
    ch = int(input("Enter your Choice : "))
    if ch == 1 : 
        os.system('reset')
        login()
    elif ch == 2 :
        os.system('reset')
        signup()
    elif ch == 3 :
        os.system('reset')
        exit(0)
    else :
        print("\n\nInvalid Input\nTry Again")
        os.system('reset')
        main()


# In[9]:


 
main()

