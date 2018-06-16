import socket 
import sys

try :
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("\n\nSocket is created \n")
except socket.error as e :
    print("There is an error !!!",e)
    
ip = socket.gethostbyname('localhost')
port = 12345

s.bind((ip,port))
print("\nSocket is ready to listen on ",ip,"at port ",port)


s.listen(1)

c,addr = s.accept()

print("Got a connection from ",addr)

c.send("\n\nWelcome to my connection".encode('ascii'))

data = c.recv(1024)
print(data.decode())

s.close()
