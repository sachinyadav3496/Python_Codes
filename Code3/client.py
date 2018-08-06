import socket
host = 'DESKTOP-FSIF8SI'
port = 12345
s = socket.socket()
s.connect(s.bind((host,port)))
while True:
    ch=("receive msg - y/n'")
    if ch == 'y':
        print(s.recv(1024))
        s.send(input("message->server:").encode('ascii'))
    else:
        s.close()
        break

