import socket
import time
import threading

from itertools import count

HEADER_SIZE = 4

IP = '127.0.0.1'
PORT = 4242
ENCODING = "utf-8"


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((socket.gethostname(), PORT))
serverSocket.listen(5)

SELF_MSG = "Client {} connected to port {}!"
MSG = "Connection established with server!"

# Packet Header Template

runningThreads = list()

def newCommunication(clientSocket, clientAdress, message):
    for i in count(0):    
        packetSizeRaw = clientSocket.recv(HEADER_SIZE)
        packetSizeString = packetSizeRaw.decode(encoding=ENCODING).split()[0]
        print("raw:", packetSizeRaw)
        packetSize = int(packetSizeString, 10)
        
        messageRaw = clientSocket.recv(packetSize)
        message = messageRaw.decode(encoding=ENCODING)

        print(f"Client Ip: {clientAdress[0]}$", message)

def main():
    while True:
        newClient, newClientAdress = serverSocket.accept()
        newThread = threading.Thread(target=newCommunication, args=(newClient, newClientAdress, MSG))
        runningThreads.append(newThread)
        newThread.start()


if __name__ == '__main__':
    main()