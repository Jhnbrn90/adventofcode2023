import pytest

from solution import (
    matches_to_points,
    parse_scratch_card,
    calculate_number_of_matches,
)

@pytest.mark.parametrize('number_of_matches, points', [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 4),
    (4, 8),
    (5, 16),
    (6, 32),
    (7, 64),
    (8, 128),
    (9, 256),
    (10, 512),
])
def test_convert_matches_to_points(number_of_matches, points):
    assert points == matches_to_points(number_of_matches)


@pytest.mark.parametrize('scratch_card_input, winning, actual', [
    ('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53', [41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),
    ('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19', [13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]),
])
def test_parse_scratch_card(scratch_card_input, winning, actual):
    assert parse_scratch_card(scratch_card_input) == (winning, actual)


@pytest.mark.parametrize('winning, actual, matches', [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 3, 5, 7], 4),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [11, 111, 0, 13], 1),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [111, 0, 13], 0),
])
def test_count_number_of_matches(winning, actual, matches):
    assert calculate_number_of_matches(winning, actual) == matches
