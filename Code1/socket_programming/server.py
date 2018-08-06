import socket

s = socket.socket()

hostname = socket.gethostname()
port = 12345
s.bind((hostname,port))
s.listen(1)
addr,ss = s.accept()
print("We got connection from ",ss)
print("\nYou can start Chat\n\n")
while True:
    data = input(">>")
    if data.lower() == 'exit':
        s.close()
        break
    addr.send(data.encode())
    msg=addr.recv(1024)
    print("\t\t\t\t<<",msg.decode())


