from .exceptions import *
import random

class GuessAttempt(object):
    pass


class GuessWord(object):
    
    def __init__(self, passed_word):
        self.answer = passed_word
        self.masked = '*' * len(passed_word)


class HangmanGame(object):
    
    WORD_LIST = ['rmotr', 'python', 'awesome']
    
    def __init__(self, word_list=None, number_of_guesses=5):
        self.word_list = HangmanGame.WORD_LIST if not word_list else word_list
        self.previous_guesses = []
        self.remaining_misses = number_of_guesses
        self.word = GuessWord(self.select_random_word(word_list))
    
    @classmethod   
    def select_random_word(cls, list_of_words):
        if list_of_words == []:
            raise InvalidListOfWordsException()
        return random.choice(list_of_words)



