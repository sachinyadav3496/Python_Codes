import socket

client_socket = socket.socket()
server_addr = input("Enter IP of Server like 192.168.1.200 :")
server_port = int(input("Enter port to connect on : "))

client_socket.connect((server_addr,server_port))
print("Got Connected from server at IP 192.168.1.200 on port 54321")
print()
print()
print()
fname = client_socket.recv(1024)
fname = fname.decode()
f = open(fname,'wb')
while True:
    data = client_socket.recv(1024)
    if data.decode() :
        f.write(data)
    else :
        f.close()
        client_socket.close()
        break
print("file received sucessfully")
