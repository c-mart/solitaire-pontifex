import random

"""
Helper functions for generating, validating, and formatting keys
"""


def get_reference_key():
    """Returns ordered reference list of cards represented as numbers from 1-54 inclusive"""
    return [x for x in range(1, 55)]


def get_reference_key_string():
    """Returns ordered reference list of cards represented as strings per readme.md"""
    string_key = list()
    for suit in ['C', 'D', 'H', 'S']:
        for rank in ['A'] + [str(x) for x in range(2, 11)] + ['J', 'Q', 'K']:
            string_key.append(suit + rank)
    string_key += ['JA', 'JB']  # Two jokers
    return string_key


def get_reference_key_unicode():
    """Returns ordered reference list of cards represented as unicode playing card characters
    See http://www.unicode.org/charts/PDF/U1F0A0.pdf
    """
    unicode_cards = list()
    # Generate unicode codepoints for each suit, ordered per specification and readme.md
    for suit_unicode_hex_digit in ['D', 'C', 'B', 'A']:
        prefix_str = '0x1F0{0}'.format(suit_unicode_hex_digit)
        suit = list(range(eval(prefix_str+'1'), eval(prefix_str+'C'))) + [eval(prefix_str+'D'), eval(prefix_str+'E')]
        [unicode_cards.append(chr(card)) for card in suit]
    # Add two jokers
    [unicode_cards.append(chr(joker)) for joker in [0x1F0CF, 0x1F0DF]]
    return unicode_cards


def randomize_key(key):
    """Returns a randomized (shuffled) copy of key"""
    random.shuffle(key[:])
    return key


def validate_key(key):
    """Asserts that key is a valid key in numeric, string, or unicode playing card format according to readme.md"""
    if key[0] in get_reference_key():
        assert sorted(key) == sorted(get_reference_key()), \
            "Numeric representation of key must be a list of all integers from 1 to 54 inclusive (in any order)"
    elif key[0] in get_reference_key_string():
        assert sorted(key) == sorted(get_reference_key_string()), \
            "String representation of key must be a list of all 54 card strings as described in readme.md"
    elif key[0] in get_reference_key_unicode():
        assert sorted(key) == sorted(get_reference_key_unicode()), \
            "Unicode representation of key must be a list of 54 unicode playing cards as described in readme.md"
    else:
        raise TypeError("Key must be a list of integers 1 to 54, or a list of strings as described in readme.md")


def get_key_format(key):
    """Gets format of key or keystream.
    Returns 'n', 's', or 'u' for numeric, string, or unicode playing card format."""
    if key[0] in get_reference_key():
        return 'n'
    elif key[0] in get_reference_key_string():
        return 's'
    elif key[0] in get_reference_key_unicode():
        return 'u'


def format_key(key, output_format='n'):
    """Converts key or keystream to desired format. key can be in numeric, string, or unicode playing card format per readme.md.
    format can be 'n', 's', or 'u' for numeric, string, or unicode; defaults to numeric.
    """
    input_format = get_key_format(key)
    formats = {'n': get_reference_key, 's': get_reference_key_string, 'u': get_reference_key_unicode}
    card_lookup = dict()
    for k, v in zip(formats[input_format](), formats[output_format]()):
        card_lookup[k] = v
    return [card_lookup[card] for card in key]
