from flask import Flask,render_template,request
import pymysql as sql 


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
@app.route('/hello/<string:name>')
def hello(name=None):
    return render_template('hello.html',username=name)

@app.route('/login',methods=['POST','GET'])
def login():
    try : 
        db = sql.connect('localhost','root','','bank')
        c = db.cursor()
        form = request.form
        username = form['username']
        password = form['password']
        signin = form['keep_signin']
        query = f"select * from user where acc={int(username)}"
        c.execute(query)
        data = c.fetchone()
        if data : 
            if password == data[2] : 
                page = f"""<!Doctype html>
                <html>
                <body>
                <p>Account Number = {username}</p>
                <p>Username = {data[1]}
                <p>Password = {password}</p>
                <p>Balance = {data[3]} </p>
                """
                return page
            else : 
                return '<h1>Invalid Password Try Again</h1>'
        else :
            return "<h1>No such user exists</h1>"

    except Exception as e : 
        return f"<h1 style='color:red'>Something Went Wrong</h1>{e}"
        #return render_template('login.html',user=username,password=password,var=signin)


if __name__ == "__main__" : 

    app.run(host='localhost',port=80,debug=True)
