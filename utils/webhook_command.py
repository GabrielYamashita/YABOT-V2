
import re
import json


def process_command(command):
    # Define Geração de Imagem = False
    imgGen = False

    # Comando para Gerar QR Code para um Link
    if 'qr' in command.lower():
        link = command.split(' ')[1]

        resp = f'QR Code Generated for {link}'
        imgGen = f'https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=%3C{link}%3E'

    elif 'show json' in command.lower():
        file = './data/reminders.json'
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        resp = data

    elif 'add reminder' in command.lower():
        # text = ' '.join(command.split(' ')[3:]).strip()

        type = re.search(r"Reminder Type: ([^\n]+)", command).group(1)
        reminder = re.search(r"Reminder: ([^\n]+)", command).group(1)
        time = re.search(r"Time: ([^\n]+)", command).group(1)
        message = re.search(r"Message: ([^\n]+)", command).group(1)

        reminder = [int(num) for num in reminder.split(",")]
        resp = f'Reminder adicionado! \n-->\n{command}\n\n- {type}<--'

        # d = {
        #     "reminderType": type,
        #     "reminder": reminder,
        #     "time": time,
        #     "message": message
        # }

        # file = './data/reminders.json'
        # with open(file, "r", encoding="utf-8") as f:
        #     data = json.load(f)

        # data['reminders'].append(d)

        # with open(file, 'w', encoding='utf-8') as f:
        #     json.dump(data, f, indent=4)


    elif 'template' in command.lower():
        resp = """
Reminder Type: 
Reminder: 
Time: 
Message: 
"""

    # elif 'set' in command.lower():
    #     file = './data/reminders.json'
    #     with open(file, "r", encoding="utf-8") as f:
    #         data = json.load(f)

    #     curState = data["state"]
    #     setState = command.split(' ')[1]
    #     data["state"] = setState

    #     with open(file, 'w', encoding='utf-8') as f:
    #         json.dump(data, f, indent=4)

    #     resp = curState




    # Sem Comando
    else:
        resp = 'Command not Found!'

    return resp, imgGen # retorno texto, img


