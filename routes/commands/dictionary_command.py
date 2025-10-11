from .command_helper import newJson
import PyDictionary
from PyDictionary import PyDictionary  

dictionary=PyDictionary()


def get_definition(command, confidence, word):
    definition = dictionary.meaning(word)
    return newJson(command, confidence, definition)

def get_synonym_antonym(command, confidence, word):
    synonym = dictionary.synonym(word)
    antonym = dictionary.antonym(word)
    combined = [synonym, antonym]
    return newJson(command, confidence, combined)