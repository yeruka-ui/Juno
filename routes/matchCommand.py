def match_command(input):
    command = input['command']

    match command:
        case 'joke':
            return 'joke'
        case 'weather':
            return 'weather'
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