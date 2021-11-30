import socket
import threading

name = input("Type a name to join the server : ")
if name == 'admin':
    pwd = input("Enter password : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 65000))

stop_thread = False

# communicate with the server
def recieve():
    while True:
        global stop_thread
        if stop_thread == True:
            exit()
        
        try:
            message = client.recv(1024).decode('ascii')
            
            if message == 'NAME':
                client.send(name.encode('ascii'))
                next_msg = client.recv(1024).decode('ascii')
                
                if next_msg == 'PWD':
                    client.send(pwd.encode('ascii'))
                    
                    if client.recv(1024).decode('ascii') == 'REF':
                        print("Wrong password. Connection refused.")
                        stop_thread = True
                        exit()
                
                elif next_msg == 'BAN':
                    print('Connection refused. This name is banned.')
                    client.close()
                    stop_thread = True
                    exit()
            else:
                print(message)      
        except:
            print("Some error has occured. Closing client")
            client.close()
            exit()

# communicate with others
def write():
    while True:
        if stop_thread == True:
            exit()
        
        note = input("")
        message = f'{name} : {note}'
        
        if message[len(name) + 3 :].startswith('/'):
            if name == 'admin':
                if message[len(name) + 3 :].startswith('/kick'):
                    client.send(f'KICK {message[len(name) + 3 + 6 :]}'.encode('ascii'))
                
                elif message[len(name) + 3 :].startswith('/ban'):
                    client.send(f'BAN {message[len(name) + 3 + 5 :]}'.encode('ascii'))
            else:
                print("Commands can only be executed by admin !")
        else:
            client.send(message.encode('ascii'))


recieve_thread = threading.Thread(target = recieve)
recieve_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()