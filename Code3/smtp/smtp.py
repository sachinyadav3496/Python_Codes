import smtplib
try:
    server_ssl=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server_ssl.elho()
except Exception as e:
    print("Something went wrong",e)

