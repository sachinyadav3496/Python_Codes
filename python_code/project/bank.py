import filestore
import time
import datetime



#This is the function that is called at the beginning of the program
def postbank():                                                                         
    print ("Welcome to PostBank, We care for you\n")                                    
    prompt=int(input("""To open a new bank account, Press 1\n"""+                                        
                        """To access your existing account & transact press 2\n"""))    
    if prompt==1:                                                                       
        cus=BankAccount()#creates a new customer profile                                
    elif prompt==2:                                                                     
        cus=ReturnCustomer()#checks for existing customer                               
    else:                                                                               
        print("You have pressed the wrong key, please try again")                        
        postbank()                                                                      





##class for creating an instance of a new back account and other default bank functions
class BankAccount:
    """Class for a bank account"""
    type="Normal Account"
    def __init__(self):
        ##calls functions in the module filestore
        self.username, self.userpassword, self.balance=filestore.cusaccountcheck()
        print ("Thank you %s, your account is set up and ready to use,\n a 100 pounds has been credited to your account" %self.username)
        time.sleep(2)
        self.userfunctions()



    def userfunctions(self):
        print("\n\nTo access any function below, enter the corresponding key")
        print ("""To:
check Balance, press B.
deposit cash,  press D.
withdraw cash, press W.
Delete account press X.
exit service,  press E\n
:""")
        ans=input("").lower()
        if ans == 'b':
            ##passcheck function confirms stored password with user input
            self.passcheck()
            self.checkbalance()
        elif ans == 'd':
            self.passcheck()
            self.depositcash()
        elif ans== 'w':
            self.passcheck()
            self.withdrawcash()
        elif ans=='x':
            print ("%s, your account is being deleted"%self.username)
            time.sleep(1)
            print ("Minions at work")
            time.sleep(1)
            filestore.deleteaccount(self.username)
            print ("Your account has been successfuly deleted, goodbye")
        elif ans=='e':
            print ("Thank you for using PostBank Services")
            time.sleep(1)
            print ("Goodbye %s" %self.username)
            exit()

        else:
            print("No function assigned to this key, please try again")
            self.userfunctions()

    def checkbalance(self):
        date=datetime.date.today()
        date=date.strftime('%d-%B-%Y')
        self.working()
        print(("Your account balance as at {} is {}").format(date, self.balance))
        self.transact_again()

    def withdrawcash(self):
        amount=float(input("::\n Please enter amount to withdraw\n: "))
        self.balance-=amount
        self.working()
        print("Your new account balance is %.2f" %self.balance)
        print("::\n")
        filestore.balupdate(self.username, -amount)
        self.transact_again()

    def depositcash(self):
        amount=float(input("::\nPlease enter amount to be deposited\n: "))
        self.balance+=amount
        self.working()
        print("Your new account balance is %.2f" %self.balance)
        print("::\n")
        filestore.balupdate(self.username, amount)
        self.transact_again()



    def transact_again(self):
        ans=input("Do you want to do any other transaction? (y/n)\n").lower()
        self.working()
        if ans=='y':
            self.userfunctions()
        elif ans=='n':
            print("Thank you for using PostBank we value you. Have a good day")
            time.sleep(1)
            print("Goodbye {}").format(self.username)
            exit()
        elif ans!='y' and ans!='n':
            print("Unknown key pressed, please choose either 'N' or 'Y'")
            self.transact_again()


    def working(self):
        print("working"),
        time.sleep(1)
        print ("..")
        time.sleep(1)
        print("..")
        time.sleep(1)


    def passcheck(self):
        """prompts user for password with every transaction and counterchecks it with stored passwords"""
        b=3
        while b>0:
            ans=input("Please type in your password to continue with the transaction\n: ")
            if ans==self.userpassword:
                return True


            else:
                print("That is the wrong password")
                b-=1
                print("%d more attempt(s) remaining" %b)

        print("Account has been freezed due to three wrong password attempts,\n contact your bank for help, bye bye")
        time.sleep(1)
        print ("...")
        time.sleep(1)
        print("...")
        time.sleep(1)

        exit()


class ReturnCustomer(BankAccount):
    type="Normal Account"
    def __init__(self):
        self.username, self.userpassword, self.balance=filestore.oldcuscheck()
        self.userfunctions()

postbank() ##calling the function to run the program
