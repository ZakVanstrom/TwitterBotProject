#!/usr/bin/python3

import json
import tweepy

# - - - - Twitter Authentication  - - - -
with open('twitter_auth.json') as json_file:
    data = json.load(json_file)
    api_token = data["api"]
    apiSecret_token = data["apiSecret"]
    access_token = data["access"]
    accessSecret_token = data["accessSecret"]
    bearer_token = data["bearer"]

auth = tweepy.OAuthHandler(api_token, apiSecret_token)
auth.set_access_token(access_token, accessSecret_token)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# _ _ _ _ _

# - - - - Send PayLoad - - - -

# - - - - Send PayLoad - - - -
def sendPayload(user=1112163454192967680,
                message="Good Morning Maren!!! I love us dearly and can't wait to see your ass :) \n\n Make sure to take your medicine!!"):
    api.send_direct_message(user, message, attachment_type=media, attachment_media_id=)


# - - - - - - - - - - - - - - -


def __main__():
    sendPayload(message="hey baby this progress is pretty slow but im doing my best :) ")


__main__()
