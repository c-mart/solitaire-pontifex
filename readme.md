Implementation of [Solitaire](https://www.schneier.com/cryptography/solitaire/) encryption algorithm by Bruce Schnier, a.k.a. Pontifex cipher from Neal Stephenson's [Cryptonomicon](https://en.wikipedia.org/wiki/Cryptonomicon).

Supports generation of keystream, encryption and decryption of messages, and various utility functions.

## Disclaimer
Solitaire has known cryptographic weaknesses. I am not a cryptographer, and this implementation has not been reviewed by one. So, please don't use this for any truly sensitive information.

## Basic Usage
    >>> import solitaire, key_helpers
    >>> my_key = solitaire.get_key_from_passphrase("MANZANITA")
    >>> print(key_helpers.format_key(my_key, 'u'))
    ['🃘', '🃙', '🃚', '🃛', '🃝', '🃞', '🃁', '🃑', '🃄', '🃅', '🃆', '🃇', '🃈', '🃉', '🃊', '🃋', '🃕', '🃏', '🂸', '🂢', '🂣', '🂦', '🂧', '🃔', '🃖', '🃗', '🃟', '🃍', '🃎', '🂱', '🂲', '🂳', '🂴', '🂵', '🂶', '🃒', '🂹', '🂺', '🂻', '🂽', '🂾', '🂡', '🃂', '🂤', '🂥', '🃃', '🂨', '🂩', '🂪', '🂫', '🂭', '🃓', '🂷', '🂮']
    
    >>> ciphertext = solitaire.encrypt(my_key, "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG")
    >>> print(ciphertext)
    CCOUZQMDZCLFCJNTLHQUBDHRXHITYODDRFY
    
    >>> solitaire.decrypt(my_key, ciphertext)
    'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'


## Supported Key Representations
A key is an ordered deck of cards represented as a list of 54 elements, which can be represented three different ways for computation or human-friendly output. The numeric representation is used internally for cryptographic operations, but we can also accept input or display output as either two-character strings or unicode playing card characters.

### Numeric
As in Schnier's specification, each card is an integer from 1 to 54 inclusive.
Within a suit, each card has a value between 1 (Ace) and 13 (King). Using the bridge ordering, each suit is offset by 13:

- Clubs (face value)
- Diamonds (+13)
- Hearts (+26)
- Spades (+39)

Jokers A and B are 53 and 54 respectively.

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]

### String
Each card is a short string: the first letter of suit, followed by the rank (number of numeric card or first letter of face card). Jokers A and B are 'JA' and 'JB' respectively.

    ['CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK', 'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'JA', 'JB']

### Unicode
Each card is a unicode playing card character as defined [here](http://www.unicode.org/charts/PDF/U1F0A0.pdf).

    ['🃑', '🃒', '🃓', '🃔', '🃕', '🃖', '🃗', '🃘', '🃙', '🃚', '🃛', '🃝', '🃞', '🃁', '🃂', '🃃', '🃄', '🃅', '🃆', '🃇', '🃈', '🃉', '🃊', '🃋', '🃍', '🃎', '🂱', '🂲', '🂳', '🂴', '🂵', '🂶', '🂷', '🂸', '🂹', '🂺', '🂻', '🂽', '🂾', '🂡', '🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', '🂫', '🂭', '🂮', '🃏', '🃟']

## Other
"Key" and "deck" refer the same data structure, but have different meanings in different parts of the code.

Internal functions that have a "deck" parameter expect it to be passed in numeric form.

A deck uses the same data structure of a key, but is mutated while performing cryptographic operations in deck_ops.py.

Functions that refer to a "deck" typically mutate the deck.
Functions that refer to a "key" typically use the key as input but do not modify it.

These 