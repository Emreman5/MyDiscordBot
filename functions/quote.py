import requests
import json
from translator import get_translate
def getQuote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = get_translate(json_data[0]['q']) + ' -' + json_data[0]['a']
    return quote