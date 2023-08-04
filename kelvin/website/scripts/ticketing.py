import os
from django.conf import settings
import ssl
import smtplib
import json

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders
from email.mime.image import MIMEImage

import django
# Change mysite if your project has a different name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kelvin.settings')
django.setup()

from website.models import Order

ticketGenDir = (os.path.dirname(os.path.realpath(__file__)))  + '/'

standardIDs = []
concessionIDs = []

for i in settings.CONCERT_LIST:
    standardIDs.append(i['standardTicketID'])
    concessionIDs.append(i['concessionTicketID'])


def createDatabaseEntry(cartInfo, customerDetails, pid):
    orderinfo = json.dumps(cartInfo)



    ticketNumber = 0
    for x in orderinfo:
        for y in range(x["quantity"]):
            ticketNumber += 1
            ticketCode = pid[-5:] + '_' + ticketNumber

            concertNumber = 0

            if y['price']['id'] in concessionIDs:
                concertNumber = concessionIDs.index(y['price']['id']) + 1
                order = Order(email=customerDetails["email"], name=customerDetails["name"], purchase_id=pid,
                              ticket_code=ticketCode, concession=True, concert_number=concertNumber)

                order.save
            elif y['price']['id'] in standardIDs:
                concertNumber = standardIDs.index(y['price']['id']) + 1
                order = Order(email=customerDetails["email"], name=customerDetails["name"], purchase_id=pid,
                              ticket_code=ticketCode, concession=False, concert_number=concertNumber)

                order.save
            else:
                raise Exception("Error processing ticket, ID not found.")
                break



    print(orderinfo)

    order = Order(email=customerDetails["email"], name=customerDetails["name"], purchase_id=pid)
    order.save()



def sendConfirmation(cartInfo, customerDetails, pid):
    createDatabaseEntry(cartInfo, customerDetails, pid)

    print("Cart Info")
    print(cartInfo)

    html = open(ticketGenDir + "confirmation_template.html")
    sender_password = settings.TICKETS_PASSWORD
    sender_address = 'tickets@kelvin-ensemble.co.uk'

    customerName = customerDetails["name"]
    customerEmail = customerDetails["email"]

    msg = MIMEMultipart('alternative')
    msg['From'] = sender_address
    msg['To'] = customerEmail
    msg['Subject'] = "Tickets for " + settings.CONCERT_NAME + " - Kelvin Ensemble"
    msg.attach(MIMEText(html.read().format(customerName, settings.CONCERT_NAME, pid), 'html'))

    fp = open(ticketGenDir + 'KELogoLong.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<kelLogo1>')
    msg.attach(msgImage)

    email_string = msg.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_address, sender_password)
        server.sendmail(msg['From'], msg['To'], email_string)

