import pytest

from key_helpers import *

reference_key_numeric_literal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                                 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                                 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
                                 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                                 53, 54]

reference_key_string_literal = ['CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
                                'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK',
                                'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK',
                                'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
                                'JA', 'JB']

reference_key_unicode_literal = ['🃑', '🃒', '🃓', '🃔', '🃕', '🃖', '🃗', '🃘', '🃙', '🃚', '🃛', '🃝', '🃞',
                                 '🃁', '🃂', '🃃', '🃄', '🃅', '🃆', '🃇', '🃈', '🃉', '🃊', '🃋', '🃍', '🃎',
                                 '🂱', '🂲', '🂳', '🂴', '🂵', '🂶', '🂷', '🂸', '🂹', '🂺', '🂻', '🂽', '🂾',
                                 '🂡', '🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', '🂫', '🂭', '🂮',
                                 '🃏', '🃟']


def test_reference_key():
    assert get_reference_key() == reference_key_numeric_literal, "Reference numeric key incorrect"


def test_reference_key_string():
    assert get_reference_key_string() == reference_key_string_literal, "Reference string key incorrect"


def test_reference_key_unicode():
    assert get_reference_key_unicode() == reference_key_unicode_literal, "Reference unicode key incorrect"


def test_randomize_key():
    key2 = randomize_key(reference_key_numeric_literal)
    assert sorted(reference_key_numeric_literal) == sorted(key2)


def test_validate_key_happy_case():
    validate_key(reference_key_numeric_literal)
    validate_key(reference_key_string_literal)
    validate_key(reference_key_unicode_literal)


def test_validate_key_missing_one_element():
    invalid_numeric_key = reference_key_numeric_literal[:-1]
    with pytest.raises(AssertionError):
        validate_key(invalid_numeric_key)
    invalid_string_key = reference_key_string_literal[:-1]
    with pytest.raises(AssertionError):
        validate_key(invalid_string_key)
    invalid_unicode_key = reference_key_unicode_literal[:-1]
    with pytest.raises(AssertionError):
        validate_key(invalid_unicode_key)


def test_validate_key_duplicate_element():
    invalid_numeric_key = reference_key_numeric_literal + [47]
    with pytest.raises(AssertionError):
        validate_key(invalid_numeric_key)
    invalid_string_key = reference_key_string_literal + ["C9"]
    with pytest.raises(AssertionError):
        validate_key(invalid_string_key)
    invalid_unicode_key = reference_key_unicode_literal + [chr(0x1F0B8)]
    with pytest.raises(AssertionError):
        validate_key(invalid_unicode_key)


def test_validate_key_wrong_element_type():
    invalid_numeric_key = reference_key_numeric_literal[:-1] + ["JB"]
    with pytest.raises(TypeError):
        validate_key(invalid_numeric_key)
    invalid_string_key = reference_key_string_literal[:-1] + [chr(0x1F0DF)]
    with pytest.raises(AssertionError):
        validate_key(invalid_string_key)
    invalid_unicode_key = reference_key_unicode_literal[:-1] + [54]
    with pytest.raises(TypeError):
        validate_key(invalid_unicode_key)


def test_get_key_format():
    assert get_key_format(reference_key_numeric_literal) == 'n'
    assert get_key_format(reference_key_string_literal) == 's'
    assert get_key_format(reference_key_unicode_literal) == 'u'


def test_format_key():
    ref_keys_formats = ((reference_key_numeric_literal, 'n'),
                        (reference_key_string_literal, 's'),
                        (reference_key_unicode_literal, 'u'))
    for input_key, _ in ref_keys_formats:
        for output_key, output_format in ref_keys_formats:
            assert format_key(input_key, output_format) == output_key, "Formatted output key not as expected"
