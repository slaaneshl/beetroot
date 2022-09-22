import asyncio
import socket
from asyncio import AbstractEventLoop

PORT = 8004
SERVER = socket.gethostbyname(socket.gethostname())


async def echo(connection: socket, loop: AbstractEventLoop):
    try:
        while massage := await loop.sock_recv(connection, 1024):
            await loop.sock_sendall(connection, massage)
    except Exception as error:
        print(error)


async def listen_for_connection(server_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'Got a connection from {address}')
        asyncio.create_task(echo(connection, loop))


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (SERVER, PORT)

    server_socket.setblocking(False)

    server_socket.bind(server_address)

    server_socket.listen()
    print(f'Server {SERVER} start')
    await listen_for_connection(server_socket, asyncio.get_event_loop())


asyncio.run(main())