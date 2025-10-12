from .command_helper import newJson
from PyMultiDictionary import MultiDictionary
dictionary = MultiDictionary()

def get_definition(command, confidence, word):
    definition = dictionary.meaning('en', word)
    return newJson(command, confidence, definition)

def get_synonym_antonym(command, confidence, word):
    synonym = dictionary.synonym('en', word)
    antonym = dictionary.antonym('en', word)
    combined = {"orig_word": word, "synonyms": synonym, "antonyms": antonym}
    return newJson(command, confidence, combined)
    