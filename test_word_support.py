import re


def load_file(file_name):
    try:
        with open(file_name) as words_file:
            words = trim(words_file.read().split())
        return words
    except FileNotFoundError:
        raise FileNotFoundError('The specified file name was not found\n\tEnding execution')


def trim(words):
    return list(map(lambda word: re.sub('\W+', '', word), words))


def get_largest_word(file_name):
    words = load_file(file_name)
    word = max(words, key=len) if words else None
    return (word, word[::-1]) if word else None
