import socket

s = socket.socket()

ip = socket.gethostbyname('localhost')

port = 12345

s.connect((ip,port))
print("Ready to connect ",ip,"at port ",port)

data = s.recv(1024)
print(data.decode())
s.send("hello I am client".encode('ascii'))

s.close()
