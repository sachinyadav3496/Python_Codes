import smtplib as smtp 
from getpass import getpass

user = "3496.grras@gmail.com"
password = getpass()

sender = "grrassolutions@gmail.com"

emails = [ "rohitjain064@yahoo.com","yashmthr65@gmail.com","sachin@grras.com" ]



subject = "Hurry up!! 50% dicount on new Batches!! Enroll Today"

body = """This is to inform that we are having new batches with a very big discounts.
Hurry to join.....
first come first serve policy
"""

for to in emails : 

    message = f"""From:{sender}
    To:{','.join(to)}
    Subject:{subject}

    {body}

    """

    host = "smtp.gmail.com"
    port = 465

    try : 

        server = smtp.SMTP_SSL(host,port)
        server.ehlo()

        server.login(user,password)

        server.sendmail(sender,to,message)

        print(f"Mail is Sucessfully Dileveredi to {to}")


    except Exception as error : 
        print("Something Went Wrong !!! ",error)


