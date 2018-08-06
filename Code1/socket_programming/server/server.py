import socket

s = socket.socket()

hostname = socket.gethostname()
port = 12345
s.bind((hostname,port))
s.listen(1)
addr,ss = s.accept()
print("We got connection from ",ss)
while True:
    data = input()
    addr.send(data.encode())
    d  = addr.recv(1024)
    d.strip()
    print("\t\t\t\t",d)
    if data.lower() == 'eof':
        break
s.close()


