import socket
import time
import os
from socket_utils import packetProcess, hello_txt, connection


USER_NAME = input("Username: ")

IP = socket.gethostbyname(socket.gethostname())
PORT = 4242
HEADER_SIZE = 4
ENCODING = "utf-8"

host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host.connect((socket.gethostname(), PORT))
#sock.setblocking(False)


def main():
    connection(time.sleep)
    os.system('cls')
    hello_txt(USER_NAME)

    while True:
        PACKET = packetProcess(USER_NAME, HEADER_SIZE, ENCODING)
        host.send(PACKET)


if __name__ == '__main__':
    main()