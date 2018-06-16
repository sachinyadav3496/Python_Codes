import socket
client = socket.socket()
hostname = socket.gethostname()
port = 5400
client.connect((hostname,port))
print("Got Connection ",hostname)
while True:
    msg = client.recv(1024)
    print(">>",msg.decode())
    data = input("\t\t\t\t>>")
    if data.lower == "eof":
        exit(0)
        client.close()
        break
    client.send(data.encode())

