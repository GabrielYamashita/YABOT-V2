
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