import os
import google.auth
from google.oauth2.credentials import Credentials
from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file

from config import CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN

class GoogleAssistant:
    def __init__(self):
        # Load the API credentials from the config file
        self.credentials = Credentials.from_authorized_user_info(info=None, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, refresh_token=REFRESH_TOKEN)
        self.device_model_id, self.device_id = existing_file(os.path.join(os.path.expanduser('~/.config'), 'google-oauthlib-tool', 'credentials.json'))

    def speak(self, text):
        # Initialize the Google Assistant SDK
        with Assistant(self.device_model_id, self.device_id, self.credentials) as assistant:
            # Speak the text using the Google Assistant
            assistant.start_conversation()
            assistant.send_text_query(text)
