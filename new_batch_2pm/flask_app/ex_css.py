from flask import Flask,render_template,url_for,request
import pymysql as sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ex_css.html')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('ex_hello.html',name=name)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST' :
        name = request.form['name']
        password = request.form['passwd']
        try : 
            db = sql.connect('localhost','root','','bank')
            c = db.cursor()
            c.execute('select * from data where name="%s"'%(name))
            data = c.fetchone()
            if password == data[2] :
                return render_template('ex_logged.html',data=data)
            else :
                return '<h1>Error:Password Incorrect Try Again</h>'

        except Exception as e:
            return '<h1>Database Connectivity Error</h1>'
        
    else :
        return "<h1>Error WE only work on Post Methods</h1>"


@app.route('/profile')
def pk():
    #database
    try : 
        db = sql.connect('localhost','root','','bank')
        c = db.cursor()
        c.execute('select * from data')
        data = c.fetchall()
        db.close()
        return render_template('ex_profile.html',data=data)
    except Exception as e:
        return '<h1>Database Connectivity Error</h1>'

if __name__ == "__main__" :
    app.run(host='localhost',port=80,debug=True)
