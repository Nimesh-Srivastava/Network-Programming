import smtplib

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.smtp('smtp.gmail.com', 25)
server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('testphp29@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'TestAccount'
msg['To'] = 'testmail@spaml.de'
msg['Suject'] = 'Test email from python mailing client'