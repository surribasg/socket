import socket
import time

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

    names = [200,"Maria","Rodrigo","","Gonzalo","kevin"] 

    for name in names:
    #<HEADER><PAYLOAD>
         strData = str(name)
         data_len = str(len(strData))

         data = f"{data_len:<{HEADER}}{strData}".encode('utf-8')
         s.send(data)

         time.sleep(1)                 # Espero un segundo entre envio y envio




    

    


