
# import os
# import requests
# from dotenv import load_dotenv

# # Replace 'your_account_sid' and 'your_auth_token' with your actual Twilio credentials
# load_dotenv()
# account_sid = os.getenv('ACCOUNT_SID')
# auth_token = os.getenv('AUTH_TOKEN')

# # Assuming you have the MediaUrl0 from the incoming_message dictionary
# media_url = 'https://api.twilio.com/2010-04-01/Accounts/ACc906b1cb84d639c680889d5ab72f36d1/Messages/MM4d62c5fc32c10d3ba9ae4d5d7c27c3d5/Media/ME6f6efe4beb3d816500fb02913f6ad2ea'



# # Make a GET request to the media URL with Twilio credentials
# response = requests.get(
#     media_url,
#     auth=(account_sid, auth_token)
# )

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Access the binary content of the media
#     media_content = response.content
#     print(media_content)
#     print("")

#     # Now you can do something with the media content, e.g., save it to a file
#     with open('downloaded_media.jpg', 'wb') as file:
#         file.write(media_content)
# else:
#     print(f"Failed to retrieve media. Status code: {response.status_code}")









# import json
# import time
# import datetime

# while True:
#     timeNow = datetime.datetime.now()
#     # print(timeNow)
#     time.sleep(0.95)

#     if timeNow.second == 0:
#         current_time = timeNow.strftime("%H:%M") # current time
#         # current_day = timeNow.strftime("%A") # day written
#         weekDay = int(timeNow.strftime('%w')) + 1 # day in number
#         monthDay = timeNow.day # day in number

#         print(f"{timeNow} | {current_time} | {weekDay} | {monthDay}")


#         with open("reminders.json", "r") as f:
#             data = json.load(f)

#         for reminder in data["reminders"]:
#             if reminder["time"] == current_time:
#                 if (
#                     (reminder["reminderType"] == "W" and weekDay in reminder["reminder"]) or
#                     (0 in reminder["reminder"])
#                 ):
#                     print(reminder["message"])

#                 if (
#                     (reminder["reminderType"] == "M" and monthDay in reminder["reminder"]) or
#                     (True)
#                 ):
#                     print(reminder["message"])






                # print(reminder["message"])