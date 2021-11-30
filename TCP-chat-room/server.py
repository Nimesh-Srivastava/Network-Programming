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
            msg = message = client.recv(1024)

            if msg.decode('ascii').startswith('KICK'):
                if names[clients.index(client)] == 'admin':
                    name_kicked = msg.decode('ascii')[5:]
                    kick_client(name_kicked) 
                else:
                    client.send('Command refused. Tampering detected with client.py!'.encode('ascii'))
            elif msg.decode('ascii').startswith('BAN'):
                if names[clients.index(client)] == 'admin':
                    name_banned = msg.decode('ascii')[4:]
                    kick_client(name_banned)
                    with open('bans.txt', 'a') as f:
                        f.write(f'{name_banned}\n')                
                    print(f'{name_banned} is banned from the server')                
                else:
                    client.send('Command refused. Tampering detected with client.py!'.encode('ascii'))
            else:
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

        with open('bans.txt', 'r') as f:
            bans = f.readlines()

        if name+'\n' in bans:
            client.send('BAN'.encode('ascii'))
            client.close()
            continue

        # admin check
        if name == 'admin':
            client.send('PWD'.encode('ascii'))
            pwd = client.recv(1024).decode('ascii')

            if pwd != 'admin':
                client.send('REF'.encode('ascii'))
                client.close()
                continue

        names.append(name)
        clients.append(client)

        print(f'Name of client is "{name}"')
        broadcast(f'"{name}" has joined the room'.encode('ascii'))

        client.send('Connected to the server'.encode('ascii'))

        # we will run 1 thread for each client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def kick_client(name):
    if name in names:
        name_index = names.index(name)
        kicked_client = clients[name_index]
        clients.remove(kicked_client)
        kicked_client.send('You were kicked by admin'.encode('ascii'))
        kicked_client.close()
        names.remove(name)
        broadcast(f'{name} was kicked by admin'.encode('ascii'))

print("Chat server has started...")
main()