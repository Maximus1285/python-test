import unittest
from word import Word
import test_word_support


class TestWord(unittest.TestCase):

    FILE_DIR = 'txt_files/'

    @classmethod
    def setUpClass(cls):
        cls.words = Word(f'{TestWord.FILE_DIR}words.txt')
        cls.one_word = Word(f'{TestWord.FILE_DIR}words2.txt')
        cls.empty_file = Word(f'{TestWord.FILE_DIR}words3.txt')
        cls.no_words_file = Word(f'{TestWord.FILE_DIR}words4.txt')
        cls.no_file = Word(f'{TestWord.FILE_DIR}no_file.txt')

    def test_trim(self):
        self.assertEqual(self.words.trim(
            [' .,test$&', 'another1^#@test ']), ['test', 'another1test'])
        self.assertEqual(self.words.trim(''), None)
        self.assertEqual(self.words.trim(None), None)

    def test_largest_word(self):
        self.assertEqual(self.words.largest_word(['this', 'those']), 'those')
        self.assertEqual(self.words.largest_word(['this', '']), 'this')
        self.assertEqual(self.words.largest_word(['', '']), '')
        self.assertEqual(self.words.largest_word(None), None)

    def test_print_word(self):
        self.assertEqual(self.words.print_word('word'), ('word', 'drow'))
        self.assertEqual(self.words.print_word(''), None)
        self.assertEqual(self.words.print_word(None), None)

    def test_largest_word_non_empty_file(self):
        result = self.words.process_largest_word()
        result_validation = test_word_support.get_largest_word(
            f'{TestWord.FILE_DIR}words.txt')
        self.assertEqual(result, result_validation)

    def test_largest_word_one_word_file(self):
        result = self.one_word.process_largest_word()
        result_validation = test_word_support.get_largest_word(
            f'{TestWord.FILE_DIR}words2.txt')
        self.assertEqual(result, result_validation)

    def test_largest_word_empty_file(self):
        result = self.empty_file.process_largest_word()
        result_validation = test_word_support.get_largest_word(
            f'{TestWord.FILE_DIR}words3.txt')
        self.assertEqual(result, result_validation)

    def test_largest_word_no_words_file(self):
        result = self.no_words_file.process_largest_word()
        result_validation = test_word_support.get_largest_word(
            f'{TestWord.FILE_DIR}words4.txt')
        self.assertEqual(result, result_validation)

    def test_largest_word_no_file_found(self):
        with self.assertRaises(FileNotFoundError):
            self.no_file.process_largest_word()


if __name__ == '__main__':
    unittest.main()
