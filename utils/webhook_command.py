
def process_command(command, incoming_msg):
    # Implement command processing logic
    imgGen = False

    if 'qr' in command.lower():
        link = command.split(' ')[1:]

        resp = f'QR Code Generated {link}'
        imgGen = f'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=%3C{link}%3E'

    else:
        resp = 'Command not Found!y'

    return resp, imgGen


