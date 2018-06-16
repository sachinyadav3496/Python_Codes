import smtplib

print("Welcome to Grras Solutions Private  Ltd. Email Service ")

gmail_user = input("Enter your Mail ID to login - ")
gmail_password = input("Enter your password for authntication - ")

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    print("Connection established ")
    server.ehlo()
    server.login(gmail_user, gmail_password)
    print("You have Successfully logged in your account ",gmail_user)
except Exception as e:
    print("Error!!! in Connection ")
    print(e)
    exit(0)
sent_from = gmail_user

i = int(input("Enter no. of recipients - "))

print("Enter Recipients Email Addressess - ")

to = []

for k in range(i):
    to.append(input())


subject = input("\n\nPlease Type in Subject of The Mail - ")

print("\n\nType in Your Message (Type in EOF to FINISH)i\n\n")


message=[]

while True:
    msg = input()
    if msg.upper() == 'EOF' :
        break
    else :

        message.append(msg)

print("\n\nMessege is Ready for Delivery\n\n ")

body = '\n'.join(message)

email_text = """From:%s  
To:%s  
Subject:%s
%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    print("Email sending is  in process  - \n  ")
    server.sendmail(sent_from, to, email_text)
    server.close()
except Exception as e:
    print('Something went wrong...',e)
else:
    print("Message Delivered to - \n")
    for i in to:
        print(i)
    print("**********************Exiting********************")
    print("Thanks For using Grras Mail Service ")


