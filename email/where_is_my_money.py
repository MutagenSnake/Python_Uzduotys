import smtplib # biblioteka susikalbėjimui su pašto serveriu
from email.message import EmailMessage
from passworddd import password # importuoju slaptažodį,                   # (galima nurodyti ir tiesiai į parametrus)
from string import Template

def inform_client(client_email, money_ammount):
    with open('index_money.html', 'r') as f:
        html = f.read()

    sablonas = Template(html)

    email = EmailMessage()
    email['from'] = 'Skolos išmušėjas'
    email['to'] = f'{client_email}'
    email['subject'] = 'Dėl skolos'

    email.set_content(sablonas.substitute({'money': str(money_ammount)}),'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()  # žiūrėkite, kaip į pasisveikinimą su serveriu
        smtp.starttls()  # inicijuojame šifruotą kanalą
        smtp.login('martynaspythonautoemail@gmail.com', password)  # nurodome prisijungimo duomenis
        smtp.send_message(email)  # išsiunčiame žinutę

inform_client('dantysmartynas@yahoo.com', 666)