import socket
import time
import threading
from   itertools import count
from   socket_utils import newCommunication

IP = socket.gethostbyname(socket.gethostname())
PORT = 4242
HEADER_SIZE = 4
ENCODING = "utf-8"

runningThreads = list()

class mySocket(object):
    def __init__(self 
                ,sock
                ,name 
                ,ip
                ,port         = 4242
                ,family       = socket.AF_INET
                ,protocol     = socket.SOCK_STREAM
                ,encoding     = 'utf-8'
                ,headerSize   = 4 
                ,isServer     = False
    ):                         
        self._SOCK            = sock
        self.name             = name
        self.ip               = ip 
        self.port             = port
        self.family           = family
        self.protocol         = protocol
        self._ENCODING        = encoding
        self._HEADER_SIZE     = headerSize
        self.isServer         = isServer
        self.receivedMessages = 0                  # Number of messages
        self.sentBytes        = 0
        self.receivedBytes    = 0                  # Without header!
        self.numClients       = 0
        self.clients          = dict()

    def initialize(self):
        self._SOCK = socket.socket(self.family, self.protocol)
        self._SOCK.bind((self.ip, self.port))
        
    def listen(self, num):    
        self._SOCK.listen(num)

    def accept(self):
        self.numClients += 1
        client, clientAddr = self._SOCK.accept()
        self.clients[clientAddr[0]] = client      # ip adress => key, client socket => value
        return (client, clientAddr)

    def send(self, message):
        pass
    
    def receive(self, clientSocket):
        packetSizeRaw = clientSocket.recv(HEADER_SIZE)
        packetSizeString = packetSizeRaw.decode(encoding=ENCODING).split()[0]
        packetSize = int(packetSizeString, 10)
        
        messageRaw = clientSocket.recv(packetSize)
        message = messageRaw.decode(encoding=ENCODING)
        self.receivedMessages += 1
        self.receivedBytes += packetSize

        return message


serverSocket = mySocket(None
                        ,name       = 'server' 
                        ,ip         = IP
                        ,port       = PORT
                        ,family     = socket.AF_INET
                        ,protocol   = socket.SOCK_STREAM 
                        ,encoding   = ENCODING  
                        ,headerSize = HEADER_SIZE
                        ,isServer   = True
                )
def main():
    """     serverSocket = mySocket(None
                           ,name       = 'server' 
                           ,ip         = IP
                           ,port       = PORT
                           ,family     = socket.AF_INET
                           ,protocol   = socket.SOCK_STREAM 
                           ,encoding   = ENCODING  
                           ,headerSize = HEADER_SIZE
                           ,isServer   = True
                    ) """

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
                                    ,args   = (serverSocket, client, newClientAdress) ) 
        
        newThread.start()
        runningThreads.append(newThread)


if __name__ == '__main__':
    main()