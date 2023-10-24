import socket
#socket é o endpoint de uma comunicação, onde voce envia e recebe informações de uma comunicação
import json 

msg = "teste"

def sendData(msg):
    return {"nome": msg, "idade": 28}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #primeiro argumento: tipo da familia, AF_INET corresponde a IPV4, segundo argumento: SOCK_STREAM, corresponde a TCP

s.bind((socket.gethostname(), 1234)) #gethostname porque estamos usando numa maquina local #ip e porta
s.listen(5)

print("aguardando conexão...")

while True:
    clientsocket, adress = s.accept()
    print(f"Connection from {adress} has been established")
#clientsocket.send(bytes("welcome to the server", "utf-8")) #enviar informação pro client socket

    data_to_send = sendData(msg)#{"nome": "Pedro", "idade": 28}

    json_data = json.dumps(data_to_send)

    clientsocket.send(json_data.encode())
#clientsocket.close()