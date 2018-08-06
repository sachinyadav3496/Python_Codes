import socket
s = socket.socket()
hostname = socket.gethostname()
port = 12345
s.connect((hostname,port))
print("Got Connected")
while  True:
   data =  s.recv(1024)
   print("\t\t\t",data.decode())
   d = input()
   if d == 'eof':
       s.close()
       break
   s.send(d.encode())

