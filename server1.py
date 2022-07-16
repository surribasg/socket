import socket

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP

#El argumento AF_INET indica que estás solicitando un socket de Protocolo de Internet (IP), 
#específicamente IPv4. 
#El segundo argumento es el tipo de protocolo de transporte SOCK_STREAM para sockets TCP.

HOST = "127.0.0.1"                 # Direccion loopback
PORT = 65123                       # > 1023 puerto de escucha

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn,addr = s.accept()
 
    with conn:
        print(f"Conectado a {addr} :")
        while True:
            data = conn.recv(1024)
            if not data:
                break

            conn.sendall(data)

    