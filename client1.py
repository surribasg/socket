import socket

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP

#El argumento AF_INET indica que estás solicitando un socket de Protocolo de Internet (IP), 
#específicamente IPv4. 
#El segundo argumento es el tipo de protocolo de transporte SOCK_STREAM para sockets TCP.

HOST = "127.0.0.1"                 # IP Servidor
PORT = 65123                       # > 1023 puerto de envio

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b"Hola Mundo")

    data = s.recv(1024)

print("Recibido", repr(data))



    

    


