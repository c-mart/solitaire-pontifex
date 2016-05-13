import string

"""
Helper functions for working with strings of plaintext and ciphertext
"""


def validate_letter_str(letter_str):
    """Confirms that a plaintext matches the specification accepted by the algorithm"""
    assert type(letter_str) == str, "input must be a string"
    assert all([letter in string.ascii_letters for letter in letter_str]), "input must consist entirely of letters"


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


def pad_plaintext(plaintext):
    """Using the letter X, pads plaintext out to a multiple of five characters"""
    validate_letter_str(plaintext)
    if len(plaintext) % 5 == 0:
        pad_length = 0
    else:
        pad_length = 5 - len(plaintext) % 5
    return plaintext + "X" * pad_length
