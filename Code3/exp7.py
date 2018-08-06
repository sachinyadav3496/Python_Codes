class myException(FileNotFoundError):
    def __init__(self):
        pass
    def error(self):
        print("Error reslove it ")
try:
    if 6 > 5:
            raise myException#("File is not available please select accordant file ")
except myException as e:
    e.error()
else:
    print("yo you have done it man")
