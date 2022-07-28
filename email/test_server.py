import requests
import smtplib
from email.message import EmailMessage
from passworddd import password
from time import sleep
from datetime import datetime
import mimetypes


def warning_mail(message):

    information = f'Your server is broken: {message}'

    email = EmailMessage()
    email['from'] = 'System'
    email['to'] = 'dantysmartynas@yahoo.com'
    email['subject'] = 'Server error information'

    email.set_content(information)

    file = 'server_info.txt'
    mimetype = mimetypes.guess_type(file)[0]
    subtype = mimetype.split('/')[1]
    with open(file, 'rb') as img:
        content = img.read()
        email.add_attachment(
            content,
            maintype=mimetype,
            subtype=subtype,
            filename=file)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('martynaspythonautoemail@gmail.com', password)
        smtp.send_message(email)


while True:
    try:
        site = requests.get('http://127.0.0.1:8000', timeout=5)
        with open('server_info.txt', 'a') as f:
            f.write(f'{site.status_code}: {datetime.now()}\n')
        print('do work')
        sleep(5)
    except Exception as error:
        print('no work')
        print(error)
        with open('server_info.txt', 'a') as f:
            f.write(f'{error}: {datetime.now()}\n')
        warning_mail(error)
        break
