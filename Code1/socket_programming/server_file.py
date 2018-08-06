import socket
server_socket = socket.socket()
#hostname = '192.168.1.200' 
#hostname = socket.gethostbyname(socket.gethostname())
hostname = input("Enter hostname or IP to create server : ").strip()
port = int(input("Enter port number : "))
server_address = (hostname,port)
server_socket.bind(server_address)

print("Sever Socket is sucessfully Created ")
print("Hostname = ",hostname)
print("Port = ",port)

server_socket.listen()
print("Server is Listening on IP {} at Port {} for connection from client".format(hostname,port))

client_socket,client_address = server_socket.accept()
c_ip,c_port = client_address
print("Got a connection from client {}:{}".format(c_ip,c_port))
print()
print("Starting Communication With Client")
print("Type EOF to end communication")
print()
print()
fname = input("Enter file name : ")
client_socket.send(fname.encode())
f = open(fname,'rb')
while True :
    msg = f.readline()
    if msg:
        client_socket.send(msg)
    else :
        f.close()
        client_socket.close()
        break
