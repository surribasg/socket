import socket
import pickle

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP

#El argumento AF_INET indica que estás solicitando un socket de Protocolo de Internet (IP), 
#específicamente IPv4. 
#El segundo argumento es el tipo de protocolo de transporte SOCK_STREAM para sockets TCP.

HOST = "127.0.0.1"                 # Direccion loopback
PORT = 65123                       # > 1023 puerto de escucha
HEADER = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
 
    try:
        with conn:
            print(f"Conectado a {addr[0]}:{addr[1]}")
            while True:
                data_len = conn.recv(HEADER)
                if not data_len:
                    break
                else:
                   data = b''
                   data += conn.recv(int(data_len))
                   data_deserial = pickle.loads(data)
                   print(data_deserial)
                   print(type(data_deserial))
                   

    except KeyboardInterrupt:
        pass

print("Cerrando conexion")

