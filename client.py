import socket
import time
import os
#from socket_utils import *

HEADER_SIZE = 4

USER_NAME = input("Username: ")

IP = socket.gethostbyname(socket.gethostname())
PORT = 4242

ENCODING = "utf-8"

host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host.connect((socket.gethostname(), PORT))
#sock.setblocking(False)


def main():
    for i in range(1, 4):
        print("Connecting" + i * '.'); time.sleep(i)
        os.system('cls')

    print(f"Hello {USER_NAME}! Welcome to IRC, press Q if you would like to exit.", end='\n\n')

    while True:
        message = input(f"{USER_NAME}$ ")
        message = message.encode(ENCODING)
        HEADER = f"{ len(message) : <{HEADER_SIZE}}"
        PACKET = HEADER.encode(ENCODING) + message 
        host.send(PACKET)


if __name__ == '__main__':
    main()