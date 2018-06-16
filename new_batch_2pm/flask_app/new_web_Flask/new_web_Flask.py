from flask import Flask,render_template,request,make_response,session
import pymysql as sql
app = Flask(__name__)
app.secret_key='anythingthatwillusetoencrypted'
try :
    db = sql.connect(host='localhost',port=3306,user='root',password='',database='student')
    c = db.cursor()
except Exception as e:
    print("Error!%s"%e)
@app.route('/hello')
def hello():
    return render_template('hello.html')
@app.route('/')
def hello_world():
    if 'UserID' in session:
        name = session['UserID']
        return render_template('index.html',data=name)
    else :
        return render_template('index.html')

@app.route('/login',methods=['POST',"GET"])
def login():
    name = request.form['username']
    password = request.form['passwd']
    try:
        cmd = 'select * from student where name="%s"'%(name)
        c.execute(cmd)
        data = c.fetchone()
        if  data:
            if password == data[1] :
                data = { 'Name':data[0],'Address':data[1],'Grade':data[2],'Ph_no':data[3] }
                session['UserID'] = name
                return render_template('profile.html',info=data)
            else:
                return '<h1>Error!!!Password Incorrect</h1>'
        else:
            return '<h1>Error!!No such user Exist</h1>'
    except Exception as e:
        return '<h1>Errror!!%s</h1>'%(e)

@app.route('/logout')
def logout():
     session.pop('UserID')
     return render_template('index.html ')
     #resp = make_response(render_template('index.html'))
     #resp.delete_cookie('UserID')
     #return resp

if __name__ == '__main__':
    app.run(host='localhost',port=80,debug=True)
