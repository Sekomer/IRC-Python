""" @accepts(socket.socket, socket.socket, str)
@returns(None) """
def newCommunication(server, clientSocket, clientAdress):
    while True:    
        rcv_msg = server.receive(clientSocket)
        print(f"{clientAdress[0]}$", rcv_msg)


""" @accepts(str, int, str)
@returns(bytes) """
def packetProcess(USER_NAME, HEADER_SIZE, ENCODING):
    message = input(f"{USER_NAME}$ ")
    message = message.encode(ENCODING)
    HEADER = f"{ len(message) : <{HEADER_SIZE}}"
    PACKET = HEADER.encode(ENCODING) + message 
    return PACKET


def connection(func_ptr):
    for i in range(1, 4):
        print("Connecting" + i * '.'); func_ptr(i/2)  


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