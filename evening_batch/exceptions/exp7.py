class myerror(Exception):
    def __init__(self):
            Exception.__init__(self)
            self.m = "This is my error\n I can do anything in python "
    def __str__(self):
        return self.m
def error():
    try :
        a = int(input("enter a no "))
        if a < 0 :
             raise myerror
    except myerror as e:
        print(e)
        error()
    else :
        print("Yaa you have learn it")

if __name__ == "__main__":
    error()

