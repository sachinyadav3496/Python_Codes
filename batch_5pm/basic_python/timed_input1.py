from threading import Timer

timeout = 3

t = Timer(timeout,print,["Sorry Times Up"])

t.start()

prompt = "You have {} time to give input.".format(timeout)

answer = input(prompt)

t.cancle()
