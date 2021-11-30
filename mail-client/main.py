import smtplib

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# your gmail id:
my_id = 'example@gmail.com'

# recieving gmail id:
recepient = 'example2@gmail.com'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login(my_id, password)

msg = MIMEMultipart()
msg['From'] = 'TestAccount'
msg['To'] = recepient
msg['Suject'] = 'Test email from python mailing client'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'https://github.com/Nimesh-Srivastava/Network-Programming/blob/main/mail-client/Image%2031-10-21%20at%204.02%20PM.jpg'
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
server.sendmail(my_id, recepient, text)
