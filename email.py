import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'demo.com'
sender_email = '***@demo.com'
receiver_email = '***@demo.com'
password = 'password'

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Sample Email Subject'

body = 'This is a sample email message.'
message.attach(MIMEText(body, 'plain'))

with smtplib.SMTP(smtp_server, 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())