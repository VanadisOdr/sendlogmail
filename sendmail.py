import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version
from dotenv import load_dotenv

load_dotenv()

server = 'smtp.mail.ru'
user = 'olegsendtest@mail.ru'
password = os.getenv('PASSWORD')

subject = 'sendmailtest'

filepath = "debug.log"
basename = os.path.basename(filepath)
filesize = os.path.getsize(filepath)

msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = os.getenv('MAIL2')
msg['To'] = os.getenv('MAIL')
msg['Reply-To'] = os.getenv('MAIL2')
msg['Return-Path'] = os.getenv('MAIL2')


part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
part_file.set_payload(open(filepath, "rb").read())
part_file.add_header('Content-Description', basename)
part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
encoders.encode_base64(part_file)

msg.attach(part_file)

mail = smtplib.SMTP_SSL(server)
mail.login(user, password)
mail.sendmail(os.getenv('MAIL2'), os.getenv('MAIL'), msg.as_string())
mail.quit()