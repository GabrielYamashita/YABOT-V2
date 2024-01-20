
# Enviroment
import os
from dotenv import load_dotenv

# Twilio Client
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Functions
from webhook_command import process_command
from webhook_respond import categorize_msg

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
        # msg.body(f"Incoming Message:\n\n{incoming_msg}\n\n{'-'*7}\n\nBody: {msgBody}\nNumMedia: {hasMedia}\nMedia Content Type: {contentTypeMedia}\nMedia URL: {urlMedia}")
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

