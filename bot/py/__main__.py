#!/usr/bin/python3

import tweepy
import json

#Twitter Authentication  - - - -
with open('TwitterBotProject/bot/py/twitter_auth.json') as json_file:
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
def sendPayload(user=1112163454192967680, message="Good Morning Maren!!! I love you dearly and can't wait to see your ass :) \n\n Make sure to take your medicine!!"):
    api.send_direct_message(user, message)
# - - - - - - - - - - - - - - -



sendPayload(message="hi there my bitch. this is my first real send! take your medicine, be happy, and know that you're the baddest bitch around. sincerely, your majesty, Lovey :)")



