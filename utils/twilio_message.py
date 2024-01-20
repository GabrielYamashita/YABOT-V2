
# Enviroment
import os
from dotenv import load_dotenv

# Twilio Client
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Functions
from .webhook_command import process_command
from .webhook_respond import categorize_msg

def respond(incoming_msg):
    resp = MessagingResponse()
    msg = resp.message()

    msgBody = incoming_msg.get('Body')

    if msgBody.lower().startswith("!command"):
        command = " ".join(msgBody.split(" ")[1:])

        # Handle the command and generate a response
        response_message = process_command(command, incoming_msg)
        msg.body(response_message)
            
    else:
        # Handle regular messages
        msg.body(categorize_msg(incoming_msg))
        # msg.body(f"Incoming Message:\n\n{incoming_msg}")
        # msg.media(GOOD_BOY_URL)

    return resp


def send_message(message):
    load_dotenv() # carrega as variáveis de ambiente
    account_sid = os.getenv('ACCOUNT_SID') # account sid para rodar localmente
    auth_token = os.getenv('AUTH_TOKEN')

    client = Client(account_sid, auth_token)


    # Implement Twilio code to send a message
    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+5511991982436'

    message = client.messages.create(
        body=message,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )

    # print("Sending message:", message)

# respond(
#     [
#         ('SmsMessageSid', 'SMc7e34b5928ea30ede3380c63082a3b69'),
#         ('NumMedia', '0'),
#         ('ProfileName', 'Gabriel Yamashita'),
#         ('SmsSid', 'SMc7e34b5928ea30ede3380c63082a3b69'),
#         ('WaId', '5511991982436'),
#         ('SmsStatus', 'received'),
#         ('Body', '!command show log'),
#         ('To', 'whatsapp:+14155238886'),
#         ('NumSegments', '1'),
#         ('ReferralNumMedia', '0'),
#         ('MessageSid', 'SMc7e34b5928ea30ede3380c63082a3b69'),
#         ('AccountSid', 'ACc906b1cb84d639c680889d5ab72f36d1'),
#         ('From', 'whatsapp:+5511991982436'),
#         ('ApiVersion', '2010-04-01')
#     ]
# )

from werkzeug.datastructures import ImmutableMultiDict

# Creating an empty ImmutableMultiDict
# immutable_multi_dict = ImmutableMultiDict()

# Creating an ImmutableMultiDict with some initial data
data = [
    ('SmsMessageSid', 'SMc7e34b5928ea30ede3380c63082a3b69'),
    ('NumMedia', '0'),
    ('ProfileName', 'Gabriel Yamashita'),
    ('SmsSid', 'SMc7e34b5928ea30ede3380c63082a3b69'),
    ('WaId', '5511991982436'),
    ('SmsStatus', 'received'),
    ('Body', '!command show log'),
    ('To', 'whatsapp:+14155238886'),
    ('NumSegments', '1'),
    ('ReferralNumMedia', '0'),
    ('MessageSid', 'SMc7e34b5928ea30ede3380c63082a3b69'),
    ('AccountSid', 'ACc906b1cb84d639c680889d5ab72f36d1'),
    ('From', 'whatsapp:+5511991982436'),
    ('ApiVersion', '2010-04-01')
]
immutable_multi_dict_with_data = ImmutableMultiDict(data)

respond(immutable_multi_dict_with_data)