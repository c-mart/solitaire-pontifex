import pytest

from text_helpers import *


def test_validate_letter_str_happy_case():
    validate_letter_str("GUACAMOLE")


def test_validate_letter_str_sad_case():
    with pytest.raises(AssertionError):
        validate_letter_str("I HAVE SPACES")


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


def test_pad_plaintext():
    assert pad_plaintext("GUACA") == "GUACA"
    assert pad_plaintext("GUACAMOLE") == "GUACAMOLEX"