import key_helpers
import deck_ops
import text_helpers


def get_key_from_passphrase(passphrase):
    """Generate a key from a passphrase of entirely letters using keying method 3 in specification"""
    text_helpers.validate_letter_str(passphrase)
    key_deck = key_helpers.get_reference_key()
    for letter in passphrase:
        key_deck = deck_ops.advance_joker_a(key_deck)
        key_deck = deck_ops.advance_joker_b(key_deck)
        key_deck = deck_ops.triple_cut(key_deck)
        key_deck = deck_ops.count_cut(key_deck)
        key_deck = deck_ops.count_cut_from_letter(key_deck, letter)
    return key_deck


def generate_keystream(key, length):
    """Implements the Solitaire algorithm.
    Using given key, generates output keystream (numbers 1-54 inclusive) of given length."""
    key_helpers.validate_key(key)
    working_deck = key_helpers.format_key(key)
    keystream = []
    for i in range(length):
        # Iterate through algorithm until we get an output that is not a joker
        while True:
            working_deck = deck_ops.advance_joker_a(working_deck)
            working_deck = deck_ops.advance_joker_b(working_deck)
            working_deck = deck_ops.triple_cut(working_deck)
            working_deck = deck_ops.count_cut(working_deck)
            try:
                keystream.append(deck_ops.read_output_keystream_value(working_deck))
                break
            except deck_ops.JokerException:
                continue
    return keystream


def encrypt(key, plaintext):
    """Uses a given key to encrypt a given plaintext, return ciphertext"""
    text_helpers.validate_letter_str(plaintext)
    padded_plaintext = text_helpers.pad_plaintext(plaintext)
    keystream = generate_keystream(key, len(padded_plaintext))
    ciphertext = ""
    for pt_letter, keystream_val in zip(padded_plaintext, keystream):
        pt_number = text_helpers.letter_to_number(pt_letter)
        ct_char = text_helpers.number_to_letter(pt_number + keystream_val)
        ciphertext += ct_char
    return ciphertext


def decrypt(key, ciphertext):
    """Uses a given key to encrypt a given ciphertext, return plaintext"""
    text_helpers.validate_letter_str(ciphertext)
    keystream = generate_keystream(key, len(ciphertext))
    plaintext = ""
    for ct_letter, keystream_val in zip(ciphertext, keystream):
        ct_number = text_helpers.letter_to_number(ct_letter)
        pt_char = text_helpers.number_to_letter(ct_number - keystream_val)
        plaintext += pt_char
    return plaintext
