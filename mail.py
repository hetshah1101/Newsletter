import os
import smtplib
from email.message import EmailMessage
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


# function for reading the message template ie message.txt
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

# names, emails = get_contacts('mycontacts.txt') 
names, emails = 'HET', EMAIL_ADDRESS

# function to generate and send mail
def send_email(name, email, mail_template):
    message_template = read_template(mail_template)

    msg = MIMEMultipart()
    message = message_template.substitute(PERSON_NAME=name.title())

    msg['Subject'] = 'TEST MAIL'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email

    msg.attach(MIMEText(message, 'plain'))

    with open('img.jpg', 'rb') as f:
        file_data = f.read()
        file_name = f.name

    img = MIMEImage(file_data, _subtype="jpg")
    img.add_header('Content-Disposition', 'attachment; filename="%s"' % file_name)
    msg.attach(img)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    del msg

send_email(names, emails, "message.txt")