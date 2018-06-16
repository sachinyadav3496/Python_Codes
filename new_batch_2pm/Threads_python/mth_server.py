import threading as th 
import time
import socket

s = socket.socket()
host = socket.gethostname()
port = 1234

s.bind((host,port))

