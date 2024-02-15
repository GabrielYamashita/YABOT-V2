
import requests


def categorize_msg(incoming_msg):
    msgBody = incoming_msg.get('Body')
    hasMedia = int(incoming_msg.get('NumMedia'))

    if hasMedia == 1:
        contentTypeMedia = incoming_msg.get('MediaContentType0')
        urlMedia = incoming_msg.get('MediaUrl0')

        typeContent = contentTypeMedia.split('/')

        if typeContent[0] == 'image' and msgBody != '':
            return f'img and msg'
        elif typeContent[0] == 'image':
            return f'img'
        elif typeContent[0] == 'video' and msgBody != '':
            return f'video and msg'
        elif typeContent[0] == 'video':
            return f'video'
        elif typeContent[0] == 'audio':
            return f'audio'
        elif typeContent[0] == 'application':
            return f'application'
        elif typeContent[0] == 'text':
            return f'text'

    else:
        lat = incoming_msg.get('Latitude')
        long = incoming_msg.get('Longitude')

        if lat != None and long != None:
            return f'location'
        else:
            return f'msg'



def process_msg(typeMsg, incoming_msg):
    imgGen = False
    print(typeMsg)

    if 'img' in typeMsg:
        resp = 'Obrigado pela Imagem!'
    elif 'img' in typeMsg and 'msg' in typeMsg:
        resp = 'Obrigado pela Mensagem e Imagem!'
    elif 'video' in typeMsg:
        resp = 'Obrigado pelo Vídeo!'
    elif 'video' in typeMsg and 'msg' in typeMsg:
        resp = 'Obrigado pelo Mensagem e Vídeo!'
    elif 'audio' in typeMsg:
        resp = 'Obrigado pelo Áudio!'
    elif 'applicatiom' in typeMsg:
        resp = 'Obrigado pelo Documento!'
    elif 'text' in typeMsg:
        resp = 'Obrigado pelo Cartão de Contato!'
    elif 'location' in typeMsg:
        lat = incoming_msg.get('Latitude')
        long = incoming_msg.get('Longitude')
        resp = f'Obrigado pela Localização!\n\nLat: {lat}, Long: {long}'


    elif 'msg' in typeMsg:
        msgBody = incoming_msg.get('Body')

        if checkPhraseIntent(msgBody, [["manda", "imagem"], ["mande", "imagem"], ["manda", "img"], ["mande", "img"]]):
            resp = 'OK, toma uma foto de um cachorro!'
            imgGen = generateRandomDogImg()
        else:
            resp = 'Obrigado pela Mensagem!'

    return resp, imgGen



def checkPhraseIntent(string, patterns):
    string = string.lower()
    
    return any(all(pattern.lower() in string for pattern in pattern_group) for pattern_group in patterns)



def generateRandomDogImg():
    response = requests.get('https://dog.ceo/api/breeds/image/random')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the image URL
        dog_image_url = data.get('message', '')

        return dog_image_url
