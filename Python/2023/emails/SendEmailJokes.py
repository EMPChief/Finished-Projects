import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import json
import pyjokes
import requests


SENDER_EMAIL = 'joke@bjornmagne.com'
SENDER_PASSWORD = '----'
JOKE_CONTENT_FILE = "JokeEmail.html"
SMTP_SERVER = "smtp.hostinger.com"
SMTP_PORT = 465
GIPHY_API_KEY = '-----'
GIPHY_API_URL = f'http://api.giphy.com/v1/gifs/random?api_key={
    GIPHY_API_KEY}&tag=funny'
SUBJECT = 'Daily Jokes'
RECIPIENTS_JSON_PATH = 'recipients.json'
WORD_REPLACEMENT_JSON_PATH = 'WordForReplacement.json'

with open(RECIPIENTS_JSON_PATH, 'r', encoding='utf-8') as recipients_file:
    recipients = json.load(recipients_file)

with open(WORD_REPLACEMENT_JSON_PATH, 'r', encoding='utf-8') as word_file:
    word_replacements = json.load(word_file)


def replace_content(content, replacements):
    for placeholder, replacement in replacements.items():
        content = content.replace(placeholder, replacement)
    return content


def get_random_joke():
    try:
        joke = pyjokes.get_joke()
        return joke
    except pyjokes.PyJokesException as e:
        print(f"Error getting joke: {e}")
        return None


def get_random_gif():
    try:
        response = requests.get(GIPHY_API_URL)
        response.raise_for_status()
        data = response.json().get('data', {})
        images = data.get('images', {})
        original = images.get('original', {})
        gif_url = original.get('url')

        if gif_url is None:
            print("Error: 'url' key not found in GIPHY API response.")
            return None
        else:
            gif_data = requests.get(gif_url).content
            return gif_data

    except requests.exceptions.RequestException as err:
        print(f"An error occurred during the GIPHY API request: {err}")
        return None


def send_email(subject, content, image_data, recipient_email, recipient_name, smtp, replacements):
    try:
        email = EmailMessage()
        email['From'] = SENDER_EMAIL
        email['To'] = recipient_email
        email['Subject'] = SUBJECT

        email_content = replace_content(content, replacements)
        email.set_content(email_content, 'html')

        if image_data:
            email.add_attachment(image_data, maintype='image',
                                 subtype='gif', filename='funny_gif')

        smtp.send_message(email)
        print(f"Email sent to {recipient_name} ({recipient_email})!")

    except Exception as e:
        print(f"An error occurred while sending the email to {
              recipient_name} ({recipient_email}): {e}")


joke = get_random_joke()
gif_data = get_random_gif()

if joke or gif_data:
    with smtplib.SMTP_SSL(host=SMTP_SERVER, port=SMTP_PORT) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        print("Login successful.")

        with open(JOKE_CONTENT_FILE, 'r', encoding='utf-8') as file:
            email_content_template = file.read()

        for recipient in recipients:
            word_replacements["$joke_content"] = joke
            word_replacements["$name"] = recipient['name']

            send_email(SUBJECT, email_content_template, gif_data,
                       recipient['email'], recipient['name'], smtp, word_replacements)

        print("Logging out.")
