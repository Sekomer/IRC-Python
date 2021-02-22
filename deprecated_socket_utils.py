def socket__send(socket, message, HEADER_SIZE, encoding='utf-8'):
    if not len(message):
        return -1

    messageLength = len(message)
    header = f"{messageLength}:<{HEADER_SIZE}" + message
    encapsulatedMessage = bytes(header, encoding=encoding)

    socket.send(encapsulatedMessage)

def socket1024(socket, message, BUFFER_SIZE, encoding='utf-8'):
    if not len(message):
        return -1

    encapsulatedMessage = bytes(message, encoding=encoding)
    socket.send(encapsulatedMessage)