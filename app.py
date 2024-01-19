# Environment
import os
from dotenv import load_dotenv

# Flask Environment
from flask import Flask, request
from flask_apscheduler import APScheduler

# Dates Checkup
import json
import datetime
from pytz import timezone

# Twilio Client
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse


# Credentials Import
load_dotenv() # carrega as variáveis de ambiente
account_sid = os.getenv('ACCOUNT_SID') # account sid para rodar localmente
auth_token = os.getenv('AUTH_TOKEN')


# Init of Classes
client = Client(account_sid, auth_token)

app = Flask(__name__)
scheduler = APScheduler()

GOOD_BOY_URL = (
    "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1"
    "&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
)


# Home Page
@app.route("/")
def home():
    return "<h1>Hello World!</h1> Welcome to YABOT!"


# Endpoint to Handle the Webhook
@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.form
    
    msgBody = incoming_msg.get('Body')
    hasMedia = int(incoming_msg.get('NumMedia'))
    contentTypeMedia = incoming_msg.get('MediaContentType0')
    urlMedia = incoming_msg.get('MediaUrl0')

    resp = MessagingResponse()
    msg = resp.message()

    # Feature 1: Commands processing
    if msgBody.lower().startswith("!command"):
        command = msgBody.split(" ")[1:].join()

        # Handle the command and generate a response
        response_message = process_command(command, incoming_msg)
        msg.body(response_message)
            
    else:
        # Handle regular messages
        msg.body(f"Body: {msgBody}\nNumMedia: {hasMedia}\nMedia Content Type: {contentTypeMedia}\nMedia URL: {urlMedia}")
        msg.media(GOOD_BOY_URL)

    return str(resp)


# Scheduler Check
@scheduler.task('interval', id='send_reminders', seconds=1)
def send_reminders():
    utc = datetime.datetime.now(datetime.timezone.utc) # setando o tempo para UTC
    BRSP = timezone('America/Sao_Paulo') # escolhendo o fuso horário
    timeNow = utc.astimezone(BRSP) # adicionando o fuso horário de SP

    if timeNow.second == 0:
        current_time = timeNow.strftime("%H:%M") # current time
        # current_day = timeNow.strftime("%A") # day in week (written)
        weekDay = int(timeNow.strftime('%w')) + 1 # day in week (number)
        monthDay = timeNow.day # day in month

        # print(f"{timeNow} | {current_time} | {weekDay} | {monthDay}")
        
        with open("reminders.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        for reminder in data["reminders"]:
            if reminder["time"] == current_time:
                # Check for Weekly Reminders
                if (
                    (reminder["reminderType"] == "W" and weekDay in reminder["reminder"]) or
                    (0 in reminder["reminder"])
                ):
                    send_message(reminder["message"])

                # Check for Monthly Reminders
                if (
                    (reminder["reminderType"] == "M" and monthDay in reminder["reminder"]) or
                    (False)
                ):
                    send_message(reminder["message"])


def process_command(command, incoming_msg):
    # Implement command processing logic
    if process_command == 'show log':
        return f'Incoming Message:\n\n{incoming_msg}'


    return f"Command processed: {command}"


def resp_message():
    pass


def send_message(message):
    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+5511991982436'

    message = client.messages.create(
        body=message,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )


# Running the App
if __name__ == "__main__":
    # Initializing
    print("Running...")
    send_message("New Deploy has been Launched")

    # Scheduler
    scheduler.init_app(app)
    scheduler.start()

    # Start Flask app
    port = os.getenv("PORT", 5000)
    app.run(debug=False, host="0.0.0.0", port=port)
