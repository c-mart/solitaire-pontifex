from solitaire_pontifex import *
import pytest


def test_letter_to_number_happy_case():
    for letter, number in [("A", 1), ("Z", 26), ("O", 15)]:
        assert letter_to_number(letter) == number, "Letter {0} should be at position {1}".format(letter, number)


def test_letter_to_number_sad_case():
    with pytest.raises(AssertionError):
        letter_to_number("chicken")
    with pytest.raises(AssertionError):
        letter_to_number(3)


def test_number_to_letter_happy_case():
    for number, letter in [(1, "A"), (26, "Z"), (11, "K"), (52, "Z"), (29, "C")]:
        assert number_to_letter(number) == letter, "Number {0} should correspond to letter {1}".format(number, letter)


def test_number_to_letter_sad_case():
    with pytest.raises(AssertionError):
        letter_to_number("chicken")
    with pytest.raises(AssertionError):
        letter_to_number(3.14159265358979)


def test_sample_keystream_output():
    my_deck = Deck(reference_numeric_key())
    assert my_deck.generate_keystream(10) == [4, 49, 10, 24, 8, 51, 44, 6, 4, 33], \
        "Output of keystream from unkeyed deck does not match specification"

def test_sample_keystream_output_foo():
    my_deck = Deck(key_from_passphrase("FOO"))
    assert my_deck.generate_keystream(15) == [8, 19, 7, 25, 20, 9, 8, 22, 32, 43, 5, 26, 17, 38, 48]