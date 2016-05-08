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
        """Key is list of cards represented numerically (1 to 54 inclusive) or with strings (as described in readme.md)
        If key is not provided, deck will be generated in random order"""
        if key:
            self.cards = self._validate_key(key)
        else:
            self.cards = self._random_key()
        self.verbose = verbose
        self.show_as_strs = show_as_strs

    @staticmethod
    def reference_numeric_key():
        """Returns ordered reference list of cards represented as numbers from 1-54 inclusive"""
        return [x for x in range(1, 55)]

    @staticmethod
    def reference_string_key():
        """Returns ordered reference list of cards represented as strings per readme.md"""
        string_key = list()
        for suit in ['C', 'D', 'H', 'S']:
            for rank in ['A'] + [str(x) for x in range(2, 11)] + ['J', 'Q', 'K']:
                string_key.append(suit + rank)
        string_key += ['JA', 'JB']  # Two jokers
        return string_key

    @staticmethod
    def _random_key():
        """Generates a random key for use - a shuffled deck, if you will"""
        cards = [x for x in range(1, 55)]
        random.shuffle(cards)
        return cards

    @staticmethod
    def _validate_key(self, key):
        """Check that user input key is valid, then return key represented as numbers, converting it if necessary"""
        if type(key[0]) is int:
            assert sorted(key) == sorted(self.reference_numeric_key()), \
                "Numeric representation of key must be a list of all integers from 1 to 54 inclusive (in any order)"
            return key
        elif type(key[0]) is str:
            assert sorted(key) == sorted(self.reference_string_key()), \
                "String representation of key must be a list of all 54 card strings as described in readme.md"
            return self._card_strings_to_nums(key)
        else:
            raise TypeError("Key must be a list of integers 1 to 54, or a list of strings as described in readme.md")

    def __repr__(self):
        if self.show_as_strs:
            return "Deck with state {0}".format(self._card_nums_to_strings(self.cards))
        else:
            return "Deck with state {0}".format(self.cards)

    def _card_nums_to_strings(self, cards):
        pass

    def _card_strings_to_nums(self, cards):
        # Use two reference keys to build lookup dictionary
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

print(Deck.reference_string_key())