import socket

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP

#El argumento AF_INET indica que estás solicitando un socket de Protocolo de Internet (IP), 
#específicamente IPv4. 
#El segundo argumento es el tipo de protocolo de transporte SOCK_STREAM para sockets TCP.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#enlaza la dirección (nombre del host, número de puerto) al socket.
s.bind((socket.gethostname(), 1234))

#configura e inicia TCP listener.
s.listen(5)

while True:
    #acepta la conexión del cliente TCP
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established.")
    clientsocket.send(bytes("Welcome to the server","utf-8"))
    clientsocket.send(bytes("Hey there!!!","utf-8"))
    clientsocket.close()
    



