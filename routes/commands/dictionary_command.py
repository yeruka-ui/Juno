from .command_helper import newJson
from PyMultiDictionary import MultiDictionary
dictionary = MultiDictionary()

def get_definition(command, confidence, word):
    definition = dictionary.meaning('en', word)

    if isinstance(definition, dict):
        parts = list(definition.keys())

        short_def = " ".join(sum(definition.values(), []))[:200] + "..."

        long_def = "\n".join(
            f"{pos}: " + "; ".join(meanings)
            for pos, meanings in definition.items()
        )

        content = [word, parts, short_def, long_def]
    else:
        content = [word, [], str(definition), ""]

    return newJson(command, confidence, content)

def get_synonym_antonym(command, confidence, word):
    synonym = dictionary.synonym('en', word)
    antonym = dictionary.antonym('en', word)
    combined = {"orig_word": word, "synonyms": synonym, "antonyms": antonym}
    return newJson(command, confidence, combined)
    