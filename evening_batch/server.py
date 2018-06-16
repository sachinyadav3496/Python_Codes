import socket

s = socket.socket()

hostname = socket.gethostname()
port = 12345

s.bind((hostname,port))

s.listen(5)

while True:
    c,addr = s.accept()
    print("Got a connection from - ",addr)
    c.send("server->hello".encode())
    msg = c.recv(1024)
    print("client->",msg.decode())

