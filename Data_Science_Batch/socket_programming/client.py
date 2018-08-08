import socket

host = '192.168.1.111' # address of server
port = 1234 # port of server

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


server_socket.connect((host,port))

print("Connect with server at  {}:{}".format(host,port))

while True :
    smsg = server_socket.recv(1024)
    print("\t\t\t\tserver-->",smsg.decode())
    cmsg = input("cmsg-->")
    server_socket.send(cmsg.encode())
    if smsg.decode() == 'bye' or cmsg == 'bye' : 
        server_socket.close()
        break
