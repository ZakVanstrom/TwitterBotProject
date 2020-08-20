# API key
# hThF15q5Z0j0TVv8tolWUCXJe

# API secret key
# a1W3b5gjkbOgyRRe8NtW28QQkiwVSIQbrF5WIFEJNqryLC4VqA

# Bearer token
# AAAAAAAAAAAAAAAAAAAAAAU%2BGwEAAAAAvOYkNLfAHVCrFiiJ%2FLPmPt5Ptuo%3DCqjJsoVyLl67F7riuLyEZ4chKtjQp5ETZDCVin8B4wi92kg28s

import tweepy

import json
from gphotospy import authorize
client_id = "client_id.json"
service = authorize.init(client_id)

#sleep timer
import datetime
import pause

#Twitter Authentication  - - - -
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

# Listener Class - - - -
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")
# - - - - - - - - - - - -

# - - - - Send PayLoad - - - -
def sendPayload(user=1112163454192967680):
    api.send_direct_message(user, "Good Morning Maren!!! I love you dearly and can't wait to see your ass :) \n\n Make sure to take your medicine!!")
# - - - - - - - - - - - - - - -



# tweetsListener = MyStreamListener(api)
# stream = tweepy.Stream(api.auth, tweetsListener)
# stream.filter(track=["@vanstrom_zak", ], languages=["en"])

def sendAtTime():
    curTime = datetime.datetime.now()
    if curTime.hour >= 5:
        curTime.day = curTime.day + 1
    nextSend = datetime.datetime(curTime.year, curTime.month, curTime.day, 5, 0, 0)
    while True:
        pause.until(nextSend)
        sendPayload()
        pause.time(1000)
        nextSend.day = nextSend.day + 1



