from flask import Flask
from flask_mail import Mail, Message
app =Flask(__name__)
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jangidrakesh71@gmail.com'
app.config['MAIL_PASSWORD'] = '7891016482'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)
@app.route("/")
def index():
    msg = Message(
'Hello',
sender='jangidrakesh71@gmail.com',
recipients=
['parul2595@gmail.com','shivani.sharma231996@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"   
    mail.send(msg)
    return "Sent"

if __name__ == '__main__' : 
    app.run(host='localhost',port=80,debug=True)
