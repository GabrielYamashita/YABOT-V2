
import re

# JSON Handler
from utils import JSON_Handler

from handlers import Teste


def process_command(command):
    # Define Geração de Imagem = False
    imgGen = False

    # Comando para Gerar QR Code para um Link
    if 'qr' in command.lower():
        link = command.split(' ')[1]

        resp = f'QR Code Generated for {link}'
        imgGen = f'https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=%3C{link}%3E'


    # Comando para mostrar o JSON --> Resumo?
    elif 'show json' in command.lower():
        reminderPath = './data/reminders.json'
        resp = JSON_Handler.read_reminders(reminderPath)


    # Comando para enviar Template de Add Reminder
    elif 'template' in command.lower():
        resp = "Reminder Type: \nReminder: \nTime: \nMessage: "


    # Comando para Adicionar Reminder
    elif 'add reminder' in command.lower():
        type = re.search(r"Reminder Type: ([^\n]+)", command).group(1)
        reminder = re.search(r"Reminder: ([^\n]+)", command).group(1)
        time = re.search(r"Time: ([^\n]+)", command).group(1)
        message = re.search(r"Message: ([^\n]+)", command).group(1)

        reminder = [int(num) for num in reminder.split(",")]

        reminderDict = {
            "reminderType": type,
            "reminder": reminder,
            "time": time,
            "message": message
        }

        reminderPath = './data/reminders.json'
        JSON_Handler.add_reminder(reminderPath, reminderDict)

        resp = f'Reminder adicionado!'


    # Comando para Mudar o State --> Conversacional?
    elif 'set' in command.lower():
        reminderPath = './data/reminders.json'
        setState = command.split(' ')[1]
        currState = JSON_Handler.change_state(reminderPath, setState)

        resp = f'The current state is: *{currState}*'

    elif 'teste' in command.lower():
        resp = Teste.randomNumber()




    # Sem Comando
    else:
        resp = 'Command not Found!'

    return resp, imgGen # retorno texto, img


