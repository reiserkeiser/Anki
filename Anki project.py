import requests
from googletrans import Translator

def translate_to_swedish(text):
    translator = Translator()
    translation = translator.translate(text, dest='sv')
    return translation.text

def create_anki_card(front, back):
    url = 'http://localhost:8765'
    headers = {'Content-Type': 'application/json'}
    data = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "English-Swedish",
                "modelName": "Basic",
                "fields": {
                    "Front": front,
                    "Back": back
                },
                "tags": ["language_learning"]
            }
        }
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

# Example usage
input_text = input("Enter text in English to translate to Swedish: ")
translated_text = translate_to_swedish(input_text)
print("Translated Text:", translated_text)

# Add to Anki
result = create_anki_card(input_text, translated_text)
print("Added to Anki:", result)