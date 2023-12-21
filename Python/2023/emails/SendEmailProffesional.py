import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from string import Template
from pathlib import Path
import json

SENDER_EMAIL = 'admin@empchief.com'
SENDER_PASSWORD = '-----'
SMTP_SERVER = "smtp.hostinger.com"
SMTP_PORT = 465
SET_SUBJECT = 'Important Update: Bug Fix Required'
TEXT_CONTENT_FILE = 'PronominalEmail.html'
RECIPIENTS_FILE = 'recipients.json'


def create_html_content(template, name):
    return template.substitute({'name': name})


try:
    with open(TEXT_CONTENT_FILE, 'r', encoding='utf-8') as file:
        html_template = Template(file.read())

    with open(RECIPIENTS_FILE, 'r', encoding='utf-8') as recipients_file:
        recipients = json.load(recipients_file)

    with smtplib.SMTP_SSL(host=SMTP_SERVER, port=SMTP_PORT) as smtp:
        print("Connection established.")

        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        print("Login successful.")

        for recipient in recipients:
            name = recipient['name']
            email = recipient['email']

            html_content = create_html_content(html_template, name)

            msg = EmailMessage()
            msg['From'] = SENDER_EMAIL
            msg['To'] = email
            msg['Subject'] = SET_SUBJECT

            msg.set_content(html_content, subtype='html')

            try:
                smtp.send_message(msg)
                print(f"Email sent to {name} ({email})!")

            except Exception as e:
                print(f"An error occurred while sending the email to {
                      name} ({email}): {e}")

        print("Logging out.")

except FileNotFoundError as e:
    print(f"Error: {e.filename} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
