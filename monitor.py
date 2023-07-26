import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
current_time = datetime.now().time()


response = requests.get('https://catalog.extra.ge/api/products/dell-p2723qe-lcd-monitor-27-monitori/747028?requestId=bbd0b0db-e2d0-e820-16df-1a6a748c7bd0')

jsondata = response.json()
product = jsondata['data']['product']

productPrice = product['sellPrice']
productOriginalSlug = product['productOriginalSlug']
modelId = product['modelId']
id = product['id']


def send_email (param):
    if param == 'ok':
        # Email configuration
        sender_email = "gurami.ivanidze.96@gmail.com"
        sender_password = "ParoliSkullbusher12"
        receiver_email = "gurami151097@gmail.com"
        subject = f"Its Your chance To buy {productOriginalSlug} "
        message = f''' 
        time to buy !!!!!
        product: {product['title']}
        price: {productPrice}
        time: {current_time}
        '''
        app_pass = 'mfilnqtlctuwaipi'
        # Create the email
        email = MIMEMultipart()
        email["From"] = sender_email
        email["To"] = receiver_email
        email["Subject"] = subject
        email.attach(MIMEText(message, "plain"))

        # Connect to the SMTP server
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()

        # Login to your account
        smtp_connection.login(sender_email, app_pass)

        # Send the email
        smtp_connection.sendmail(sender_email, receiver_email, email.as_string())

        # Close the connection
        smtp_connection.quit()
    else:
        # Email configuration
        sender_email = "gurami.ivanidze.96@gmail.com"
        sender_password = "ParoliSkullbusher12"
        receiver_email = "gurami151097@gmail.com"
        subject = f"cron started "
        message = f''' 
        cron started but price not shemcirda
        time: {current_time}
        '''
        app_pass = 'mfilnqtlctuwaipi'
        # Create the email
        email = MIMEMultipart()
        email["From"] = sender_email
        email["To"] = receiver_email
        email["Subject"] = subject
        email.attach(MIMEText(message, "plain"))

        # Connect to the SMTP server
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()

        # Login to your account
        smtp_connection.login(sender_email, app_pass)

        # Send the email
        smtp_connection.sendmail(sender_email, receiver_email, email.as_string())

        # Close the connection
        smtp_connection.quit()


if productPrice<1000 and productOriginalSlug =="dell-p2723qe-lcd-monitor-27-monitori" and modelId == 113333 and id ==747028 :
    send_email('ok')
else:
    send_email("notLower")
