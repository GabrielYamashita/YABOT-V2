
# Environment
import os

# Flask Environment
from flask import Flask, request
from flask_apscheduler import APScheduler

# Webhook Handler
from utils import twilio_message
from utils import scheduler_message

# Incialização do App
app = Flask(__name__)
scheduler = APScheduler()


# Home Page
@app.route("/")
def home():
    return "<h1>Hello World!</h1> Welcome to YABOT!"


# Endpoint to Handle the Webhook
@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.form
    resp = twilio_message.respond(incoming_msg)

    return str(resp)


# Reminder Check
@scheduler.task('interval', id='send_reminders', seconds=1)
def send_reminders():
    # Puxando Horário com Fuso de SP
    timeNow = scheduler_message.getCurrentTime('America/Sao_Paulo')

    if timeNow.second == 0:
        current_time = timeNow.strftime("%H:%M") # current time
        weekDay = int(timeNow.strftime('%w')) + 1 # day in week (number)
        monthDay = timeNow.day # day in month

        # print(f"{timeNow} | {current_time} | {weekDay} | {monthDay}")
        
        # Carregando Reminders
        data = scheduler_message.read_reminders('./data/reminders.json')

        # Checando cada Reminder
        for reminder in data["reminders"]:
            if reminder["time"] == current_time:
                # Checando Reminders Semanais [W]
                if ( (reminder["reminderType"] == "W" and weekDay in reminder["reminder"]) or (0 in reminder["reminder"]) ):
                    twilio_message.send_message(reminder["message"])

                # Checando Reminders Mensais [M]
                if ( (reminder["reminderType"] == "M" and monthDay in reminder["reminder"]) or (False) ):
                    twilio_message.send_message(reminder["message"])


# Running the App
if __name__ == "__main__":
    # Initializing
    print("Running...")
    twilio_message.send_message("New Deploy has been Launched")

    # Scheduler
    scheduler.init_app(app)
    scheduler.start()

    # Start Flask app
    port = os.getenv("PORT", 5000)
    app.run(debug=False, host="0.0.0.0", port=port)
