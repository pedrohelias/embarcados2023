import socket 

def processar_dado(dado):
    if dado!="sair":
        print("o numero recebido foi " + str(dado) +"\n")
    
def enviar_dados_ao_servidor(dados):
    # Configurar o cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 1234)  # Substitua com o endereço do seu servidor
    client_socket.connect(server_address)


    # Enviar os dados para o servidor
    client_socket.send(dados.encode())

    # Receber uma possível resposta do servidor
    resposta = client_socket.recv(1024).decode()
    print("Resposta do servidor:", resposta)

    # Fechar a conexão do cliente
    client_socket.close()