class robot:

    """Hi I am a robot \nI have three function show set_var msg"""
    msg = "Everthing is cool\nStay cool"
    counter = 0
    def __init__(self,name='robot',age='28',work='default'):

        self.name = name
        self.age = age
        self.work = work
        robot.counter += 1

    def show(self):
        """show()->use to print details of a robot."""
        print("Robot Name = ",self.name)
        print("Robot Age = ",self.age)
        print("Robot work = ",self.work)
        print("Class Message = ",robot.msg)

    def print_msg(self):
        """msg()->print Shared Messege"""
        print("Message = ",robot.msg)

    def set_var(self):
        """set_var()->Brodcast Message"""
        print("Old Messege is %s"%robot.msg)
        print("Broadcase New Messege to All Active Objects")
        robot.msg = input("Enter your message - \n")
        print("All instances are update to %s"%robot.msg)
    def no_robot(self):
        print("There are %s robots out there from robot class"%(robot.counter))

if __name__ == "__main__" :
    print("Starting class objects \nWe have %s objects right now"%robot.counter)
    chitti = robot('chitti',45,'all most everthig')
    chitti.no_robot()
    gone = robot('gone',25,'technical')
    gone.no_robot()
    rob1 = robot()
    rob1.no_robot()
    rob2 = robot('new robot')
    rob2.no_robot()
    rob3 = robot(name='fan',work='normal')
    rob3.no_robot()





