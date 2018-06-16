class rob(object):
    """Hi i am a robot"""
    def __init__(self,name):
        self.name = name
    def show(self):
        print("My name is ",self.name)

    def __str__(self):
        return 'HI I am {}'.format(self.name)
    
if __name__ == "__main__" :
    rob1 = rob('python')
    rob1.show()
    rob2 = rob('hello')
    rob2.show()
