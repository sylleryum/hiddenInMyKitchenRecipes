from himkrecipes.utils import api_call

API_KEY = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
ENDPOINT = 'https://libretranslate.de/translate'


def translate(text, target):
    payload = {
        'q': text,
        'source': 'en',
        'target': target,
        'format': 'text',
        'api_key': API_KEY
    }
    responseTranslate = api_call.post(ENDPOINT, payload)
    return responseTranslate.json()
