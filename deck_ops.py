import text_helpers

"""
Functions that manipulate a deck (key in numeric format).
Used to generate keystream and derive key deck from a passphrase.

Caution: these functions are mostly intended for internal use, so they do not validate input. (Input validation is
handled by user-facing functions.) So, their behavior is undefined if you do not pass in a valid key in numeric format.
"""


def advance_joker_a(deck):
    """Given a deck, locate joker A and advance it one position, return new deck"""
    # Locate joker A and advance it one position
    ja_loc = deck.index(53)
    if ja_loc == 53:  # If joker A is on the bottom of the deck, move it to one card below the top card
        return [deck[0]] + [53] + deck[1:53]
    else:
        return deck[:ja_loc] + [deck[ja_loc + 1]] + [53] + deck[ja_loc + 2:]


def advance_joker_b(deck):
    """Given a deck, locate joker B and advance it two positions, return new deck"""
    jb_loc = deck.index(54)
    if jb_loc == 53:  # If joker B is on the bottom of the deck, move it to two positions below the top card
        return deck[0:2] + [54] + deck[2:53]
    if jb_loc == 52:  # If joker is second from bottom of the deck, move it to one position below the top card
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
    2. Cut from after the nth (1-indexed) card up to (but not including) the bottom card
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
    cut_pos = text_helpers.letter_to_number(letter)
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
