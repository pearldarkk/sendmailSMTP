# !/usr/bin/python
# coding=utf-8

import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os.path import basename

#use unicode instead of ascii to write Vietnamese
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

def addName(name):
    f = open("content.txt", 'r')
    f.seek(0)
    next(f)
    save = f.read()
    f.close()
    f = open("content.txt", 'w')
    f.write("<p><em><strong>Kính gửi: ")
    f.write(name)
    f.write("</em></strong><br>\n")
    f.close()
    f = open('content.txt', 'a')
    f.write(save)
    f.close()

def send_mail(name, email):
    # bodytext
    # add corporation's name
    addName(name)
    f = open('content.txt', 'r')
    content = f.read()
    msg.attach(MIMEText(content, 'html'))

    # attachments
    fileName = 'Hồ sơ tài trợ Ulis Jobfair 2021.pdf'
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(fileName, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment' ,filename=fileName)
    msg.attach(part)

    fileName = 'Hồ sơ tài trợ Ulis Jobfair 2021. ver Eng.pdf'
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(fileName, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment' ,filename=fileName)
    msg.attach(part)

    # Create SMTP to send mail
    recipients = email.split()
    msg['To'] = ", ".join(recipients)
    text = msg.as_string()
    session.sendmail(sender, recipients, text)


# sender
sender = "sender@gmail.com"
sender_pass = "password"

# Setup msg container
msg = MIMEMultipart()
msg['Subject']  = "[ULIS] Thư mời tham dự Ngày hội việc làm ULIS JOBFAIR 2021 - ĐHNN ĐHQGHN"
msg['From'] = sender

# list of recipients
f = open("recipientsname.txt")
rp_name = f.read().splitlines()
f.close()
f = open("recipientsemail.txt")
rp_mail = f.read().splitlines()
f.close()

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls() #enable security
session.login(sender, sender_pass) #login with mail_id and password

for i in range(0, len(rp_name)):
    send_mail(rp_name[i], rp_mail[i])

session.quit()
print("Sent!")








