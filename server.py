import socket
import time
import threading
from   itertools import count
from   socket_utils import newCommunication, safeThread, mySocket
import sys

OUTPUT_PATH = open('stdout.txt', 'w+')

IP = socket.gethostbyname(socket.gethostname())
PORT = 4242
HEADER_SIZE = 4
ENCODING = "utf-8"
runningThreads = list()


serverSocket = mySocket(None
                        ,name       = 'server' 
                        ,ip         = '127.0.0.1'
                        ,port       = PORT
                        ,family     = socket.AF_INET
                        ,protocol   = socket.SOCK_STREAM 
                        ,encoding   = ENCODING  
                        ,headerSize = HEADER_SIZE
                        ,isServer   = True
                )


def main(serverSocket):
    serverSocket.initialize()
    serverSocket.listen(5)

    while True:
        client, newClientAdress = serverSocket.accept()
        newClientIp, newClientPort = newClientAdress
        
        ###################################################################
        willbeimplemented = """
        newClient = mySocket(sock     = client,
                             name     = f"client{serverSocket.numClients}",
                             ip       = newClientIp, 
                             port     = newClientPort, 
                             family   = serverSocket.family, 
                             protocol = serverSocket.protocol, 
                             isServer = False )
        """
        #####################################################################

        newThread = threading.Thread(target = newCommunication 
                                    ,args   = (serverSocket 
                                              ,client
                                              ,newClientAdress
                                              ,OUTPUT_PATH )) 
        
        newThread.start()
        runningThreads.append(newThread)

def kernel():
    mainThread = safeThread(target = main ,args = (serverSocket,), daemon=True)
    mainThread.start()

    while True:
        opt = input("root$ ")

        # Honorable mentions: Nazım the Debugger
        if opt == 'killmain':
            mainThread.stop()
            break 

if __name__ == '__main__':
    kernel()