import smtplib # biblioteka susikalbėjimui su pašto serveriu
from email.message import EmailMessage
from passworddd import password # importuoju slaptažodį,                   # (galima nurodyti ir tiesiai į parametrus)
from string import Template

with open('index.html', 'r') as f:
    html = f.read()

sablonas = Template(html)

# elementarios email žinutės sukūrimas:
email = EmailMessage()
email['from'] = 'Testinis Emailas'
email['to'] = 'dantysmartynas@yahoo.com'
email['subject'] = 'email from python'

email.set_content(sablonas.substitute({'vardas': 'Karabasas'}), 'html')
# email.set_content(html, 'html')

with open('elephant.png', 'rb') as file:
    content = file.read()
    email.add_attachment(
        content,
        maintype='image/png',
        subtype='png',
        filename='elephant.png')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() # žiūrėkite, kaip į pasisveikinimą su serveriu
    smtp.starttls() # inicijuojame šifruotą kanalą
    smtp.login('martynaspythonautoemail@gmail.com', password) # nurodome prisijungimo duomenis
    smtp.send_message(email) # išsiunčiame žinutę