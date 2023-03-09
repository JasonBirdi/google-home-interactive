import os
import time
import random
import json
from google import GoogleAssistant

if __name__ == '__main__':
    # Load the quotes from the quotes.json file
    with open('quotes.json') as f:
        quotes = json.load(f)

    # Initialize the Google Assistant
    google = GoogleAssistant()

    # Choose a random quote from the list
    quote = random.choice(quotes)

    # Use the Google Assistant to read the quote
    google.speak(quote)
