
def process_type(incoming_msg):
    msgBody = incoming_msg.get('Body')
    hasMedia = int(incoming_msg.get('NumMedia'))

    if hasMedia == 1:
        contentTypeMedia = incoming_msg.get('MediaContentType0')
        urlMedia = incoming_msg.get('MediaUrl0')

        typeContent = contentTypeMedia.split('/')

        if typeContent[0] == 'image' and msgBody != '':
            return f'image and msg type'
        
        elif typeContent[0] == 'image':
            return f'image type'

        elif typeContent[0] == 'audio':
            return f'audio type'

        elif typeContent[0] == 'video':
            return f'video type'

        elif typeContent[0] == 'application':
            return f'application type'
        
        elif typeContent[0] == 'text':
            return f'text type'
        
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
    


# def process_command(command):
#     # Implement command processing logic
#     return f"Command processed: {command}"


# def resp_message():
#     pass


# def send_message(client, message):
#     # Implement Twilio code to send a message
#     from_whatsapp_number = 'whatsapp:+14155238886'
#     to_whatsapp_number = 'whatsapp:+5511991982436'

#     message = client.messages.create(
#         body=message,
#         from_=from_whatsapp_number,
#         to=to_whatsapp_number
#     )

#     # print("Sending message:", message)


