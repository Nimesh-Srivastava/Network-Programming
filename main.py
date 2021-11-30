import smtplib

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('andromedag90@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'TestAccount'
msg['To'] = 'snimesh412@gmail.com'
msg['Suject'] = 'Test email from python mailing client'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'img.jpeg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header(
    "Content-Disposition",
    "attachment; filename={}".format(filename),
)
msg.attach(p)

text = msg.as_string()
server.sendmail('andromedag90@gmail.com', 'snimesh412@gmail.com', text)