
import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))
s.listen(5)
while True:
    c, addr = s.accept()
    print("Connection is stablished from client",addr)
    c.send("Thank  you for connecting to our server ")
    c.close()

