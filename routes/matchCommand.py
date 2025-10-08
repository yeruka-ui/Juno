from .commands import *
from flask import jsonify
from .commands import command_helper

def match_command(input):

    command = input['command_id'] #gets command
    confidence = input['confidence']
    user_args = input['arguments']

    match command:
        case 'joke':
            return get_joke(command, confidence)
        case 'weather':
            return get_weather(command, confidence, user_args)
        case 'news':
            return 'news'
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
        case _:
            return 'Oh moons, I beg your pardon?'