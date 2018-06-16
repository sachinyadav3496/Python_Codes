import socket

server = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
hostname = socket.gethostname()
port = 5400

server.bind((hostname,port))
print("Server is ready to listen")
server.listen(1)
addr,conn = server.accept()
print("Got Connection from ",conn[0]," on ", conn[1])
while True:
    msg = input(">>")
    if msg.lower == "eof":
        server.close()
        exit(0)
        break
    addr.send(msg.encode())
    data = addr.recv(1024)
    print("\t\t\t\t%s"%(data.decode()))


