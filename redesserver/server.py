import socket

data = ""
# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)
print('Server listening on {}:{}'.format(*server_address))

while True:
    # Wait for a connection
    client_socket, client_address = server_socket.accept()
    
    
    print('Connection from', client_address)

    # Receive data from the client
    data = client_socket.recv(1024)
    dataDecod = data.decode('utf-8')
    print(dataDecod)

    if dataDecod == 'sair':
        client_socket.close()
        break
    print('Received:', data.decode('utf-8'))

    # Send a response back to the client
    message = 'se conectou a rede!'
    client_socket.sendall(message.encode('utf-8'))
    
        # Clean up the connection
    #client_socket.close()

# import socket

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = ('localhost', 12345)

# try:
#     server_socket.bind(server_address)
#     server_socket.listen(5)
#     print('Server listening on {}:{}'.format(*server_address))

#     while True:
#         client_socket, client_address = server_socket.accept()
#         try:
#             print('Connection from', client_address)

#             data = client_socket.recv(1024)
#             if not data:
#                 break  # No more data, connection closed

#             print('Received:', data.decode('utf-8'))

#             message = 'Hello, client! This is the server.'
#             client_socket.sendall(message.encode('utf-8'))
#         finally:
#             client_socket.close()
# finally:
#     server_socket.close()