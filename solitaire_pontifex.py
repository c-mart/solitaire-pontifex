import random

"""
Implementation of Solitaire cipher by Bruce Schnier,
a.k.a. Pontifex cipher from Neal Stephenson's Cryptonomicon,
https://www.schneier.com/cryptography/solitaire/
https://en.wikipedia.org/wiki/Solitaire_%28cipher%29
"""


class Deck(object):
    """Deck of cards used to generate keystream"""
    def __init__(self, key=None, verbose=False, show_as_strs=False):
        """Key is list of cards by number or string
        If key is not provided, deck will be shuffled in random order"""
        if key:
            self.cards = self._validate_key(key)
        else:
            self.cards = self._random_key()
        self.verbose = verbose
        self.show_as_strs = show_as_strs

    @staticmethod
    def _random_key():
        """Generates a random key for use - a shuffled deck, if you will"""
        cards = [x for x in range(1, 55)]
        random.shuffle(cards)
        return cards

    @staticmethod
    def _validate_key(self, key):
        """Checks that user input key is valid
        Returns key represented as numbers, converting it if necessary"""
        # Key must either be a list of numbers or list of strings
        # If numbers, must contain one through 53 and nothing else
        # If strings, must contain
        # If strings and is valid, convert to numbers
        if type(key[0]) is int:
            pass
        elif type(key[0]) is str:
            pass

    def __repr__(self):
        if self.show_as_strs:
            return "Deck with state {0}".format(self._card_nums_to_strings(self.cards))
        else:
            return "Deck with state {0}".format(self.cards)

    def _card_nums_to_strings(self, cards):
        pass

    def _card_strings_to_nums(self, cards):
        pass

    def generate_keystream(self, length):
        """Uses the Solitaire algorithm, generates output keystream (numbers 1-54) of given length"""
        pass

def encrypt(deck, plaintext):
    """Uses a given deck to encrypt a given plaintext"""
    pass


def decrypt(deck, ciphertext):
    """Uses a given deck to decrypt a given ciphertext"""
    pass

print(Deck._random_key())