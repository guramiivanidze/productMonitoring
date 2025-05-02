import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Load from .env
PRODUCT_URL = os.getenv("PRODUCT_URL")
TARGET_PRICE = float(os.getenv("TARGET_PRICE"))

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_PASS = os.getenv("EMAIL_APP_PASS")


def send_email(subject, body):
    email = MIMEMultipart()
    email["From"] = EMAIL_FROM
    email["To"] = EMAIL_TO
    email["Subject"] = subject
    email.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_FROM, EMAIL_PASS)
        smtp.send_message(email)


def check_price():
    response = requests.get(PRODUCT_URL)
    data = response.json()["data"]["product"]

    product_title = data["title"]
    product_price = data["sellPrice"]
    product_slug = data["productOriginalSlug"]

    if (
        product_price < TARGET_PRICE
        and product_slug == "dell-p2723qe-lcd-monitor-27-monitori"
    ):
        send_email(
            f"🔥 Deal Alert: {product_slug}",
            f"""Time to buy!
Product: {product_title}
Current Price: ₾{product_price}
Time: {current_time}
""",
        )
    else:
        send_email(
            "⏱️ Cron Executed - No Price Drop",
            f"Checked at: {current_time}\nCurrent price: ₾{product_price}",
        )


if __name__ == "__main__":
    check_price()
