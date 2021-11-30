import threading
import socket

host = '127.0.0.1'
port = 65000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()

clients = []
names = []

# broadcasting to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# handle clients by server
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            names.remove(name)
            broadcast(f'{name} has been removed from the room'.encode('ascii'))
            break

# recieve messages
def main():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        client.send('NAME'.encode('ascii'))
        name = client.recv(1024).decode('ascii')
        names.append(name)
        clients.append(client)

        print(f'Name of client is {name}')
        broadcast(f'{name} has joined the room'.encode('ascii'))

        client.send('Connected to the server'.encode('ascii'))

        # we will run 1 thread for each client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server has started")
main()