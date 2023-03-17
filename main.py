import os
import time
import random
import json
from src.google import GoogleAssistant

if __name__ == '__main__':
    # Load the quotes from the quotes.json file
    # with open('quotes.json') as f:
    #     quotes = json.load(f)

    
    assistant = GoogleAssistant()
    assistant.say("Hello, world!")
    
