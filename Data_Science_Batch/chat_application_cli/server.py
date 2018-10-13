import socket
host = socket.gethostname()
port = 1234
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((host,port))
print("SERVER is running on {}:{} ".format(host,port))
server_socket.listen(5)
client_socket,client_addr = server_socket.accept()
print("Client Connect with {}:{}".format(*client_addr))
while True :
    smsg = input("server-->")
    client_socket.send(smsg.encode())
    cmsg = client_socket.recv(1024)
    print("\t\t\t\tclient-->",cmsg.decode())
    if smsg == 'bye' or cmsg.decode() == 'bye' : 
        client_socket.close()
        server_socket.close()
        break
