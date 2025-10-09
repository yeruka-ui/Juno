from .command_helper import newJson
import requests

def get_quote(command, confidence):
    url= "https://zenquotes.io/api/random"

    response = requests.get(url).json()
    quote_data = response[0]
    quote = f'{quote_data["q"]} - <em>{quote_data["a"]}</em>'

    return newJson(command, confidence, quote)