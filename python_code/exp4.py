def hello(value):
    if value < 1:
        raise Exception(value)
    return value
try:
    hello(-12)
    print("level 1")
except Exception as e:
    print("Error in argument ",e.args[0])
