import socket
from itertools import count
#from socket_utils import *

HEADER_SIZE = 4

USER_NAME = input("Username: ")

IP = "127.0.0.1"
PORT = 4242
ENCODING = "utf-8"

host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host.connect((socket.gethostname(), PORT))


#sock.setblocking(False)


for i in count(0):
    message = input(f"{USER_NAME}$ ")
    message = message.encode(ENCODING)
    HEADER = f"{ len(message) : <{HEADER_SIZE}}"
    PACKET = HEADER.encode(ENCODING) + message 
    host.send(PACKET)