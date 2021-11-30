import smtplib

server = smtplib.smtp('smtp.gmail.com', 25)
server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('testphp29@gmail.com', password)