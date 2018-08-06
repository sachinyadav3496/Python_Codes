import smtplib

message = """From:smartsachinyadav.ram@gmail.com
To: sachinyadav3496@gmail.com
MIME-Version: 1.0
Content-type:text/html
Subject:SMTP HTML e-mail  test
This is an email messsage to be send in HTMLformat
<html>
<head><title>mymail</title>
<h1>Welcome to grras</h1>
</head>
<body>
<h1>If you are seeing this </h1>
<h2>Awesome man</h2>
<b>This is HTML Message.</b>
<p>hey this iss very good to see this</p>
<h1>This isheadline.</h1>
</body>
</html>
"""
server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.ehlo()
print("Connection Sucessfully Stablished")
server.login('smartsachinyadav.ram@gmail.com','ramsacyadav')
print("SucessFuly Logged in ")
server.sendmail('smartsachinyadav.ram@gmail.com','sachinyadav3496@gmail.com',message)
print("Mail sucessfully Delivered")
server.close()
