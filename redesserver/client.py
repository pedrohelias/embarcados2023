import asyncio
import websockets

async def receive_messages():
    uri = "ws://localhost:12345"
    async with websockets.connect(uri) as websocket:
        while True:
            # Aguarda mensagens do servidor e imprime na tela
            message = await websocket.recv()
            print(f"Recebido do servidor: {message}")

async def send_messages():
    uri = "ws://localhost:12345"
    async with websockets.connect(uri) as websocket:
        while True:
            # Solicita ao usuário para digitar uma mensagem e a envia ao servidor
            user_input = input("Digite uma mensagem: ")
            await websocket.send(user_input)

# Executa as funções de recebimento e envio em paralelo
asyncio.gather(receive_messages(), send_messages())
