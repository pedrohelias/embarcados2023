import socket
#socket é o endpoint de uma comunicação, onde voce envia e recebe informações de uma comunicação
import json


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #primeiro argumento: tipo da familia, AF_INET corresponde a IPV4, segundo argumento: SOCK_STREAM, corresponde a TCP

s.connect((socket.gethostname(), 1234))

rcv_data = s.recv(1024).decode()

data = json.loads(rcv_data)

print("dados recebidos pelo servidor:")
print(data)

s.close()

