import random

# Helper functions


def letter_to_number_mod26():
    # TODO
    pass


def number_mod26_to_letter():
    # TODO
    pass


def reference_numeric_key():
    """Returns ordered reference list of cards represented as numbers from 1-54 inclusive"""
    return [x for x in range(1, 55)]


def reference_string_key():
    """Returns ordered reference list of cards represented as strings per readme.md"""
    string_key = list()
    for suit in ['C', 'D', 'H', 'S']:
        for rank in ['A'] + [str(x) for x in range(2, 11)] + ['J', 'Q', 'K']:
            string_key.append(suit + rank)
    string_key += ['JA', 'JB']  # Two jokers
    return string_key


def random_key():
    """Generates a random key for use - a shuffled deck, if you will"""
    key = reference_numeric_key()
    random.shuffle(key)
    return key


class Deck(object):
    """Deck of cards used to generate keystream"""
    def __init__(self, key=None, verbose=False, show_as_strs=False):
        """Key is list of cards represented numerically (1 to 54 inclusive) or with strings (as described in readme.md)
        If key is not provided, deck will be generated in random order"""
        if key:
            self.cards = self._validate_key(self, key)
        else:
            self.cards = random_key()
        self.verbose = verbose
        self.show_as_strs = show_as_strs

    @staticmethod
    def _validate_key(self, key):
        """Check that user input key is valid, then return key represented as numbers, converting it if necessary
        We internally work with the key numerically"""
        if type(key[0]) is int:
            assert sorted(key) == sorted(reference_numeric_key()), \
                "Numeric representation of key must be a list of all integers from 1 to 54 inclusive (in any order)"
            return key
        elif type(key[0]) is str:
            assert sorted(key) == sorted(reference_string_key()), \
                "String representation of key must be a list of all 54 card strings as described in readme.md"
            return self._card_strings_to_nums(key)
        else:
            raise TypeError("Key must be a list of integers 1 to 54, or a list of strings as described in readme.md")

    def __repr__(self):
        if self.show_as_strs:
            return "Deck with state {0}".format(self._card_nums_to_strings(self.cards))
        else:
            return "Deck with state {0}".format(self.cards)

    @staticmethod
    def _card_nums_to_strings(cards):
        """Converts list of numeric representations of cards to list of string representations of cards"""
        n2s_lookup = dict()
        for key, value in zip(reference_numeric_key(), reference_string_key()):
            n2s_lookup[key] = value
        return [n2s_lookup[card] for card in cards]

    @staticmethod
    def _card_strings_to_nums(cards):
        """Converts list of string representations of cards to list of numeric representations of cards"""
        s2n_lookup = dict()
        for key, value in zip(reference_string_key(), reference_numeric_key()):
            s2n_lookup[key] = value
        return [s2n_lookup[card] for card in cards]

    def generate_keystream(self, length):
        """Implements the Solitaire algorithm, generates output keystream (numbers 1-54 inclusive) of given length"""
        keystream = []
        for i in range(length):
            # Iterate through algorithm until it generates an output that is not a joker
            while True:
                # Locate joker A and advance it one position
                ja_loc = self.cards.index(53)
                # TODO fix this, the bottom IS the top so we need to swap one further, or use a better data structure
                if ja_loc == 53:  # If joker A is on the bottom of the deck, move it to the top
                    self.cards = [53] + self.cards[:53]
                else:
                    self.cards = self.cards[:ja_loc] + [self.cards[ja_loc+1]] + [53] + self.cards[ja_loc+2:]

                # Locate joker B and advance it two positions
                jb_loc = self.cards.index(54)
                # TODO fix this, the bottom IS the top so we need to swap one further, or use a better data structure
                if jb_loc == 53:  # If joker B is on the bottom of the deck, move it to one position below the top
                    self.cards = [self.cards[0]] + [54] + self.cards[1:53]
                if jb_loc == 52:  # If joker is second from the bottom of the deck, move it to the top
                    self.cards = [54] + self.cards[:52] + [self.cards[53]]
                else:
                    self.cards = self.cards[:jb_loc] + self.cards[jb_loc+1:jb_loc+3] + [54] + self.cards[jb_loc+3:]

                # Perform triple cut
                first_j_loc, second_j_loc = sorted([self.cards.index(53), self.cards.index(54)])
                self.cards = self.cards[second_j_loc+1:] + self.cards[first_j_loc:second_j_loc+1] + self.cards[:first_j_loc]

                # Perform count cut
                bottom_card_val = self.cards[53]
                # 'Cheat' by using the 1-indexed card value to refer to position following zero-indexed list location
                self.cards = self.cards[bottom_card_val:53] + self.cards[:bottom_card_val] + [self.cards[53]]

                # Read output character
                top_card_val = self.cards[0]
                if top_card_val == 54:
                    # Looping back to beginning of deck
                    output_card_val = self.cards[0]
                else:
                    # Same 'cheat' as above because output card follows the nth card, where n is value of top card
                    output_card_val = self.cards[top_card_val]
                if output_card_val not in (53, 54):
                    # Output card is not a joker, add its value to keystream
                    keystream.append(output_card_val)
                    break
                else:
                    # Output card is a joker, start over again
                    continue
        return keystream


def encrypt(deck, plaintext):
    """Uses a given deck to encrypt a given plaintext"""
    # TODO
    pass


def decrypt(deck, ciphertext):
    """Uses a given deck to decrypt a given ciphertext"""
    # TODO
    pass

"""
my_key_1 = ['H3', 'DK', 'S9', 'C10', 'C8', 'D6', 'C7', 'C6', 'S4', 'S3', 'D2', 'S2', 'SK', 'S7', 'CJ', 'JB', 'DA', 'D9',
          'HA', 'CA', 'H7', 'HQ', 'D7', 'HJ', 'SQ', 'D4', 'C5', 'CK', 'D3', 'S10', 'S5', 'C2', 'H8', 'SA', 'S6', 'H6',
          'H10', 'DJ', 'H5', 'JA', 'H4', 'CQ', 'DQ', 'S8', 'H2', 'C3', 'D10', 'D5', 'H9', 'C4', 'SJ', 'D8', 'HK', 'C9']
my_deck_1 = Deck(my_key_1)
print(my_deck_1.generate_keystream(20))

my_key_2 = ['HA', 'DK', 'S9', 'C10', 'C8', 'D6', 'C7', 'C6', 'S4', 'S3', 'D2', 'S2', 'SK', 'S7', 'CJ', 'JB', 'DA', 'D9',
          'H3', 'CA', 'H7', 'HQ', 'D7', 'HJ', 'SQ', 'D4', 'C5', 'CK', 'D3', 'S10', 'S5', 'C2', 'H8', 'SA', 'S6', 'H6',
          'H10', 'DJ', 'H5', 'JA', 'H4', 'CQ', 'DQ', 'S8', 'H2', 'C3', 'D10', 'D5', 'H9', 'C4', 'SJ', 'D8', 'HK', 'C9']
my_deck_2 = Deck(my_key_2)
print(my_deck_2.generate_keystream(20))
"""

my_deck_3 = Deck(reference_numeric_key())
print(my_deck_3.generate_keystream(20))