import socket
import threading

name = input("Type a name to join the server : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 65000))

# communicate with the server
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

# communicate with others
def write():
    while True:
        message = f'{name} : {input("")}'
        client.send(message.encode('ascii'))


recieve_thread = threading.Thread(target = recieve)
recieve_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()