import socket
import threading

name = input("Type a name to join the server : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 65000))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NAME':
                client.send(name.encode('ascii'))

            else:
                print(message)
        
        except:
            print("Error")
            client.close()
            break