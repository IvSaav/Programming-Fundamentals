def count(word, phrase):
    phrase += " "
    result = phrase.count(word.upper() + " ") + phrase.count(word.lower() + " ") + phrase.count(word.capitalize() + " ")
    phrase = phrase[:-1]
    return result

