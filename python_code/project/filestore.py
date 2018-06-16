##creating empty lists everytime the program is initialized
cusnames=[]
cuspasswords=[]
cusbalance=[]

##opening the storage files to collect old customer data
namefile=open("cusnamefile.txt", "r")
passfile=open("cuspassfile.txt", "r")
balfile=open("cusbalfile.txt", "r")

##populate the empty lists with data from storage files
##check list of customer names
for line in namefile:
        cusnames.append(line[:-1])
namefile.close()

##check list of customer passwords
for line in passfile:
        cuspasswords.append(line[:-1])
passfile.close()

##check list of customer balances
for line in balfile:
        cusbalance.append(line[:-1])
balfile.close()


##function creates a new user 
def cusaccountcheck():
        name=""
        pin=""

        while name not in cusnames and len(name)<3:
                name=input("Please type in your name for this new bank account\n")
                if name not in cusnames:
                        cusnames.append(name)
                        filewrite(cusnames)
                        break
                print("Sorry, that user name is already in use")
                ans=input("Are you already a member at this bank? (y/n)\n")
                if ans.lower()=='y':
                        oldcuscheck()
                else:
                        cusaccountcheck()

        while len(pin)<4:
                pin=input("Please assign a password to this account, pin should be at least 5 characters\n")
                if len(pin)>4:
                        print("your pin has been successfully saved")
                        print("Remember to always keep your pin safe and don't disclose it to anybody")
                        cuspasswords.append(pin)
                        cusbalance.append(0)
                        balance=100.0
                        cusbalance[cusnames.index(name)]=balance
                        filewrite(cuspasswords)
                        filewrite(cusbalance)
                        break

                print("Sorry, that is a short password")

        return name,pin, balance

##Function to check returning customer
def oldcuscheck():
        name=""
        while name not in cusnames:
                name=input("What is your name?\n")
                if name in cusnames:
                        username=name
                        userpassword=cuspasswords[cusnames.index(name)]
                        balance=float(cusbalance[cusnames.index(name)])
                        return username, userpassword, balance
                else:
                        print("Sorry %s, It looks like you didn't spell you name correctly or your name is not in our records"%name)
                        again=input("would like to type in your name again? (y/n)")
                        if again.lower()=='y':
                                oldcuscheck()
                        else:
                                print("Bye bye, thank you for trying Postbank")
                                exit()




##This function writes new data into the storage files whenever called upon.      
def filewrite(item):
        if item==cusnames:
                text=open("cusnamefile.txt","w")
                for i in item:
                        text.write(i+"\n")
                text.close()

        elif item==cuspasswords:
                text=open("cuspassfile.txt", "w")
                for i in item:
                        text.write(i+"\n")
                text.close()

        elif item==cusbalance:
                text=open("cusbalfile.txt", "w")
                for i in item:
                        text.write(str(i)+"\n")
                text.close()

###This function updates the account balance after a withdraw or deposit transaction
def balupdate(ind, amount):
        accountnumber=cusnames.index(ind)
        accountbal=float(cusbalance[accountnumber])
        accountbal+=amount
        cusbalance[accountnumber]=accountbal
        text=open("cusbalfile.txt", "w")
        for i in cusbalance:
                text.write(str(i)+"\n")
        text.close()

###This function deletes an existing account and any data that was stored about it is cleared
def deleteaccount(name):
        accountnumber=cusnames.index(name)
        del cusnames[accountnumber]
        filewrite(cusnames)
        del cusbalance[accountnumber]
        filewrite(cusbalance)
        del cuspasswords[accountnumber]
        filewrite(cuspasswords)
        return None
