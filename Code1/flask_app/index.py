from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    s = '''<h1 style="color:red">Welcome to First Flask Page</h1>
    <h2><a href='/hello'>Click Me</a></h2>'''
    return s

@app.route('/hello')
def hello():
    return '<h1>Welcome to hello page</h1>'

if __name__ == "__main__" :
    app.run(host='localhost',port=80,debug=True)
