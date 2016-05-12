from key_helpers import *
from solitaire import *


reference_key_numeric_literal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                                 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,
                                 47, 48, 49, 50, 51, 52, 53, 54]


def test_sample_keystream_output():
    assert generate_keystream(reference_key_numeric_literal, 10) == [4, 49, 10, 24, 8, 51, 44, 6, 4, 33], \
        "Output of keystream from unkeyed deck does not match specification"


def test_encrypt_10_a_with_reference_deck():
    assert encrypt(reference_key_numeric_literal, "AAAAAAAAAA") == "EXKYIZSGEH", \
        "Encryption output does not match specification"


def test_decrypt_10_a_with_reference_deck():
    assert decrypt(reference_key_numeric_literal, "EXKYIZSGEH") == "AAAAAAAAAA", \
        "Decryption output does not match specification"


def test_sample_keystream_output_foo():
    key = get_key_from_passphrase("FOO")
    assert generate_keystream(key, 15) == [8, 19, 7, 25, 20, 9, 8, 22, 32, 43, 5, 26, 17, 38, 48]


def test_encrypt_15_a_with_foo():
    key = get_key_from_passphrase("FOO")
    assert encrypt(key, "AAAAAAAAAAAAAAA") == "ITHZUJIWGRFARMW", "Encryption output does not match specification"


def test_decrypt_15_a_with_foo():
    key = get_key_from_passphrase("FOO")
    assert decrypt(key, "ITHZUJIWGRFARMW") == "AAAAAAAAAAAAAAA", "Decryption output does not match specification"


def test_encrypt_solitaire_with_cryptonomicon():
    key = get_key_from_passphrase("CRYPTONOMICON")
    assert encrypt(key, "SOLITAIRE") == "KIRAKSFJAN", "Encryption output does not match specification"


def test_decrypt_solitaire_with_cryptonomicon():
    key = get_key_from_passphrase("CRYPTONOMICON")
    assert decrypt(key, "KIRAKSFJAN") == "SOLITAIREX", "Decryption output does not match specification"


def test_encrypt_decrypt_random_key():
    plaintext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    key = randomize_key(reference_key_numeric_literal)
    ciphertext = encrypt(key, plaintext)
    assert decrypt(key, ciphertext) == plaintext, "Encryption and decryption should return same plaintext"
