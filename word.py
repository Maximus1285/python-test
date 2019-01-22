import re
import sys


class Word():

    FILE_NOT_FOUND = 'The specified file name was not found\n\tEnding execution'
    EMPTY_FILE = 'The file did not include any words'

    def __init__(self, file_name):
        self.file_name = file_name

    def process_largest_word(self):
        self.load()
        word = self.largest_word(self.words)
        return self.print_word(word) if word else print(Word.EMPTY_FILE)

    def load(self):
        try:
            with open(self.file_name) as words_file:
                self.words = self.trim(words_file.read().split())
        except FileNotFoundError:
            print(Word.FILE_NOT_FOUND)
            raise FileNotFoundError(Word.FILE_NOT_FOUND)

    def trim(self, words):
        if words:
            return list(map(lambda word: re.sub('\W+', '', word), words))

    def largest_word(self, words):
        return max(words, key=len) if words else None

    def print_word(self, word):
        if word:
            print(word)
            reversed_word = word[::-1]
            print(reversed_word)
            return (word, reversed_word)

if __name__ == '__main__':
    Word(sys.argv[1]).process_largest_word()
