from solitaire_pontifex import *

def test_sample_keystream_output():
    my_deck_3 = Deck(reference_numeric_key())
    assert my_deck_3.generate_keystream(10) == [4, 49, 10, 24, 8, 51, 44, 6, 4, 33], \
        "Output of keystream from unkeyed deck does not match specification"
