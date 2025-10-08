from .command_helper import newJson
import pyjokes

#gets joke and return as json
def get_joke(command, confidence):
    joke = pyjokes.get_joke(language='en')
    return newJson(command, confidence, joke)