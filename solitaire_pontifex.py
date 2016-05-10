import random
import string


# Helper functions

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


def letter_to_number(letter):
    """Given a single letter, return its 1-indexed number in the alphabet."""
    validate_letter_str(letter)
    assert len(letter) == 1, "Must pass a single letter"
    return string.ascii_uppercase.index(letter.upper()) + 1


def number_to_letter(number):
    """Given number (an integer), return its associated 1-indexed letter.
    If number is greater than 26, return 1-indexed letter associated with number modulo 26."""
    assert type(number) == int, "Number must be an integer"
    return string.ascii_uppercase[(number - 1) % 26]


# Functions used to generate keystream and derive starting deck from a passphrase.

def advance_joker_a(deck):
    """Given a deck (numeric representation), locate joker A and advance it one position, return new deck"""
    # Locate joker A and advance it one position
    ja_loc = deck.index(53)
    if ja_loc == 53:  # If joker A is on the bottom of the deck, move it to one card below the top
        return [deck[0]] + [53] + deck[1:53]
    else:
        return deck[:ja_loc] + [deck[ja_loc + 1]] + [53] + deck[ja_loc + 2:]


def advance_joker_b(deck):
    """Given a deck (numeric representation), locate joker B and advance it two positions, return new deck"""
    jb_loc = deck.index(54)
    if jb_loc == 53:  # If joker B is on the bottom of the deck, move it to two positions below the top
        return deck[0:2] + [54] + deck[2:53]
    if jb_loc == 52:  # If joker is second from bottom of the deck, move it to one position below the top
        return [deck[0]] + [54] + deck[1:52] + [deck[53]]
    else:
        return deck[:jb_loc] + deck[jb_loc + 1:jb_loc + 3] + [54] + deck[jb_loc + 3:]


def triple_cut(deck):
    """Given a deck, perform a triple cut, return new deck.
    A triple cut swaps the cards before the first-appearing joker with the cards after the last-appearing joker.
    The *relative* positions of the two jokers and cards between them do not change.
    """
    first_j_loc, second_j_loc = sorted([deck.index(53), deck.index(54)])
    return deck[second_j_loc + 1:] + deck[first_j_loc:second_j_loc + 1] + deck[:first_j_loc]


def count_cut(deck):
    """Given a deck, perform a count cut, return new deck. Count cut steps:
    1. Observe numeric value (n) of bottom card. Per specification, both jokers have value 53 (both treated as joker A)
    2. Cut from after the nth (1-indexed) card up to (but not including) the last card
    3. Move the cut section to the top of the deck
    """
    bottom_card_val = deck[53]
    # Per specification, both jokers have value 53 in this step, so if we find Joker B we treat it as Joker A
    if bottom_card_val == 54:
        bottom_card_val = 53
    # 'Cheat' by using the 1-indexed card value to refer to position following zero-indexed list location
    return deck[bottom_card_val:53] + deck[:bottom_card_val] + [deck[53]]


def count_cut_from_letter(deck, letter):
    """Given a deck, perform a count cut as defined above, with one modification:
    Use 1-indexed numeric value of letter rather than numeric value of bottom card.
    Return new deck.
    """
    cut_pos = letter_to_number(letter)
    # 'Cheat' by using the 1-indexed cut position to refer to position following zero-indexed list location
    return deck[cut_pos:53] + deck[:cut_pos] + [deck[53]]


class JokerException(Exception):
    """Used when we get a joker in our output keystream value"""
    pass


def read_output_keystream_value(deck):
    """Given a deck, returns output value for keystream or raises ValueError. To determine output:
    1. Observe numeric value (n) of top card. Per specification, both jokers have value 53 (both treated as joker A)
    2. Return numeric value (p) of card after nth (1-indexed) card, unless it is a joker, raise JokerException
    """
    top_card_val = deck[0]
    if top_card_val == 54:
        top_card_val = 53
    # 'Cheat' by using the 1-indexed card value to refer to position following zero-indexed list location
    output_card_val = deck[top_card_val]
    if output_card_val in (53, 54):
        raise JokerException
    else:
        return output_card_val


def key_from_passphrase(passphrase):
    """Generate a key deck from a passphrase of entirely letters using keying method 3 in specification"""
    validate_letter_str(passphrase)
    key_deck = reference_numeric_key()
    for letter in passphrase:
        key_deck = advance_joker_a(key_deck)
        key_deck = advance_joker_b(key_deck)
        key_deck = triple_cut(key_deck)
        key_deck = count_cut(key_deck)
        key_deck = count_cut_from_letter(key_deck, letter)
    return key_deck


class Deck(object):
    """Deck of cards used to generate keystream"""
    def __init__(self, deck=None, show_as_strs = False):
        """Key is list of cards represented numerically (1 to 54 inclusive) or with strings (as described in readme.md)
        If key is not provided, deck will be generated in random order"""
        if deck:
            self.deck = self._validate_key(self, deck)
        else:
            self.deck = random_key()
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
            return "Deck with state {0}".format(self._card_nums_to_strings(self.deck))
        else:
            return "Deck with state {0}".format(self.deck)

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
            # Iterate through algorithm until we get an output that is not a joker
            while True:
                self.deck = advance_joker_a(self.deck)
                self.deck = advance_joker_b(self.deck)
                self.deck = triple_cut(self.deck)
                self.deck = count_cut(self.deck)
                try:
                    keystream.append(read_output_keystream_value(self.deck))
                    break
                # If output card is a joker, do not add to keystream and start over again
                except JokerException:
                    continue
        return keystream


def validate_letter_str(letter_str):
    """Confirms that a plaintext matches the specification accepted by the algorithm"""
    assert type(letter_str) == str, "input must be a string"
    assert all([letter in string.ascii_letters for letter in letter_str]), "input must consist entirely of letters"


def pad_plaintext(plaintext):
    """Using the letter X, pads plaintext out to a multiple of five characters"""
    validate_letter_str(plaintext)
    if len(plaintext) % 5 == 0:
        pad_length = 0
    else:
        pad_length = 5 - len(plaintext) % 5
    return plaintext + "X" * pad_length


def encrypt(deck, plaintext):
    """Uses a given deck to encrypt a given plaintext, return ciphertext"""
    assert isinstance(deck, Deck), "deck must be a Deck object"
    validate_letter_str(plaintext)
    padded_plaintext = pad_plaintext(plaintext)
    keystream = deck.generate_keystream(len(padded_plaintext))
    ciphertext = ""
    for pt_letter, keystream_val in zip(padded_plaintext, keystream):
        pt_number = letter_to_number(pt_letter)
        ct_char = number_to_letter(pt_number + keystream_val)
        ciphertext += ct_char
    return ciphertext


def decrypt(deck, ciphertext):
    assert isinstance(deck, Deck), "deck must be a Deck object"
    validate_letter_str(ciphertext)
    keystream = deck.generate_keystream(len(ciphertext))
    plaintext = ""
    for ct_letter, keystream_val in zip(ciphertext, keystream):
        ct_number = letter_to_number(ct_letter)
        pt_char = number_to_letter(ct_number - keystream_val)
        plaintext += pt_char
    return plaintext