import socket
import time
import pickle

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP

#El argumento AF_INET indica que estás solicitando un socket de Protocolo de Internet (IP), 
#específicamente IPv4. 
#El segundo argumento es el tipo de protocolo de transporte SOCK_STREAM para sockets TCP.

HOST = "127.0.0.1"                 # IP Servidor
PORT = 65123                       # > 1023 puerto de envio
HEADER = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))

    names = [200,
            "Maria",
            "Rodrigo",
            3.1416,
            "Gonzalo",
            "kevin",
            (1+3j)] 

    data_serial = pickle.dumps(names)     #damps vuelca la estructura en un objeto serail

    
    #<HEADER><PAYLOAD>
    data_len = str(len(data_serial))

    data = bytes(f"{data_len:<{HEADER}}", "utf-8") + data_serial
    print(data)
    s.send(data)

    time.sleep(1)                 # Espero un segundo entre envio y envio

