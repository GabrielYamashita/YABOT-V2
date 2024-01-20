
import os
import requests
from dotenv import load_dotenv

import vobject

# Replace 'your_account_sid' and 'your_auth_token' with your actual Twilio credentials
load_dotenv()
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

# Assuming you have the MediaUrl0 from the incoming_message dictionary
media_url = 'https://api.twilio.com/2010-04-01/Accounts/ACc906b1cb84d639c680889d5ab72f36d1/Messages/MMff63c554c34dfea5d039cdea519bf641/Media/MEd2b23bd8766fde13868b7f42ab28e703'



# Make a GET request to the media URL with Twilio credentials
response = requests.get(
    media_url,
    auth=(account_sid, auth_token)
)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Access the binary content of the media
    content = response.content.decode('utf-8')
    vcard = vobject.readOne(content)

    if vcard:
        for prop in vcard.getChildren():
            print(f"{prop.name}: {prop.value}")
        # print(vcard)
        # print(f"Full Name: {vcard.fn.value}")
        # print(f"Email: {vcard.email.value}")
        # print(f"Phone: {vcard.tel.value}")

    # Now you can do something with the media content, e.g., save it to a file
    # with open('content.txt', 'wb') as file:
    #     file.write(content)
else:
    print(f"Failed to retrieve media. Status code: {response.status_code}")

