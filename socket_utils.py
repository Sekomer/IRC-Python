from os import system
from time import sleep
import socket
import threading


#class begin#
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
        print("Server initialized"
             ,f"[IP] {self.ip}"
             ,f"[Port] {self.port}"
             ,sep = "\n")
        
    def listen(self, num):    
        self._SOCK.listen(num)

    def accept(self):
        self.numClients += 1
        client, clientAddr = self._SOCK.accept()
        self.clients[clientAddr[0]] = client      # ip adress => key, client socket => value
        return (client, clientAddr)

    def broadcast(self, message):
        pass
    
    def receive(self, clientSocket):
        packetSizeRaw = clientSocket.recv(self._HEADER_SIZE)
        packetSizeString = packetSizeRaw.decode(encoding=self._ENCODING).split()[0]
        packetSize = int(packetSizeString, 10)
        
        messageRaw = clientSocket.recv(packetSize)
        message = messageRaw.decode(encoding=self._ENCODING)
        
        self.receivedMessages += 1
        self.receivedBytes += packetSize
        return message
#class end#

class safeThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(safeThread, self).__init__(*args, **kwargs)
        self.__stop_event = threading.Event()
        
    def stop(self):
        self.__stop_event.set()
    def stoppped(self):
        self.__stop_event.is_set()

""" 
@accepts(socket.socket, socket.socket, str)
@returns(None)
"""
def newCommunication(server, clientSocket, clientAdress, path):
    while True:    
        rcv_msg = server.receive(clientSocket)
        print(f"{clientAdress[0]}$", rcv_msg, file = path, flush = True)
        

""" 
@accepts(str, int, str)
@returns(bytes)
"""
def packetProcess(USER_NAME, HEADER_SIZE, ENCODING):
    message = input(f"{USER_NAME}$ ")
    
    message = message.encode(ENCODING)
    HEADER = f"{ len(message) : <{HEADER_SIZE}}"
    PACKET = HEADER.encode(ENCODING) + message 
    return PACKET

def clearScreen(platform):
    if platform == 'Windows':
        system('cls')
    else:
        system('clear')

def connection():
    for i in range(1, 4):
        print("Connecting" + i * '.') 
        sleep(i/2)  

def retire():
    print('exiting', end = '')
    for i in range(1, 4):
        sleep(i/2)
        print('.', end = '')    

def hello_txt(id):
    print(f"Hello {id}! Welcome to IRC, press Q if you would like to exit.", end='\n\n')
 

@DeprecationWarning
def socket__send(socket, message, HEADER_SIZE, encoding='utf-8'):
    if not len(message):
        return -1

    messageLength = len(message)
    header = f"{messageLength}:<{HEADER_SIZE}" + message
    encapsulatedMessage = bytes(header, encoding=encoding)

    socket.send(encapsulatedMessage)


@DeprecationWarning
def socket1024(socket, message, BUFFER_SIZE, encoding='utf-8'):
    if not len(message):
        return -1

    encapsulatedMessage = bytes(message, encoding=encoding)
    socket.send(encapsulatedMessage)