class Robot:
    " Hi I am a Robot Class."
    count = 0
    msg = None
    def __init__(self,name,age,func='gaming'):
        self.name = name
        self.age = age
        self.func = func
        Robot.count += 1

    def no_of_robot(self):
        print(Robot.count)
    def build(self,lang,country):
        self.lang = lang
        self.country = country
        self.extra = input("Enter extra information - ")

    def show(self):
        print("Name = ",self.name)
        print("Age = ",self.age)
        print("country = ",self.country)
        print("Function = ",self.func)
        print("Language = ",self.lang)
        print("Extra info = ",self.extra)
    def chat(self):
        print(Robot.msg)
        Robot.msg = input("your msg - ")

robot1 = Robot('rob1',33)
robot2 = Robot('rob2',21,'music')

robot1.build('hindi','india')
robot2.build('english','us')

robot1.show()
robot2.show()
