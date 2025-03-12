import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# email information
sender_email = "your_email@example.com"
sender_password = "your_email_password"
recipient_email = "recipient_email@example.com"
email_subject = "Subject line of your email"
email_body = "Body of your email."

# create a message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = email_subject
message.attach(MIMEText(email_body, 'plain'))

# create an SMTP object and send the message
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()
smtp_object.login(sender_email, sender_password)
smtp_object.sendmail(sender_email, recipient_email, message.as_string())
smtp_object.quit()














'''
import smtplib

sender_email = "qasim.sheikh2567@gmail.com"
rec_email = "random@gmail.com"
password = input(str("Please Enter you email passowrd: "))
msg = "Hey, This is Qasim and I am a Python Programmer!"



server = smtplib.SMTP('smtp.gmail.com', 487)
server.starttls()
server.login(sender_email, password)
print("Login Success!")
server.sendmail(sender_email, rec_email, msg)
print("Email has been sent to ", rec_email)
server.close()
print("Server closed, Thankyou! ")
'''


