from .commands import *
from flask import jsonify
from .commands import command_helper

def match_command(input):

    command = input['command_id'] #gets command
    confidence = input['confidence'] #confidence level
    user_args = (input or {}).get('arguments', "") or ""  #generated arguments from user input

    match command:
        case 'joke':
            return get_joke(command, confidence)
        case 'weather':
            return get_weather(command, confidence, user_args)
        case 'quote':
            return get_quote(command, confidence)
        case 'news':
            return get_news(command, confidence, user_args)
        case 'play':
            return 'play'
        case 'search':
            return 'search'
        case 'email':
            return 'email'
        case 'wiki':
            return 'wiki'
        case 'dictionary':
            return 'dictionary'
        case 'thesaurus':
            return 'thesaurus'
        case 'help':
            return help_command(command, confidence)
        case _:
            return 'Oh moons, I beg your pardon?'