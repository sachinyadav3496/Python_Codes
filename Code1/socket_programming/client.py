import socket
s = socket.socket()
hostname = socket.gethostname()
port = 12345
s.connect((hostname,port))
print("Got Connected from ",hostname)
print("\nStart Chat\n\n")
while  True:
   data =  s.recv(1024)
   print("\t\t\t\t>>",data.decode())
   msg = input()
   if msg.lower == 'exit':
       s.close()
       break
   s.send(msg.encode())


