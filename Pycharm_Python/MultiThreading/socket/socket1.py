import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))
s.listen(5)
while True:
    c,addr = s.accept()
    print("Got Connection from ",addr)
   # c.send('thank you for connecting'.encode('ascii'))
    while True:
        print("Messege->client: ")
        c.send(input().encode('ascii'))
        ch =  input("recv msg - y/n")
        if ch == 'y':
            print(c.recv(1024))
        else:
            c.close()
            break
    c.close()




