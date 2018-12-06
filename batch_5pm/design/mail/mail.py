import smtplib as smtp 
from getpass import getpass

#user agent
#mime types

user = input("Enter your mail address : ")
password = getpass()

sender = "grrassolutions@gmail.com"

with open(input("Enter Email File Path  : ").strip()) as fp : 
    data = fp.read()

emails = data.split('\n')

subject = input("Type in your Subject : ") 

print("\n\nType your mail Here ... Any time write EOF to exit editor \n\n")

body = ""
while True :
    line = input()
    if line.strip().lower() == 'eof' : 
        break
    body += line+'\n'



for to in emails : 

    message = f"""From: {sender}
    To: {to}
    MIME-Version: '1.0'
    Content-type: 'text/html'
    Subject: {subject}

    {body}

    """

    host = "smtp.gmail.com"
    port = 465

    try : 

        server = smtp.SMTP_SSL(host,port)
        server.ehlo()

        server.login(user,password)

        server.sendmail(sender,to,message)

        print(f"\n\nMail is Sucessfully Dileveredi to {to}")


    except Exception as error : 
        print("Something Went Wrong !!! ",error)


