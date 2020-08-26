from __future__ import print_function

import base64
import os.path
import pickle
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def create_message(sender, to, subject, message_text):
    created_message = MIMEText(message_text)
    created_message['to'] = to
    created_message['from'] = sender
    created_message['subject'] = subject
    message_string = created_message.as_string()
    message_string_bytes = message_string.encode('ascii')
    message_string_b64 = base64.b64encode(message_string_bytes)
    return message_string_b64


def send_message(service, user_id, message):
    message_to_send = (service.users().messages().send(userId=user_id, body=message).execute())
    print('Message Id: %s' % message_to_send['id'])
    return message_to_send


def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])


main()
message = create_message("zakyre17@gmail.com", "zvanstro@asu.edu", "About that night...",
                         "This is just an example text being sent")
send_message(message)
