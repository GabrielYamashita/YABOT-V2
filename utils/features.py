
# Enviroment
import os
from dotenv import load_dotenv

# Twilio Client
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse



def categorize_msg(incoming_msg):
    msgBody = incoming_msg.get('Body')
    hasMedia = int(incoming_msg.get('NumMedia'))

    if hasMedia == 1:
        contentTypeMedia = incoming_msg.get('MediaContentType0')
        urlMedia = incoming_msg.get('MediaUrl0')

        typeContent = contentTypeMedia.split('/')

        if typeContent[0] == 'image' and msgBody != '':
            return f'image and msg type | {typeContent}'
        
        elif typeContent[0] == 'image':
            return f'image type | {typeContent}'

        elif typeContent[0] == 'video' and msgBody != '':
            return f'video and msg type | {typeContent}'
        
        elif typeContent[0] == 'video':
            return f'video type | {typeContent}'

        elif typeContent[0] == 'audio':
            return f'audio type | {typeContent}'

        elif typeContent[0] == 'application':
            return f'application type | {typeContent}'
        
        elif typeContent[0] == 'text':
            return f'text type | {typeContent}'
        
    else:
        lat = incoming_msg.get('Latitude')
        long = incoming_msg.get('Longitude')

        if lat != None and long != None:
            return f'location type'
        
        else:
            return f'msg type'


    ''' 
    TO HANDLE:
    - Mensagem Padrão/ Link       --> Body
    - Localização                 --> Latitude | Longitude
    - Áudio                       --> MediaContentType0: audio/ogg
    - Imagem                      --> MediaContentType0: image/jpeg
    - Imagem com Mensagem         --> MediaContentType0: image/jpeg
    - Figurinha                   --> MediaContentType0: image/webp
    - PDF (arquivos | extensão)   --> MediaContentType0: application/pdf
    - Vídeo                       --> MediaContentType0: video/mp4
    - Catão de Contato            --> MediaContentType0: text/vcard
    '''

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
        # msg.body(f"Incoming Message:\n\n{incoming_msg}\n\n{'-'*7}\n\nBody: {msgBody}\nNumMedia: {hasMedia}\nMedia Content Type: {contentTypeMedia}\nMedia URL: {urlMedia}")
        msg.body(categorize_msg(incoming_msg))
        # msg.media(GOOD_BOY_URL)


def process_command(command, incoming_msg):
    # Implement command processing logic
    if command == 'show log':
        return f'Incoming Message:\n\n{incoming_msg}'


    return f"Command processed: '{command}'"



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


