import socket

#El argumento AF_INET indica que estás solicitando un socket de Protocolo de Internet (IP), 
#específicamente IPv4. 
#El segundo argumento es el tipo de protocolo de transporte SOCK_STREAM para sockets TCP.

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Inicia una conexión con el servidor TCP.
s.connect((socket.gethostname(), 1234))

full_msg = ''
while True:
    msg = s.recv(1024)
    if len(msg) <= 0:c
    break
    full_msg += msg.decode("utf-8")

    if len(full_msg) > 0:
        print(full_msg)