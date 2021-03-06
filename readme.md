Implementation of [Solitaire](https://www.schneier.com/cryptography/solitaire/) encryption algorithm by Bruce Schnier, a.k.a. Pontifex cipher from Neal Stephenson's [Cryptonomicon](https://en.wikipedia.org/wiki/Cryptonomicon). Supports generation and human-friendly rendering of keystream, encryption and decryption of messages, and various utility functions.

Disclaimer: Solitaire has known cryptographic weaknesses. I am not a cryptographer, and this implementation has not been reviewed by one. So, please don't use this code to communicate any truly sensitive information.

## Basic Usage

    >>> from solitaire import Key, encrypt, decrypt
    >>> 
    >>> k = Key(passphrase='THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG')
    >>> k
    [45, 2, 53, 29, 33, 30, 20, 10, 18, 1, 46, 40, 36, 37, 19, 38, 52, 12, 7, 31, 49, 15, 3, 26, 32, 34, 41, 9, 22, 23, 14, 21, 27, 25, 35, 39, 54, 48, 4, 5, 6, 51, 8, 13, 24, 16, 17, 47, 28, 11, 42, 43, 44, 50]
    >>> k.as_string()
    ['S6', 'C2', 'JA', 'H3', 'H7', 'H4', 'D7', 'C10', 'D5', 'CA', 'S7', 'SA', 'H10', 'HJ', 'D6', 'HQ', 'SK', 'CQ', 'C7', 'H5', 'S10', 'D2', 'C3', 'DK', 'H6', 'H8', 'S2', 'C9', 'D9', 'D10', 'DA', 'D8', 'HA', 'DQ', 'H9', 'HK', 'JB', 'S9', 'C4', 'C5', 'C6', 'SQ', 'C8', 'CK', 'DJ', 'D3', 'D4', 'S8', 'H2', 'CJ', 'S3', 'S4', 'S5', 'SJ']
    >>> k.as_unicode()
    ['🂦', '🃒', '🃏', '🂳', '🂷', '🂴', '🃇', '🃚', '🃅', '🃑', '🂧', '🂡', '🂺', '🂻', '🃆', '🂽', '🂮', '🃝', '🃗', '🂵', '🂪', '🃂', '🃓', '🃎', '🂶', '🂸', '🂢', '🃙', '🃉', '🃊', '🃁', '🃈', '🂱', '🃍', '🂹', '🂾', '🃟', '🂩', '🃔', '🃕', '🃖', '🂭', '🃘', '🃞', '🃋', '🃃', '🃄', '🂨', '🂲', '🃛', '🂣', '🂤', '🂥', '🂫']
    >>> 
    >>> secret_message = encrypt(k, 'MANZANITAS')
    >>> print(secret_message)
    'JDULDZBAUD'
    >>> decrypt(k, secret_message)
    'MANZANITAS'

## Key, Deck, and Keystream
A **key** (or **deck**) is an ordered deck of cards which is represented as a list of 54 elements, each corresponding to a card value. A key/deck can be represented three different ways for human-friendly I/O. The numeric representation is used internally for cryptographic operations, but we can also accept input and display output as either two-character strings or unicode playing card characters. (Internal functions that have a "deck" parameter expect it to be passed in numeric form.)

What's the difference between a key and a deck? Functions that accept a key will never mutate it, while functions accepting a deck may mutate that deck. This is intended to mirror how Solitaire is used by hand; a deck of cards is arranged to represent a static input key, then the deck is manipulated (its state is changed) to generate the keystream.

A **keystream** (as output by `generate_keystream()`) is like a key, but has a variable length that is specified when the function is called. So, a keystream will *not* necessarily contain all 54 card values, and some values may occur more than once.

## Key/Deck Representations

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

## Verbose Mode

`generate_keystream()` supports a verbose mode, to demonstrate each step of the key generation algorithm:

    >>> k = solitaire.get_key_from_passphrase("RYTIMOCRNUEWOIRCNOIDUFNOIDCFNUOISANCUINDSAJF")
    >>> k
    [8, 31, 6, 2, 34, 30, 20, 35, 11, 14, 15, 50, 18, 41, 9, 51, 16, 27, 24, 49, 52, 22, 4, 21, 25, 26, 42, 29, 45, 17, 36, 32, 54, 10, 38, 5, 47, 1, 7, 48, 46, 13, 3, 53, 28, 33, 39, 44, 12, 19, 43, 23, 37, 40]
    >>> solitaire.generate_keystream(k, 1, verbose=True)
    Deck after advancing joker A:
    [8, 31, 6, 2, 34, 30, 20, 35, 11, 14, 15, 50, 18, 41, 9, 51, 16, 27, 24, 49, 52, 22, 4, 21, 25, 26, 42, 29, 45, 17, 36, 32, 54, 10, 38, 5, 47, 1, 7, 48, 46, 13, 3, 28, 53, 33, 39, 44, 12, 19, 43, 23, 37, 40]
    Deck after advancing joker B:
    [8, 31, 6, 2, 34, 30, 20, 35, 11, 14, 15, 50, 18, 41, 9, 51, 16, 27, 24, 49, 52, 22, 4, 21, 25, 26, 42, 29, 45, 17, 36, 32, 10, 38, 54, 5, 47, 1, 7, 48, 46, 13, 3, 28, 53, 33, 39, 44, 12, 19, 43, 23, 37, 40]
    Deck after triple cut:
    [33, 39, 44, 12, 19, 43, 23, 37, 40, 54, 5, 47, 1, 7, 48, 46, 13, 3, 28, 53, 8, 31, 6, 2, 34, 30, 20, 35, 11, 14, 15, 50, 18, 41, 9, 51, 16, 27, 24, 49, 52, 22, 4, 21, 25, 26, 42, 29, 45, 17, 36, 32, 10, 38]
    Deck after count cut:
    [24, 49, 52, 22, 4, 21, 25, 26, 42, 29, 45, 17, 36, 32, 10, 33, 39, 44, 12, 19, 43, 23, 37, 40, 54, 5, 47, 1, 7, 48, 46, 13, 3, 28, 53, 8, 31, 6, 2, 34, 30, 20, 35, 11, 14, 15, 50, 18, 41, 9, 51, 16, 27, 38]
    Deck after advancing joker A:
    [24, 49, 52, 22, 4, 21, 25, 26, 42, 29, 45, 17, 36, 32, 10, 33, 39, 44, 12, 19, 43, 23, 37, 40, 54, 5, 47, 1, 7, 48, 46, 13, 3, 28, 8, 53, 31, 6, 2, 34, 30, 20, 35, 11, 14, 15, 50, 18, 41, 9, 51, 16, 27, 38]
    Deck after advancing joker B:
    [24, 49, 52, 22, 4, 21, 25, 26, 42, 29, 45, 17, 36, 32, 10, 33, 39, 44, 12, 19, 43, 23, 37, 40, 5, 47, 54, 1, 7, 48, 46, 13, 3, 28, 8, 53, 31, 6, 2, 34, 30, 20, 35, 11, 14, 15, 50, 18, 41, 9, 51, 16, 27, 38]
    Deck after triple cut:
    [31, 6, 2, 34, 30, 20, 35, 11, 14, 15, 50, 18, 41, 9, 51, 16, 27, 38, 54, 1, 7, 48, 46, 13, 3, 28, 8, 53, 24, 49, 52, 22, 4, 21, 25, 26, 42, 29, 45, 17, 36, 32, 10, 33, 39, 44, 12, 19, 43, 23, 37, 40, 5, 47]
    Deck after count cut:
    [19, 43, 23, 37, 40, 5, 31, 6, 2, 34, 30, 20, 35, 11, 14, 15, 50, 18, 41, 9, 51, 16, 27, 38, 54, 1, 7, 48, 46, 13, 3, 28, 8, 53, 24, 49, 52, 22, 4, 21, 25, 26, 42, 29, 45, 17, 36, 32, 10, 33, 39, 44, 12, 47]
    Found output keystream value 9
    [9]