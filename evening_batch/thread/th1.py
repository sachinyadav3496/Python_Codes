from _thread import start_new_thread

threadId = 1

def factorial(n):
    
    global threadId

    if  n < 1:
        print("%s : %d"%("Thread",threadId))
        threadId += 1
        return 1
    else :
         Number = n * factorial(n-1)
         print(str(n)+'! = '+str(Number)) 
         return Number

start_new_thread(factorial,(5,))
start_new_thread(factorial,(4,))
c = input("Waiting for threads to return \n")
