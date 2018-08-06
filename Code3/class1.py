class Hello:
    'This is to print Hello'
    name = 'this is class variable'
    def __init__(self,name,sur_name):
        self.name=name
        self.sur_name=sur_name
    def hello(self):
        print("Hey this is python it is awesome ! ")
        print("name = ",self.name)
        print("sur_name = ",self.sur_name)
        print("class var ", Hello.name)
       
f = Hello('python','bhai')
f.hello()
k = Hello('sachin','yadav')
k.hello()
print(Hello.__doc__)
print(dir(Hello))
print(Hello.name)

