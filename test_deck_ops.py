import pytest

from deck_ops import *


def test_advance_joker_a():
    code_path_1_start_deck = [39, 29, 30, 7, 44, 11, 1, 24, 16, 27, 28, 48, 51, 54, 9, 34, 22, 21, 13, 19, 38, 8, 35,
                              20, 37, 45, 33, 4, 2, 15, 50, 10, 23, 52, 43, 42, 12, 25, 14, 5, 3, 18, 36, 26, 17, 32,
                              46, 6, 49, 47, 31, 41, 40, 53]
    code_path_1_end_deck = [39, 53, 29, 30, 7, 44, 11, 1, 24, 16, 27, 28, 48, 51, 54, 9, 34, 22, 21, 13, 19, 38, 8, 35,
                            20, 37, 45, 33, 4, 2, 15, 50, 10, 23, 52, 43, 42, 12, 25, 14, 5, 3, 18, 36, 26, 17, 32, 46,
                            6, 49, 47, 31, 41, 40]
    assert advance_joker_a(code_path_1_start_deck) == code_path_1_end_deck, \
        "Joker A not advanced as expected, should be placed one card below the top"

    code_path_2_start_deck = [37, 22, 9, 32, 36, 41, 30, 7, 33, 14, 27, 4, 46, 5, 11, 10, 40, 39, 48, 16, 18, 34, 26,
                              12, 3, 51, 8, 1, 52, 17, 15, 45, 2, 19, 23, 42, 49, 25, 53, 6, 47, 21, 38, 35, 43, 24,
                              31, 44, 29, 13, 50, 28, 20, 54]
    code_path_2_end_deck = [37, 22, 9, 32, 36, 41, 30, 7, 33, 14, 27, 4, 46, 5, 11, 10, 40, 39, 48, 16, 18, 34, 26, 12,
                            3, 51, 8, 1, 52, 17, 15, 45, 2, 19, 23, 42, 49, 25, 6, 53, 47, 21, 38, 35, 43, 24, 31, 44,
                            29, 13, 50, 28, 20, 54]
    assert advance_joker_a(code_path_2_start_deck) == code_path_2_end_deck, \
        "Joker A not advanced as expected, should move down one card"


def test_advance_joker_b():
    code_path_1_start_deck = [28, 3, 4, 31, 47, 34, 38, 36, 48, 14, 22, 8, 27, 12, 9, 10, 49, 18, 45, 21, 30, 51, 29,
                              7, 39, 40, 35, 2, 16, 15, 43, 41, 37, 5, 26, 52, 33, 6, 25, 44, 13, 17, 32, 20, 11, 19,
                              24, 46, 1, 42, 53, 23, 50, 54]
    code_path_1_end_deck = [28, 3, 54, 4, 31, 47, 34, 38, 36, 48, 14, 22, 8, 27, 12, 9, 10, 49, 18, 45, 21, 30, 51, 29,
                            7, 39, 40, 35, 2, 16, 15, 43, 41, 37, 5, 26, 52, 33, 6, 25, 44, 13, 17, 32, 20, 11,
                            19, 24, 46, 1, 42, 53, 23, 50]
    assert advance_joker_b(code_path_1_start_deck) == code_path_1_end_deck, \
        "Joker B not advanced as expected, should be placed two cards below the top card"

    code_path_2_start_deck = [16, 18, 14, 38, 11, 8, 44, 26, 7, 5, 19, 37, 20, 28, 41, 21, 23, 34, 13, 15, 6, 24, 47,
                              48, 2, 49, 32, 3, 25, 9, 52, 51, 30, 29, 27, 1, 31, 43, 40, 22, 12, 36, 42, 33, 46, 10,
                              50, 45, 53, 17, 35, 4, 54, 39]
    code_path_2_end_deck = [16, 54, 18, 14, 38, 11, 8, 44, 26, 7, 5, 19, 37, 20, 28, 41, 21, 23, 34, 13, 15, 6, 24, 47,
                            48, 2, 49, 32, 3, 25, 9, 52, 51, 30, 29, 27, 1, 31, 43, 40, 22, 12, 36, 42, 33, 46, 10, 50,
                            45, 53, 17, 35, 4, 39]
    assert advance_joker_b(code_path_2_start_deck) == code_path_2_end_deck, \
        "Joker B not advanced as expected, should be placed one card below the top"

    code_path_3_start_deck = [43, 24, 13, 25, 22, 50, 1, 32, 8, 42, 9, 10, 37, 41, 47, 15, 49, 18, 6, 28, 48, 34, 29,
                              23, 35, 54, 12, 46, 27, 33, 21, 51, 38, 16, 14, 44, 45, 7, 17, 31, 36, 53, 52, 40, 11, 3,
                              5, 39, 4, 20, 2, 30, 26, 19]
    code_path_3_end_deck = [43, 24, 13, 25, 22, 50, 1, 32, 8, 42, 9, 10, 37, 41, 47, 15, 49, 18, 6, 28, 48, 34, 29, 23,
                            35, 12, 46, 54, 27, 33, 21, 51, 38, 16, 14, 44, 45, 7, 17, 31, 36, 53, 52, 40, 11, 3, 5,
                            39, 4, 20, 2, 30, 26, 19]
    assert advance_joker_b(code_path_3_start_deck) == code_path_3_end_deck, \
        "Joker B not advanced as expected, should move down two cards"


def test_triple_cut():
    code_path_1_start_deck = [45, 37, 11, 5, 13, 33, 27, 51, 38, 47, 10, 48, 8, 2, 44, 23, 20, 53, 30, 28, 15, 4, 42,
                              19, 32, 25, 36, 26, 6, 46, 12, 7, 17, 43, 35, 3, 50, 29, 16, 49, 34, 9, 18, 22, 41, 54,
                              40, 52, 21, 24, 31, 14, 39, 1]
    code_path_1_end_deck = [40, 52, 21, 24, 31, 14, 39, 1, 53, 30, 28, 15, 4, 42, 19, 32, 25, 36, 26, 6, 46, 12, 7, 17,
                            43, 35, 3, 50, 29, 16, 49, 34, 9, 18, 22, 41, 54, 45, 37, 11, 5, 13, 33, 27, 51, 38, 47,
                            10, 48, 8, 2, 44, 23, 20]
    assert triple_cut(code_path_1_start_deck) == code_path_1_end_deck, "Triple cut does not adhere to specification"

    code_path_2_start_deck = [53, 37, 25, 29, 20, 7, 44, 36, 11, 32, 4, 22, 23, 3, 17, 52, 47, 35, 15, 19, 9, 10, 41,
                              31, 26, 45, 42, 38, 48, 50, 30, 2, 24, 33, 8, 5, 13, 1, 6, 16, 40, 49, 34, 27, 14, 12,
                              43, 46, 51, 28, 18, 39, 21, 54]
    assert triple_cut(code_path_2_start_deck) == code_path_2_start_deck, \
        "Triple cut should not modify deck when jokers are at the ends"


def test_count_cut():
    code_path_1_start_deck = [9, 37, 21, 24, 43, 50, 33, 1, 14, 2, 11, 42, 23, 12, 41, 40, 6, 3, 27, 35, 13, 8, 45, 39,
                              29, 52, 15, 17, 31, 48, 32, 10, 38, 51, 28, 19, 18, 54, 30, 4, 53, 49, 16, 36, 25, 22,
                              34, 5, 47, 46, 26, 20, 44, 7]
    code_path_1_end_deck = [1, 14, 2, 11, 42, 23, 12, 41, 40, 6, 3, 27, 35, 13, 8, 45, 39, 29, 52, 15, 17, 31, 48, 32,
                            10, 38, 51, 28, 19, 18, 54, 30, 4, 53, 49, 16, 36, 25, 22, 34, 5, 47, 46, 26, 20, 44, 9,
                            37, 21, 24, 43, 50, 33, 7]
    assert count_cut(code_path_1_start_deck) == code_path_1_end_deck, "Count cut does not adhere to specification"

    code_path_2_start_deck = [4, 47, 34, 39, 5, 22, 7, 45, 52, 46, 27, 23, 53, 42, 41, 17, 26, 28, 13, 11, 20, 33, 24,
                              31, 38, 18, 3, 19, 21, 40, 15, 14, 50, 37, 8, 1, 29, 12, 2, 6, 51, 44, 35, 43, 32, 16,
                              10, 9, 48, 25, 30, 36, 49, 54]
    assert count_cut(code_path_2_start_deck) == code_path_2_start_deck, \
        "Count cut should not modify deck with joker B on bottom"


def test_count_cut_from_letter():
    start_deck = [8, 41, 43, 11, 27, 45, 54, 24, 6, 51, 35, 5, 49, 23, 18, 29, 3, 50, 40, 19, 16, 1, 30, 22, 20, 4, 9,
                  34, 13, 2, 37, 48, 38, 17, 14, 7, 21, 46, 15, 25, 28, 33, 26, 44, 32, 42, 36, 31, 12, 10, 39, 52, 53,
                  47]
    letter = 'P'
    end_deck = [3, 50, 40, 19, 16, 1, 30, 22, 20, 4, 9, 34, 13, 2, 37, 48, 38, 17, 14, 7, 21, 46, 15, 25, 28, 33, 26,
                44, 32, 42, 36, 31, 12, 10, 39, 52, 53, 8, 41, 43, 11, 27, 45, 54, 24, 6, 51, 35, 5, 49, 23, 18, 29, 47]
    assert count_cut_from_letter(start_deck, letter) == end_deck, \
        "Count cut from letter does not adhere to specification"


def test_read_output_keystream_value():
    code_path_1_deck = [31, 21, 17, 44, 2, 8, 22, 7, 23, 30, 45, 49, 24, 33, 35, 14, 29, 32, 27, 10, 37, 11, 36, 41,
                        13, 16, 28, 52, 18, 19, 25, 40, 4, 43, 54, 1, 39, 50, 5, 12, 53, 34, 51, 20, 47, 9, 48, 38, 26,
                        15, 6, 3, 42, 46]
    assert read_output_keystream_value(code_path_1_deck) == 40, \
        "Output keystream value does not adhere to specification"

    code_path_2_deck = [54, 21, 17, 44, 2, 8, 22, 7, 23, 30, 45, 49, 24, 33, 35, 14, 29, 32, 27, 10, 37, 11, 36, 41,
                        13, 16, 28, 52, 18, 19, 25, 40, 4, 43, 31, 1, 39, 50, 5, 12, 53, 34, 51, 20, 47, 9, 48, 38, 26,
                        15, 6, 3, 42, 46]
    assert read_output_keystream_value(code_path_2_deck) == 46, \
        "Output keystream value does not adhere to specification"

    code_path_3_deck = [6, 21, 17, 44, 2, 8, 53, 7, 23, 30, 45, 49, 24, 33, 35, 14, 29, 32, 27, 10, 37, 11, 36, 41,
                        13, 16, 28, 52, 18, 19, 25, 40, 4, 43, 31, 1, 39, 50, 5, 12, 22, 34, 51, 20, 47, 9, 48, 38, 26,
                        15, 54, 3, 42, 46]
    with pytest.raises(JokerException):
        read_output_keystream_value(code_path_3_deck)