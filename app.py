
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
# account_sid = os.environ.get('ACCOUNT_SID') # account sid para o heroku
# auth_token = os.environ.get('AUTH_TOKEN')
load_dotenv() # carrega as variáveis de ambiente
account_sid = os.getenv('ACCOUNT_SID') # account sid para rodar localmente
auth_token = os.getenv('AUTH_TOKEN')



client = Client(account_sid, auth_token)

app = Flask(__name__)
scheduler = APScheduler()



# Home Page
@app.route("/")
def home():
    return "<h1>Hello World!</h1> Welcome to YABOT!"


# Feature 1: Webhook to handle incoming messages
@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()

    # Feature 1: Commands processing
    if incoming_msg.startswith("!command"):
        command = incoming_msg.split(" ")[1]

        # Handle the command and generate a response
        # response_message = process_command(command)
        response_message = f'COMANDO {command}'
        msg = resp.message()
        msg.body(response_message)
            
    else:
        # Handle regular messages
        msg = resp.message()
        msg.body(f"Received: {incoming_msg}")

    return str(resp)


# Feature 2: Database and scheduler
@scheduler.task('interval', id='send_reminders', seconds=1)
def send_reminders():
    with open("reminders.json", "r") as f:
        data = json.load(f)

    utc = datetime.datetime.now(datetime.timezone.utc) # setando o tempo para UTC
    BRSP = timezone('America/Sao_Paulo') # escolhendo o fuso horário
    timeNow = utc.astimezone(BRSP) # adicionando o fuso horário de SP

    if timeNow.second == 0:
        current_time = timeNow.strftime("%H:%M")
        current_day = timeNow.strftime("%A")
        current_month = timeNow.strftime("%B")

        print(timeNow, current_time, current_day, current_month)

        for reminder in data["reminders"]:
            if (
                reminder["time"] == current_time and 
                reminder["day"] == current_day and 
                reminder["month"] == current_month
            ):
                # Send reminder message
                send_message(reminder["message"])


def process_command(command):
    # Implement command processing logic
    return f"Command processed: {command}"


def send_message(message):
    # Implement Twilio code to send a message
    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+5511991982436'

    message = client.messages.create(
        body=message,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )

    # print("Sending message:", message)



if __name__ == "__main__":
    # Scheduler
    scheduler.init_app(app)
    scheduler.start()


    # Start Flask app
    port = os.getenv("PORT", 5000)
    app.run(debug=False, host="0.0.0.0", port=port)
