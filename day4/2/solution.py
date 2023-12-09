import re
import time


def matches_to_points(number_of_matches):
    """Convert number of winning numbers to points.

    First winning number is 1 point, each subsequent
    winning number doubles the total points.
    """
    if number_of_matches < 1:
        return 0

    # We need to subtract 1, since the first matching
    # number is worth 1 point, which is 2^0.
    return 2**(number_of_matches - 1)


def parse_scratch_card(scratch_card_input):
    """Parse raw scratch card string to lists of winning/actual numbers."""
    # Normalize the input string
    scratch_card_input = re.sub(r'Card \d: ', '', scratch_card_input)

    # Obtain winning numbers and actual numbers as string
    parts = scratch_card_input.split(' | ')
    winning = _convert_string_to_list(parts[0])
    actual = _convert_string_to_list(parts[1])

    return winning, actual


def _convert_string_to_list(numbers_string, separator=' '):
    """"Converts a string of numbers to a list of numbers.

    Optionally accepts a separator, defaults to space.
    """
    numbers_list = []

    for number in numbers_string.split(separator):
        try:
            numbers_list.append(int(number))
        except Exception:
            # If a number couldn't be parsed / cast
            # to an int, skip it.
            pass

    return numbers_list


def calculate_number_of_matches(winning, actual):
    """Calculate the total number of matches.

    Compare the actual numbers with the list of
    winning numbers to determine the amount of
    matching numbers.
    """
    number_of_matches = 0

    for actual_number in actual:
        if actual_number in winning:
            number_of_matches += 1

    return number_of_matches


def main():
    card_dict = {}

    with open('input.txt', 'r') as f:
        for idx, line in enumerate(f.readlines()):
            # Separate winning and actual numbers
            winning, actual = parse_scratch_card(line)

            # Get number of matching numbers
            number_of_matches = calculate_number_of_matches(winning, actual)

            # Register each card in dictionary
            card_dict.update({
                idx+1: {
                    "matches": number_of_matches,
                    "amount": 1,
                }
            })

    # Sum the total amount of scratch cards
    grand_total = 0 

    # Loop through the dictionary, applying the rules
    # as given: make copies of subsequent cards.
    for card_id, properties in card_dict.items():
        number_of_copies = properties['amount']
        number_of_matches = properties['matches']

        if number_of_matches >= 1:
            # Make copy of subsequent cards, for each copy of
            # the current card we have
            for _ in range(number_of_copies):
                for i in range(card_id+1, (card_id+1+number_of_matches)):
                    card_dict[i]['amount'] += 1

        grand_total += number_of_copies 

    print(f'Total: {grand_total}')


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f'Took {end-start} seconds.')
