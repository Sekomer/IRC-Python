from os import system
from time import sleep
import threading



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

def clearScreen():
    ret = system('clear')
    # ret = 0 ==> success
    # ret = 1 ==> failure
    if ret:    
        system('cls')

#brutal fantasia
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