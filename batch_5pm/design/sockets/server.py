import socket 
import os

server = socket.socket()

host = socket.gethostbyname(socket.gethostname())
port = 12345

server.bind((host,port))

os.system('cls')

server.listen(1)

print(f"Server is listining on ip {host} on port number {port}\n")

client,addr = server.accept()


print(f"Server is Waiting for client to connect ...")

print(f"\nGot a connection from Client having ip {addr[0]} on port number {addr[1]}\n\n")


while True : 

    msg = input("server--->")
    msg = "server-->" + msg.strip()
    client.send(msg.encode())
    cmsg  = client.recv(1024)
    print(f"client--->{cmsg.decode()}".rjust(200))

    if msg.lower() == 'bye' or cmsg.decode().lower() == 'bye' : 
        client.close()
        server.close()
        break


