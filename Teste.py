
import os
import requests
from dotenv import load_dotenv

# Replace 'your_account_sid' and 'your_auth_token' with your actual Twilio credentials
load_dotenv()
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

# Assuming you have the MediaUrl0 from the incoming_message dictionary
media_url = 'https://api.twilio.com/2010-04-01/Accounts/ACc906b1cb84d639c680889d5ab72f36d1/Messages/MMf9ceb369317080e84a50a3d3366a6b18/Media/ME5377b3a191e10aaa6568891dbd5f0faa'



# Make a GET request to the media URL with Twilio credentials
response = requests.get(
    media_url,
    auth=(account_sid, auth_token)
)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Access the binary content of the media
    content = response.content
    # print(content)
    # print("")

    # Now you can do something with the media content, e.g., save it to a file
    with open('content.mp3', 'wb') as file:
        file.write(content)
else:
    print(f"Failed to retrieve media. Status code: {response.status_code}")

