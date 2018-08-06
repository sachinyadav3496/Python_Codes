import socket
client_socket = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 12345
client_socket.connect((host,port))
while True :
    cl_msg = client_socket.recv(1024)
    print("\t\t\tserver->",cl_msg.decode())
    msg = input("client->")
    client_socket.send(msg.encode())
    if ( msg.lower() == 'bye' ) or ( cl_msg.decode() == 'bye' ) :
        client_socket.close()
        break
