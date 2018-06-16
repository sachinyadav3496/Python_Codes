import socket

c = socket.socket()

hostname = socket.gethostname()
port = 12345

c.connect((hostname,port))


while True:
    msg = c.recv(1024)
    print(msg.decode())
    c.send("hello".encode())
    

