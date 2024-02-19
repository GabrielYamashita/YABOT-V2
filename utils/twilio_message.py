
# Enviroment
import os
from dotenv import load_dotenv

# Twilio Client
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Functions
from .webhook_command import process_command
from .webhook_respond import categorize_msg, process_msg


# Função para Responder Mensagens
def respond(incoming_msg):
    resp = MessagingResponse()
    msg = resp.message()

    msgBody = incoming_msg.get('Body')

    # Lidando com Comandos
    if msgBody.lower().startswith("!"):
        # Selecionando texto pós chave de comando
        command = " ".join(msgBody.split(" ")[1:])

        # Gerando Resposta e Imagem
        response_message, imgGen = process_command(command) 

        # Gerando Mensagem para Usuário
        msg.body(response_message)
        if imgGen != False:
            msg.media(imgGen)

    # Lidando com Mensagens Genéricas
    else:
        typeMsg = categorize_msg(incoming_msg)
        response_message, imgGen = process_msg(typeMsg, incoming_msg)

        msg.body(response_message)
        if imgGen != False:
            msg.media(imgGen)

    return resp


# Função para Mandar uma Mensagem
def send_message(message):
    load_dotenv() # carrega as variáveis de ambiente
    account_sid = os.getenv('ACCOUNT_SID') # account sid twilio
    auth_token = os.getenv('AUTH_TOKEN')   # auth token twilio

    client = Client(account_sid, auth_token) # inicializando cliente

    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+5511991982436'

    message = client.messages.create(
        body=message,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )
