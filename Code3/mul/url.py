import smtplib
sender = 'smartsachinyadav.ram@gmail.com'
receivers = ['sachinyadav3496@gmail.com']

message = """From: From Person sachinyadav.ram@gmail.com
To:  To person sachinyadav3496@gmail.com
Subject: smtp email test

This is a test email to check connectivity of email using smtp
"""
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message)
    print("Sucessfully send email")
except SMTPException:
    print("Error!!! : unable to send mail")

