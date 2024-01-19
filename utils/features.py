
def process_type(incoming_msg):
    profileName = incoming_msg.get('ProfileName')
    msgBody = incoming_msg.get('Body')

    hasMedia = int(incoming_msg.get('NumMedia'))

    lat = incoming_msg.get('Latitude')
    long = incoming_msg.get('Longitude')

    contentTypeMedia = incoming_msg.get('MediaContentType0')
    urlMedia = incoming_msg.get('MediaUrl0')

    return f'{profileName}:\nMessage Body: {msgBody}\n\nNum Media: {hasMedia}\n\nLatitude: {lat}\nLongitude: {long}\n\nMedia Content Type 0: {contentTypeMedia}\nURL Media: {urlMedia}'


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


