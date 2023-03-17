# Import the necessary modules
import grpc
import googlesamples.assistant.grpc.device_helpers as device_helpers
import googlesamples.assistant.grpc.audio_helpers as audio_helpers

# Import the Config class from the config module
from config import Config

# Define the GoogleAssistant class
class GoogleAssistant:
    def __init__(self):
        # Initialize a Config object and assign it to the config attribute
        self.config = Config()

        # Create a DeviceManager object to manage the conversation with the Google Assistant API
        self.device_manager = device_helpers.DeviceManager(
            project_id=self.config.PROJECT_ID,
            credentials_path=self.config.CREDENTIALS_PATH
        )

    # Define a method to send text to the Google Assistant API and play the resulting audio
    def say(self, text):
        # Initialize the conversation variable to None
        conversation = None
        
        # Create an AudioOutput object and assign it to the audio variable
        with audio_helpers.AudioOutput() as audio:
            # Start an infinite loop
            while True:
                # If the conversation variable is None, start a new conversation with the API
                if conversation is None:
                    conversation = self.device_manager.start_conversation()

                # Create a text request object
                text_request = device_helpers.converse_text_stream_request(self.config.SCOPE)

                # Set the conversation state and language code for the text request
                text_request.dialog_state_out.conversation_state = conversation.conversation_state
                text_request.dialog_state_out.language_code = 'en-US'

                # Set the text of the request to the input text
                text_request.input.text = text

                # Send the text request to the API and get the response
                response = conversation.assist(text_request)

                # If the conversation has finished, set the conversation variable to None
                if response.dialog_state_out.conversation_finished:
                    conversation = None

                # If the response contains audio data, play it using the AudioOutput object
                if response.audio_out.audio_data:
                    audio.write(response.audio_out.audio_data)

                # If the response contains supplemental display text, print it to the console
                if response.dialog_state_out.supplemental_display_text:
                    print(response.dialog_state_out.supplemental_display_text)
