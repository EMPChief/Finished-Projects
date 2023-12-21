from twilio.rest import Client
import pyjokes
joke = pyjokes.get_joke()
account_sid = '----'
auth_token = '---'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+---',
    to='+----',
    body=f'{joke}'
)

print(message.sid)
