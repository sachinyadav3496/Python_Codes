import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))
while True:
    print(s.recv(1024))
    s.send(input("enter string to send - ").encode('ascii'))
    ch = input("continue y / n - ")
    if ch == 'n':
        break
s.close()
